import math

while True:
    n = int(input("Enter the number: "))
    assert n >= 0
    if n == 0:
        print("Number of digits: 1")	
        continue
    no_digits = math.floor(math.log10(n)) + 1
    print(f"Number of digits: {no_digits}") 
