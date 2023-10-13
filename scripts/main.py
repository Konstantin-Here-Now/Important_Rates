from scripts import settings
from scripts import app_logger

logger = app_logger.get_logger('rates_dataset')


def main():
    if settings.PLATFORM == "Console":
        from scripts.console.console_run import console_main
        console_main()
    elif settings.PLATFORM == "Windows":
        from scripts.windows.windows_run import windows_main
        windows_main()
    else:
        try:
            from scripts.window.window_show import show_window
            show_window()
        except Exception as ex:
            logger.warning(ex)
            logger.warning("Platform cannot run Qt Windows. Running in console...")
            from scripts.console.console_run import console_main
            console_main()


if __name__ == '__main__':
    main()
