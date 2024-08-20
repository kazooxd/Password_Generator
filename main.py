import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

pass_chars = []
whole_pass = ""

for pass_let in range(0, nr_letters):
  pass_let = letters[random.randrange(0, len(letters))]
  pass_chars.append(pass_let)
  letters.remove(pass_let)

for pass_num in range(0, nr_numbers):
  pass_num = numbers[random.randrange(0, len(numbers))]
  pass_chars.append(pass_num)
  numbers.remove(pass_num)

for pass_sym in range(0, nr_symbols):
  pass_sym = symbols[random.randrange(0, len(symbols))]
  pass_chars.append(pass_sym)
  symbols.remove(pass_sym)

random.shuffle(pass_chars)

for each_char in range(len(pass_chars)):
  rand_whole_pass = random.choice(pass_chars)
  whole_pass += str(rand_whole_pass)
  pass_chars.remove(rand_whole_pass)

print(f"Your password is: {whole_pass}")