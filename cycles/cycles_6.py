def calculator(cook_book, persons):
  result = []
  for recipe in cook_book:
    dish = recipe[0]
    shoplist = []
    for ingridient in recipe[1]:
      item = ingridient[0]
      amount = ingridient[1] * persons
      unit = ingridient[2]
      shoplist.append(f'{item}, {amount}, {unit}')
    result.append(f'{dish}: {", ".join(shoplist)}')

  return result


cook_book = [[
    'Салат',
    [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
    ]
],
             [
                 'Пицца',
                 [
                     ['сыр', 50, 'гр.'],
                     ['томаты', 50, 'гр.'],
                     ['тесто', 100, 'гр.'],
                     ['бекон', 30, 'гр.'],
                     ['колбаса', 30, 'гр.'],
                     ['грибы', 20, 'гр.'],
                 ],
             ],
             [
                 'Фруктовый десерт',
                 [
                     ['хурма', 60, 'гр.'],
                     ['киви', 60, 'гр.'],
                     ['творог', 60, 'гр.'],
                     ['сахар', 10, 'гр.'],
                     ['мед', 50, 'мл.'],
                 ]
             ]]

result = calculator(cook_book, 3)

for shoplist in result:
  print(shoplist)
