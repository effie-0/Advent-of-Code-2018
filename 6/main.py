# 12.6
import re
import time


class Cluster:
    def __init__(self, n, _x, _y):
        self.number = n
        self.x = _x
        self.y = _y
        self.is_inf = False
        self.region = 0


def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == '__main__':
    start = time.time()
    with open("./input.txt", 'r') as f:
        cluster_list = []
        count = 0
        min_x = 1000
        min_y = 1000
        max_x = 0
        max_y = 0
        for line in f.readlines():
            match_obj = re.match(r"(.*), (.*)", line.strip())
            x = int(match_obj.group(1))
            y = int(match_obj.group(2))
            cluster_list.append(Cluster(count, x, y))
            count += 1
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y

        # itinerate the outermost part of the rectangle to find the infinitive boundary
        min_x -= 1
        min_y -= 1
        max_x += 1
        max_y += 1
        list_y = [min_y, max_y]
        list_x = [min_x, max_x]
        inf_list = []
        for i in range(min_x, max_x + 1):
            for q in range(2):
                j = list_y[q]
                dis = 10000
                temp_num = -1
                length = len(cluster_list)
                for k in range(length):
                    cluster = cluster_list[k]
                    _dis = distance(i, j, cluster.x, cluster.y)
                    if _dis < dis:
                        temp_num = k
                        dis = _dis
                if temp_num == -1:
                    continue
                if not cluster_list[temp_num].is_inf:
                    cluster_list[temp_num].is_inf = True
                    inf_list.append(cluster_list[temp_num].number)

        for j in range(min_y, max_y + 1):
            for q in range(2):
                i = list_x[q]
                dis = 10000
                temp_num = -1
                length = len(cluster_list)
                for k in range(length):
                    cluster = cluster_list[k]
                    _dis = distance(i, j, cluster.x, cluster.y)
                    if _dis < dis:
                        temp_num = k
                        dis = _dis
                if temp_num == -1:
                    continue
                if not cluster_list[temp_num].is_inf:
                    cluster_list[temp_num].is_inf = True
                    inf_list.append(cluster_list[temp_num].number)

        # count all the distances, the algorithm is similar to K-means / SLIC
        length = len(cluster_list)
        count = 0
        dist_map = {}
        number_map = {}
        total_map = {}
        for i in range(min_x, max_x + 1):
            for j in range(min_y, max_y + 1):
                for cluster in cluster_list:
                    dist = distance(i, j, cluster.x, cluster.y)
                    if number_map.__contains__((i, j)):
                        total_map[(i, j)] += dist
                        if dist < dist_map[(i, j)]:
                            dist_map[(i, j)] = dist
                            number_map[(i, j)] = cluster.number
                        elif dist == dist_map[(i, j)]:
                            if cluster.number in inf_list:
                                number_map[(i, j)] = cluster.number
                    else:
                        dist_map[(i, j)] = dist
                        number_map[(i, j)] = cluster.number
                        total_map[(i, j)] = dist

        max_region = 0
        for key, value in number_map.items():
            if value in inf_list:
                continue
            else:
                cluster_list[value].region += 1

        for cluster in cluster_list:
            if not cluster.is_inf:
                if cluster.region > max_region:
                    max_region = cluster.region

        print(max_region)

        size = 0
        for key, value in total_map.items():
            if value < 10000:
                size += 1
        print(size)

        end = time.time()
        print(end - start)
