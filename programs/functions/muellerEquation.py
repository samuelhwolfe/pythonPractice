#! /usr/bin/env python3

def leanBodyMass(lbm): #returns lean body mass figure for Mueller equation
    return (lbm * 13.587)

def fatMass(fm): #returns fat mass figure for mueller equation
    return (fm * 9.163)

def sexIdentity(sex):
    if sex in ('Male', 'male', 'm', 'M'):
        return 198
    elif sex in ('Female', 'female', 'f', 'F'):
        return 0

def ageAdjustment(age):
    return (age * 3.351)

def activityLevel(activity):
    if activity == 1:
        return 1.2
    elif activity == 2:
        return 1.375
    elif activity == 3:
        return 1.55
    elif activity == 4:
        return 1.725
    elif activity == 5:
        return 1.9

activityNumbers = {'Sedentary': 1, 'Lightly active': 2, 'Moderately active': 3,
                   'Very active': 4, 'Extremely active': 5}

def printActivityTable(itemsDict, leftWidth, rightWidth):
    print()
    print(' What is your activity level? '.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

lbm = int(input('Enter your lean body mass in kg: '))
fm = int(input('Enter your fat mass in kg: '))

while True:
    sex = str(input('What is your sex? ' ))
    if sex in ('Male', 'male', 'm', 'M', 'Female', 'female', 'f', 'F'):
        break
    else:
        print('Please type a sex')
        
age = int(input('Enter your age: '))

mueller = int(leanBodyMass(lbm) + fatMass(fm) + sexIdentity(sex) - ageAdjustment(age) + 674)

printActivityTable(activityNumbers, 35, 5)

activity = int(input('\nType the number associated with your activity: '))

print('\nYour basic metabolic rate is ' + str(mueller) + ' calories.')
print('Your maintenance calorie level is ' + str(int(mueller * activityLevel(activity))) + '.\n')

