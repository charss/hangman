  
from tkinter import *
import string
from round import Round
from random import randrange


mistakes_arr = ['_', '_', '_', '_', '_', '_']
mistakes_cnt = 0
word_arr = []


root = Tk()
root.title("Simple Calculator")

def button_click(button, letter, word):
    global mistakes_cnt, word_arr
    print(mistakes_cnt)
    button.config(state=DISABLED)
    if letter in word:
        for index, i in enumerate(word):
            if letter == i:
                word_arr[index] = i
        word_label.config(text=' '.join(word_arr))
    else:
        mistakes_arr[mistakes_cnt] = 'X'
        mistake_label.config(text='Mistakes: ' + ' '.join(mistakes_arr))
        mistakes_cnt += 1
        if mistakes_cnt == 5:
            print('Game Over')
    

with open("wordlist.txt") as file:
    words = file.read().split('\n')
    word = words[randrange(len(words))].upper()
    word_arr.extend('_' * len(word))

print(word_arr)
print(word)

buttons = []
word_label = Label(root, text=(' '.join(word_arr)))
word_label.config(font=('Courier', 44))
word_label.grid(row=0, column=0, padx=20, pady=20, columnspan=13)

mistake_label = Label(root, text='Mistakes: ' + ' '.join(mistakes_arr))
mistake_label.grid(row=1, column=0, columnspan=13)
mistake_label.config(font=('Courier', 15))
for i in range(26):
    letter = string.ascii_uppercase[i]
    button = Button(root, text=letter, width=5, height=2)
    button.config(command=lambda button=button, letter=letter: button_click(button, letter, word))
    buttons.append(button)

for index, button in enumerate(buttons):
    if index < 13:
        button.grid(row=3, column=index)
    else:
        button.grid(row=4, column=index - 13)


root.mainloop()