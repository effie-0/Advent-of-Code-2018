# 12.9


def find_scores(_num, _max, _list):
    cycle = []
    current = 0
    prev = 0
    k = 0
    for j in range(_max + 1):
        if j % 71339 == 0:
            print(int(j / 71339))
        if j % 23 != 0 or j == 0:
            prev = current
            cycle.insert(current, j)
            length = len(cycle)
            current = 1 + (current + 1) % length
        elif j % 23 == 0 and j is not 0:
            length = len(cycle)
            pos = (prev - 7) % length
            if pos < 0:
                pos += length
            _list[k] += j
            _list[k] += cycle[pos]
            prev = pos
            current = 1 + (prev + 1) % (length - 1)
            cycle.remove(cycle[pos])
        k += 1
        if k == _num:
            k = 0
    return _list


if __name__ == '__main__':
    # with open("./input.txt", 'r') as f:
    #     for line in f.readlines():
    num_players = 418
    max_marble = 71339 * 100
    player_list = []
    for i in range(num_players):
        player_list.append(0)
    player_list = find_scores(num_players, max_marble, player_list)
    print(max(player_list))
