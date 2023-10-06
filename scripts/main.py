from scripts import settings


def main():
    if settings.PLATFORM == "Windows":
        from scripts.windows.windows_run import windows_main
        windows_main()
    else:
        from scripts.console.console_run import console_main
        console_main()


if __name__ == '__main__':
    main()
