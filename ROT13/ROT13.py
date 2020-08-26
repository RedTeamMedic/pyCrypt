rot13transform = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')

def rot13(text):
	return text.translate(rot13transform)

def main():
	message = input("Enter your message to be encrypted: ")
	print(rot13(message))

if __name__ == "__main__":
	main()
