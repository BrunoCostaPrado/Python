#!/bin/python3
import sys #sistema e parametros
from datetime import datetime as dt
print(dt.now())

my_name = "Bruno"
print(my_name[0])
print(my_name[-1])

sentence = "Essa é uma sentença."
print(sentence[:4])

print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "Ele disse, \"passa o dinheiro\""
print(quote)

too_much_space ="		 hello		"
print(too_much_space.strip())

print("a" in "Apple")

letter = "A"
word = "Apple"
print(letter.lower()in word.lower()) #melhorado
movie = "Jonn Wick"
print("Meu filme favorito é {}.".format(movie))

#Dictionaries - key/value pairs {}
drinks={"White Russian":7, "Old Fashion":10, "Lemon Drop":8} #drink é a chave, preço é valor
print(drinks)

employees={"Finanças": ["Bob", "Linda", "Tina"], "IT": ["Gene" ,"Louise", "Teddy"], "RH":["Jimmy Jr","Mort"]}
print(employees)

employees['Legal'] = ["Sr . Frond"] #adiciona uma nova chave: valor par
print(employees)

employees.update({"Vendas":["Andie","Ollie"]})
print(employees)

drinks['White Russian'] = 8
print(drinks)

print(drinks.get("White Russian")) 
