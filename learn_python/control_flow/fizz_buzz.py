for num in range(1,101):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

def fizzbuzz(fizznum, buzznum, num_max):
    for num in range(1, num_max + 1):
        if num % fizznum == 0 and num % buzznum == 0:
            print("FizzBuzz")
        elif num % fizznum == 0:
            print("Fizz")
        elif num % buzznum == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz(2,10,100)