# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1:])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count('a'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
chars = {'А', 'а', 'Е', 'е', 'И', 'и', 'О', 'о', 'У', 'у', 'Ы', 'ы', 'Э', 'э', 'Я', 'я', 'Ю', 'ю'}
count = 0
for character in word:
    if character in chars:
        count += 1
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
