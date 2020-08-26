message = input("Enter the message to be decrypted: ")
translated = ' ' #decrypted text will be stored in this variable
i = len(message) - 1

while i >= 0:
	translated = translated + message[i]
	i = i - 1
print("The decrypted text is : ", translated)
