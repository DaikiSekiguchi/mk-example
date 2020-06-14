# coding: utf-8

import rhinoscriptsyntax as rs


class Domain:

    def __init__(self, origin, x_range, y_range):
        self.origin = origin
        self.x_range = x_range
        self.y_range = y_range
        self.p1 = [origin[0], origin[1], origin[2]]
        self.p2 = [origin[0], origin[1] + y_range, origin[2]]
        self.p3 = [origin[0] + x_range, origin[1] + y_range, origin[2]]
        self.p4 = [origin[0] + x_range, origin[1], origin[2]]
        self.domain_points = [self.p1, self.p2, self.p3, self.p4, self.p1]

    # 矩形を構成する4点から矩形を生成する
    def draw_domain(self):
        rs.AddPolyline(self.domain_points)