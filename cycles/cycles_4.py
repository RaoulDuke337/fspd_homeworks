def solve(boys: list, girls: list):
    result = ''
    number_of_users = len(boys + girls)
    boys = sorted(boys)
    girls = sorted(girls)
    couples = list(zip(boys, girls))

    if len(couples) != number_of_users / 2:
        result = 'Кто-то может остаться без пары!'
    else:
        result = ', '.join([f'{boy} и {girl}' for boy, girl in couples])

    return print(result)

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Nikita']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

solve(boys, girls)