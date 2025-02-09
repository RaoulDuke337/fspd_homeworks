import json 

def read_json(filepath, word_max_len=6, top_words=10):
    words_cnt = {}
    sorted_words_cnt = []
    words = []
    with open(filepath) as file:
        news = json.load(file)
    for article in news['rss']['channel']['items']:
        text = article.get('description')
        for word in text.split():
            if len(word) > word_max_len:
                words_cnt[word] = words_cnt.get(word, 1) + 1
    
    sorted_words_cnt = sorted(words_cnt.items(), key=lambda item: item[1], reverse=True)
    words = [word[0] for word in sorted_words_cnt[:top_words]]
    return words


print(read_json('/Users/kisssskai_i/Desktop/FSPD_homeworks/json/newsarf.json'))

# if __name__ == '__main__':
#     print(read_json('newsafr.json'))


