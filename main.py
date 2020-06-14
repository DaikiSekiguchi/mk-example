# coding: utf-8

import csv
from random import randint
from human import *
from domain import *


def export_csv(contents):
    with open("distance_list.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(contents)


if __name__ == "__main__":
    # domain Rect info
    origin_p = [0, 0, 0]
    rect_width = 5000
    rect_height = 5000
    domain = Domain(origin_p, rect_width, rect_height)
    domain.draw_domain()  # 基準となる矩形を描画する

    # Human info→このプログラムでは10人分の処理を行う
    human_distance_list = []

    for i in range(10):
        human_name = i
        position_x = randint(0, rect_width)  # 人(点)が指定された領域のどこにいるか(x座標)
        position_y = randint(0, rect_height)  # 人(点)が指定された領域のどこにいるか(y座標)
        position_z = 0  # 人(点)が指定された領域のどこにいるか(z座標)→今回は平面として設定
        human = Human(human_name, position_x, position_y, position_z)  # Humanインスタンス生成
        human.draw_position()  # 人の位置を描画する

        # 定義域内に位置する人(点)から定義域内への４つの距離を取得する
        distance_list = human.get_distance_to_domain(domain)
        human_distance_list.append(distance_list)

    # 距離情報をCSVファイルに書き込む
    export_csv(human_distance_list)
