# IMPORT
from calendar import c
import sys

# FUNCTIONS

def is_open_paranthese(s):
    if (s =="("):
        return True
    else:
        return False

def is_close_paranthese(s):
    if (s ==")"):
        return True
    else:
        return False

def getDeepness(calcul):
    # Init compteurs
    compt = 0
    compt_m = 0

    # Read the calcul
    for i in range(len(calcul)):
        if (is_open_paranthese(calcul[i])):
            compt += 1
        if (is_close_paranthese(calcul[i])):
            compt -= 1
        if (compt > compt_m):
            compt_m = compt
    
    return compt_m

def calc_deep(calcul, deepness):
    # Init variable
    compt = 0
    print(calcul)
    # Read all the char of the calcul
    for i in range (len(calcul)):
        if (is_open_paranthese(calcul[i])):
            compt += 1
            # Isol the simple calculus
            if(compt == deepness):
                calcul = calcul[0:i] + "|" + calcul[i+1:]
        elif (is_close_paranthese(calcul[i])):
            compt -= 1
            # Isol the simple calculus
            if(compt == deepness-1):
                calcul = calcul[0:i] + "|" + calcul[i+1:]
    
    # Transform calculus in array to isol simple calcul
    calcul = calcul.split('|')

    # Make the calcul
    calcul[1] = simple_calc(calcul[1])

    # Retransform in array
    calcul = "".join(calcul)

    return calc(calcul)

def simple_calc(calcul):
    # transform in array
    calcul = calcul.split(' ')

    # If only one element
    if (len(calcul) == 1):
        return str(calcul[0])
    # If only one operator
    elif (len(calcul)==3):
        print ("   -> " + str(calculator(calcul)))
        return str(calculator(calcul))
    # If there is more than one operator
    else:
        # Check if there is a multiplicator
        for i in range (len(calcul)):
            if (calcul[i] == "*"):
                # Add () and restart
                return addParenthese(calcul, i)
        # If there is only + and -, add () at the first operation and recalc
        return addParenthese(calcul, 1)

def addParenthese(calcul, i):
    calcul[i-1] = "(" + calcul[i-1]
    calcul[i+1] = calcul[i+1] + ")"
    calcul = arrayToString(calcul)
    return calc_deep(calcul, 1)

def arrayToString(array):
    if (len(array) == 0):
        return ""
    text = ""
    for i in range (len(array) - 1):
        text = text + str(array[i]) + " "
    text = text + str(array[len(array) - 1])
    return text

def calculator(c):
    if (c[1] == "+"):
        return float(c[0])+float(c[2])
    if (c[1] == "-"):
        return float(c[0])-float(c[2])
    if (c[1] == "*"):
        return float(c[0])*float(c[2])

def calc(calcul):
    # Get deepness
    deepness = getDeepness(calcul)

    # Resolve deepest simple calcul if deepness != 1
    if (deepness > 0):
        calcul = calc_deep(calcul, deepness)
        return calc(calcul)
    else:
        r = simple_calc(calcul)
        return r

# ALGO
if (len(sys.argv) == 1):
    print('\033[91m'+"[Error]: No expression given"+'\033[0m')
else :
    print('\033[92m' + "[Result]: "+ calc(sys.argv[1])+ '\033[0m')