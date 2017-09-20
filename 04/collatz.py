def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(number * 3 + 1)
        return number * 3 + 1

print('Enter number to test Collatz Conjecture: ')
n = int(input())
while n != 1:
    n = collatz(n)
    