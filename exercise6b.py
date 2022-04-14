def fct(number):
    if number < 1:
        print("The factorial of 0 is 1, and there are no factorials for negetive numbers.")
    else:
        countDown = number
        print("count down",countDown)
        cycle = 0
        while countDown > 1:
            fctNumber = int(number)
            fctMultiplication = fctNumber * (number-1)
            countDown-=1
            print(fctMultiplication)
            number-=cycle
            print("count down",countDown)
            cycle-=1
        return number, countDown, cycle
    
fct(4)