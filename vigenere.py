from helpers import alphabet_position, rotate_character 

def encrypt(text, enkey):


    enkey_ints = []
    rot_string = ""
    enkey_counter = 0
    for j in enkey:

        enkey_ints.append(alphabet_position(j))
    
    for i in text:
            
        if i.isalpha() == False: 
            rot_string += i 

        if i.isalpha():
            rot_string += (rotate_character(i, enkey_ints[enkey_counter % len(enkey_ints)] ))
            enkey_counter += 1   
    
    return rot_string

def main():

    from sys import argv

    if len(argv) == 1:
        print("usage: python vigenere.py keyword")
        exit()
    
    elif argv[1].isalpha():

        enkey = (argv[1])
        text = str(input("Type a message: "))
        print(encrypt(text, enkey))

    else:
        print("usage: python vigenere.py keyword")
        exit()

if __name__ == "__main__":

    main()
