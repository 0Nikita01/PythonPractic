#7.10
print('''Дана строка, состоящая из русских слов, разделенных пробелами
(одним или несколькими). Найти длину самого короткого слова.
''')

s = input("Введите строку S: ")

newStr = ""

words = s.split(' ')
i = 0
minLength = 500

for word in words:
    length = len(word)
    if word != "" and 1040 <= ord(word[0]) <= 1071 and length < minLength:
        minLength = length


print("Ответ: ", minLength)
