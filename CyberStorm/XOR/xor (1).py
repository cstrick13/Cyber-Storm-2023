import sys

with open('key','rb') as file:
	key = bytearray(file.read())
        #stackoverflo
text = sys.stdin.buffer.read()
#List comprhension that loops throught the text
#checks if it equal if not equal cycles through the  key by the modulus 
# xor th text and the key by doing a for loop the runs through the len of text and passes i throug both
#the cycle trick i learned from a video of sliding ciphers

if len(key) == len(text):
	result = bytearray([text[i] ^ key[i] for i in range(len(text))])
else:
	result = bytearray([text[i] ^ key[i % len(key)] for i in range(len(text))])
  #return as bit using bytearray      

sys.stdout.buffer.write(result)
    

