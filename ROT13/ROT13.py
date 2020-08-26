encrypt = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
decrypt = str.maketrans('NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm','ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

def rot13encrypt(text):
	return text.translate(encrypt)

def rot13decrypt(text):
	return text.translate(decrypt)

def main():
	choice = input("Would you like to encrypt or decrypt? Enter e for encrypt or d for decrypt: ")
	if choice == 'e':
		message = input("Enter your message to be encrypted: ")
		print(rot13encrypt(message))
	elif choice == 'd':
		message = input("Enter your message to be decrypted: ")
		print(rot13decrypt(message))
	else:
		print("Sorry, I didn't get that. Please try again. Goodbye.")

if __name__ == "__main__":
	main()
