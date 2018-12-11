# 12.11

if __name__ == '__main__':
    _input = 5034
    grid = {}
    for i in range(1, 301):
        for j in range(1, 301):
            rack_id = i + 10
            pow_level = rack_id * j
            pow_level += _input
            pow_level *= rack_id
            num = int(pow_level / 100) % 10
            num -= 5
            grid[(i, j)] = num

    max_fuel = 0
    x = 0
    y = 0
    size = 0
    fuel_grid = {}

    # question 1
    for i in range(1, 301 - 3):
        for j in range(1, 301 - 3):
            fuel = 0
            for k in range(3):
                for q in range(3):
                    fuel += grid[(i + k, j + q)]
            if fuel > max_fuel:
                max_fuel = fuel
                x = i
                y = j
    print("Q1 max_fuel = " + str(max_fuel))
    print("Q1 x = " + str(x))
    print("Q2 y = " + str(y))
    print("---------------------------------------------")

    # question 2
    for length in range(1, 301):
        print("length = " + str(length))
        for i in range(1, 301):
            for j in range(1, 301):
                if not fuel_grid.__contains__((i, j)):
                    fuel_grid[(i, j)] = []
                fuel_list = fuel_grid[(i, j)]
                if i + length > 301 or j + length > 301:
                    break
                len_list = len(fuel_list)
                if len_list > 0:
                    last = fuel_list[len_list - 1]
                else:
                    last = 0
                fuel_list.append(last)
                for l in range(length):
                    if j + l > 300:
                        break
                    fuel_list[len_list] += grid[(i + length - 1, j + l)]
                for l in range(length-1):
                    if i + l > 300:
                        break
                    fuel_list[len_list] += grid[(i + l, j + length - 1)]
                if fuel_list[len_list] > max_fuel:
                    max_fuel = fuel_list[len_list]
                    x = i
                    y = j
                    size = length
                    print("max_fuel = " + str(max_fuel))
                    print("x = " + str(x))
                    print("y = " + str(y))
                    print("size = " + str(size))
    print("---------------------------------------------")
    print(max_fuel)
    print(x)
    print(y)
    print(size)
