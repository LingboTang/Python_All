# global database

number_base = ['780-412-3456','780-444-1234','403-456-1234','403-556-7891','604-395-1122']

def check_number(number):
	if number in number_base:
		return 1
	else:
		return 0

def list_search(number_base,number):
	if (check_number(number)==1):
		base_size = len(number_base)
		comparator1 = number[0:3]
		for i in range(0,base_size):
			comparator2 = number_base[i][0:3]
			if (comparator1 == comparator2):
				print(number_base[i])
	else:
		print("not found")
		number_base.append(number)

def main():
	number = input("Enter number: ")
	list_search(number_base,number)

main()
