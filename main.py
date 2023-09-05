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
import tomato_clock
import record
import website
import menu


class MenuWindowImprove(menu.MenuWindow, QMainWindow):
    def __init__(self):
        super(MenuWindowImprove, self).__init__()

    # 打开番茄时钟界面
    def on_tomato_clock_button(self):
        change_window(2)

    # 打开日程界面
    def on_record_button(self):
        change_window(3)

    # 打开精品网站界面
    def on_website_buttion(self):
        change_window(4)


class TomatoWindowImprove(tomato_clock.TomatoWindow, QMainWindow):
    def __init__(self):
        super(TomatoWindowImprove, self).__init__()

    def back_event(self):
        change_window(1)


class RecordWindowImprove(record.RecordWindow, QMainWindow):
    def __init__(self):
        super(RecordWindowImprove, self).__init__()

    def back_event(self, event):
        # 创建一个消息框,上面有俩按钮:Yes 和 No
        reply = QMessageBox.question(self, 'Message',
                                     'Have you saved the messages?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # 如果已经保存，则返回主界面，否则进一步提醒
        if reply == QMessageBox.Yes:
            change_window(1)
        else:
            reply_s = QMessageBox.question(self, 'Message',
                                           'Are you sure to leave?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply_s == QMessageBox.Yes:
                change_window(1)
            else:
                pass


class WebsiteWindowImprove(website.WebsiteWindow, QMainWindow):
    def __init__(self):
        super(WebsiteWindowImprove, self).__init__()

    def back_event(self, event):
        # 创建一个消息框,上面有俩按钮:Yes 和 No
        reply = QMessageBox.question(self, 'Message',
                                     'Would you like to save the changes?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        # 如果已经保存，则返回主界面，否则进一步提醒
        if reply == QMessageBox.Yes:
            self.save_file()
        else:
            pass
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
