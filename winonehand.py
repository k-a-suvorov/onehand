#Функция Рулетки, пока без анимации	
#конструкция if elif громоздкая, так как нужно проверить множество выигрышных условий	
import os
import sys
import time
import random
import datetime
import math


money = 100
currency = '$'


from ctypes import *
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))


def color(c): #setconsoletextcolor
	windll.Kernel32.SetConsoleTextAttribute(h,c)


def colorLine(c, s): #Win color text
	#os.system("cls")
	color(c)
	print("*" * (len(s) +2))
	print(" " + s)
	print("*" * (len(s) +2))


def oneHand():
	switch = True
	global money
	colorLine(14, 'Добро пожаловать в игру \"Однорукий бандит!\" Ваш баланс \n')
	print(f"{money}, так же в игре можно делать ставки: ")
	print('''Выберете соответствующий пункт меню
	1 - начать игру
	2 - выйти из игры''')
	
	select = int(input('>>> '))
	if ((select < 0) or (select > 2)):
		exit()
	elif (select == 2):
		exit()
	elif (select == 1):
				
		x = random.randint(1,9)
		y = random.randint(1,9)
		z = random.randint(1,9)
					
		color(11)
		colorLine(11, 'Ждем результата игры...')	
		time.sleep(2)
		print(" " * 8, "-----------")
		print(' ' * 10, x, end=' ')
		time.sleep(2)
		print(y, end=' ')
		time.sleep(2)
		print(z,)
		print(" " * 8, "------------")

		if (x == y == z):
			colorLine(11, 'Полное совпадение!')
			money = money * 3	
			print(F'Ваш баланс {money, currency}')
			writeMoney()
			time.sleep(2)	
			os.system('cls')
			tempMenu()
		elif ((x == y) or (y == z) or (x == z)):
			colorLine(14, 'Совпало 2 цифры из трех!')
			money = round(((money * 3) / 6), 2)
			print(F'Ваш баланс {money, currency}')
			writeMoney()
			time.sleep(2)
			os.system('cls')
			tempMenu()
		elif (x != y != z):
			colorLine(12, 'Вы проиграли!')
			money = round(((math.sqrt(money) * 3) / 6) - 1, 2)
			print(F'Ваш баланс {money, currency}')
			writeMoney()
			time.sleep(2)
			os.system('cls')
			tempMenu()


def writeMoney():
	global money
	f = open("money.dat", "w", encoding="utf-8")
	f.write(str(money))
	f.close()


def tempMenu():
	global money
	if (money <= 0):
		colorLine(12, 'У вас Нулевой баланс.')
		exit()
	colorLine(2, 'Сыграете еще раз (1 - Да, 2 - Выход)')
	menu = int(input('>>> '))
	
	if (menu < 0 or menu > 2):
		exit()
	elif(menu == 2):
		exit()
	elif (menu == 1):
		oneHand()	


def exit():
	colorLine(12, 'До свидания!')
	switch = False

oneHand()
