#импорт библиотек
#Некоторые особенности игры будут реализованы позже

import time
import sys
import os
import random

#prepare to work with the colors of unix console
import colorama
from colorama import Fore, Back, Style
colorama.init()

money = 100
currency = "$"

print(Fore.YELLOW + 'Однорукий бандит. ver. 0.1\nCreated by Opsis ')
time.sleep(2)
os.system('clear')

def oneHand():
	switch = True
	global money
	print(Fore.GREEN + 'Добро пожаловать в игру \"Однорукий бандит!\" Ваш баланс \n')
	print(Fore.GREEN + f"{money}, так же в игре можно делать ставки: ")
	print(Fore.GREEN + '''Выберете соответствующий пункт меню
	1 - начать игру
	2 - выйти из игры''')
	
	select = int(input(Fore.GREEN + '>>> '))
	if ((select < 0) or (select > 2)):
		exit()
	elif (select == 2):
		exit()
	elif (select == 1):
				
		x = random.randint(1,9)
		y = random.randint(1,9)
		z = random.randint(1,9)
					
		print(Fore.GREEN + 'Ждем результата игры...')	
		time.sleep(2)
		print(Fore.RED + " " * 8, "-----------")
		print(Fore.BLUE + ' ' * 10, x, end=' ')
		time.sleep(2)
		print(Fore.BLUE + f"{y}", end=' ')
		time.sleep(2)
		print(Fore.BLUE + f"{z}")
		print(Fore.RED + " " * 8, "------------")

		if (x == y == z):
			print(Fore.GREEN + 'Полное совпадение!')
			money = money * 3	
			print(Fore.GREEN + F'Ваш баланс {money, currency}')
			writeMoney()
			time.sleep(2)	
			os.system('clear')
			tempMenu()
		elif ((x == y) or (y == z) or (x == z)):
			print(Fore.GREEN + 'Совпало 2 цифры из трех!')
			money = round(((money * 3) / 6), 2)
			print(Fore.GREEN + F'Ваш баланс {money, currency}')
			writeMoney()
			time.sleep(2)
			os.system('clear')
			tempMenu()
		elif (x != y != z):
			print(Fore.RED + 'Вы проиграли!')
			money = round(((math.sqrt(money) * 3) / 6) - 1, 2)
			print(Fore.RED + F'Ваш баланс {money, currency}')
			writeMoney()
			time.sleep(2)
			os.system('clear')
			tempMenu()


def writeMoney():
	global money
	f = open("money.dat", "w", encoding="utf-8")
	f.write(str(money))
	f.close()


def tempMenu():
	global money
	if (money <= 0):
		print(Fore.RED + 'У вас Нулевой баланс.')
		exit()
	print(Fore.GREEN + 'Сыграете еще раз (1 - Да, 2 - Выход)')
	menu = int(input(Fore.GREEN + '>>> '))
	
	if (menu < 0 or menu > 2):
		exit()
	elif(menu == 2):
		exit()
	elif (menu == 1):
		oneHand()	


def exit():
	print(Fore.MAGENTA + 'До свидания!')
	switch = False

oneHand()
