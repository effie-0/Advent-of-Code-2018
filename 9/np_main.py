# 12.9
import numpy as np


def find_scores(_num, _max, _list):
    cycle = np.array([])
    current = 0
    prev = 0
    k = 0
    for j in range(_max + 1):
        if j % 71339 == 0:
            print(int(j / 71339))
        if j % 23 != 0 or j == 0:
            prev = current
            cycle = np.insert(cycle, current, j, 0)
            length = cycle.size
            current = 1 + (current + 1) % length
        elif j % 23 == 0 and j is not 0:
            length = cycle.size
            pos = (prev - 7) % length
            if pos < 0:
                pos += length
            _list[k] += j
            _list[k] += cycle[pos]
            prev = pos
            current = 1 + (prev + 1) % (length - 1)
            cycle = np.delete(cycle, pos, 0)
        k += 1
        if k == _num:
            k = 0
    return _list


if __name__ == '__main__':
    num_players = 418
    max_marble = 71339 * 100
    player_list = np.zeros(num_players)
    player_list = find_scores(num_players, max_marble, player_list)
    print(max(player_list))
