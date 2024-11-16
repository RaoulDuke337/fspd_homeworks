import os
from pprint import pprint

class Cookbook():
    def __init__(self, filepath, encoding):
        self.filepath = filepath
        self.encoding = encoding
        self.cook_book = {}
        self.ingridient_recomendation = {}
        
    def reader(self):
        cook_book = {}
        with open(self.filepath, encoding=self.encoding) as f:
            for dish in f:
                number_of_ingridients = int(f.readline())
                for i in range(number_of_ingridients):
                    ingridient = f.readline().strip().split('|')
                    ingridient_dict = {
                        'ingredient_name': ingridient[0],
                        'quantity': ingridient[1],
                        'measure': ingridient[2]
                        }
                    cook_book.setdefault(dish.strip(), []).append(ingridient_dict)
                f.readline()
        return cook_book

    def get_shop_list_by_dishes(self, dishes, person_count):
        self.cook_book = self.reader()
        for dish in dishes:
            for ingridients_dict in self.cook_book[dish]:
                ingridient = ingridients_dict['ingredient_name']
                if ingridient not in self.ingridient_recomendation.keys():
                    amount_dict = {
                        'measure': ingridients_dict.get('measure'),
                        'quantity': int(ingridients_dict.get('quantity')) * person_count
                    }
                    self.ingridient_recomendation[ingridient] = amount_dict
                else:
                    self.ingridient_recomendation[ingridient]['quantity'] += int(ingridients_dict['quantity'] * person_count)
        return self.ingridient_recomendation

            



filepath = os.path.join(os.getcwd(), 'files', 'Омлет.txt')

# with open(filepath, encoding='utf-8') as f:
#     for row in f:
#         print(row)

cook_book = Cookbook(filepath=filepath, encoding='utf-8')
dishes_list = ['Запеченный картофель', 'Омлет']
persons = 2

pprint(cook_book.get_shop_list_by_dishes(dishes_list, persons))