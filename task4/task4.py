import sys


def min_step(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    steps = sum(abs(num - median) for num in nums)
    return steps


if len(sys.argv) != 2:
    print("Введите следующую команду:  python task4.py <файл>")
else:
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            numbers = [int(line) for line in file]
            steps = min_step(numbers)
            print(steps)
    except FileNotFoundError:
        print("Файл не найден")
