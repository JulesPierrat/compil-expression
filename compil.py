# IMPORT
from cmath import nan
import sys
import re

from numpy import array

# FUNCTION

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

def organizeParenthese(equat):
    new = ""
    compt = 0
    for i in range (len(equat)):
        if (is_open_paranthese(equat[i])):
            compt += 1
            new = new + (compt)*"|"+"$"
        elif (is_close_paranthese(equat[i])):
            new = new + (compt)*"|"+"$"
            compt -= 1
        else:
            new = new + equat[i]

    return new;

def getProf(equat):
    compt = 0
    compt_m = 0
    for i in range (len(equat)):
        if is_open_paranthese(equat[i]):
            compt += 1
        if is_close_paranthese(equat[i]):
             compt -= 1
        if (compt > compt_m):
            compt_m = compt

    return compt_m

def calc(arr):
    if(len(arr) == 1):
        return arr
    elif (len(arr) == 3):
        return calculator(arr)
    else:
        for i in range (len(arr)):
            if (arr[i] == '*'):
                m = calculator(arr[i-1:i+2]);
                new = arr[0:i-1]
                new += [m]
                new += arr[i+2:]
                return calc(new)

        return calc([calculator(arr[0:3])]+arr[3:])

        

def calculator(arr):
    if (arr[1] == "+"):
        return str(float(arr[0]) + float(arr[2]))
    if (arr[1] == "-"):
        return str(float(arr[0]) - float(arr[2]))
    if (arr[1] == "*"):
        return str(float(arr[0]) * float(arr[2]))

def arrayToString(array):
    text = ""
    for i in range(len(array)):
        text = text + str(array[i])
    return text

def resolve(equat, prof):
    if(prof == 0):
        r = arrayToString(calc(equat.split(" ")))
        print(r)
        return float(r)
    else:
        array = equat.split(prof*'|'+"$")
        for i in range (len(array)):
            if ((array[i].find((prof-i-1)*'|'+"$") == -1 ) and (array[i] != '')):
                array[i] = calc(array[i].split(" "))
                equat = arrayToString(array)
        resolve(equat, prof-1)



def compilExpression (equat):
    # get profondeur
    p = getProf(equat)

    # organize parentheses
    e = organizeParenthese(equat)

    # Resolve
    result = resolve(e, p)
    print(result)

    return result

# ALGO
if (len(sys.argv) == 1):
    print('\033[91m'+"[Error]: No expression given"+'\033[0m')
else :
    print('\033[92m' + "[Result]: "+ compilExpression(sys.argv[1])+ '\033[0m')