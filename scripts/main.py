import app_logger
import settings

logger = app_logger.get_logger('main')


def main():
    if settings.PLATFORM == "Console":
        logger.info("Running in console...")
        from runners.console_run import console_main
        console_main()
    elif settings.PLATFORM == "Windows":
        logger.info("Running on Windows...")
        from runners.windows_run import windows_main
        windows_main()
    else:
        try:
            from scripts.window_show import show_window
            show_window()
        except Exception as ex:
            logger.warning(ex)
            logger.warning("Platform cannot run Qt Windows. Running in console...")
            from runners.console_run import console_main
            console_main()


if __name__ == '__main__':
    main()
