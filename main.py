queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]
list_len = len(queries)

string_len = []
for items in queries:
    string_len.append(len(items.split()))

unique_len = set(string_len)

for item in unique_len:
    num_of_duplicate = string_len.count(item)
    percents = num_of_duplicate * 100 / list_len
    if item > 1:
        print(f'из {item} слов {round(percents)}% предложний')
    else:
        print(f'из {item} слова {round(percents)}% предложний')
