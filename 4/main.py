# 12.4
import re


if __name__ == '__main__':
    with open("./input.txt", 'r') as f:
        input_list = {}  # datetime, event
        _map = {}  # id : list(minute, times)
        for line in f.readlines():
            match_object = re.match(r"\[(.*)\] (.*)", line.strip())
            input_list[match_object.group(1)] = match_object.group(2)
            if "begins shift" in match_object.group(2):
                month = int(match_object.group(1)[5:7])
                date = int(match_object.group(1)[8:10])

        input_list = [(k, input_list[k]) for k in sorted(input_list.keys())]
        start = 0
        end = 0
        _id = 0
        for (_time, event) in input_list:
            if "shift" in event:
                _id = re.match(r"Guard #(.*) begins shift", event).group(1)
                _id = int(_id)
            elif "asleep" in event:
                start = int(_time[-2:])
            elif "wake" in event:
                end = int(_time[-2:])
                if start:
                    if _map.__contains__(_id):
                        for i in range(start, end):
                            _map[_id][i] += 1
                    else:
                        _list = []
                        for i in range(60):
                            _list.append(0)

                        _map[_id] = _list
                        for i in range(start, end):
                            _map[_id][i] += 1

        chosen_id = 0
        max_length = 0
        max_times = 0
        minute = 0
        for _id, _list in _map.items():
            length = sum(_list)
            if length > max_length:
                chosen_id = _id
                max_length = length
                list_max = max(_list)
                max_times = list_max
                minute = _list.index(list_max)

        print(chosen_id * minute)

        chosen_id = 0
        max_times = 0
        minute = 0
        for _id, _list in _map.items():
            list_max = max(_list)
            if list_max > max_times:
                chosen_id = _id
                max_times = list_max
                minute = _list.index(list_max)

        print(chosen_id * minute)
