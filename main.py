# --------------------- MORSE CODE CONVERTOR ---------------------

is_on = True

while is_on:
	decision = input("\nWould you like to convert a message to morse code or to latin alphabet? Type 'morse code'"
	                 " or 'alphabet'."
	                 "\nType 'exit' if you wish to exit the programme: ")
	if decision == "exit":
		is_on = False
	else:
		morse_code_dict = {
			"A": ".-",
			"B": "-...",
			"C": "-.-.",
			"D": "-..",
			"E": ".",
			"F": "..-.",
			"G": "--.",
			"H": "....",
			"I": "..",
			"J": ".---",
			"K": "-.-",
			"L": ".-..",
			"M": "--",
			"N": "-.",
			"O": "---",
			"P": ".--.",
			"Q": "--.-",
			"R": ".-.",
			"S": "...",
			"T": "-",
			"U": "..-",
			"V": "...-",
			"W": ".--",
			"X": "-..-",
			"Y": "-.--",
			"Z": "--..",
			"1": ".----",
			"2": "..---",
			"3": "...--",
			"4": "....-",
			"5": ".....",
			"6": "-....",
			"7": "--...",
			"8": "---..",
			"9": "----.",
			"0": "-----",
			",": "--..--",
			".": ".-.-.-",
			"?": "..--..",
			"/": "-..-.",
			"-": "-....-",
			"(": "-.--.",
			")": "-.--.-",
		}

		if decision == "morse code":
			is_on = True
			while is_on:
				message = input("\nType the message you want to convert: ").upper()
				if message == "EXIT":
					is_on = False
				else:
					def encrypt(code):
						response = ""
						# Convert each letter into morse code
						for letter in code:
							# Check if the character is in the dictionary
							if letter in morse_code_dict:
								response += morse_code_dict[letter] + " "
							else:
								response += " "

						print("Your message is: ")
						print(response)


					encrypt(message)

		elif decision == "alphabet":
			is_on = True
			while is_on:
				message = input("\nType the morse code message you want to convert: ")
				if message == "exit":
					is_on = False
				else:
					def decrypt(code):
						response = " "
						# Convert morse code symbol into letter
						code = code.split(" ")
						for symbols in code:
							# Check if the character is in the dictionary
							for symbol, sym in morse_code_dict.items():
								if sym == symbols:
									response += symbol

						print("Your message is: ")
						print(response)

					decrypt(message)

		else:
			print("\nSorry, please type your decision again. ")
