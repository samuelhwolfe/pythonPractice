#! /usr/bin/env python3

# getting client stats
import math

# function that calculates body fat pecentage for men
def maleBodyFatPercentage(waist, neck, height):
    rtn  = 495 / (1.0324 - .19077 * (math.log((waist - neck), 10)) + .15456 * (math.log(height, 10))) - 450
    return rtn

# function that calculates body fat pecentage for women
def femaleBodyFatPercentage(weight, height, waist, hip):
    rtn = 495 / (1.29579 - .35004 * (math.log((waist + hip - neck), 10)) + .22100 * (math.log(height, 10))) - 450
    return rtn

# function that defines fat mass
def fatMass(bodyfat, weight):
    rtn = bodyfat * weight
    return rtn

# function that defines lean mass
def leanMass(weight, fatmass):
    rtn = weight - fatmass
    return rtn

# function that defines various activity levels
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

print('First, let\'s get some information.')
sex = input('Are you male or female? ')
height = int(input('Enter your height in cm: '))
weight = int(input('Enter your weight in kg: '))
neck = int(input('Enter your neck (at narrowest): '))

if sex in ('Male', 'male', 'm', 'M'):
    waist = int(input('Enter your waist (at navel): '))
    bodyfat = maleBodyFatPercentage(waist, neck, height)
    fatmass = fatMass(bodyfat, weight)/100
    
    print('Your bodyfat percentage is: ' + str(int(maleBodyFatPercentage(waist, neck, height))) + '%')
    print('Your fat mass is: ' + str(round(float(fatMass(bodyfat, weight)/100))) + 'kg')
    print('Your lean mass is: ' + str(round(float(leanMass(weight, fatmass)))) + 'kg')

elif sex in ('Female', 'female', 'f', 'F'):
    waist = int(input('Enter your waist (at narrowest): '))
    hip = int(input('Enter your hip (at widest): '))
    bodyfat = femaleBodyFatPercentage(weight, height, waist, hip)
    fatmass = fatMass(bodyfat, weight)/100

    print('Your bodyfat percentage is: ' + str(int(femaleBodyFatPercentage(weight, height, waist, hip))) + '%')
    print('Your fatmass is: ' + str(round(float((fatMass(bodyfat, weight)/100)))) + 'kg')
    print('Your lean mass is: ' + str(round(float(leanMass(weight, fatmass)))) + 'kg')







