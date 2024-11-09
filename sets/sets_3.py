import itertools

class Courses():
    
    def __init__(self, courses) -> None:
        self.course_names = courses

    def get_pairs(self):
        self.pairs = list()
        for name in itertools.combinations(self.course_names, 2):
            self.pairs.append(name)
        return self.pairs

    def get_pair_indexes(self):
        self.pair_indexes = list()
        for ids in itertools.combinations(range(len(self.course_names)), 2):
            self.pair_indexes.append(ids)
        return self.pair_indexes


class Staff():

    def __init__(self, names) -> None:
        self.names = names

    def get_first_names(self):
        self.first_names = list()
        for staff in self.names:
            name_list = list()
            for name in staff:
                name_list.append(name.split()[0])
            self.first_names.append(name_list)
        return self.first_names
    
    def get_intersections(self, combinations):
        self.intersections = list()
        for pair in combinations:
            intersect = sorted(set(self.first_names[pair[0]]) & set(self.first_names[pair[1]]))
            self.intersections.append(intersect)
        return self.intersections

courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

course_names = Courses(courses)
ids = course_names.get_pair_indexes()
course_pairs = course_names.get_pairs()

staff = Staff(mentors)
f_names = staff.get_first_names()
intersections = staff.get_intersections(ids)

# print(intersections)

for id, pair in enumerate(ids):
    print(f"{id + 1} На курсах '{course_names.course_names[pair[0]]}' и '{course_names.course_names[pair[1]]}' преподают: {', '.join(intersections[id])}")