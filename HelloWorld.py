#addition
def add(num1, num2):
	return num1 + num2
	
#subtraction
def sub(num1, num2):
	return num1 - num2
	
#multiply
def mul(num1, num2):
	return num1 * num2

#division
def div(num1, num2):
	return num1/num2

#calculator program
def calc(num1, oper, num2):
	if(oper == "+"):
		return add(num1, num2)
	elif (oper == "-"):
		return sub(num1, num2)
	elif (oper == "*"):
		return mul(num1, num2)
	elif (oper == "/"):
		return div(num1, num2)
	else:
		return "Invalid Operation:" + oper
		
#main program
def main():
	num1 = int(input())
	oper = input()
	num2 = int(input())
	res = calc(num1, oper, num2)
	print(res)


main()