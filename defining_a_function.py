# dog_name = 'Codie'
# dog_weight = 40
# if dog_weight > 20:
#     print(dog_name, 'says WOOF WOOF')
# else:
#     print(dog_name, 'says woof woof')   

# dog_name = 'Sparky'
# dog_weight = 9
# if dog_weight > 20:
#     print(dog_name, 'says WOOF WOOF')
# else: 
#     print(dog_name, 'says woof woof')

# dog_name = 'Jackson'
# dog_weight = 12
# if dog_weight > 20:
#     print(dog_name, 'says WOOF WOOF')
# else: 
#     print(dog_name, 'says woof woof')

# dog_name = 'Fido'
# dog_weight = 65
# if dog_weight > 20:
#     print(dog_name, 'says WOOF WOOF')
# else: 
#     print(dog_name, 'says woof woof')

def bark(name, weight):
    if weight > 20:
        print(name, 'says WOOF WOOF')
    else:
        print(name, 'says woof woof')

bark('Codie', 40)
bark('Sparky', 9)
bark('Jackson', 12)
bark('Fido', 65)




def get_bark(weight):
    if weight > 20:
        return 'WOOF WOOF'
    else:
        return 'woof woof'

roses_bark = get_bark(40)
print("Roses's bark is", roses_bark)




def how_should_I_get_there(miles):
    if miles > 120.0:
        print('Take a plane')
    elif miles >= 2.0:
        print('Take a car')
    else:
        print('Walk')

how_should_I_get_there(800.3)

how_should_I_get_there(2.0)

how_should_I_get_there(.5)





def make_greeting(name):
    return 'Hi ' + name + '!'

make_greeting('Speedy')

def compute(x, y):
    total = x + y
    if (total > 10):
        total = 10
    print(total)

compute(2, 3)

def allow_access(person):
    if person == 'Dr Evil':
        answer = True
    else:
        answer = False
    print(answer)

allow_access('Dr Evil')    

# hair = input("what color hair? [brown]")
# if hair == '':
#     hair = 'brown'
# print('You chose', hair)

# hair_legnth = input("what hair length [short]? ")
# if hair_legnth == '':
#     hair_length = 'short'
# print('You chose', hair_length)

# eyes = input("What eye color [blue]? ")
# if eyes == '':
#     eyes = 'blue'
# print('You chose', eyes)

# gender = input("What gender [female]? ")
# if gender == '':
#     gender = 'female'
# print('YOu chose', gender)

def get_attribute(query, default):
    question = query + ' [' + default + ']? '
    answer = input(question)
    if (answer == ''):
        answer = default
    print('You chose', answer)
    return answer

hair = get_attribute('What hair color', 'brown')
hair_length = get_attribute('What hair length', 'short')
eye = get_attribute('What eye color', 'blue')
gender = get_attribute('What gender', 'female')
glasses = get_attribute('Has glasses', 'no')
beard = get_attribute('Has beard', 'no')






def drink_me(param):
    msg = 'Drinking ' + param + ' glass'
    print(msg)
    param = 'empty'
    
glass = 'full'
drink_me(glass)
print('The glass is', glass)

# Drinking full glass
# The glass is full




greeting = 'Greetings'

def greet(name, message):
    global greeting
    print(greeting, name + '.', message)

greet('June', 'See you soon!')

# Greeting June. See you soon!

greeting = 'Greetings'

def greet(name, message):
    global greeting
    greeting = 'Hi'
    print(greeting, name + '.', message)

greet('June', 'See you soon!')
print(greeting)

# Hi June. See you soon!
# var greeting = Hi





# default parameters

# def greet(name, message='You rule!', emoticon):
#     print('Hi', name + '.', message, emoticon')
# DOESNT WORK BECAUSE THE KEYWORD PARAMETERS NEED TO BE AT THE END

def greet(name, emoticon, message='You rule!'):
    print('Hi', name + '.', message, emoticon)

greeting = greet('Danielle', 'Thumbs up')


def make_sundae(ice_cream='vanilla', sauce='chocolate', nuts=True, banana=True, brownies=False, whipped_cream=True):
    recipe = ice_cream + ' ice cream and ' + sauce + ' sauce ' 
    if nuts:
        recipe = recipe + 'with nuts and '
    if banana:
        recipee = recipe + 'a banana and '
    if brownies:
        recipe = recipe + 'a brownie and '
    if not whipped_cream:
        recipe = recipe + 'no '
    recipe = recipe + 'whipped cream on top.'
    return recipe

sundae = make_sundae()
print('One sundae coming up with', sundae)

sundae = make_sundae('chocolate')
print('One sundae coming up with', sundae)

sundae = make_sundae(sauce='caramel', whipped_cream=False, banana=False)
print('One sundae coming up with', sundae)

sundae = make_sundae(whipped_cream=False, banana=True, brownies=True, ice_cream='peanut butter')
print('One sundae coming up with', sundae)



#  practice with nested functions

for i in range(0 ,4):
    for j in range(0, 4):
        print(i * j)

for word in ['ox', 'cat', 'lion', 'tiger', 'bobcag']:
    for i in range(2, 7):
        letters = len(word)
        if (letters % i) == 0:
            print(i, word)

full = False

donations = []
full_load = 45

toys = ['robot', 'doll', 'ball', 'slinky']

while not full:
    for toy in toys:
        donations.append(toy)
        size = len(donations)
        if (size >= full_load):
            full = True

print('Full with', len(donations), 'toys')
print(donations)





