# IMPORT
from calendar import c
import sys

# FUNCTIONS
''' Check if a char is '(' '''
def is_open_paranthese(s):
    if (s =="("):
        return True
    else:
        return False

''' Check if a char is ')' '''
def is_close_paranthese(s):
    if (s ==")"):
        return True
    else:
        return False

''' Calcul the max deepness of a calcul '''
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
    
    # return the deepness of the calcul
    return compt_m

''' Resolve the deepest calcul of a calcul '''
def calc_deep(calcul, deepness):
    # Init variable
    compt = 0
    
    # Print for explaination
    print(calcul)

    # Read all the char of the calcul and select the first deepest simple calcul
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
                break
    
    # Transform it into array to isol simple calcul
    calcul = calcul.split('|')

    # Make the calcul
    calcul[1] = simple_calc(calcul[1])

    # Retransform in string
    calcul = "".join(calcul)

    # calc this new simplified calcul
    return calc(calcul)

''' Resolve a simple calcul '''
def simple_calc(calcul):
    # transform in array
    calcul = calcul.split(' ')

    # If only one element
    if (len(calcul) == 1):
        return str(calcul[0])
    # If only one operator
    elif (len(calcul)==3):
        # Print result of operation for explaination
        print ("   -> " + str(calculator(calcul)))

        # Return the operation
        return str(calculator(calcul))

    # If there is more than one operator
    else:
        # Check if there is a multiplicator
        for i in range (len(calcul)):
            # If ther is a multiplicator
            if (calcul[i] == "*"):
                # Add () arround it (Deepness += 1)
                calcul = addParenthese(calcul, i)

                # Recalc the new calcul with a deepness of 1
                return calc_deep(calcul, 1)

        # If there is only + and -, add () at the first operation (Deepness += 1)
        calcul = addParenthese(calcul, 1)

        # Recalc the new calcul with a deepness of 1
        return calc_deep(calcul, 1)

''' Add parenthese arround an operator '''
def addParenthese(calcul, i):
    # Add parenthese at i-1 and i+1
    calcul[i-1] = "(" + calcul[i-1]
    calcul[i+1] = calcul[i+1] + ")"

    # Transform in a string
    calcul = arrayToString(calcul)

    return calcul

''' Transform a calcul array into a string calcul'''
def arrayToString(array):
    # If the array is empty
    if (len(array) == 0):
        # return empty string
        return ""

    # If the array is not empty : add space between char
    text = ""
    for i in range (len(array) - 1):
        text = text + str(array[i]) + " "
    text = text + str(array[len(array) - 1])

    # return the string
    return text

''' Make a simple operation between two number '''
def calculator(c):
    # If the operation is an addition
    if (c[1] == "+"):
        return float(c[0])+float(c[2])
    # If the operation is a soustraction
    if (c[1] == "-"):
        return float(c[0])-float(c[2])
    # If the operation is a multiplication
    if (c[1] == "*"):
        return float(c[0])*float(c[2])

''' Resolve a string calcul expression '''
def calc(calcul):
    # Get deepness
    deepness = getDeepness(calcul)

    # Resolve deepest simple calcul if deepness != 1
    if (deepness > 0):
        calcul = calc_deep(calcul, deepness)
        return calc(calcul)
    # Else resolve simple calcul 
    else:
        r = simple_calc(calcul)
        return r

# ALGO
if (len(sys.argv) == 1):
    print('\033[91m'+"[Error]: No expression given"+'\033[0m')
else :
    print('\033[92m' + "[Result]: "+ calc(sys.argv[1])+ '\033[0m')