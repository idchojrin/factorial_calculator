# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


Value = int(input("Enter a number: "))
if Value < 1:
    print("You have to enter a number greater than 0.")
else:
    Counter = Value - 1
    Result = Value
    while Counter > 0:
        Result = Result * Counter
        Counter = Counter - 1
    print("The result is " + str(Result))