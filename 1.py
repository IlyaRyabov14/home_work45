import random
txt = "абв"
print("Слово которое нужно удалить из текста: ", txt)
list_word= (int(input("Количество слов в тексте: ")))
num_word = []
print("Рандомный текст: ")
for x in range (num_word):
    random_txt = random.sample(txt, 3)
    list_word.append("".join(random_txt))

print(" ".join(list_word))

print("Текст без абв: ")
list_word2 = list(filter(lambda x: txt not in x, list_word))
print(" ".join(list_word2))