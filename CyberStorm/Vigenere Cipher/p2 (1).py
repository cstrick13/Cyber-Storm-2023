import sys

def main():
	list1 = []

	#takes information form the arguemnts
	cryption = sys.argv[1]
	#takes the key into a list makes it all upppercase
	key = list((sys.argv[2].upper()).replace(" ",""))



	#constantly checks the standard input
	for string in sys.stdin:
		#removes the new line chracter
		string1 = string[:-1]
		#looks and adds the key to the key list untill matching the list of the string
		for i in range(len(string1)-len(key)):
			if key[i].isspace():
				continue
			else:
				key.append(key[i%len(key)])
		

		#if statment to check if we are encrypting or decrypting
		if cryption == '-e':
			encryption(string1,key)
		else:
			decryption(string1,key)

def encryption(input,key):
	#list for adding the values one at a time
	text = []

	#loop that goes through the length of the desired input
	for i in range(len(input)):
		
		#checks if the value is a letter
		if input[i].isalpha():

			#takes the character and encypts it and adds 97 to match up with the begging of ascii
			enc = (ord(input[i].upper()) + ord(key[i]))%26
			enc += 97

			#checks of the original input is capital or not, then adds it to text list
			if input[i].islower():
				text.append(chr(enc))
			else:
				text.append(chr(enc).upper())
		#takes values that are not letters and adds them to the text list
		else:
			text.append(input[i])
			key.insert(i,' ')

	text = "".join(text)
	print(text)

def decryption(input,key):
	text = []
	for i in range(len(input)):
		
		if input[i].isalpha():
			enc = (26+ord(input[i].upper()) - ord(key[i]))%26
			enc += 97

			if input[i].islower():
				text.append(chr(enc))
			else:
				text.append(chr(enc).upper())

		else:
			text.append(input[i])
			key.insert(i,' ')

	text = "".join(text)
	print(text)




main()