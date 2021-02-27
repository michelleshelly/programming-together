ingredient1 = "chicken"
ingredient2 = "rice"

Michsays = input ("What is inside this hawker chicken rice?")

if (Michsays == ingredient1 or Michsays == ingredient2):
    print("correct!")
else:
    print("look again!")

# == takes precedence over or

Michasks = input("How much is the hawker chicken rice?")
floatConvertedMichasks = float(Michasks)

# price = 3.5 (dont need to assign values, alr in criteria)
if floatConvertedMichasks == 3.5: 
    print("the price is right!")
if floatConvertedMichasks > 3.5: 
    print("hmm that may be too expensive! sad")
if floatConvertedMichasks < 3.5: 
    print("wow thats peanuts")


