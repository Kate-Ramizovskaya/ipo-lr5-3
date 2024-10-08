with open('text.txt', 'r', encoding='utf-8') as f:
    str=f.read()
words=str.split()
lenght=len(words)
print("Кол-во слов в файле: ", lenght)