def leanBodyMass(lbm):
    return (lbm * 13.587)

def fatMass(fm):
    return (fm * 9.163)

def sexIdentity(sex):
    if sex in ('Male', 'male', 'm', 'M'):
        return 198
    elif sex in ('Female', 'female', 'f', 'F'):
        return 0

def ageAdjustment(age):
    return (age * 3.351)

def activityLevel(activity):
    if activity in ('Sedentary', 'sedentary'):
        return 1.2
    elif activity in ('Lightly active', 'lightly active'):
        return 1.375
    elif activity in ('Moderately active', 'moderately active'):
        return 1.55
    elif activity in ('Very active', 'very active'):
        return 1.725
    elif activity in ('Extra active', 'extra active'):
        return 1.9


lbm = int(input('Enter your lean body mass in kg: '))
fm = int(input('Enter your fat mass in kg: '))
sex = input('What is your sex? ' )
age = int(input('Enter your age: '));
activity = input('What is your activity level (choose one):\n'
                 '- Sedentary\n'
                 '- Lightly active\n'
                 '- Moderately active\n'
                 '- Very active\n'
                 '- Extra active\n');

mueller = int(leanBodyMass(lbm) + fatMass(fm) + sexIdentity(sex) - ageAdjustment(age) + 674)

print('Your basic metabolic rate is ' + str(mueller) + ' calories.')
print('Your maintenance calorie level is ' + str(int(mueller * activityLevel(activity))) + '.')

