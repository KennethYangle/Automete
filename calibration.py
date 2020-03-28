import json
import argparse
from utils import *

def main(args):
    settings = dict()
    settings["LocationSelection"] = dict()
    settings["Modifications"] = dict()
    settings["ResultsAndExport"] = dict()

    print("标定开始")
    print("Location selection菜单下，选好城市")
    print("鼠标放在Next上，按下回车")
    while True:
        if get_one_key() == 13:
            p = get_mouse_point()
            time.sleep(0.01)
            break
    settings["LocationSelection"]["Next"] = p
    print("点击Next")

    print("鼠标放在Inclination框上，按下回车")
    while True:
        if get_one_key() == 13:
            p = get_mouse_point()
            time.sleep(0.01)
            break
    settings["Modifications"]["Inclination"] = p

    print("鼠标放在Results and export菜单栏上，按下回车")
    while True:
        if get_one_key() == 13:
            p = get_mouse_point()
            time.sleep(0.01)
            break
    settings["ResultsAndExport"]["Menu"] = p
    print("点击Results and export菜单栏，等待计算完成")

    print("点击Data table")
    print("鼠标放在Year行数据上，按下回车")
    while True:
        if get_one_key() == 13:
            p = get_mouse_point()
            time.sleep(0.01)
            break
    settings["ResultsAndExport"]["Year"] = p

    print("鼠标放在Modifications & data import菜单栏上，按下回车")
    while True:
        if get_one_key() == 13:
            p = get_mouse_point()
            time.sleep(0.01)
            break
    settings["Modifications"]["Menu"] = p
    print("标定完成")

    string = json.dumps(settings, indent=4)
    with open(args.settings_file, 'w')as f:
        f.write(string)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", dest="settings_file", default="./settings.json")
    args = parser.parse_args()
    print(args)
    main(args)
