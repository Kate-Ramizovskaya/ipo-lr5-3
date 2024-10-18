with open('text.txt', 'r', encoding='utf-8') as f: #открытие файла для дальнейшего чтения
    str=f.read() #присваивание переменной str открытому файлу
words=str.split() #присваивание переменной words через str
lenght=len(words) #перебор и подсчет переменной words
print("Кол-во слов в файле: ", lenght) #вывод кол-ва
