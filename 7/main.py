# 12.7
# try.txt:
# time + 1, # worker < 2
# input.txt
# time + 61, # worker < 5
import re


class Worker:
    def __init__(self, number, word):
        self.number = number
        self.work = word
        self.time = ord(word) - ord('A') + 61

    def elapse(self):
        self.time -= 1


if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        prev_map = {}
        start = []
        ready = []
        waiting = []
        for line in f.readlines():
            match_obj = re.match(r"Step (.*) must be finished before step (.*) can begin.", line.strip())
            _prev = match_obj.group(1)
            _next = match_obj.group(2)
            if prev_map.__contains__(_next):
                prev_map[_next].append(_prev)
            else:
                prev_map[_next] = [_prev]

            if _prev not in start and _prev not in waiting:
                start.append(_prev)
            if _next in start:
                start.remove(_next)

            if _prev not in waiting:
                waiting.append(_prev)
            if _next not in waiting:
                waiting.append(_next)

        timer = 0
        workers = []
        starting = True
        while len(waiting) > 0:
            while len(start) > 0:
                if len(start) > 0:
                    start.sort()
                    target = start[0]
                    num = len(workers)
                    if num < 5:
                        workers.append(Worker(num, target))
                    else:
                        break
                    start.remove(target)

            if len(workers) > 0:
                new_ready_list = []
                remove_list = []
                timer += 1
                for worker in workers:
                    worker.elapse()
                    if worker.time <= 0:
                        remove_list.append(worker)
                        ready.append(worker.work)
                        waiting.remove(worker.work)
                        new_ready_list.append(worker.work)
                        print(worker.work)  # done

                for worker in remove_list:
                    workers.remove(worker)

                if len(new_ready_list) > 0:
                    for key, v_list in prev_map.items():
                        for new_ready in new_ready_list:
                            if new_ready in v_list:
                                v_list.remove(new_ready)
                                if len(v_list) == 0:
                                    start.append(key)

        print(timer)
