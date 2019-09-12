salaries = {'Ken': 30000, 'Tom': 60000, 'Jim': 90000, 'Sean': 110000}

def sumSalaries(team):
    total_salary = 0
    for x in team.values():
        total_salary = total_salary + x
    print('The total salary is $' + str(total_salary))

sumSalaries(salaries)
        
