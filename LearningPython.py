if "Sarah" >= "Andrew":
  print("True")
else:
  print("False")
i = 0
while i < 5:
  print("Andrew")
  i += 2

my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list)):
  print(my_list[i])

for each in my_list:
  print(each)

my_set = {1, 2, "Andy", False}
print(my_set)

my_list = [1, 2, 3]
my_list.append(4)
my_list.insert(1, 1.5)
my_list.pop(1)
print(my_list)

my_dict = {"Tony": "Instructor"}
my_dict["Andy"] = "Student"
print(my_dict)
for each in my_dict.keys():
  print(each, my_dict[each])

for each, value in my_dict.items():
  print(each, value)

print(len(my_dict))

def hello(temp):
  print(temp)

print('hello')

print("This program averages a list of 5 integers")
i = 0
grades = []
while i < 5:
  grade = input("What is your grade? ")
  grades.append(grade)
  i += 1
total = 0
for each in grades:
  each = int(each)
  total += each
print(total/5)

print(ord('E'))
print(chr(37))

number = int(input("Enter an integer: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not prime.")
            break
    else:
        print(number, "is prime.")
else:
    print(number, "is not prime.")

x = input("Enter your message please ")
y = []
for each in x:
  temp = ord(each)
  temp = temp + 3
  y.append(chr(temp))

print(''.join(map(str, y)))

w = input("Enter your message please ")
z = []
for each in w:
  temp = ord(each)
  temp = temp - 3
  z.append(chr(temp))

print(''.join(map(str, z)))

number = int(input("Enter a two-digit number please "))
tens_digit = number // 10
ones_digit = number % 10
print("The tens digit is", tens_digit)
print("The ones digit is", ones_digit)

import random
winner = random.randint(10, 99)
number = int(input("Enter a two-digit number please "))
print("The winning number was", winner)

t1 = winner // 10
o1 = winner % 10
t2 = number // 10
o2 = number // 10

if winner == number:
  print("You win $10,000!")
elif t1 == o2 and o1 == t2:
  print("You win $3,000!")
elif t1 == t2 or o1 == o2:
  print("You win $1,000!")
else:
  print("You win $0!")

year = int(input("Enter a year please: "))
if year % 4 == 0:
  if year % 100 == 0 and year % 400 != 0:
    print("This year is not a leap year.")
  else:
    print("This year is a leap year.")
else:
  print("This year is not a leap year.")

text = input("Enter your text please: ")
text = text.lower()
print("Each letter occured this many times:")
letters = ['a', 'b', 'c', 'c', 'e', 'f', 'g', 'h', 'i', 'j',
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
'w', 'x', 'y', 'z']
for letter in letters:
  print(letter + ":", text.count(letter))

import string
text = input("Enter your text please: ")
text = text.lower()
letters = string.ascii_lowercase
for letter in letters:
  print(letter + ":", text.count(letter))

import string
text = input("Enter your text please: ")
remove = string.whitespace + string.punctuation
for each in remove:
  text = text.replace(each, '')
lowers = string.ascii_lowercase
uppers = string.ascii_uppercase
numbers = string.digits
chars = lowers + uppers + numbers
total = 0
for lower in lowers:
  value = text.count(lower)
  total += value
  print(lower + ":", value)
  if value > 0:
    chars = chars.replace(lower, '')
x = total
for upper in uppers:
  value = text.count(upper)
  total += value
  print(upper + ":", value)
  if value > 0:
    chars = chars.replace(upper, '')
y = total
for number in numbers:
  value = text.count(number)
  total += value
  print(number + ":", value)
  if value > 0:
    chars = chars.replace(number, '')
print("There are", total, "alphanumeric characters.")
print("There are", x, "lower case letters and", y - x, "upper case letters.")
letters = lowers + uppers + numbers
max_value = 0
max_char = ''
for letter in letters:
  if text.count(letter) > max_value:
    max_value = text.count(letter)
    max_char = letter
print("The most frequent character is:", max_char)
print("The absent letters were:", chars)

import string
print("Welcome to the Python Calculator")
problem = input("Enter a problem: ")
temp = string.whitespace
for c in temp:
  problem = problem.replace(c, '')
if ord(problem[1]) == 43:
  print(int(problem[0]) + int(problem[2]))
if ord(problem[1]) == 45:
  print(int(problem[0]) - int(problem[2]))
if ord(problem[1]) == 42:
  print(int(problem[0]) * int(problem[2]))
if ord(problem[1]) == 47:
  print(int(problem[0]) / int(problem[2]))

def Exercise1():
  import string
  password = input("Enter your password please: ")
  total_digits = 0
  digits = string.digits
  for digit in digits:
    total_digits += password.count(digit)
  if len(password) < 8:
    print("Sorry. Eight characters required.")
  elif not password.isalnum():
    print("Sorry. Alphanumeric characters only.")
  elif total_digits < 2:
    print("Sorry. Two digits required.")
  else:
    print("Nice password.")

def Exercise1():
  import random
  length = int(input("Enter the length of DNA: "))
  bases = ['A', 'T', 'G', 'C']
  new = ''
  for each in range(length):
    new += bases[random.randint(0,3)]
  print(new)

def Exercise2():
  strand = input("Enter the strand of DNA with the start and end indicated by dashes: ")
  strand = strand.replace('-', '')
  dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
  new = ''
  for base in strand:
    new += dict[base]
  print(new)

def Exercise3():
  strand = input("Enter the strand of DNA with its start and end indicated by dashes: ")
  pair = input("Enter the base pair with its start and end indicated by dashes: ")
  strand = strand.replace('-', '')
  pair = pair.replace('-', '')
  fixable = []
  fix_count = 0
  unfixable = []
  unfix_count = 0
  for base in strand:
    if base == 'X':
      pos = strand.find('X')
      if pair[pos] == 'A':
        strand = strand.replace('X', 'T')
        fixable.append(str(pos) + 'AT')
        fix_count += 1
      if pair[pos] == 'T':
        strand = strand.replace('X', 'A')
        fixable.append(str(pos) + 'TA')
        fix_count += 1
      if pair[pos] == 'G':
        strand = strand.replace('X', 'C')
        fixable.append(str(pos) + 'GC')
        fix_count += 1
      if pair[pos] == 'C':
        strand = strand.replace('X', 'G')
        fixable.append(str(pos) + 'CG')
        fix_count += 1
      if pair[pos] == 'X':
        unfixable.append(str(pos) + 'XX')
        unfix_count += 1

  for base in pair:
    if base == 'X':
      pos = pair.find('X')
      if strand[pos] == 'A':
        pair = pair.replace('X', 'T')
        fixable.append(str(pos) + 'AT')
        fix_count += 1
      if strand[pos] == 'T':
        pair = pair.replace('X', 'A')
        fixable.append(str(pos) + 'TA')
        fix_count += 1
      if strand[pos] == 'G':
        pair = pair.replace('X', 'C')
        fixable.append(str(pos) + 'GC')
        fix_count += 1
      if strand[pos] == 'C':
        pair = pair.replace('X', 'G')
        fixable.append(str(pos) + 'CG')
        fix_count += 1

  print("The original strand is", strand, "and the base pair is", pair)
  print(fix_count, "base pairs could be fixed.")
  print(unfix_count, "base pairs could not be fixed.")
  print("The pairs that were fixed and their locations:", fixable)
  print("The pairs that could not be fixed and their locations:", unfixable)

exercise = input("Which exercise would you like to do? ")
if exercise == '1':
  Exercise1()
if exercise == '2':
  Exercise2()
if exercise == '3':
  Exercise3()

with open('my_lunch.txt') as read_file:
  for line in read_file:
    print(line)

x = 'An          dy'
print(x.strip('Andy'))

x = "Today is a good day, isn't it?"
print(x.split())
print(x.split('is', 2))

x = ['Today', 'is', 'a', 'nice', 'day']
x = ['a', 'p', 'p', 'l', 'e']
print("".join(x))
my_list = ['1', '2', '3', '4', '5', '6']
joint_list = '->'.join(my_list)
print(joint_list)
print(joint_list.split('->'))

x = 'Tony is a good good teacher'
print(x.replace('good', 'bad', 1))

import string
statements = ["Wow. I didn't know that.", "I'm not sure about sure about that.", "I don't think I understand."]
import random
print("Hello. I am an AI. You can talk about anything with me. ")
language = input("What language do you speak? ")
languages = {}
with open ('Hello.txt') as read_file:
  for line in read_file:
    line = line.split(':')
    line[0] = line[0].strip()
    line[1] = line[1].strip()
    languages[line[1]] = line[0]
for each, value in languages.items():
  if language == each:
    print(value)
while True:
  x = input("Say something: ")
  temp = string.whitespace
  if x == 'exit':
    break
  elif "My name" in x:
    y = x.split()
    print(f"Hi {y[3]}. My name is AI.")
  elif "How are you" in x:
    print("I'm fine. Thank you.")
  elif "don't like" in x:
    print("Neither do I.")
  elif "help" in x:
    print("No!!!")
  elif "+" in x:
    for c in temp:
      x = x.replace(c, '')
    print(int(x[0]) + int(x[2]))
  elif "-" in x:
    for c in temp:
      x = x.replace(c, '')
    print(int(x[0]) - int(x[2]))
  elif "*" in x:
    for c in temp:
      x = x.replace(c, '')
    print(int(x[0]) * int(x[2]))
  elif "/" in x:
    for c in temp:
      x = x.replace(c, '')
    print(int(x[0]) / int(x[2]))
  else:
    print(statements[random.randint(0, 2)])

with open('MachineLearning.txt') as doc:
  i = 0
  punctuations = ['.', '!', '?']
  for line in doc:
    for punctuation in punctuations:
      line = line.replace(punctuation, '.')
    sentence_count = 0
    if '.' in line:
      my_dict = {}
      word_count = 0
      i += 1
      words = line.split()
      word_count += len(words)
      for char in line:
        if char == '.':
          sentence_count += 1
      print("Number of sentences in paragraph", str(i) + ":", sentence_count)
      sentences = line.split('.')
      del sentences[-1]
      sentence_number = 0
      for sentence in sentences:
        words = 0
        sentence_number += 1
        for char in sentence:
          if char == ' ':
            words += 1
        print("There are", words, "words in sentence", str(sentence_number) + '.')
      print("Number of words in pargraph", str(i) + ':', word_count)
      print("Average words per sentence:", word_count / sentence_count)
      line = line.split()
    for word in line:
      count = line.count(word)
      my_dict[word] = count
    most_words = {}
    for k in range(10):
      max_value = 0
      for word in my_dict.keys():
        value = my_dict[word]
        if value > max_value:
          max_value = value
          most_word = word
      number_times = my_dict[most_word]
      del my_dict[most_word]
      most_words[most_word] = number_times
    print("The top 10 most used words in paragraph", str(i) + ':', most_words)
Abstraction: showing just enough info to user that allows them to interact with object
Encapsulation: bundling all related smaller components together into one larger object

class Car:
  def __init__(self):
    self.brand = "Audi"
    self.tire - "3 stars"
    self.isDriving = False
  def drive(self):
    self.isDriving = True
    print("Hello, I'm driving")
carObj = Car()
carObj.drive()

class Person:
  def __init__(self, name):
    self.name = name
    print(self.name, 'is born.')
    self.tired = True
    self.steps = 0

  def walk(self):
    if not self.tired:
      self.steps += 1
      print(self.name, 'took 1 step.')
      if self.steps > 3:
        self.tired = True
        print(self.name, 'is too tired to walk again.')
    else:
      print(self.name, 'is too tired to walk.')

  def rest(self):
    self.tired = False
    self.steps = 0
    print(self.name, 'is fully rested.')

  def get_steps(self):
    print(self.name, 'has taken', self.steps, 'steps since his last rest.')

Andy = Person('Andy')
Andy.walk()
Andy.rest()
for i in range(10):
  Andy.walk()
Andy.get_steps()

class Car:
  def __init__(self, color='white', mpg=10, gas_tank_capacity=15):
    self.color = color
    self.gas_in_tank = 0
    self.mpg = mpg
    self.miles_driven = 0
    self.gas_tank_capacity = gas_tank_capacity
    self.next_maintenance = 5000
    print("Bob's properties:", 'Color:', self.color, 'Current gas:', self.gas_in_tank, 'MPG:', self.mpg, 'Tank Capacity:', self.gas_tank_capacity, 'Next maintenance:', self.next_maintenance)

  def get_color(self):
    print(self.color)

  def repaint_car(self, color):
    if self.color == color:
      print("Sorry. Same color not allowed.")
    else:
      self.color = color
      print("The color has been changed to", color + '.')

  def get_gas_in_tank(self):
    if self.gas_in_tank >= 0:
      print("There are", self.gas_in_tank, "gallons in the tank.")
    else:
      print("Gas in tank cannot be less than 0.")

  def refuel(self, gallons):
    if gallons < self.gas_tank_capacity - self.gas_in_tank:
      self.gas_in_tank += gallons
      print("Successfully refueled", gallons, "gallons.")
    else:
      print("The gas tank cannot hold that much gas.")

  def get_miles_driven(self):
    print(self.miles_driven)

  def drive(self, miles):
    if miles > self.gas_in_tank * self.mpg:
      print("There is not enough gas to drive that far.")
    elif miles < 0:
      print("You cannnot drive negative miles.")
    elif self.miles_driven + miles > self.next_maintenance:
      print("Maintenance required.")
    else:
      self.miles_driven += miles
      self.gas_in_tank -= miles / self.mpg
      print(miles, "miles have been added to the car.")

  def send_for_maintenance(self):
    self.next_maintenance += 5000
    print("The next maintenance is due after", self.next_maintenance - self.miles_driven, "miles.")

  def miles_till_maintenance(self):
    print("The next maintenance is due after", self.next_maintenance - self.miles_driven, "miles.")

  def __str__(self):
    return("The car is " + self.color + " color, has " + str(self.gas_in_tank) + " gallons in the tank, has a mpg of " + str(self.mpg) + " has driven " + str(self.miles_driven) + " has a capacity of " + str(self.gas_tank_capacity) + " and needs maintenance in " + str(self.next_maintenance) + " miles")

Bob = Car()
print(Bob)

import random
attacker = 1000
defender = 1000
attacker_list = []
defender_list = []

while True:
  for i in range(3):
    attacker_list.append(random.randint(1,6))
  for i in range(2):
    defender_list.append(random.randint(1,6))
  attacker_list.sort()
  defender_list.sort()
  if attacker_list[-1] > defender_list[-1]:
    defender -= 1
  elif attacker_list[-1] <= defender_list[-1]:
    attacker -= 1
  if attacker_list[-1] > defender_list[-1]:
    defender -= 1
    attacker_list.clear()
    defender_list.clear()
  elif attacker_list[-1] <= defender_list[-1]:
    attacker -= 1
    attacker_list.clear()
    defender_list.clear()
  if attacker == 0:
    print("Defender wins!")
    break
  if defender == 0:
    print("Attacker wins!")
    break

import random

class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    if str(rank).isdigit() == True:
      self.value = int(self.rank)
    elif rank == 'A':
      self.value = 11
    else:
      self.value = 10

  def __add__(self, other):
    return self.value + other.value

  def __str__(self):
    return self.rank + " of " + self.suit

  def __repr__(self):
    return str(self)

my_card = Card('Hearts', 'J')
my_card2 = Card('Spades','2')

print("Suit:", my_card.suit)
print("Rank:", my_card.rank)
print("Value:", my_card.value)

print(my_card + my_card2)

class Deck:
  def __init__(self):
    suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    self.deck = []
    for suit in suits:
      for rank in ranks:
        self.deck.append(Card(suit, rank))

  def print_deck(self):
    print("Deck:", self.deck)

  def deal(self, number):
    dealed_cards = []
    for i in range(number):
      x = random.randint(0, len(self.deck) - 1)
      dealed_cards.append(self.deck[x])
      self.deck.pop(x)
    return dealed_cards

my_deck = Deck()
print(my_deck.deal(26))
print(my_deck.deal(26))
my_deck.print_deck()
