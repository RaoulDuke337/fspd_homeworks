def solve(models, available, manufacturers):
    accepted_models = []
    amount = 0
    
    for model, status in zip(models, available):
        if status == 1:
            splitted_model = model.split()
        else:
            continue
        for manufact in manufacturers:
            if manufact in splitted_model:
                accepted_models.append(model)
                amount += 1

    return print(f'Модели: {accepted_models} \nКоличество: {amount}')

models = [
    '480 ГБ 2.5" SATA накопитель Kingston A400', 
    '500 ГБ 2.5" SATA накопитель Samsung 870 EVO', 
    '480 ГБ 2.5" SATA накопитель ADATA SU650', 
    '240 ГБ 2.5" SATA накопитель ADATA SU650', 
    '250 ГБ 2.5" SATA накопитель Samsung 870 EVO', 
    '256 ГБ 2.5" SATA накопитель Apacer AS350 PANTHER', 
    '480 ГБ 2.5" SATA накопитель WD Green', 
    '500 ГБ 2.5" SATA накопитель WD Red SA500'
]

available = [1, 1, 1, 1, 0, 1, 1, 0]
manufacturers = ['Intel', 'Samsung', 'WD']

solve(models, available, manufacturers)