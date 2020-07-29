#FizzBuzz 

for fizzbuzz in range(100):
    #if number is divisible by 3 or 5, with remainder 0
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    #if number is divisible by 3 with remainder of 0
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    #if number is divisible by 5 with remainder of 0
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    #otherwise, print fizzbuzz
    print(fizzbuzz)
	