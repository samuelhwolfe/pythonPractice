print('Enter your name')
myName = input()
print('Enter your age')
myAge = input()
print('Wow, Samuel! Your age is ' + str(int(myAge)) + '! That means you will be 100 in ' + str(int(100) - int(myAge)) + ' years.')

# more streamlined way of doing it

name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2019-age) + 100)
print('Woah! You will be 100 years old in the year ' + year + '.')
