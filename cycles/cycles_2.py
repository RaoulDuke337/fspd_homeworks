def solve(hare_dist, turtle_dist):
    hare_total = sum(hare_dist)
    turtle_total = sum(turtle_dist)

    if hare_total > turtle_total:
        result = 'заяц'
    elif hare_total == turtle_total:
        result = 'одинаково'
    else:
        result = 'черепаха'
    return result

result = solve([8, 5, 3, 2, 0, 1, 1], [3, 3, 3, 3, 3, 3, 3])
assert result == "черепаха", f"Победитель определен неверно: {result}"
print(f"Победитель: {result}")
result = solve([8, 5, 3, 2, 2, 1, 1], [3, 3, 3, 3, 3, 3, 3])
assert result == "заяц", f"Победитель определен неверно: {result}"
print(f"Победитель: {result}")
result = solve([8, 5, 3, 2, 1, 1, 1], [3, 3, 3, 3, 3, 3, 3])
assert result == "одинаково", f"Победитель определен неверно: {result}"
print(f"Победитель: {result}")