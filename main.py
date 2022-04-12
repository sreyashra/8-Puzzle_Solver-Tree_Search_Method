class Node:
    def __init__(self, data, level, fValue):
        self.data = data
        self.level = level
        self.fValue = fValue

    def child_generate(self):
        a, b = self.find(self.data, '0')
        values_list = [[a - 1, b], [a + 1, b], [a, b - 1], [a, b + 1]]
        children = []
        for i in values_list:
            child = self.move(self.data, a, b, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children

    def move(self, puzz, a1, b1, a2, b2):
        if 0 <= a2 < len(self.data) and 0 <= b2 < len(self.data):
            puzz_temp = []
            puzz_temp = self.copy(puzz)
            temp = puzz_temp[a2][b2]
            puzz_temp[a2][b2] = puzz_temp[a1][b1]
            puzz_temp[a1][b1] = temp
            return puzz_temp
        else:
            return None

    def copy(self, root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def find(self, puzz, a):
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puzz[i][j] == a:
                    return i, j


class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open = []
        self.closed = []

    def accept(self):
        puzz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puzz.append(temp)
        return puzz

    def heuristic(self, start, goal):
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '0':
                    temp += 1
        return temp

    def process(self):
        print("Enter the puzzle start state \n")
        start = self.accept()
        print("Enter the puzzle goal state \n")
        goal = self.accept()

        start = Node(start, 0, 0)
        start.fValue = self.heuristic(start, goal)
        self.open.append(start)
        print("\n\n")
        while True:
            cur = self.open[0]
            print("")
            print(" || ")
            print(" || ")
            print(" || \n")
            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")
            if self.h(cur.data, goal) == 0:
                break
            for i in cur.child_generate():
                i.fValue = self.heuristic(i, goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]

            self.open.sort(key=lambda x: x.fValue, reverse=False)


puzz = Puzzle(3)
puzz.process()

Input()