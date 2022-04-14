website = input("Please paste in a website url: ") # the program asks for a website url

result = website.startswith('http') # the variable result will become true if the the user input something that starts with http

if result is True: # this if else function will give an output based on if the user input starts with http
    print("Thanks for the website!")
else:
    print("This is not a valid link.")