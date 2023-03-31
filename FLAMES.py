# -*- coding: UTF-8 -*-
# ToolName   : FLAMES
# Author     : Anand-Velpuri
# Version    : 2.0
# License    : MIT
# Copyright  : Anand-Velpuri (2023-2024)
# Github     : https://github.com/Anand-Velpuri
# Contact    : https://telegram.me/AnandVelpuri
# Description: FLAMES helps you to know the relationship status between you and your partner
# 1st Commit : 31/03/2023
# Language   : Python

"""
MIT License

Copyright (c) 2023 Anand-Velpuri

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
print("""
    
 ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌          
▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌
▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌                    ▐░▌
▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌
▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                            -By ANAND VELPURI.
""")
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', ':', ';', '.', '{', '}', '"', '?', '/', "'", '-', '=', '<',
           '>', '[', ']', '^', '|']


def is_valid_input(name):
    for char in name:
        if char.isdigit() or char in symbols:
            return False
    return True


name_1 = []
while not name_1 or not is_valid_input(name_1):
    name_1 = list(input("Enter Your Name: ").lower().replace(" ", ""))
    if not name_1:
        print("Your name cannot be empty🤔")
    elif not is_valid_input(name_1):
        print("Don't enter symbols or numbers in your name🤬.")

name_2 = []
while not name_2 or not is_valid_input(name_2) or name_2 == name_1:
    name_2 = list(input("Enter Your Partner Name: ").lower().replace(" ", ""))
    if not name_2:
        print("Your partner's name cannot be empty😒")
    elif not is_valid_input(name_2):
        print("Don't enter symbols or numbers in your partner's name🤬.")
    elif name_2 == name_1:
        print("Partner name cannot be the same as your name😤")
name_3 = name_1 + name_2
for i in name_3:
    if i in name_1 and i in name_2:
        name_1.remove(i)
        name_2.remove(i)

result_word = name_1 + name_2

res = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]

while len(res) > 1:
    splitIndex = (len(result_word) % len(res) - 1)
    if splitIndex >= 0:
        right = res[splitIndex + 1:]
        left = res[: splitIndex]
        res = right + left
    else:
        res = res[: len(res) - 1]

print("Relationship Status: ", res[0])
