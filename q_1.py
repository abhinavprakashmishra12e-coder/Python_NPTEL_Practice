
N = int(input())

numbers = list(map(int, input().split()))

odd = [num for num in numbers if num % 2 != 0]

cube =list(map(lambda x: x ** 3, odd))

print(cube)

print(cube[::-1])
