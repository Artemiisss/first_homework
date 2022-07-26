"""Написати функцію, яка визначить, чи є введений текст паліндромом
(той який читається однаково з будь-якого боку), приклад:
Шалаш, зараз, Дід, Піп, 13231
Паліндром — і ні морд, ні лап"""

text = input('Enter a word:')
reversed_text = text[::-1]


def determine_palindrome(txt):
    while True:
        if txt[::1] == reversed_text:
            print(txt, '\nThis word is a palindrome ')
            break
        if txt != reversed_text:
            print(text, '\nThis word is not a palindrome!')
            break


print(determine_palindrome(text))
