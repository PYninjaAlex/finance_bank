def suggestions():
    with open('suggestions.txt', 'r', encoding='utf-8') as sug:
        print('Предложения SkysmartBank')
        print(sug.read())

suggestions()