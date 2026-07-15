class FreqStack:

    def __init__(self):
        self.stack = []


    def push(self, val: int) -> None:
        if val is not None:
            self.stack.append(val)

    def pop(self) -> int:
        count = {}
        for num in self.stack:
            count[num] = count.get(num, 0) + 1

        max_freq = max(count.values())

        for i in range(len(self.stack) - 1, -1, -1):
            value = self.stack[i]
            if count[value] == max_freq:
                self.stack.pop(i)
                return value


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()