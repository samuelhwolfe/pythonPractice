
def collatz(number):
    
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
        print(3 * number + 1)
        return 3 * number + 1

n = input("Type me a number: ")
while n != 1:
    try:
        n = collatz(int(n))
    except ValueError:
        n = input('Please type an integer: ')
        continue

    
