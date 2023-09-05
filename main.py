#!python3
# coding=utf8
'''
Project: 有趣工具箱
番茄时钟 + 日程 + 精品网站 
界面切换、图片切换、音乐播放

Author: Mychord
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from tomato_clock import TomatoWindow
from record import RecordWindow
from website import WebsiteWindow
from menu import MenuWindow


class MenuWindowImprove(MenuWindow, QMainWindow):
    def __init__(self):
        super(MenuWindowImprove, self).__init__()

    # 退出应用
    def exit_event(self, event):
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
        
    # 打开番茄时钟界面
    def on_tomato_clock_button(self):
        change_window(2)

    # 打开日程界面
    def on_record_button(self):
        change_window(3)

    # 打开精品网站界面
    def on_website_buttion(self):
        change_window(4)


class TomatoWindowImprove(TomatoWindow, QMainWindow):
    def __init__(self):
        super(TomatoWindowImprove, self).__init__()

    # 返回主界面
    def back_event(self):
        change_window(1)


class RecordWindowImprove(RecordWindow, QMainWindow):
    def __init__(self):
        super(RecordWindowImprove, self).__init__()

    # 返回主界面
    def back_event(self, event):
        self.save_records()
        change_window(1)


class WebsiteWindowImprove(WebsiteWindow, QMainWindow):
    def __init__(self):
        super(WebsiteWindowImprove, self).__init__()

    # 返回主界面
    def back_event(self, event):
        self.save_websites()
        change_window(1)


def show_window(type):
    global main_window
    if type == 1:
        main_window = MenuWindowImprove()
    elif type == 2:
        main_window = TomatoWindowImprove()
    elif type == 3:
        main_window = RecordWindowImprove()
    elif type == 4:
        main_window = WebsiteWindowImprove()
    main_window.show()


def close_window():
    global main_window
    main_window.close()


def change_window(type):
    close_window()
    show_window(type)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_window(1)
    # 进入事件循环
    app.exec()
