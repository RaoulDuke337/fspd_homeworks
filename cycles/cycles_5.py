def solve(phrases):
    result = []
    cleaned_phrases = [phrase.replace(' ', '').lower() for phrase in phrases]
    
    for i in range(len(phrases)):
        if cleaned_phrases[i] == cleaned_phrases[i][::-1]:
            result.append(phrases[i])

    return print(result)

phrases = [
           "нажал кабан на баклажан", 
           "дом как комод", 
           "рвал дед лавр", 
           "азот калий и лактоза",
           "а собака боса", 
           "тонет енот", 
           "карман мрак", 
           "пуст суп"
]

solve(phrases)
