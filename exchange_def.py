#Swap helps for exchange number

def exchange(number1,number2):
	Swap = number1
	number1=number2
	number2 = Swap
	return number1, number2

number1=int(input('number1: '))
number2=int(input('number2: '))
print('Before exchange: ' +str(number1) + ' and ' + str(number2))
number1, number2 = exchange(number1,number2)
print('After exchange: ' + str(number1) + ' and ' + str(number2))
