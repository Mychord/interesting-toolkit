#!python3
# coding=utf8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import sip
import json


class RecordWindow(QMainWindow):
    def __init__(self):
        super(RecordWindow, self).__init__()
        self.resize(1080, 920)
        # 窗口居中
        self.center()
        self.init_ui()
        self.init_signal_slot()

        # 载入已有信息
        self.init_data()

        # 设置标题
        self.setWindowTitle("日程")

    # UI界面设置
    def init_ui(self):
        self.vLayout = QVBoxLayout()
        self.hLayout = QHBoxLayout()

        # 添加按钮
        self.create_record_button = QPushButton('新建日程', self)
        self.back_button = QPushButton('返回', self)
        self.save_button = QPushButton('保存', self)

        # 文本编辑框
        self.text_edit = QTextEdit()

        # 按钮样式设置
        self.create_record_button.setFixedSize(80, 28)
        self.back_button.setFixedSize(80, 28)
        self.save_button.setFixedSize(80, 28)
        self.create_record_button.setStyleSheet(
            '''QPushButton{background:#FFFAF0;border-radius:20px;}QPushButton:hover{background:lightblue;}''')
        self.back_button.setStyleSheet(
            '''QPushButton{background:#FFFAF0;border-radius:20px;}QPushButton:hover{background:lightcyan;}''')
        self.save_button.setStyleSheet(
            '''QPushButton{background:#FFE4C4;border-radius:20px;}QPushButton:hover{background:lavender;}''')

        # 设置提示词
        QToolTip.setFont(QFont('SansSerif', 10))
        self.create_record_button.setToolTip('单击新建一个日程')
        self.back_button.setToolTip('单击返回主页面')
        self.save_button.setToolTip('单击保存')

        # 摆放控件
        self.hLayout.addWidget(self.create_record_button, 1)
        self.hLayout.addWidget(self.save_button, 1)
        self.hLayout.addWidget(self.back_button, 1)
        self.vLayout.addLayout(self.hLayout)

        # 框架放到窗口上
        self.up_frame = QWidget()
        self.up_frame.setLayout(self.vLayout)
        self.setMenuWidget(self.up_frame)

    # 将信号与槽关联
    def init_signal_slot(self):
        self.create_record_button.clicked.connect(self.create_record)
        self.save_button.clicked.connect(self.save_records)
        self.back_button.clicked.connect(self.back_event)

    # 初始化数据
    def init_data(self):
        # 数据文件路径
        self.file_path = './resource/datas/records.json'
        # 数据
        self.records = []
        # 删除按钮
        self.delete_buttons = []
        # 载入网站
        self.load_records()

    # 创造新的日程
    def create_record(self):
        # 日程总数大于12条则跳过
        if len(self.records) >= 12:
            reply = QMessageBox.question(self, 'information',
                                         "最多存在12条日程",
                                         QMessageBox.Ok, QMessageBox.Ok)
            # 点OK按钮关闭组件
            if reply == QMessageBox.Ok:
                pass
        else:
            self.build_record('')

    # 日程记录 UI 界面建立
    def build_record(self, record):
        # 删除按钮等
        new_delete_button = QPushButton("删除")
        new_text_edit = QTextEdit()

        # 增加提示词
        QToolTip.setFont(QFont('SansSerif', 10))
        new_delete_button.setToolTip('单击按钮删除该条日程')

        # 样式设置
        new_delete_button.setFixedHeight(54)
        new_text_edit.setFont(QFont('SansSerif', 11))
        new_text_edit.setPlainText(record)
        new_text_edit.setFixedHeight(54)
        new_text_edit.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)

        index = len(self.records)
        # 直接连接信号和槽
        new_delete_button.clicked.connect(
            lambda: self.on_delete_button(index))

        # 将文本框与和删除按钮合成一行
        new_hlayout = QHBoxLayout()
        new_hlayout.addWidget(new_text_edit)
        new_hlayout.addWidget(new_delete_button)

        self.vLayout.addLayout(new_hlayout)
        self.vLayout.setSpacing(10)
        self.records.append(new_text_edit)
        self.delete_buttons.append(new_delete_button)

    # 按下删除按钮
    def on_delete_button(self, index):
        self.delete_event(self, index)

    # 删除确认
    def delete_event(self, event, index):
        def reconnect(item, number):
            item.clicked.disconnect()
            item.clicked.connect(lambda: self.on_delete_button(number))

        # 创建一个消息框,上面有俩按钮:Yes和No。
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to delete this message?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # 判断返回值，如果点击的是Yes按钮，就删除这条日程，否则忽略该事件。
        if reply == QMessageBox.Yes:
            item1 = self.records.pop(index)
            item2 = self.delete_buttons.pop(index)
            self.vLayout.removeWidget(item1)  # 移除控件
            self.vLayout.removeWidget(item2)  # 移除控件
            sip.delete(item1)  # 彻底删除控件
            sip.delete(item2)  # 彻底删除控件
            for index, item in enumerate(self.delete_buttons):
                reconnect(item, index)
        else:
            pass

    # 保存日程
    def save_records(self):
        # 创建一个消息框,上面有俩按钮:Yes 和 No。
        reply = QMessageBox.question(self, 'Message',
                                     'Would you like to save the changes?', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Yes)
        # 判断返回值
        if reply == QMessageBox.Cancel:
            return False
        elif reply == QMessageBox.Yes:
            with open(self.file_path, 'w') as json_file:
                json.dump([record.toPlainText() for record in self.records], json_file,
                          ensure_ascii=False, indent=4)
        return True

    # 加载已有日程
    def load_records(self):
        # 使用 json.load() 方法读取 JSON 文件并将其转换为 Python 对象
        with open(self.file_path, 'r') as json_file:
            datas = json.load(json_file)
        for data in datas:
            self.build_record(data)

    # 窗口居中
    def center(self):
        # 获得主窗口所在的框架。
        qr = self.frameGeometry()
        # 获取显示器的分辨率，然后得到屏幕中间点的位置。
        cp = QDesktopWidget().availableGeometry().center()
        # 然后通过move函数把主窗口的左上角移动到其框架的左上角，这样就把窗口居中了。
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 返回确认
    def back_event(self, event):
        pass
