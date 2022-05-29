from libs.domain.direction import Direction
from libs.domain.position import Position
from libs.util.simlator import Simulator
from libs.domain.ant import Ant
from libs.domain.field import Field
from libs.setting_app import SettingApp
from libs.canvas_app import CanvasApp


def main():
    setting_app = SettingApp()
    setting_app.run()
    try:
        simulator = setting_app.app.generated_simulator
    except AttributeError:
        print("error")
        exit(1)
    
    canvas_app = CanvasApp(simulator=simulator,
                           size=500,
                           plus_minus_range=50,
                           ants_color="#FF8080",
                           bg_color="#404040",
                           field_states_colors=["#8080FF", "#FFFF80"])
    canvas_app.run()


if __name__ == "__main__":
    main()
