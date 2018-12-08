# 12.3
import re


class Rectangle(object):
    def __init__(self, _id, _left_margin, _top_margin, _width, _height):
        self.id = int(_id)
        self.left_margin = int(_left_margin)
        self.top_margin = int(_top_margin)
        self.width = int(_width)
        self.height = int(_height)


if __name__ == "__main__":

    with open('./input.txt', 'r') as f:
        input_list = []
        _map = {}
        count = 0
        id_list = [0]
        for line in f.readlines():
            input_list.append(line.strip())
            match_obj = re.match(r"#(.*) @ (.*),(.*): (.*)x(.*)", line.strip())
            id = match_obj.group(1)
            left_margin = match_obj.group(2)
            top_margin = match_obj.group(3)
            width = match_obj.group(4)
            height = match_obj.group(5)
            square = Rectangle(id, left_margin, top_margin, width, height)
            input_list.append(square)
            id_list.append(1)

            for i in range(square.top_margin, square.top_margin + square.height):
                for j in range(square.left_margin, square.left_margin + square.width):
                    if _map.__contains__((i, j)):
                        _map[(i, j)].append(square.id)
                        if len(_map[(i, j)]) == 2:
                            count += 1
                    else:
                        _map[(i, j)] = [square.id]

        print(count)

        for key, _list in _map.items():
            if len(_list) > 1:
                for _id in _list:
                    id_list[_id] = 0

        for i in range(len(id_list)):
            if id_list[i]:
                print(i)
