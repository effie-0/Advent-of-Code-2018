# 12.8


class Node:
    def __init__(self, _start, num_child, num_metadata):
        self.start = _start
        self.num_child = num_child
        self.num_metadata = num_metadata
        self.children = []
        self.metadata = []

    def add_metadata(self, data):
        self.metadata.append(data)

    def add_child(self, node):
        self.children.append(node)

    def get_sum(self):
        if self.num_child == 0:
            return sum(self.metadata)
        else:
            count = 0
            for num in self.metadata:
                ref = num - 1
                if ref >= len(self.children):
                    count += 0
                else:
                    count += self.children[ref].get_sum()
            return count


def build_tree(_root, _line):
    count = 0
    j = _root.start + 2
    for k in range(_root.num_child):
        _child_num = int(line[j])
        _meta_num = int(line[j + 1])
        new_node = Node(j, _child_num, _meta_num)
        new_count, new_ending = build_tree(new_node, _line)
        _root.add_child(new_node)
        count += new_count
        j = new_ending
    for k in range(_root.num_metadata):
        num = int(line[j + k])
        count += num
        _root.add_metadata(num)
    ending = j + _root.num_metadata

    return count, ending


if __name__ == '__main__':
    with open("./input.txt", 'r') as f:
        for line in f.readlines():
            length = len(line.strip())
            line = line.split()

            i = 0
            start = 0
            child_num = int(line[i])
            meta_num = int(line[i + 1])
            root = Node(start, child_num, meta_num)
            total_count, end = build_tree(root, line)
            print(total_count)
            print(root.get_sum())
