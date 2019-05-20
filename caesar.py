from helpers import alphabet_position, rotate_character

def encrypt(text, rot):

    rot_string = ""
    for i in text:
        
        rot_string += (rotate_character(i, rot))
    
    return rot_string

def main():

    from sys import argv, exit
    
    if len(argv) == 1:
        print("usage: python caesar.py n")
        exit()

    elif argv[1].isdigit():

        text = str(input("Type a message: "))
        rot = int(argv[1])
        print(encrypt(text, rot))

    else:
        print("usage: python caesar.py n")
        exit()

  
if __name__ == "__main__":

    main()
