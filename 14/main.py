# 12.14
import re


if __name__ == '__main__':
    input_num = 990941
    recipe_list = [3, 7]
    recipe_str = "37"
    worker1 = 0
    worker2 = 1
    while len(recipe_list) < (input_num + 10):
        _sum = recipe_list[worker1] + recipe_list[worker2]
        new_r1 = int(_sum / 10)
        new_r2 = int(_sum % 10)
        if new_r1 != 0:
            recipe_list.append(new_r1)
            recipe_str += str(new_r1)
        recipe_list.append(new_r2)
        recipe_str += str(new_r2)
        worker1 += recipe_list[worker1] + 1
        worker1 = worker1 % len(recipe_list)
        worker2 += recipe_list[worker2] + 1
        worker2 = worker2 % len(recipe_list)

    print(recipe_list[input_num:input_num + 10])
    match_obj = re.search(r'990941', recipe_str)
    if match_obj:
        print(match_obj)
    else:
        while not match_obj:
            _sum = recipe_list[worker1] + recipe_list[worker2]
            new_r1 = int(_sum / 10)
            new_r2 = int(_sum % 10)
            if new_r1 != 0:
                recipe_list.append(new_r1)
                recipe_str += str(new_r1)
            recipe_list.append(new_r2)
            recipe_str += str(new_r2)
            worker1 += recipe_list[worker1] + 1
            worker1 = worker1 % len(recipe_list)
            worker2 += recipe_list[worker2] + 1
            worker2 = worker2 % len(recipe_list)
            match_obj = re.search(r'990941', recipe_str[-12:])
        print(len(recipe_str) - 12 + match_obj.span()[0])

