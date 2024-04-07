alphabet_rus_up = ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
alphabet_rus = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
alphabet_en_up = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
alphabet_en = ('abcdefghijklmnopqrstuvwxyz')
alphabet = alphabet_en_up + alphabet_en + alphabet_rus + alphabet_rus_up
message = input('Введите слово или предложение: ')
cipher = ''
for i in message:
    if i in alphabet_rus:
        place = alphabet_rus.find(i)
        if place < 30:
            new_place = place + 3
        else:
            new_place = place - 30
        cipher += alphabet_rus[new_place]
    if i in alphabet_rus_up:
        place = alphabet_rus_up.find(i)
        if place < 30:
            new_place = place + 3
        else:
            new_place = place - 30
        cipher += alphabet_rus_up[new_place]
    if i in alphabet_en:
        place = alphabet_en.find(i)
        if place < 23:
            new_place = place + 3
        else:
            new_place = place - 23
        cipher += alphabet_en[new_place]
    if i in alphabet_en_up:
        place = alphabet_en_up.find(i)
        if place < 23:
            new_place = place + 3
        else:
            new_place = place - 23
        cipher += alphabet_en_up[new_place]
    if i not in alphabet:
        cipher += ' '
print(cipher)
