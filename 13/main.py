# 12.13


class Cart:
    def __init__(self, _x, _y, ori):
        self.x = _x
        self.y = _y
        self.ori = ori
        self.cross_times = 0
        self.dead = False

    def next(self):
        _x = self.x
        _y = self.y
        if self.ori is '^':
            _x -= 1
        elif self.ori is 'v':
            _x += 1
        elif self.ori is '<':
            _y -= 1
        elif self.ori is '>':
            _y += 1
        _pos = (_x, _y)
        return _pos

    def move(self, ori):
        _pos = self.next()
        self.x = _pos[0]
        self.y = _pos[1]
        self.ori = ori


def count_key(elem):
    return elem.x * 9999 + elem.y


def turn_left(ori):
    new_ori = ' '
    if ori is '^':
        new_ori = '<'
    elif ori is 'v':
        new_ori = '>'
    elif ori is '<':
        new_ori = 'v'
    elif ori is '>':
        new_ori = '^'
    return new_ori


def turn_right(ori):
    new_ori = ' '
    if ori is '^':
        new_ori = '>'
    elif ori is 'v':
        new_ori = '<'
    elif ori is '<':
        new_ori = '^'
    elif ori is '>':
        new_ori = 'v'
    return new_ori


if __name__ == '__main__':
    with open("./input.txt", 'r') as f:
        _map = {}
        carts = []
        x = 0
        y = 0
        for line in f.readlines():
            y = 0
            for letter in line:
                if letter in ('/', '\\', '-', '|', '+'):
                    _map[(x, y)] = letter
                elif letter in ('^', 'v', '<', '>'):
                    carts.append(Cart(x, y, letter))
                    if letter in ('^', 'v'):
                        _map[(x, y)] = '|'
                    elif letter in ('<', '>'):
                        _map[(x, y)] = '-'
                y += 1
            x += 1

        crash = False
        crash_pos = (-1, -1)
        delete_carts = []

        _dict = {}
        # Initialize
        for cart in carts:
            _dict[(cart.x, cart.y)] = cart

        while len(carts) > 1:
            carts.sort(key=count_key)
            delete_carts = []
            for cart in carts:
                if cart.dead:
                    continue
                del _dict[(cart.x, cart.y)]
                next_pos = cart.next()
                if cart.ori in ('^', 'v') and _map[next_pos] is '|':
                    cart.move(cart.ori)
                elif cart.ori in ('<', '>') and _map[next_pos] is '-':
                    cart.move(cart.ori)

                if _map[next_pos] is '/':
                    if cart.ori is '^':
                        cart.move('>')
                    elif cart.ori is 'v':
                        cart.move('<')
                    elif cart.ori is '<':
                        cart.move('v')
                    elif cart.ori is '>':
                        cart.move('^')
                elif _map[next_pos] is '\\':
                    if cart.ori is '^':
                        cart.move('<')
                    elif cart.ori is 'v':
                        cart.move('>')
                    elif cart.ori is '<':
                        cart.move('^')
                    elif cart.ori is '>':
                        cart.move('v')
                elif _map[next_pos] is '+':
                    cart.cross_times += 1
                    if cart.cross_times % 3 == 1:
                        cart.move(turn_left(cart.ori))
                    elif cart.cross_times % 3 == 2:
                        cart.move(cart.ori)
                    else:
                        cart.move(turn_right(cart.ori))

                if _dict.__contains__((cart.x, cart.y)):
                    if crash_pos[0] == -1:
                        crash_pos = (cart.x, cart.y)
                    prev = _dict[(cart.x, cart.y)]
                    delete_carts.append(prev)
                    delete_carts.append(cart)
                    prev.dead = True
                    cart.dead = True
                    del _dict[(cart.x, cart.y)]
                else:
                    _dict[(cart.x, cart.y)] = cart

            for cart in delete_carts:
                carts.remove(cart)

        # question 1
        print((crash_pos[1], crash_pos[0]))
        # question 2
        final_cart = carts[0]
        print((final_cart.y, final_cart.x))
