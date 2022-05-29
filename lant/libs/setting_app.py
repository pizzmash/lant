import tkinter

from libs.widget.setting.core import SettingWidget


class SettingApp():
    def __init__(self):
        root = tkinter.Tk()
        root.title("Settings")
        self.app = SettingWidget(root)

    def run(self):
        self.app.mainloop()
