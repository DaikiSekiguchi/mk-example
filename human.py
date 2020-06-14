# coding: utf-8

import rhinoscriptsyntax as rs


class Human:

    # コンストラクタ
    def __init__(self, name, pos_x, pos_y, pos_z):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.position = [pos_x, pos_y, pos_z]

    # 人がある定義領域のどこに位置しているのかを描画する
    def draw_position(self):
        rs.AddPoint(self.pos_x, self.pos_y, self.pos_z)

    # 定義域までの４つの距離を取得
    def get_distance_to_domain(self, domain):
        to_point1 = [self.pos_x, domain.origin[1], self.pos_z]
        to_point2 = [self.pos_x, domain.origin[1] + domain.y_range, self.pos_z]
        to_point3 = [domain.origin[0], self.pos_y, self.pos_z]
        to_point4 = [domain.origin[0] + domain.x_range, self.pos_y, self.pos_z]

        to_points = [to_point1, to_point2, to_point3, to_point4]

        # 距離を算出する(from_point(人の座標値) to to_point(定義域(矩形)までの距離))
        distance_list = []
        for to_point in to_points:
            distance = rs.Distance(self.position, to_point)
            distance_list.append(distance)

            # debug
            # rs.AddLine(self.position, to_point)

        return distance_list
