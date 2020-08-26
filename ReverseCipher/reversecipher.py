choice = input("Do you want to encrypt or decrypt? Enter e for encrypt or d for decrypt: ")
if choice == 'd':

	message = input("Enter the message to be decrypted: ")
	translated = ' ' #decrypted text will be stored in this variable
	i = len(message) - 1

	while i >= 0:
		translated = translated + message[i]
		i = i - 1
	print("The decrypted text is : ", translated)

elif choice == 'e':
	message = input("Enter the message to be encrypted: ")
	translated = ' ' #cipher text is stored in this variable
	i = len(message) - 1

	while i >= 0:
		translated = translated + message[i]
		i = i - 1
	print("The cipher text is : ", translated)
else:
	print("Sorry, I didn't get that. Try again. Goodbye.")
