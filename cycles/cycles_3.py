def solve(todo_list: list, workday: float = 8):
    worktime = 0.0
    for time in todo_list:
        worktime += time[1]
    breaktime = workday - worktime
    return round(breaktime, 1)

todo_list = [
    ["Разобрать почту", 1],
    ["Обзвонить клиентов", 2],
    ["Запланировать дела на завтра", 0.6],
    ["Сделать презентацию", 3],
    ["Созвон с командой", 0.5]
]
result = solve(todo_list)
print(f"Время на отдых: {result}")