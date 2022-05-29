from libs.setting_app import SettingApp


def main():
    setting_app = SettingApp()
    setting_app.run()
    try:
        manager = setting_app.generated_manager
    except AttributeError:
        exit(1)

    manager.forward()


if __name__ == "__main__":
    main()
