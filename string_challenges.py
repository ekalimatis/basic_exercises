# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1:])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count('a'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
chars='АаЕеИиОоУуЫыЭэЯяЮю'
count=0
for ch in chars:
    count+=word.count(ch)
print(count)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
word_count = len(sentence.split())
sum_word_len = (len(sentence) - len(sentence.split()) + 1)
print(sum_word_len / word_count)