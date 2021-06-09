import argparse
import time
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path, save_one_box
from utils.plots import colors, plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized

import os
import numpy as np

@torch.no_grad()
def detect(opt):
    result = {}
    # top, pant, top_color, pant_color = opt.top, opt.top_color, opt.pant, opt.pant_color
    source, weights, view_img, save_txt, imgsz = opt.source, opt.weights, opt.view_img, opt.save_txt, opt.img_size
    save_img = not opt.nosave and not source.endswith('.txt')  # save inference images

    # Directories
    save_dir = increment_path(Path(opt.project) / opt.name, exist_ok=opt.exist_ok)  # increment run
    (save_dir / 'labels' if save_txt else save_dir).mkdir(parents=True, exist_ok=True)  # make dir

    # Initialize
    set_logging()
    device = select_device(opt.device)
    half = device.type != 'cpu'  # half precision only supported on CUDA

    # Load model
    model = attempt_load(weights, map_location=device)  # load FP32 model
    stride = int(model.stride.max())  # model stride
    imgsz = check_img_size(imgsz, s=stride)  # check img_size
    names = model.module.names if hasattr(model, 'module') else model.names  # get class names
    if half:
        model.half()  # to FP16

    # Second-stage classifier
    classify = False
    if classify:
        modelc = load_classifier(name='resnet101', n=2)  # initialize
        modelc.load_state_dict(torch.load('weights/resnet101.pt', map_location=device)['model']).to(device).eval()

    # Set Dataloader
    vid_path, vid_writer = None, None
    dataset = LoadImages(source, img_size=imgsz, stride=stride)

    # Run inference
    if device.type != 'cpu':
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  # run once
    t0 = time.time()

    for path, img, im0s, vid_cap in dataset:
        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        # Inference
        t1 = time_synchronized()
        pred = model(img, augment=opt.augment)[0]

        # Apply NMS
        pred = non_max_suppression(pred, opt.conf_thres, opt.iou_thres, opt.classes, opt.agnostic_nms,
                                   max_det=opt.max_det)

        # Apply Classifier
        if classify:
            pred = apply_classifier(pred, modelc, img, im0s)

        # Process detections
        for i, det in enumerate(pred):  # detections per image
            p, s, im0, frame = path, '', im0s.copy(), getattr(dataset, 'frame', 0)

            p = Path(p)  # to Path
            save_path = str(save_dir / p.name)  # img.jpg
            txt_path = str(save_dir / 'labels' / p.stem) + ('' if dataset.mode == 'image' else f'_{frame}')  # img.txt
            s += '%gx%g ' % img.shape[2:]  # print string
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            imc = im0.copy() if opt.save_crop else im0  # for opt.save_crop

            if len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                # Write results
                for *xyxy, conf, cls in reversed(det):

                    if save_img or opt.save_crop or view_img:  # Add bbox to image
                        c = int(cls)  # integer class
                        label = None if opt.hide_labels else (names[c] if opt.hide_conf else f'{names[c]} {conf:.2f}')
                        plot_one_box(xyxy, im0, label=label, color=colors(c, True), line_thickness=opt.line_thickness)

                        if names[c] == opt.top or names[c] == opt.pant:
                            if p.name in result:
                                result[p.name] += 30
                            else:
                                result[p.name] = 30

            temp_result = color_detect(opt.top_color, opt.pant_color, p.name)

            if p.name in result:
                result[p.name] += temp_result
            else:
                result[p.name] = temp_result

            print("")

    print(result)

