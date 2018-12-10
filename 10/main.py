# 12.10
from tkinter import *
import re


class Point:
    def __init__(self, number, start_x, start_y, v_x, v_y):
        self.num = number
        self.x = start_x
        self.y = start_y
        self.v_x = v_x
        self.v_y = v_y

    def elapse(self):
        self.x += self.v_x
        self.y += self.v_y

    def elapse_500(self):
        self.x += 500 * self.v_x
        self.y += 500 * self.v_y


class MainWindow:

    def __init__(self, points, _length):
        self.window = Tk()
        self.points = points
        self.frame = None
        self.button = None
        self.button2 = None
        self.canvas = None
        self.actual_points = []
        self.time = 0
        self.length = _length
        self.min_x = 0
        self.min_y = 0
        self.init_window()

    def init_window(self):
        self.frame = Frame(self.window)
        self.frame.grid()  # note 1

        self.canvas = Canvas(self.frame, bg="light gray", height=800, width=800)
        self.canvas.grid(row=1, column=1)
        self.button = Button(self.frame, text="time + 1", command=self.click)
        self.button.grid(row=2, column=1, padx=4, pady=4)  # note 1 grid
        self.button2 = Button(self.frame, text="time + 500", command=self.click_500)
        self.button2.grid(row=2, column=2, padx=4, pady=4)  # note 1 grid

        self.paint()

    def click(self):
        # write whatever commands you want after clicking
        self.time += 1
        for point in self.points:
            point.elapse()
        self.clear()
        self.paint()
        print(self.time)

    def click_500(self):
        # write whatever commands you want after clicking
        self.time += 500
        for point in self.points:
            point.elapse_500()
        self.clear()
        self.paint()
        print(self.time)

    def clear(self):
        _length = len(self.actual_points)
        for i in range(_length):
            pair = self.actual_points.pop()
            for j in pair:
                self.canvas.delete(j)

    def get_length(self):
        _min_x = 10000000
        _max_x = -10000000
        _min_y = _min_x
        _max_y = _max_x
        for point in self.points:
            if point.x < _min_x:
                _min_x = point.x
            if point.x > _max_x:
                _max_x = point.x
            if point.y < _min_y:
                _min_y = point.y
            if point.y > _max_y:
                _max_y = point.y
        if (_max_x - _min_x) > (_max_y - _min_y):
            self.length = int((_max_x - _min_x) * 1.2)
        else:
            self.length = int((_max_y - _min_y) * 1.2)
        self.min_x = _min_x
        self.min_y = _min_y
        print("my_length = " + str(self.length))

    def paint(self):
        self.get_length()
        for point in self.points:
            x = int((point.x - self.min_x + 1) / self.length * 800)
            y = int((point.y - self.min_y + 1) / self.length * 800)
            line1 = self.canvas.create_line(x - 1, y - 1, x + 1, y + 1)
            line2 = self.canvas.create_line(x + 1, y - 1, x - 1, y + 1)
            self.actual_points.append((line1, line2))


if __name__ == '__main__':
    with open("./input.txt", 'r') as f:
        point_list = []
        count = 0
        min_x = 10000000
        max_x = -10000000
        min_y = min_x
        max_y = max_x
        for line in f.readlines():
            match_obj = re.match(r"position=<(.*), (.*)> velocity=<(.*), (.*)>", line.strip())
            _x = int(match_obj.group(1))
            _y = int(match_obj.group(2))
            _v_x = int(match_obj.group(3))
            _v_y = int(match_obj.group(4))
            point_list.append(Point(count, _x, _y, _v_x, _v_y))
            if _x < min_x:
                min_x = _x
            if _x > max_x:
                max_x = _x
            if _y < min_y:
                min_y = _y
            if _y > max_y:
                max_y = _y
        if (max_x - min_x) > (max_y - min_y):
            length = int((max_x - min_x) * 1.2)
        else:
            length = int((max_y - min_y) * 1.2)
        window = MainWindow(point_list, length)
        window.window.mainloop()
