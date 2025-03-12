"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Rostyslav Luzan
email: roluzan@email.cz

"""


TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

def analyze_text(text):
    words = text.split()  
    word_count = len(words)  

    capitalized_count = 0  
    uppercase_count = 0  
    lowercase_count = 0  
    number_count = 0  
    sum_numbers = 0  
    length_counts = {}  

    for word in words:
        clean_word = word.strip(".,!?")  

        if clean_word.istitle():
            capitalized_count += 1
        if clean_word.isupper():
            uppercase_count += 1
        if clean_word.islower():
            lowercase_count += 1
        if clean_word.isdigit():
            number_count += 1
            sum_numbers += int(clean_word)

       
        word_length = len(clean_word)
        if word_length > 0:  
            if word_length in length_counts:
                length_counts[word_length] += 1
            else:
                length_counts[word_length] = 1

    
    print(f"Total words: {word_count}")
    print(f"Words starting with a capital letter: {capitalized_count}")
    print(f"Words in uppercase: {uppercase_count}")
    print(f"Words in lowercase: {lowercase_count}")
    print(f"Numbers found: {number_count}")
    print(f"Sum of all numbers: {sum_numbers}")

   
    separator = "-" * 30
    print("\nLEN | OCCURRENCES        | NR.")
    print(separator)
    for length, count in sorted(length_counts.items()):
        print(f"{length:3} | {'*' * count:<20} | {count}")
        

users = [("bob","123"),("ann", "pass123"), ("mike", "password123"),("liz","pass123")]
separater = "-" * 40

name_in = input("Username: ")
pas_in = input("Password: ")
print (separater)

authenticated = False 

for name, password in users:
    if (name_in, pas_in) == (name, password):
         authenticated = True
         print(f"Hello, {name_in}!\nWe have 3 texts to be analyzed")
         print(separater)
         break
    
if not authenticated:
        print("unregistered user, terminating the program..")  
        exit()

choice = input("Enter a number between 1 and 3 to select: ")

if choice.isdigit():
    choice = int(choice)  
    if 1 <= choice <= 3:
        analyze_text(TEXTS[choice - 1]) 
    else:
        print("Invalid choice! There is no such text!")
else:
    print("Invalid input!")
