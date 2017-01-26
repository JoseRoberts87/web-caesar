
from sys import argv, exit
import string
from helpers import alphabet_position, rotate_character
def encrypt(text, rot):
    res = ""
    for i in text:        
        res = res + rotate_character(i, rot)
    return res

def user_input_is_valid(cl_args):

	if len(cl_args) == 3:
		if not cl_args[1].isdigit():
			return False
		return True
	elif len(cl_args) == 2:
		if not cl_args[1].isdigit():
			return False
		return True
	else:
		return False

def main():
	# print("I know that these are the words the user typed on the command line: ", argv)
	if user_input_is_valid(argv) == False:
		print('usage: python3 caesar.py n')
		exit()
	else:
		rot = int(argv[1])
		text = argv[2]
		print(encrypt(text, rot))

if __name__ == '__main__':
	main()