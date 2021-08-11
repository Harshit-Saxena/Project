print(f"Sr.no \tDecimal Hexadecimal \tOctal \tBinary")

for number in range (15,1-1,-1):   # * in range (B,A-1,-1)   B = Start A = end
     print(f"{number} \t{number} \t {hex(number)} \t\t{oct(number)} \t{bin(number)}")
print()



print(f"Sr.no\tDecimal\tHexadecimal\tOctal\tBinary")

for number in range (1,16):  
     print(f"{number}\t{number}\t{hex(number)}\t\t{oct(number)}\t{bin(number)}")