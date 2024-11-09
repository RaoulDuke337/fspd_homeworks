receipts = [123, 145, 346, 246, 235, 166, 112, 351, 436, 4534, 433]
counter = 0

for i, check in enumerate(receipts):
    if (i+1) % 3 == 0:
        print(f'победитель с чеком № {check}')
        counter += 1
print(f'Кол-во победителей: {counter}')