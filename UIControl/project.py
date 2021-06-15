import os
import cv2
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from color import color_detect

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(677, 587)
        self.frame_1 = QtWidgets.QFrame(Dialog)
        self.frame_1.setGeometry(QtCore.QRect(20, 20, 631, 43))
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.file = QtWidgets.QLabel(self.frame_1)
        self.file.setObjectName("file")
        self.horizontalLayout.addWidget(self.file)
        self.file_path = QtWidgets.QLabel(self.frame_1)
        self.file_path.setObjectName("file_path")
        self.horizontalLayout.addWidget(self.file_path)
        self.file_browse = QtWidgets.QPushButton(self.frame_1)
        self.file_browse.setObjectName("file_browse")
        self.horizontalLayout.addWidget(self.file_browse)
        self.file_browse.clicked.connect(self.file_open)

        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(20, 90, 631, 40))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.up_category = QtWidgets.QLabel(self.frame_2)
        self.up_category.setObjectName("up_category")
        self.horizontalLayout_2.addWidget(self.up_category)
        self.up = QtWidgets.QComboBox(self.frame_2)
        self.up.setObjectName("up")
        self.up.addItem("")
        self.up.addItem("")
        self.up.addItem("")
        self.up.addItem("")
        self.up.addItem("")
        self.up.addItem("")
        self.up.addItem("")
        self.up.addItem("")
        self.up.addItem("")
        self.up.addItem("")
        self.horizontalLayout_2.addWidget(self.up)
        self.up_category_color = QtWidgets.QLabel(self.frame_2)
        self.up_category_color.setObjectName("up_category_color")
        self.horizontalLayout_2.addWidget(self.up_category_color)
        self.up_color = QtWidgets.QComboBox(self.frame_2)
        self.up_color.setObjectName("up_color")
        self.up_color.addItem("")
        self.up_color.addItem("")
        self.up_color.addItem("")
        self.up_color.addItem("")
        self.up_color.addItem("")
        self.up_color.addItem("")
        self.up_color.addItem("")
        self.up_color.addItem("")
        self.up_color.addItem("")
        self.up_color.addItem("")
        self.up_color.addItem("")
        self.up_color.addItem("")
        self.up_color.addItem("")
        self.up_color.addItem("")
        self.up_color.addItem("")
        self.horizontalLayout_2.addWidget(self.up_color)

        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(20, 160, 631, 40))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.down_category = QtWidgets.QLabel(self.frame_3)
        self.down_category.setObjectName("down_category")
        self.horizontalLayout_3.addWidget(self.down_category)
        self.down = QtWidgets.QComboBox(self.frame_3)
        self.down.setObjectName("down")
        self.down.addItem("")
        self.down.addItem("")
        self.down.addItem("")
        self.down.addItem("")
        self.horizontalLayout_3.addWidget(self.down)
        self.down_category_color = QtWidgets.QLabel(self.frame_3)
        self.down_category_color.setObjectName("down_category_color")
        self.horizontalLayout_3.addWidget(self.down_category_color)
        self.down_color = QtWidgets.QComboBox(self.frame_3)
        self.down_color.setObjectName("down_color")
        self.down_color.addItem("")
        self.down_color.addItem("")
        self.down_color.addItem("")
        self.down_color.addItem("")
        self.down_color.addItem("")
        self.down_color.addItem("")
        self.down_color.addItem("")
        self.down_color.addItem("")
        self.down_color.addItem("")
        self.down_color.addItem("")
        self.down_color.addItem("")
        self.down_color.addItem("")
        self.down_color.addItem("")
        self.down_color.addItem("")
        self.down_color.addItem("")
        self.horizontalLayout_3.addWidget(self.down_color)

        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setGeometry(QtCore.QRect(20, 280, 631, 40))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.execute = QtWidgets.QPushButton(self.frame_4)
        self.execute.setObjectName("execute")
        self.horizontalLayout_4.addWidget(self.execute)
        self.reset = QtWidgets.QPushButton(self.frame_4)
        self.reset.setObjectName("reset")
        self.horizontalLayout_4.addWidget(self.reset)
        self.execute.clicked.connect(self.execute_dialog)
        self.reset.clicked.connect(self.reset_dialog)

        self.frame_5 = QtWidgets.QFrame(Dialog)
        self.frame_5.setGeometry(QtCore.QRect(20, 220, 631, 40))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.accessory = QtWidgets.QLabel(self.frame_5)
        self.accessory.setObjectName("accessory")
        self.horizontalLayout_5.addWidget(self.accessory)
        self.radioButton = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_5.addWidget(self.radioButton)

        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 370, 631, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(20, 330, 631, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.file.setText(_translate("Dialog", "FILE :"))
        self.file_path.setText(_translate("Dialog", "FILE_PATH"))
        self.file_browse.setText(_translate("Dialog", "Browse"))
        self.up_category.setText(_translate("Dialog", "TOP :"))
        self.up.setItemText(0, _translate("Dialog", "short_sleeved_shirt"))
        self.up.setItemText(1, _translate("Dialog", "long_sleeved_shirt"))
        self.up.setItemText(2, _translate("Dialog", "short_sleeved_outwear"))
        self.up.setItemText(3, _translate("Dialog", "long_sleeved_outwear"))
        self.up.setItemText(4, _translate("Dialog", "vest"))
        self.up.setItemText(5, _translate("Dialog", "sling"))
        self.up.setItemText(6, _translate("Dialog", "short_sleeved_dress"))
        self.up.setItemText(7, _translate("Dialog", "long_sleeved_dress"))
        self.up.setItemText(8, _translate("Dialog", "vest_dress"))
        self.up.setItemText(9, _translate("Dialog", "sling_dress"))
        self.up_category_color.setText(_translate("Dialog", "COLOR :"))
        self.up_color.setItemText(0, _translate("Dialog", "RED"))
        self.up_color.setItemText(1, _translate("Dialog", "ORANGE"))
        self.up_color.setItemText(2, _translate("Dialog", "YELLOW"))
        self.up_color.setItemText(3, _translate("Dialog", "CHARTREUSE_GREEN"))
        self.up_color.setItemText(4, _translate("Dialog", "GREEN"))
        self.up_color.setItemText(5, _translate("Dialog", "SPRING_GREEN"))
        self.up_color.setItemText(6, _translate("Dialog", "CYAN"))
        self.up_color.setItemText(7, _translate("Dialog", "AZURE"))
        self.up_color.setItemText(8, _translate("Dialog", "BLUE"))
        self.up_color.setItemText(9, _translate("Dialog", "VIOLET"))
        self.up_color.setItemText(10, _translate("Dialog", "MAGENTA"))
        self.up_color.setItemText(11, _translate("Dialog", "ROSE"))
        self.up_color.setItemText(12, _translate("Dialog", "BLACK"))
        self.up_color.setItemText(13, _translate("Dialog", "GRAY"))
        self.up_color.setItemText(14, _translate("Dialog", "WHITE"))
        self.down_category.setText(_translate("Dialog", "PANT :"))
        self.down.setItemText(0, _translate("Dialog", "shorts"))
        self.down.setItemText(1, _translate("Dialog", "trousers"))
        self.down.setItemText(2, _translate("Dialog", "skirt"))
        self.down.setItemText(3, _translate("Dialog", "none"))
        self.down_category_color.setText(_translate("Dialog", "COLOR :"))
        self.down_color.setItemText(0, _translate("Dialog", "RED"))
        self.down_color.setItemText(1, _translate("Dialog", "ORANGE"))
        self.down_color.setItemText(2, _translate("Dialog", "YELLOW"))
        self.down_color.setItemText(3, _translate("Dialog", "CHARTREUSE_GREEN"))
        self.down_color.setItemText(4, _translate("Dialog", "GREEN"))
        self.down_color.setItemText(5, _translate("Dialog", "SPRING_GREEN"))
        self.down_color.setItemText(6, _translate("Dialog", "CYAN"))
        self.down_color.setItemText(7, _translate("Dialog", "AZURE"))
        self.down_color.setItemText(8, _translate("Dialog", "BLUE"))
        self.down_color.setItemText(9, _translate("Dialog", "VIOLET"))
        self.down_color.setItemText(10, _translate("Dialog", "MAGENTA"))
        self.down_color.setItemText(11, _translate("Dialog", "ROSE"))
        self.down_color.setItemText(12, _translate("Dialog", "BLACK"))
        self.down_color.setItemText(13, _translate("Dialog", "GRAY"))
        self.down_color.setItemText(14, _translate("Dialog", "WHITE"))
        self.execute.setText(_translate("Dialog", "EXECUTE"))
        self.reset.setText(_translate("Dialog", "RESET"))
        self.accessory.setText(_translate("Dialog", "ACCESSORY:"))
        self.radioButton.setText(_translate("Dialog", "Back_Pack"))

    def file_open(self):
        _translate = QtCore.QCoreApplication.translate
        FileOpen = QtWidgets.QFileDialog.getOpenFileName(self.file_browse, 'Open file', './')
        self.file_path.setText(_translate("Dialog", FileOpen[0]))

    def execute_dialog(self):
        self.reset.setEnabled(False)

        if self.file_path.text() != "FILE_PATH":
            # 영상 => 이미지
            self.textBrowser.setText("")
            self.textBrowser.append("이미지 1초 단위 분할 시작")
            if os.path.exists('./video') :
                os.rmdir('./video')
            os.system(f'mkdir video')
            os.system(f'ffmpeg -i {self.file_path.text()} -ss 00:00:01 -vf "yadif=0:-1:0,fps=2" -qscale:v 2 video/%d.jpg')
            self.progressBar.setProperty("value", 10)
            self.textBrowser.append("이미지 1초 단위 분할 종료")

            # Person Detect
            self.textBrowser.append("사람 탐색 시작")
            os.system(f'python detect.py --class 0 --save-crop --weights ./weights/yolov5x6.pt --source video --conf-thres 0.1')
            self.progressBar.setProperty("value", 30)
            self.textBrowser.append("사람 탐색 종료")

            # Child Detect
            self.textBrowser.append("아동 탐색 시작")
            os.system(f'python detect.py --weights ./weights/child.pt --img-size 320 --line-thickness 1 --conf-thres 0.5 --source ./runs/detect/exp/crops/person  --save-crop')
            self.progressBar.setProperty("value", 50)
            self.textBrowser.append("아동 탐색 종료")

            # Fashion Detect
            self.textBrowser.append("옷 탐색 시작")\
            os.system(f'python detect.py --weights ./weights/fashion.pt --img-size 320 --line-thickness 1 --conf-thres 0.5 --source ./runs/detect/exp/crops/person --save-crop')
            self.progressBar.setProperty("value", 70)
            self.textBrowser.append("옷 탐색 종료")

            # Accessories(Back_Pack) Detect
            if self.radioButton.isChecked():
                self.textBrowser.append("악세사리 탐색 시작")
                os.system(f'python detect.py --weights ./weights/yolov5x6.pt --class 24 --img-size 320 --line-thickness 1 --conf-thres 0.5 --source ./runs/detect/exp/crops/person --save-crop')
                self.textBrowser.append("악세사리 탐색 종료")
            self.progressBar.setProperty("value", 90)

            # 가중치 계산 + 결과 추력
            self.textBrowser.append("평가 중...")
            result = {}
            overlap = {}
            color_result = []
            top = set()
            pant = set()

            for i in os.listdir("./runs/detect/exp/crops/person"):
                result[i] = 0
                overlap[i] = 1
                top_color_val, pant_color_val, ratio, ratio2 = color_detect(self.up_color.currentText(), self.down_color.currentText(), self.down.currentText(),i)
                color_result.append([i, top_color_val, pant_color_val, ratio, ratio2])

            with open("txt/top_color.txt", "w") as f:
                for i, top_color_val, pant_color_val, ratio, ratio2 in color_result:
                    if top_color_val > 0:
                        result[i] += 40
                        f.write(f'{i}\n')

            with open("txt/pant_color.txt", "w") as f:
                for i, top_color_val, pant_color_val, ratio, ratio2 in color_result:
                    if pant_color_val > 0:
                        result[i] += 40
                        f.write(f'{i}\n')

            with open("txt/top_color&pant_color.txt", "w") as f:
                for i, top_color_val, pant_color_val, ratio, ratio2 in color_result:
                    if top_color_val + pant_color_val == 80:
                        result[i] += 20
                        f.write(f'{i}\n')

            with open("txt/child.txt", "w") as f:
                for i in os.listdir("./runs/detect/exp2/crops/child"):
                    splice = i.split("_")
                    name = splice[0] + "_" + splice[1] + ".jpg"

                    if len(splice[-1]) != 4:
                        overlap[name] += 1

                    result[name] += 30
                    f.write(f'{name}\n')

            with open("txt/top.txt", "w") as f:
                if os.path.exists(f'./runs/detect/exp3/crops/{self.up.currentText()}'):
                    for i in os.listdir(f'./runs/detect/exp3/crops/{self.up.currentText()}'):
                        splice = i.split("_")
                        name = splice[0] + "_" + splice[1] + ".jpg"

                        if len(splice[-1]) != 4:
                            overlap[name] += 1

                        result[name] += 30
                        top.add(name)
                        f.write(f'{name}\n')

            with open("txt/pant.txt", "w") as f:
                if os.path.exists(f'./runs/detect/exp3/crops/{self.down.currentText()}'):
                    for i in os.listdir(f'./runs/detect/exp3/crops/{self.down.currentText()}'):
                        splice = i.split("_")
                        name = splice[0] + "_" + splice[1] + ".jpg"

                        if len(splice[-1]) != 4:
                            overlap[name] += 1

                        result[name] += 30
                        pant.add(name)
                        f.write(f'{name}\n')

            with open("txt/top&pant.txt", "w") as f:
                for i in top.intersection(pant):
                    result[i] += 20
                    f.write(f'{i}\n')

            for key, value in result.items():
                result[key] = value // overlap[key]

            if self.radioButton.isChecked():
                with open("txt/backpack.txt", "w") as f:
                    for i in os.listdir(f'./runs/detect/exp4/crops/backpack'):
                        splice = i.split("_")
                        name = splice[0] + "_" + splice[1] + ".jpg"

                        if len(splice[-1]) != 4:
                            overlap[name] += 1

                        result[name] += 30
                        f.write(f'{name}\n')

            result = sorted(result.items(), key=lambda i: (i[1], i[0]), reverse=True)
            max_val = result[0][1]
            # print(result)

            self.progressBar.setProperty("value", 100)
            self.textBrowser.append("탐색 종료.")

            with open("txt/result.txt", "w") as f:
                for key in result:
                    f.write(f'{key[0]} : {key[1]}\n')
                    num = key[0].split("_")

                    if key[1] == max_val:
                        img0 = cv2.imread('./runs/detect/exp/' + num[0] + '.jpg')
                        img0 = cv2.resize(img0, dsize=(512, 512))
                        cv2.namedWindow(f'{num}Second Image')
                        cv2.moveWindow(f'{num}Second Image', 0, 0)
                        cv2.imshow(f'{num}Second Image', img0)

                        img1 = cv2.imread('./runs/detect/exp2/' + key[0])
                        cv2.namedWindow(f'{num}Second Child Image')
                        cv2.moveWindow(f'{num}Second Child Image', 600, 0)
                        cv2.imshow(f'{num}Second Child Image', img1)

                        img2 = cv2.imread('./runs/detect/exp3/' + key[0])
                        cv2.namedWindow(f'{num}Second Fashion Image')
                        cv2.moveWindow(f'{num}Second Fashion Image', 600, 400)
                        cv2.imshow(f'{num}Second Fashion Image', img2)

                        if self.radioButton.isChecked():
                            img3 = cv2.imread('./runs/detect/exp4/' + key[0])
                            cv2.namedWindow(f'{num}Second Accessory Image')
                            cv2.moveWindow(f'{num}Second Accessory Image', 600, 800)
                            cv2.imshow(f'{num}Second Accessory Image', img3)

                        cv2.waitKey()
                        cv2.destroyAllWindows()

            self.reset.setEnabled(True)
        else:
            self.textBrowser.setText("파일을 첨부하세요")

        # print("파일경로 : " + self.file_path.text())
        # print('상의 : ' + self.up.currentText() + '상의 색깔 : ' + self.up_color.currentText())
        # print('하의 : ' + self.down.currentText() + '하의 색깔 : ' + self.down_color.currentText())
        # print(self.radioButton.isChecked())

    def reset_dialog(self):
        _translate = QtCore.QCoreApplication.translate
        self.file_path.setText(_translate("Dialog", "FILE_PATH"))
        self.up.setCurrentIndex(0)
        self.up_color.setCurrentIndex(0)
        self.down.setCurrentIndex(0)
        self.down_color.setCurrentIndex(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

