import tkinter as tk 
from tkinter import messagebox #для окон с сообщениями
from string import ascii_uppercase #английские заглавные буквы
from random import shuffle #перемешивать

try:
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1) #запускаем музыку бесконечно
except Exception:
    print('Музыка не запущена (нет pygame или файла music.mp3)')


def generate(): #генериуем ключ
    word = word_entry.get()
    if len(word) != 6 or not word.isalpha() or not word.isascii():
        messagebox.showerror('Ошибка', 'Введите слово из 6 латинских букв')
        return

    word = word.upper()

    #составляем цифры кода из букв слова
    digits = ''
    for l in word:
        number = ascii_uppercase.index(l) + 1
        digit = number % 10
        digits += str(digit)

    #рандом для букв
    letters = list(word)
    shuffle(letters)
    block1 = ''.join(letters[:3])
    block3 = ''.join(letters[3:])

    key_label.configure(text=f'{block1}-{digits}-{block3}')


COLOR_STEP = 0
COLORS = ['#00ff00', '#00ffff', '#ff00ff', '#ffff00']


#изменение цвета
def animate():
    global COLOR_STEP
    key_label.configure(fg=COLORS[COLOR_STEP % len(COLORS)]) #% чтобы не выйти за пределы списка
    COLOR_STEP += 1
    window.after(300, animate) #меняем цвет каждые 300 мс


window = tk.Tk()
window.title('KeyGen')
window.geometry('400x253')
window.resizable(0, 0) #не даем изменять размер окна
bg_img = tk.PhotoImage(file='image.png')

#изображение
label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

#заголовок
title_label = tk.Label(window,
                       text='KEYGEN',
                       font=('Consolas', 20, 'bold'),
                       bg='black',
                       fg='white')
title_label.pack(pady=5) #отступы сверху и снизу

#ввод слова
word_entry = tk.Entry(window, width=10, font=('Verdana 16'), justify='center')
word_entry.insert(0, 'BARBOS') 
word_entry.pack(pady=5)

#кнопка генерации
btn = tk.Button(window,
                text='Generate',
                width=10,
                font=('Verdana 12'),
                command=generate)
btn.pack(pady=5)

#вывод ключа
key_label = tk.Label(window,
                     text='XXX-XXXXXX-XXX',
                     font=('Consolas', 18, 'bold'),
                     bg='black',
                     fg='#00ff00', width=18)
key_label.pack(pady=10)

animate()
window.mainloop()