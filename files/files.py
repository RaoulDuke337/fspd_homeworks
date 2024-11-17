import os
from pprint import pprint

class Cookbook():
    def __init__(self, filepath, encoding):
        self.filepath = filepath
        self.encoding = encoding
        self.cook_book = {}
        self.ingridient_recomendation = {}

# Прочитываем книгу во вложенный словарь Название блюда: [Словари с ингридиентами]
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

            
def read_files(filepath, files_list):
    texts_list = []
    for file in os.listdir(filepath):
        path_to_file = os.path.join(filepath, file)
        if file in files_list:
            with open(path_to_file) as f:
                texts_list.append(f.readlines())
    return texts_list

def write_file_sorted(filepath, texts: list):
    open(filepath, 'w').close()
    sotred_texts = sorted(texts, reverse=True)
    for idx, text in enumerate(sotred_texts):
        name = str(idx + 1) + '.txt' + '\n'
        rows = str(len(text)) + '\n'
        with  open(filepath, 'a', encoding='utf-8') as file:
            file.write(name)
            file.write(rows)
            file.writelines(text)
            file.write('\n')


# Задача №1. Делаем словарь поваренной книги экземпляром класса Cookbook
filepath = os.path.join(os.getcwd(), 'files', 'Омлет.txt')

# При инициализации экземпляра не происходит чтения, но предполагается, что при вызове других функций это будет происходить
cook_book = Cookbook(filepath=filepath, encoding='utf-8')

# Задача №2 
dishes_list = ['Запеченный картофель', 'Омлет']
persons = 2

pprint(cook_book.get_shop_list_by_dishes(dishes_list, persons))


filepath_3 = os.path.join(os.getcwd(), 'files', 'texts')
files = ['1.txt', '2.txt', '3.txt']

# Задача №3
# Сначала читаем файлы и кладем в пременную 
texts_list = read_files(filepath_3, files)

path_to_write = os.path.join(os.getcwd(), 'files', 'texts', 'result.txt')

# Затем записываем в итоговый файл с помощью функции
write_file_sorted(path_to_write, texts_list)
