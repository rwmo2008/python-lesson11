counter = 1
try:
    while (counter >= 1):
        number = 2.0 ** counter
        #print(number)
        #print()
        counter = counter + 0.001
except OverflowError:
    print()
    print("Stopped by overflow error. Value of number:", number)
except KeyboardInterrupt:
    print()
    print("Stopped by keyboard interrupt. Value of number:", number)
