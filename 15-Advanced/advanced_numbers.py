import math

#hex number
#hex() - convert base 10 to hex number
print(type(hex(1000))) #string
print(hex(1000)) #0x3e8
print(hex(2000)) #0x7d0 

#binary number
#bin() - convert base 10 to binary
print(type(bin(1000))) #string
print(bin(1000)) #0b1111101000 
print(bin(2000)) #0b11111010000

#pow function
print(pow(4,2)) #4 ^ 2 = 16
print(pow(4,2,5)) #1 ~ (4 ^ 2) % 5 (more efficient)

#abs function
print(abs(-3)) #3

#round function
print(round(3.1)) #3.0 (float)
print(round(3.9)) #4.0 (float)

#specify the number of rounding digits
print(round(math.pi, 3)) #3.142
