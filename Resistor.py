#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      achu
#
# Created:     23-12-2015
# Copyright:   (c) achu 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def fourband():
    try:
        a= input("Enter colour of the first band on resistor : ")
        val1=band(a)
        val1=val1*10

        b= input("Enter colour of the second band on resistor : ")
        val2=band(b)

        mul= input("Enter colour of the third band on resistor : ")
        val3=multiplier(mul)

        tolerance= input("Enter colour of the fourth band on resistor : ")
        val4=tol(tolerance)
        finalresult= result(val1,val2,val3)
        print(str(finalresult) +" ohms, " +str(val4))
        return
    except:
        print("Invalid Input")

def fiveband():
    try:
        a= input("Enter colour of the first band on resistor : ")
        val1=band(a)
        val1=val1*100

        b= input("Enter colour of the second band on resistor : ")
        val2=band(b)
        val2=val2*10

        c=input("Enter colour of the third band on resistor: ")
        valc=band(c)

        mul= input("Enter colour of the fourth band on resistor : ")
        val3=multiplier(mul)

        tolerance= input("Enter colour of the fifth band on resistor : ")
        val4=tol(tolerance)
        finalresult= result(val1,val2,val3,valc)
        print(str(finalresult) +" ohms, " +str(val4))
        return
    except:
        print('Invalid Input')

def result(val1,val2,val3,valc=0):
    res = float ((val1 + val2 + valc) * val3)
    return res


def tol(strtol):
        if (strtol.lower() == 'brown'):
     	   	band='+/-1%'
        elif (strtol.lower() == 'red'):
            band='+/-2%'
        elif (strtol.lower() == 'gold'):
        	band='+/-5%'
        elif (strtol.lower() == 'silver'):
    	   	band='+/-10%'
        return band

def multiplier(strmul):
    if (strmul.lower() == 'black'):
 	   	band=1
    elif (strmul.lower() == 'brown'):
        band=10
    elif (strmul.lower() == 'red'):
	   	band=100
    elif (strmul.lower() == 'orange'):
	   	band=1000
    elif (strmul.lower() == 'yellow'):
	   	band=10000
    elif (strmul.lower() == 'green'):
	   	band=100000
    elif (strmul.lower() == 'blue'):
	   	band=1000000
    elif (strmul.lower() == 'gold'):
    	band=0.1
    elif (strmul.lower() == 'silver'):
	   	band=0.01
    return band


def band(strband):
        if (strband.lower() == 'black'):
     	   	band=0
        elif (strband.lower() == 'brown'):
            band=1
        elif (strband.lower() == 'red'):
    	   	band=2
        elif (strband.lower() == 'orange'):
    	   	band=3
        elif (strband.lower() == 'yellow'):
    	   	band=4
        elif (strband.lower() == 'green'):
    	   	band=5
        elif (strband.lower() == 'blue'):
    	   	band=6
        elif (strband.lower() == 'violet'):
        	band=7
        elif (strband.lower() == 'grey'):
    	   	band=8
        elif (strband.lower() == 'white'):
    	   	band=9
        return band

bandval = input("Enter the number of bands on the resistor : ")
if bandval=='4':
    fourband()
elif bandval=='5':
    fiveband()
else:
    print("Invalid Input")





