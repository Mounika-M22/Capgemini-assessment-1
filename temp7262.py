# Temperature Conversion Tool
# - Write a program that converts temperatures between Celsius, Fahrenheit, and Kelvin
# based on user input.
# - Use functions for each conversion.


while(True):
    temp=int(input("enter options::\n1.cel to fah\n2.fah to cel\n3.fan to kel\n4.kel to fah\n5.kel to cel\n6.cel to kel\n"))
    match temp:
        case 1:
            cel=int(input("enter the temperature in celcius::\n"))
            def cf(cel):
                fah=((9/5)*cel)+32
                print(f'the converted value is {fah} degree fahrenheit\n')
            cf(cel)
            exit
        case 2:
            fah=int(input("enter the temperature in fahrenheit::\n"))
            def fc(fah):
                cel=(fah-32)*(5/9)
                print(f'the converted value is {cel} degree celcius\n')
            fc(fah)
            exit
        case 3:
            fah=int(input("enter the temperature in fahrenheit::\n"))
            def fk(fah):
                kel=(fah-32)*(5//9)+273.15
                print(f'the converted value is {kel} degree kelvin\n')
            fk(fah)
            exit
        case 4:
            kel=int(input("enter the temperature in kelvin ::\n"))
            def kf(kel):
                fah=(kel-273.15)*1.8+32
                print(f'the converted value is {fah} degree fahrenheit\n')
            kf(kel)
            exit
        case 5:
            kel=int(input("enter the temperature in kelvin ::\n"))
            def kc(kel):
                cel=kel-273.15
                print(f'the converted value is {cel} degree celcius\n')
            kc(kel)
            exit
        case 6:
            cel=int(input("enter the temperature in celcius ::\n"))
            def ck(cel): 
                kel=cel+273.15
                print(f'the converted value is {kel} degree kelvin\n')
            ck(cel)
            exit
        case _:
            print("wrong option")
            break

            

    
    
