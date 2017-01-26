import string
def alphabet_position(letter):
    alpha = string.ascii_lowercase
    ualpha = alpha.upper()
    for i in letter:
        if i in alpha:
            iletter = alpha.index(i)
        elif i in ualpha: 
            iletter = ualpha.index(i)
        elif i not in alpha or i not in ualpha:
            iletter = i
    return iletter  

def rotate_character(char, rot):
    alpha = string.ascii_lowercase
    ualpha = alpha.upper()
    char = str(char)
    if char in alpha:
        malpha = alpha  
    elif char in ualpha: 
        malpha = ualpha
    else:
        malpha = char
        return malpha
    rchar = (alphabet_position(char) + rot) % 26
    rchar = malpha[rchar]
    return rchar  