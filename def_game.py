import random

print("-----------Make Up a number between 1-100-----------")
print("---If you want exit, you must enter 0, but if you want start again, you must enter 1 ---")

def start_game(attempt, number) :
	case=random.randint(1,100)
	while number != case:
		number=int(input("Your Number: "))
		attempt += 1
		if number ==0:
			print("Correct Answer is: " + str(case) + ", Bye")
			break
		if number==1:
			print("You Reset the program, start again")
			continue
		if number < case:
			print(str(number) + ' is smallest number')
		elif number > case:
			print(str(number) + ' is very large number')
		elif number == case:
			print(str(number) + ' is OK, Congrats! You have found Random Number')
	return attempt
def end_game(attempt):
	print("You try " + str(attempt) + " steps.")

#Main Programm

game = start_game(0,0)
end_game(game)
