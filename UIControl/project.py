import os
import time
import sys
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from ast import literal_eval

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
        ffPath = './ffmpegImg'
        self.reset.setEnabled(False)
<<<<<<< HEAD
        result = {}

        if self.file_path.text() != "FILE_PATH":
            self.textBrowser.setText("")
            self.textBrowser.append("이미지 1초 단위 분할 시작")
            os.system(f'mkdir video')
            os.system(f'ffmpeg -i {self.file_path.text()} -ss 00:00:01 -vf "yadif=0:-1:0,fps=2" -qscale:v 2 -threads 2 video/%d.jpg')
            self.progressBar.setProperty("value", 20)
            self.textBrowser.append("이미지 1초 단위 분할 종료")
=======
        os.system(f'mkdir ffmpegImg')
        os.system(f'ffmpeg -i {self.file_path.text()} -ss 00:00:01 -vf "yadif=0:-1:0,fps=2" -qscale:v 2 {ffPath}/%d.jpg')
>>>>>>> 4812d0e681b35d4dfe43864929cfacd2f055437d

            # Person Detect
            self.textBrowser.append("사람 탐색 시작")
            os.system(f'python detect_person.py --class 0 --save-crop --weights ./weights/yolov5x6.pt --source video')
            for file in os.listdir('./runs/detect/exp/crops/person'):
                result[file] = 0
            self.progressBar.setProperty("value", 40)
            self.textBrowser.append("사람 탐색 종료")
            print("사람 탐색 종료")

            # Child Detect
            self.textBrowser.append("아동 탐색 시작")
            os.system(f'python detect_child.py --weights ./weights/child.pt --img-size 320 --line-thickness 1 --conf-thres 0.3 --source ./runs/detect/exp/crops/person > ./child.txt')
            with open("child.txt") as f:
                child_result = f.readlines()[len(os.listdir('./runs/detect/exp/crops/person'))]
                literal_eval(child_result)
                for key, value in eval(child_result).items():
                    if key in result:
                        result[key] += value
            self.progressBar.setProperty("value", 60)
            self.textBrowser.append("아동 탐색 종료")
            print("아동 탐색 종료")

            # Fashion Detect + Color Detect (detect_fashion.py에 Color Detect 필요)
            self.textBrowser.append("옷 탐색 시작")
            os.system(f'python detect_fashion.py --weights ./weights/fashion.pt --img-size 320 --line-thickness 1 --conf-thres 0.1 --source ./runs/detect/exp/crops/person --top {self.up.currentText()} --top-color {self.up_color.currentText()} --pant {self.down.currentText()} --pant-color {self.down_color.currentText()} > ./fashion.txt')
            with open("fashion.txt") as f:
                fashion_result = f.readlines()[len(os.listdir('./runs/detect/exp/crops/person'))]
                literal_eval(fashion_result)
                for key, value in eval(fashion_result).items():
                    if key in result:
                        result[key] += value
            self.progressBar.setProperty("value", 80)
            self.textBrowser.append("옷 탐색 종료")
            print("옷 색깔 탐색 종료")

<<<<<<< HEAD
            # Accessories(Back_Pack) Detect
            if self.radioButton.isChecked():
                self.textBrowser.append("악세사리 탐색 시작")
                os.system(f'python detect_accessory.py --weights ./weights/yolov5x6.pt --class 24 --img-size 320 --line-thickness 1 --conf-thres 0.05 --source ./runs/detect/exp/crops/person > ./accessory.txt')
                with open("accessory.txt") as f:
                    accessory_result = f.readlines()[len(os.listdir('./runs/detect/exp/crops/person'))]
                    literal_eval(accessory_result)
                    for key, value in eval(accessory_result).items():
                        if key in result:
                            result[key] += value
                self.textBrowser.append("악세사리 탐색 종료")
            print("액세서리 탐색 종료")

            self.textBrowser.append("탐색 종료")
            self.progressBar.setProperty("value", 100)
=======
            # Accessories Detect
            # os.system(f'python3 detect_accessory.py --save-crop --weights 악세사리 모델경로 --img-size 320 --line-thickness 1 --conf-thres 0.1 --source ./person/crops/  --augment --project ./ --name accessory')
        else:
            pass
            # Person Detect
            os.system(f'python3 detect.py --class 0 --save-crop --weights ./weights/yolov5x6.pt --source {ffPath} --project ./ --name person')

            # Child Detect
            os.system(f'python3 detect.py --save-crop --weights 9.pt --line-thickness 1 --source ./person/person --project ./ --name detectedChild')
>>>>>>> 4812d0e681b35d4dfe43864929cfacd2f055437d

            sorted_result = sorted(result.items(), key = lambda item: item[1], reverse=True)
            max_result = sorted_result[0][1]
            print(sorted_result)
            print(max_result)

            for i in sorted_result:
                if max_result == i[1]:
                    img0 = cv2.imread('./runs/detect/exp/' + i[0][0] + '.jpg')
                    dst0 = cv2.resize(img0, dsize=(512, 512))
                    img = cv2.imread('./runs/detect/exp/crops/person/' + i[0])
                    dst = cv2.resize(img, dsize=(512, 512))
                    cv2.imshow('result0', dst0)
                    cv2.imshow('result', dst)
                    cv2.waitKey()
                    cv2.destroyAllWindows()


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

