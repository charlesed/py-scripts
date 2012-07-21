#!/usr/bin/env python3

# Temperature conversion F<=>C

# F => C Funtion
def FtoC(Tf):
    Tc = ( 5 / 9 ) * ( Tf - 32 )
    return Tc

# C => F Function
def CtoF(Tc):
    Tf = ( 9 / 5 ) * Tc + 32
    return Tf

print("Temperature Converter\n")
retries = 0
temp = float(input("Enter a temperature: "))
print(temp)
while retries < 3:
    convert_to = input("Convert to (F)ahrenheit or (C)elsius? ").lower()
    if convert_to == "f":
    print(round(CtoF(temp), 2))
        break
    elif convert_to == "c":
    print(round(FtoC(temp), 2))
        break
    else:
        print("C or F only...")
        retries = retries + 1

input("Press ENTER to exit")
