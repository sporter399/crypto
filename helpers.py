alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def alphabet_position(letter):

    let_pos = alphabet.index(letter.capitalize())
    
    return let_pos
    
def rotate_character(char, rot):

    if char.isalpha() == False:
        return char

    rot_pos = (alphabet_position(char) + rot) % 26
    rot_letter = alphabet[rot_pos]
    
    if char.islower():
        return rot_letter.lower()
    else:
        return rot_letter  
