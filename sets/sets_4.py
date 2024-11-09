from pprint import pprint

courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

codes_info = [
	"",
	"1 — число цели, которая проявляется в форме агрессивности и амбиций",
	"2 — число равновесия и контраста одновременно, поддерживает равновесие, смешивая позитивные и негативные качества",
	"3 — неустойчивость, объединяет талант и весёлость, символ приспосабливаемости",
	"4 — означает устойчивость и прочность",
	"5 — символизирует риск, свободу и душевное беспокойство, которое толкает человека к путешествиям и новому опыту. С одной стороны, это самое счастливое число, с другой — самое непредсказуемое",
	"6 — символ надёжности. Идеальное число, которое делится как на чётное, так и на нечётное, объединяя элементы каждого",
	"7 — символизирует тайну, а также изучение и знание как путь исследования неизвестного и невидимого",
	"8 — число материального успеха, означает надёжность, доведённую до совершенства, символ всеобщего успеха",
	"9 — указывает на сильную личность с потенциальным интеллектом, способную к высокому развитию"
]
# Здесь ничего менять не нужно, это готовый код, который считает число имени
def calc_namecode(name):
	letters = ["", "А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т",
			   "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]

	name = name.upper()
	code = 0
	for letter in name:
		try:
			ltr_code = letters.index(letter) % 9
		except:
			continue
		if ltr_code == 0:
			ltr_code = 9
		code += ltr_code

	while code > 9:
		curr = code // 10 + code % 10
		code = curr

	return code
	
def to_dict(courses, mentors):
	courses_dict = list()
	for course, mentor in zip(courses, mentors):
		courses_dict.append({"title": course, "mentors": mentor})
	return courses_dict

def uniq_names(courses_dict: list):
	names = set()
	for dict in courses_dict:
		lst = dict.get("mentors")
		for item in lst:
			names.add(item)
	return names

def uniq_first_names(names_list):
	uniq_names = set()
	for name in names_list:
		uniq_names.add(name.split()[0])
	return sorted(uniq_names)

def code_names_match(names, codes_info):
	codenames_dict = dict()
	for name in names:
		code = calc_namecode(name)
		codenames_dict.setdefault(code, list())
		codenames_dict[code].append(name)
	return codenames_dict


def main():
	courses_dict = to_dict(courses, mentors)
	name_lst = uniq_names(courses_dict)
	first_names = uniq_first_names(name_lst)
	code_names_dict = code_names_match(first_names, codes_info)
	
	for item in range(1, len(code_names_dict) + 1):
		names = ', '.join(code_names_dict[item])
		print(codes_info[item])
		print(f'Коду {item} соответствуют: {names}')

main()