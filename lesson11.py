try:
    age = eval(input('Please enter your age: '))
    ten_years = age + 10
    print("In 10 years, you'll be", ten_years)
#except NameError:
#    print("You must enter a number for your age.")
#except SyntaxError:
#    print("You must enter a number for your age.")
except (NameError, SyntaxError):
    print("You must enter a number for your age.")
except Exception:
    print("Something unexpected has happened.")
    
print("Have a nice day. Goodbye.")
