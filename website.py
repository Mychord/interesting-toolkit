#!python3
# coding=utf8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import sip
import json


class WebsiteWindow(QMainWindow):
    def __init__(self):
        super(WebsiteWindow, self).__init__()
        self.resize(1080, 920)
        # 窗口居中
        self.center()
        self.init_ui()
        self.init_signal_slot()

        # 数据初始化
        self.init_data()

        # 设置标题
        self.setWindowTitle('精品网站')

    # UI界面设置
    def init_ui(self):
        self.vLayout = QVBoxLayout()
        self.hLayout = QHBoxLayout()

        # 添加按钮
        self.create_button = QPushButton('添加', self)
        self.save_button = QPushButton('保存', self)
        self.back_button = QPushButton('返回', self)

        # 按钮样式设置
        self.create_button.setFixedSize(40, 40)
        self.back_button.setFixedSize(40, 40)
        self.save_button.setFixedSize(40, 40)
        self.create_button.setStyleSheet(
            '''QPushButton{background:#9ACD32;border-radius:20px;}QPushButton:hover{background:springgreen;}''')
        self.save_button.setStyleSheet(
            '''QPushButton{background:#F5F5F5;border-radius:20px;}QPushButton:hover{background:lavender;}''')
        self.back_button.setStyleSheet(
            '''QPushButton{background:#FFEFD5;border-radius:20px;}QPushButton:hover{background:lightcyan;}''')

        # 设置提示词
        QToolTip.setFont(QFont('SansSerif', 10))
        self.create_button.setToolTip('单击新添网站')
        self.save_button.setToolTip('单击保存')
        self.back_button.setToolTip('单击返回主页面')

        # 摆放控件
        self.hLayout.addWidget(self.create_button, 1)
        self.hLayout.addWidget(self.save_button, 1)
        self.hLayout.addWidget(self.back_button, 1)
        self.vLayout.addLayout(self.hLayout)

        # 框架放到窗口上
        self.up_frame = QWidget()
        self.up_frame.setLayout(self.vLayout)
        self.setMenuWidget(self.up_frame)

    # 将信号与槽关联
    def init_signal_slot(self):
        self.create_button.clicked.connect(self.create_website)
        self.save_button.clicked.connect(self.save_websites)
        self.back_button.clicked.connect(self.back_event)

    # 初始化数据
    def init_data(self):
        # 数据文件路径
        self.file_path = './resource/datas/websites.json'
        # 数据
        self.websites = []
        # 载入网站
        self.load_websites()

    # 创造新的网站记录
    def create_website(self):
        self.website_name = ''
        self.website_address = ''
        # 网站总数大于20个则不再增加
        if len(self.websites) >= 20:
            reply = QMessageBox.question(self, 'information',
                                         '最多存在20个网站',
                                         QMessageBox.Ok, QMessageBox.Ok)
            # 点 OK 按钮关闭组件
            if reply == QMessageBox.Ok:
                pass
        elif self.input_website() == True:
            website = '网站:{name}  <a href="{address}">点击打开查看</a>'.format(
                name=self.website_name, address=self.website_address)
            self.build_website(website)
        else:
            pass

    # 网站名 UI 界面建立
    def build_website(self, website):
        # 删除按钮等
        new_delete_button = QPushButton('删除网站')
        new_website = QLabel()

        # 增加提示词
        QToolTip.setFont(QFont('SansSerif', 10))
        new_delete_button.setToolTip('单击按钮删除记录')

        # 样式设置
        new_delete_button.setFixedHeight(25)
        new_delete_button.setFont(QFont('SansSerif', 11))
        new_website.setFont(QFont('SansSerif', 11))
        new_website.setText(website)
        new_website.setFixedHeight(25)
        # 使其成为超链接
        new_website.setOpenExternalLinks(True)
        # 双击可选中文本
        new_website.setTextInteractionFlags(
            Qt.TextBrowserInteraction)

        # 直接连接槽与信号
        new_delete_button.clicked.connect(
            lambda: self.on_delete_button(website, new_delete_button, new_website))

        # 将文本框与和删除按钮合成一行
        new_hlayout = QHBoxLayout()
        new_hlayout.addWidget(new_website, 1)
        new_hlayout.addWidget(new_delete_button, 1)

        self.vLayout.addLayout(new_hlayout)
        self.vLayout.setSpacing(10)
        self.websites.append(website)

    # 初始化设置部分网站
    def load_websites(self):
        # 使用 json.load() 方法读取 JSON 文件并将其转换为 Python 对象
        with open(self.file_path, 'r') as json_file:
            datas = json.load(json_file)
        for data in datas:
            self.build_website(data)

    # 输入网址和名称
    def input_website(self):
        text1, ok1 = QInputDialog.getText(self, 'Input', '输入名称:')
        if ok1:
            if len(text1) == 0:
                reply = QMessageBox.question(self, 'information',
                                             '名称不能为空',
                                             QMessageBox.Ok, QMessageBox.Ok)
                # 点OK按钮关闭组件
                if reply == QMessageBox.Ok:
                    pass
                return False
            text2, ok2 = QInputDialog.getText(self, 'Input', '输入网址:')
            if ok2:
                if len(text2) == 0:
                    reply = QMessageBox.question(self, 'information',
                                                 '网址不能为空',
                                                 QMessageBox.Ok, QMessageBox.Ok)
                    # 点 OK 按钮关闭组件
                    if reply == QMessageBox.Ok:
                        pass
                    return False
                self.website_name = str(text1)
                self.website_address = str(text2)
                return True
        return False

    # 按下删除按钮
    def on_delete_button(self, website, item1, item2):
        self.delete_event(self, website, item1, item2)

    # 删除确认
    def delete_event(self, event, website, item1, item2):
        # 创建一个消息框,上面有俩按钮:Yes 和 No。
        reply = QMessageBox.question(self, 'Message',
                                     'Are you sure to delete this website?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # 判断返回值，如果点击的是 Yes 按钮，就删除这个网站，否则忽略该事件。
        if reply == QMessageBox.Yes:
            self.vLayout.removeWidget(item1)
            self.vLayout.removeWidget(item2)
            sip.delete(item1)
            sip.delete(item2)
            self.websites.remove(website)
        else:
            pass

    # 保存网站
    def save_websites(self):
        # 创建一个消息框,上面有俩按钮:Yes 和 No。
        reply = QMessageBox.question(self, 'Message',
                                     'Would you like to save the changes?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        # 判断返回值，如果点击的是 Yes 按钮，就保存已有改变，否则忽略该事件。
        if reply == QMessageBox.Yes:
            with open(self.file_path, 'w') as json_file:
                json.dump(self.websites, json_file,
                          ensure_ascii=False, indent=4)
        else:
            pass

    # 窗口居中
    def center(self):
        # 获得主窗口所在的框架。
        qr = self.frameGeometry()
        # 获取显示器的分辨率，然后得到屏幕中间点的位置。
        cp = QDesktopWidget().availableGeometry().center()
        # 然后通过move函数把主窗口的左上角移动到其框架的左上角，这样就把窗口居中了。
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 返回主界面
    def back_event(self, event):
        pass
