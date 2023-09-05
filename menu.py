#!python3
# coding=utf8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from asyncio.windows_events import NULL
import random
import pygame
from glob import glob

# 随机照片集合
picture_array = glob('./resource/pictures/*.jpg')
# 随机音乐集合
music_array = glob('./resource/music/*.mp3')

pygame.mixer.init()

class MenuWindow(QMainWindow):
    def __init__(self):
        super(MenuWindow, self).__init__()
        # 调整页面大小
        self.resize(1080, 920)
        # 设置窗口标题
        self.setWindowTitle('有趣工具箱')
        # 设置窗口透明度
        self.setWindowOpacity(0.93)
        # 窗口居中
        self.center()

        # 载入UI界面
        self.init_ui()
        # 连接信号和槽
        self.init_signal_slot()

    # UI界面设置
    def init_ui(self):
        # 添加主要功能按钮
        self.tomato_clock_button = QPushButton('番茄时钟')
        self.record_button = QPushButton('日程')
        self.website_button = QPushButton('精品网站')
        self.exit_button = QPushButton('退出')
        self.about_button = QPushButton('关于')
        self.welcome_text = QLabel('WELCOME')
        self.timer = QTimer()
        self.time_label = QLabel()

        # 添加图片按钮
        self.picture_button = QToolButton()
        self.picture_button.setText('换一换')
        # 随机选择一张图片
        self.picture_link = random.choice(picture_array)
        self.picture_button.setIcon(QIcon(self.picture_link))
        self.picture_button.setIconSize(QSize(1080, 600))
        self.picture_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.picture_button.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 添加音乐按钮
        self.play_music_button = QPushButton('随机播放一首音乐')
        self.pause_music_button = QPushButton('暂停音乐')
        self.continue_music_button = QPushButton('继续播放')
        self.music_state_label = QLabel()
        self.music_name_label = QLabel()
        self.music_link = NULL

        # 按钮样式设置
        self.welcome_text.setFixedHeight(40)
        # 标签居中
        self.welcome_text.setAlignment(Qt.AlignCenter)
        self.welcome_text.setFont(QFont('SansSerif', 18))
        self.tomato_clock_button.setFixedSize(80, 40)
        self.record_button.setFixedSize(80, 40)
        self.website_button.setFixedSize(80, 40)
        self.exit_button.setFixedSize(80, 40)
        self.about_button.setFixedSize(80, 40)
        self.play_music_button.setFixedSize(180, 60)
        self.continue_music_button.setFixedSize(82, 78)
        self.pause_music_button.setFixedSize(82, 78)
        self.music_state_label.setFixedWidth(40)
        self.music_name_label.setFont(QFont('Perpetua', 10))
        # 开始时标签为灰色代表音乐未播放
        self.music_state_label.setStyleSheet(
            '''QLabel{background:gainsboro;border-radius:5px;}''')
        # 标签居中
        self.time_label.setAlignment(Qt.AlignCenter)
        self.tomato_clock_button.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:20px;}QPushButton:hover{background:red;}''')
        self.record_button.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:20px;}QPushButton:hover{background:yellow;}''')
        self.website_button.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:20px;}QPushButton:hover{background:green;}''')
        self.exit_button.setStyleSheet(
            '''QPushButton{background:#FFFAF0;border-radius:20px;}QPushButton:hover{background:honeydew;}''')
        self.about_button.setStyleSheet(
            '''QPushButton{background:#F0F8FF;border-radius:20px;}QPushButton:hover{background:lightblue;}''')
        self.play_music_button.setStyleSheet(
            '''QPushButton{background:#F0FFFF;border-radius:20px;}QPushButton:hover{background:aliceblue;}''')
        self.pause_music_button.setStyleSheet(
            '''QPushButton{background:#FFEBCD	;border-radius:20px;}QPushButton:hover{background:beige;}''')
        self.continue_music_button.setStyleSheet(
            '''QPushButton{background:#F0FFF0;border-radius:20px;}QPushButton:hover{background:paleturquoise;}''')
        self.tomato_clock_button.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:20px;}QPushButton:hover{background:red;}''')

        # 提示信息
        QToolTip.setFont(QFont('SansSerif', 10))
        self.exit_button.setToolTip('退出程序')
        self.tomato_clock_button.setToolTip('使用番茄时钟')
        self.record_button.setToolTip('使用日程')
        self.website_button.setToolTip('使用精品网站')
        self.about_button.setToolTip('查看关于')
        self.picture_button.setToolTip('点击切换图片')
        self.play_music_button.setToolTip('点击播放音乐')
        self.pause_music_button.setToolTip('点击暂停播放音乐')
        self.continue_music_button.setToolTip('点击继续播放音乐')
        self.music_state_label.setToolTip('灰色：音乐未播放\n黄色：音乐暂停\n绿色：音乐播放中')

        # 设置水平/垂直布局（将按钮放到布局中）
        hlayout1 = QHBoxLayout()
        hlayout2 = QHBoxLayout()
        vlayout = QVBoxLayout()
        hlayout1.addWidget(self.tomato_clock_button, 1)
        hlayout1.addWidget(self.record_button, 1)
        hlayout1.addWidget(self.website_button, 1)
        hlayout1.addWidget(self.exit_button, 1)
        hlayout1.addWidget(self.about_button, 1)
        hlayout2.addWidget(self.pause_music_button, 1, Qt.AlignCenter)
        hlayout2.addWidget(self.music_name_label, 1, Qt.AlignCenter)
        hlayout2.addWidget(self.continue_music_button, 1, Qt.AlignCenter)
        vlayout.addWidget(self.welcome_text, 1)
        vlayout.addSpacing(5)
        vlayout.addWidget(self.time_label, 1)
        vlayout.addLayout(hlayout1)
        # 设置间距
        vlayout.addSpacing(12)
        vlayout.addWidget(self.picture_button, 1)
        # 设置间距
        vlayout.addSpacing(26)
        # 按键居中
        vlayout.addWidget(self.play_music_button, 1, Qt.AlignCenter)
        # 设置间距
        vlayout.addSpacing(5)
        vlayout.addLayout(hlayout2)
        vlayout.addWidget(self.music_state_label, 1, Qt.AlignCenter)

        # 框架放到窗口上
        up_frame = QWidget()
        up_frame.setLayout(vlayout)
        self.setCentralWidget(up_frame)

    # 将信号与槽关联
    def init_signal_slot(self):
        self.tomato_clock_button.clicked.connect(self.on_tomato_clock_button)
        self.exit_button.clicked.connect(self.on_exit_button)
        self.about_button.clicked.connect(self.on_about_button)
        self.picture_button.clicked.connect(self.on_picture_button)
        self.record_button.clicked.connect(self.on_record_button)
        self.website_button.clicked.connect(self.on_website_buttion)
        self.play_music_button.clicked.connect(self.on_play_music_button)
        self.pause_music_button.clicked.connect(self.on_pause_music_button)
        self.continue_music_button.clicked.connect(self.on_continue_music_button)
        # 通过调用槽函数来刷新时间
        self.timer.timeout.connect(
            lambda: self.show_current_time(self.time_label))
        # 每隔一秒刷新一次
        self.timer.start(1000)

    # 打开关于
    def on_about_button(self, event):
        # 创建一个消息框,上面有一按钮:Yes
        reply = QMessageBox.question(self, 'information',
                                     "软件名称：有趣工具箱\n大致功能有:\n日程记录、精品网站收集、番茄时钟\n图片切换、音乐播放\n\n作者:  Mychord",
                                     QMessageBox.Ok, QMessageBox.Ok)
        # 点击OK按钮关闭组件
        if reply == QMessageBox.Ok:
            pass

    # 切换图片
    def on_picture_button(self):
        # 随机选择一张图片
        link = random.choice(picture_array)
        # 使用循环判断使切换的图片不重复
        while link == self.picture_link:
            # 随机选择一张图片
            link = random.choice(picture_array)
        self.picture_link = link
        self.picture_button.setIcon(QIcon(self.picture_link))

    # 按下随机播放音乐按钮
    def on_play_music_button(self):
        # 随机选择一首音乐
        link = random.choice(music_array)
        # 使用循环判断使切换的音乐不重复
        while link == self.music_link:
            # 随机选择一首音乐
            link = random.choice(music_array)
        self.music_link = link
        # 标签变绿色代表正在播放音乐
        self.music_state_label.setStyleSheet(
            '''QLabel{background:mediumaquamarine;border-radius:5px;}''')
        self.music_play(self.music_link)

    # 音乐播放
    def music_play(self, music_name):
        try:
            # 载入音乐
            pygame.mixer.music.load(music_name)
            # 截取字串输出音乐名
            music_str = ""
            for i in range(len(music_name)):
                if music_name[i] == '\\':
                    music_str = music_name[i+1:]
                    break
            # 显示音乐名称
            self.music_name_label.setText(music_str)
            # 播放音乐
            pygame.mixer.music.play()
        except Exception as e:
            print(e)

    # 音乐暂停播放
    def on_pause_music_button(self):
        pygame.mixer.music.pause()
        # 标签变黄色代表音乐暂停播放
        self.music_state_label.setStyleSheet(
            '''QLabel{background:gold;border-radius:5px;}''')

    # 音乐继续播放
    def on_continue_music_button(self):
        pygame.mixer.music.unpause()
        # 标签变绿色代表正在播放音乐
        self.music_state_label.setStyleSheet(
            '''QLabel{background:mediumaquamarine;border-radius:5px;}''')

    # 打开番茄时钟界面
    def on_tomato_clock_button(self):
        pass

    # 打开日程界面
    def on_record_button(self):
        pass

    # 打开精品网站界面
    def on_website_buttion(self):
        pass

    # 窗口居中
    def center(self):
        # 获得主窗口所在的框架
        qr = self.frameGeometry()
        # 获取显示器的分辨率,然后得到屏幕中间点的位置
        cp = QDesktopWidget().availableGeometry().center()
        # 通过move函数把主窗口的左上角移动到其框架的左上角,使得窗口居中
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 按下关闭程序按钮
    def on_exit_button(self):
        self.close_event(self)

    # 关闭确认
    def close_event(self, event):
        # 创建一个消息框,上面有俩按钮:Yes 和 No
        reply = QMessageBox.question(self, 'Message',
                                     'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # 判断返回值,如果点击的是 Yes 按钮,就关闭组件和应用,否则就忽略关闭事件
        if reply == QMessageBox.Yes:
            # 创建应用程序对象
            app = QApplication.instance()
            # 退出应用程序
            app.quit()
        else:
            pass

    # 获取当前时间
    def show_current_time(self, time_label):
        # 获取系统当前时间
        time = QDateTime.currentDateTime()
        # 设置系统时间的显示格式
        time_display = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        # 状态栏显示
        time_label.setText(time_display)