def color_detect(top_color, pant_color, path):
    # 이미지 파일 불러오기
    result, ratio = 0, 0
    img = cv2.imread("./runs/detect/exp/crops/person/"+str(path))
    height, width, channel = img.shape

    img_1 = img[0:round(height / 2), :]
    img_2 = img[round(height / 2): height, :]
    # HSV 형태로 변환
    img_1_hsv = cv2.cvtColor(img_1, cv2.COLOR_BGR2HSV)
    h1, s1, v1 = cv2.split(img_1_hsv)
    img_2_hsv = cv2.cvtColor(img_2, cv2.COLOR_BGR2HSV)
    h2, s2, v2 = cv2.split(img_2_hsv)

    basic_color = {"RED": 0, "ORANGE": 15, "YELLOW": 30, "CHARTREUSE_GREEN": 45,
                   "GREEN": 60, "SPRING_GREEN": 75, "CYAN": 90, "AZURE": 105,
                   "BLUE": 120, "VIOLET": 135, "MAGENTA": 150, "ROSE": 165,
                   "BLACK": 256, "WHITE": 50, "GRAY": 16}

    # 추출 색깔 초기화
    color_1 = basic_color[top_color]
    color_2 = basic_color[pant_color]

    # BLACK
    if color_1 == 256:
        lower = (0, 0, 0)
        upper = (179, 40, 40)

        img_mask = cv2.inRange(img_1_hsv, lower, upper)
        ratio = np.count_nonzero(img_mask == 255) / np.size(img_mask)
    # WHITE
    elif color_1 == 50:
        lower = (0, 0, 220)
        upper = (179, 25, 255)

        img_mask = cv2.inRange(img_1_hsv, lower, upper)
        ratio = np.count_nonzero(img_mask == 255) / np.size(img_mask)
    # GRAY
    elif color_1 == 16:
        lower = (30, 2, 45)
        upper = (240, 15, 80)

        img_mask = cv2.inRange(img_1_hsv, lower, upper)
        ratio = np.count_nonzero(img_mask == 255) / np.size(img_mask)
    # RED
    elif color_1 == 0:
        img_mask = cv2.inRange(img_1_hsv, (0, 30, 30), (7, 255, 255))
        img_mask_2 = cv2.inRange(img_1_hsv, (173, 30, 30), (179, 255, 255))
        ratio = np.count_nonzero(img_mask == 255) / np.size(img_mask) + np.count_nonzero(img_mask_2 == 255) / np.size(img_mask_2)
    # ETC
    else:
        # lower = (color_1 - 7, 30, 30)
        # upper = (color_1 + 7, 255, 255)
        # img_mask = cv2.inRange(img_1_hsv, lower, upper) # 범위내의 픽셀들은 흰색, 나머지 검은색
        # ratio = np.count_nonzero(img_mask==255) / np.size(img_mask)
        img_mask = cv2.inRange(h1, color_1-15, color_1+15) # 범위내의 픽셀들은 흰색, 나머지 검은색
        ratio = np.count_nonzero(img_mask==255) / np.size(img_mask)

    if ratio >= 0.4:
        result += 40
        ratio = 0

    # BLACK
    if color_2 == 256:
        lower = (0, 0, 0)
        upper = (179, 40, 40)

        img_mask = cv2.inRange(img_2_hsv, lower, upper)
        ratio = np.count_nonzero(img_mask == 255) / np.size(img_mask)
    # WHITE
    elif color_2 == 50:
        lower = (0, 0, 220)
        upper = (179, 25, 255)

        img_mask = cv2.inRange(img_2_hsv, lower, upper)
        ratio = np.count_nonzero(img_mask == 255) / np.size(img_mask)
    # GRAY
    elif color_2 == 16:
        lower = (30, 2, 45)
        upper = (240, 15, 80)

        img_mask = cv2.inRange(img_2_hsv, lower, upper)
        ratio = np.count_nonzero(img_mask == 255) / np.size(img_mask)
    # RED
    elif color_2 == 0:
        img_mask = cv2.inRange(img_2_hsv, (0, 30, 30), (7, 255, 255))
        img_mask_2 = cv2.inRange(img_2_hsv, (173, 30, 30), (179, 255, 255))
        ratio = np.count_nonzero(img_mask == 255) / np.size(img_mask) + np.count_nonzero(img_mask_2 == 255) / np.size(
            img_mask_2)
    # ETC
    else:
        # lower = (color_1 - 7, 30, 30)
        # upper = (color_1 + 7, 255, 255)
        # img_mask = cv2.inRange(img_1_hsv, lower, upper) # 범위내의 픽셀들은 흰색, 나머지 검은색
        # ratio = np.count_nonzero(img_mask==255) / np.size(img_mask)
        img_mask = cv2.inRange(h1, color_2-15, color_2+15) # 범위내의 픽셀들은 흰색, 나머지 검은색
        ratio = np.count_nonzero(img_mask==255) / np.size(img_mask)

    if ratio >= 0.4:
        result += 40

    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='yolov5s.pt', help='model.pt path(s)')
    parser.add_argument('--source', type=str, default='data/images', help='source')  # file/folder, 0 for webcam
    parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
    parser.add_argument('--max-det', type=int, default=1000, help='maximum number of detections per image')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='display results')
    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
    parser.add_argument('--save-crop', action='store_true', help='save cropped prediction boxes')
    parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--update', action='store_true', help='update all models')
    parser.add_argument('--project', default='runs/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    parser.add_argument('--line-thickness', default=3, type=int, help='bounding box thickness (pixels)')
    parser.add_argument('--hide-labels', default=False, action='store_true', help='hide labels')
    parser.add_argument('--hide-conf', default=False, action='store_true', help='hide confidences')
    parser.add_argument('--top', default="", help='top')
    parser.add_argument('--top-color', default="", help='top color')
    parser.add_argument('--pant', default="", help='pant')
    parser.add_argument('--pant-color', default="", help='pant color')
    opt = parser.parse_args()
    check_requirements(exclude=('tensorboard', 'pycocotools', 'thop'))

    if opt.update:  # update all models (to fix SourceChangeWarning)
        for opt.weights in ['yolov5s.pt', 'yolov5m.pt', 'yolov5l.pt', 'yolov5x.pt']:
            detect(opt=opt)
            strip_optimizer(opt.weights)
    else:
        detect(opt=opt)
