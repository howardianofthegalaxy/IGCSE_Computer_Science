#what is a string?
#return length of a string - len()
#lower -> uppercase
alphabet = "abcdefghifklmnopqrstuvwxyz"
alphabet_length = len(alphabet)
uppercase_alphabet = alphabet.upper()
print(alphabet_length)
print(uppercase_alphabet)
position_of_letter_d = alphabet.index("e")
print(position_of_letter_d + 1)

message = "hello world"
print(message)
uppercase_message = message.upper()
print(uppercase_message)
print(message)


english_a = "a"
ASCII_a = ord(english_a)
print (ASCII_a)


ASCII_code_for_a = 97
a_z_letter = chr(97)
print(a_z_letter)

string_one = "good morning"
string_two = " my neighbor"
combined = string_one + "" + string_two
print(combined)