#!/bin/python3


#Variables and Methods
quote = "Tudo vale no amor e na guerra."
print(quote.upper()) #MAISCULO
print(quote.lower()) #minusculo
print(quote.title()) # titulo
print(len(quote))

name = "Bruno" #string
age = 17 #int int(17)
gpa = 4.1 #float float(3.7)

print(int(age))
print(int(17.9))

print("Meu nome é " + name + " e eu tenho " + str(age) + " anos")
age +=1
print(age)
aniversario = 1
age += aniversario
print(age)

print('\n')
#functions
print("Exemplo, essa é uma função:")

def who_am_i(): #essa é uma função
	name = "Bruno"
	age = 17
	print("Meu nome é " + name + " e eu tenho " + str(age) + " anos")
who_am_i()

#adding parameters
def add_one_hundred(num):
	print(num + 100)
add_one_hundred(100)

#mult parameters
def add(x,y):
	print(x + y)
add(7,7)

def multiply(x,y):
	return x * y
print(multiply(7,7))

def square_root(x):
	print(x ** .5)
square_root(64)

def nl():
	print('\n')
nl()

#Bollean expression (Verdadeiro ou falso)
print("Boolean expressions:")

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

nl()
#Relational and Boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7>= 7
less_than_equal_to = 7 <= 7

test_and = (7>5) and (5<7) #Verdadeiro
test_and2 = (7>5) and (5>7) #Falso
test_or = (7>5) or (5<7) #Verdadeiro
test_or2 = (7>5) or (5>7) #Verdadeiro

test_not = not True #Falso

nl()
#Conditional Statements
def drink(money):
	if money >= 2:
		return "Delicia!"
	else:
		return "Pobre é uma coisa triste!"
print(drink(3))
print(drink(1))
def alcool (age , money):
	if (age >= 18) and (money>=5):
		return "Boa compra volte novamente"
	elif (age >= 18) and (money<5):
		return "Tira uma latinha"
	elif (age<18) and (money<5):
		return "Chama a segurança por favor"
	else: 
		return "Tira uma latinha"	
print(alcool(18,5))
print(alcool(18,4))
print(alcool(17,4))
print(alcool(18,4))

nl()
#Listas - Tem Chaves [] 
movies = ["O Todo Poderoso", "Detetive Pikachu", "Smosh the movie", "John Wick"]
print(movies[0]) #Primeiro item
print(movies[1]) #Segundo item
#print(movies[2]) #Terceiro item
#print(movies[3]) #Quarto item
print(movies[1:4])
print(movies[1:])
print(movies[-1])
print(len(movies))
movies.append("JAWS")
print(movies)
movies.pop()
print(movies)
movies.pop(0)
print(movies)

nl()
#Tuples - Nâo muda, ()
grades = ("MB","B","R","R-","I")
print(grades[1])

nl()
#Looping

#For loops - start to finish
vegetais = ["pepino","espinafre","couve"] 
for x in vegetais:
	print(x)
	
#While loops - Executa enquanto é verdade

i=1 
while i<10:
	print(i)
	i+=1

