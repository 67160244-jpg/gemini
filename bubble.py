class BubbleSorter:
    def __init__(self, data):
        self.data = data

    def sort(self):
        n = len(self.data)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
            print(f"After round {i + 1}: {self.data}")

    def display(self):
        print(self.data)


nums = [64, 34, 25, 12, 22, 11, 90]
print("Befor sorting: ")
print(f"Current data: {nums}")

print(" ")
sorter = BubbleSorter(nums)
sorter.sort()

print("\nAfter sorting: ")
print(f"Current data: {nums}")