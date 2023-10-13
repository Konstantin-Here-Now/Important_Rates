import wx
from wx.adv import TaskBarIcon, EVT_TASKBAR_LEFT_DOWN

from scripts import app_logger
from scripts.rates_dataset import RatesDataset
from scripts.window.window_show import show_window

TRAY_TOOLTIP = 'Курсы ЦБ'
TRAY_ICON = 'assets/cb_logo.png'

logger = app_logger.get_logger('main')


def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.Append(item)
    return item


class OurTaskBarIcon(TaskBarIcon):
    def __init__(self, frame):
        self.frame = frame
        super(OurTaskBarIcon, self).__init__()
        self.set_icon(TRAY_ICON)
        self.Bind(EVT_TASKBAR_LEFT_DOWN, self.on_left_down)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        # create_menu_item(menu, 'Menu Function', self.some_menu_func)
        # menu.AppendSeparator()
        create_menu_item(menu, 'Закрыть', self.on_exit)
        return menu

    def set_icon(self, path):
        icon = wx.Icon(wx.Bitmap(path))
        self.SetIcon(icon, TRAY_TOOLTIP)

    def on_left_down(self, event):
        """
        Not a static method.
        """
        show_window(dataset)

    # def some_menu_func(self, event):
    #     print('I am some menu function!')

    def on_exit(self, event):
        logger.info('App manually closed.')
        wx.CallAfter(self.Destroy)
        self.frame.Close()


class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(None)
        self.SetTopWindow(frame)
        OurTaskBarIcon(frame)
        return True


def windows_main():
    app = App(False)
    logger.info('App ready to use.')
    app.MainLoop()


if __name__ == '__main__':
    dataset = RatesDataset()
    logger.info('Got data for further use.')
    windows_main()
