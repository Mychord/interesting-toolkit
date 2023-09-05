#!python3
# coding=utf8
from time import sleep
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# 当前剩余时间
tomato_time = 0


class TomatoWindow(QMainWindow):
    def __init__(self):
        super(TomatoWindow, self).__init__()
        self.resize(1080, 920)
        # 设置窗口透明度
        self.setWindowOpacity(0.97)
        # 窗口居中
        self.center()
        self.remainSeconds = tomato_time
        self.init_ui()
        self.init_signal_slot()
        self.setWindowTitle('番茄时钟')
        self.update()

    # UI界面设置
    def init_ui(self):
        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()
        self.vNum = QLCDNumber(self)

        # 添加按钮
        self.start_button_15 = QPushButton('计时15分钟', self)
        self.start_button_20 = QPushButton('计时20分钟', self)
        self.start_button_30 = QPushButton('计时30分钟', self)
        self.back_button = QPushButton('返回', self)
        self.clear_buttion = QPushButton('清零', self)
        self.start_button_15.setStyleSheet(
            '''QPushButton{background:#FFFAF0;border-radius:20px;}QPushButton:hover{background:lightblue;}''')
        self.start_button_20.setStyleSheet(
            '''QPushButton{background:#FFFAF0;border-radius:20px;}QPushButton:hover{background:lightblue;}''')
        self.start_button_30.setStyleSheet(
            '''QPushButton{background:#FFFAF0;border-radius:20px;}QPushButton:hover{background:lightblue;}''')
        self.back_button.setStyleSheet(
            '''QPushButton{background:#FFFAF0;border-radius:20px;}QPushButton:hover{background:lightblue;}''')
        self.clear_buttion.setStyleSheet(
            '''QPushButton{background:#FFFAF0;border-radius:20px;}QPushButton:hover{background:lightblue;}''')

        # 显示数字样式修改
        self.vNum.setStyleSheet('''\
        QLCDNumber{
            color: mediumaquamarine;
            background-color: azure;
        }
        ''')

        # 设置提示词
        QToolTip.setFont(QFont('SansSerif', 10))
        self.start_button_15.setToolTip('单击按钮开始计时')
        self.start_button_20.setToolTip('单击按钮开始计时')
        self.start_button_30.setToolTip('单击按钮开始计时')
        self.back_button.setToolTip('单击按钮返回主页面')
        self.clear_buttion.setToolTip('单击按钮清零时间')

        # 摆放控件
        hLayout.addWidget(self.start_button_15, stretch=1)
        hLayout.addWidget(self.start_button_20, stretch=1)
        hLayout.addWidget(self.start_button_30, stretch=1)
        hLayout.addWidget(self.clear_buttion, stretch=1)
        hLayout.addWidget(self.back_button, stretch=1)
        vLayout.addWidget(self.vNum, stretch=1)
        vLayout.addLayout(hLayout)

        # 框架放到窗口上
        frame = QWidget()
        frame.setLayout(vLayout)
        self.setCentralWidget(frame)

    # 将信号与槽关联
    def init_signal_slot(self):
        self.timer = QTimer(self)
        self.start_button_15.clicked.connect(self.init_time_15)
        self.start_button_20.clicked.connect(self.init_time_20)
        self.start_button_30.clicked.connect(self.init_time_30)
        self.clear_buttion.clicked.connect(self.on_clear_button)
        self.back_button.clicked.connect(self.back_event)
        self.timer.timeout.connect(self.on_timer)

    # 获取剩余的分钟和秒数
    def get_remain_seconds(self):
        minute = self.remainSeconds // 60
        second = self.remainSeconds % 60
        return f'{minute:02d}:{second:02d}'

    # 更新时间
    def update(self):
        self.vNum.display(self.get_remain_seconds())

    # 十五分钟
    def init_time_15(self):
        global tomato_time
        tomato_time = 15 * 60
        self.start_count()

    # 二十分钟
    def init_time_20(self):
        global tomato_time
        tomato_time = 20 * 60
        self.start_count()

    # 三十分钟
    def init_time_30(self):
        global tomato_time
        tomato_time = 30 * 60
        self.start_count()

    # 开始计时
    def start_count(self):
        self.remainSeconds = tomato_time
        self.timer.start(1000)
        self.update()

    # 时间清零
    def on_clear_button(self):
        self.remainSeconds = 0

    # 时间流动
    def on_timer(self):
        self.remainSeconds -= 1
        if self.remainSeconds < 0:
            self.remainSeconds = 0
            self.timer.stop()
        self.update()

    # 窗口居中
    def center(self):
        # 获得主窗口所在的框架
        qr = self.frameGeometry()
        # 获取显示器的分辨率,然后得到屏幕中间点的位置
        cp = QDesktopWidget().availableGeometry().center()
        # 然后通过move函数把主窗口的左上角移动到其框架的左上角,这样就把窗口居中了
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 返回主界面
    def back_event(self):
        pass
