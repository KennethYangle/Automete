from utils import *
import argparse
import json
import time


def search(settings, s, is_first=False):
    """读入倾角，返回评价值"""
    if s in stash.keys():
        print(s, stash[s])
        return stash[s]

    if is_first:
        p = settings["LocationSelection"]["Next"]
        mouse_click(p[0], p[1])
        is_first = False

    p = settings["Modifications"]["Inclination"]
    mouse_dclick(p[0], p[1])
    key_input(str(s))
    time.sleep(1)

    p = settings["ResultsAndExport"]["Menu"]
    mouse_click(p[0], p[1])
    time.sleep(10)

    p = settings["ResultsAndExport"]["Year"]
    mouse_click(p[0], p[1])
    key_input("Cc")

    # time.sleep(1)
    p = settings["Modifications"]["Menu"]
    mouse_click(p[0], p[1])

    data = find_nums(readtxt())
    stash[s] = data[1]
    print(s, stash[s])
    return stash[s]

def main(args):
    # 准备阶段
    print("Location selection菜单下，选好城市，按回车确认")
    while True:
        if get_one_key() == 13:
            break

    # 读配置文件
    settings_file = open(args.settings_file)
    settings = json.load(settings_file)
    print(settings)

    search(settings, 10, True)
    search(settings, 20)

    # 根据先验值粗调，没有则遍历
    search_coarse = list()
    if args.prior > 0:
        for a in range(args.prior-10, args.prior+15, 5):
            if a > 0:
                search_coarse.append(a)
    else:
        for a in range(0, 95, 5):
            search_coarse.append(a)

    best_coarse, best_value = 0, 0
    for s in search_coarse:
        value = search(settings, s)
        if value > best_value:
            best_coarse, best_value = s, value
        else: break
    
    # 微调
    search_fine = list()
    for a in range(best_coarse-4, best_coarse+5):
        if a > 0:
            search_fine.append(a)

    best_fine, best_value = 0, 0
    values = list()
    for s in search_fine:
        value = search(settings, s)
        values.append([s, value])
        if value >= best_value:
            best_fine, best_value = s, value
        else: break

    values.sort(key=lambda x: (-x[1], x[0]))
    print("最佳倾角: {}".format(values[0][0]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", dest="settings_file", default="./settings.json")
    parser.add_argument("-p", dest="prior", type=int, default=-1)
    args = parser.parse_args()
    print(args)
    stash = dict()
    main(args)