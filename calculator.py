import re
import random
print("This is Dynamic Calculator")

while True:
    user_input = input("Enter expression: ")
    if user_input.lower() == "exit":
        break
    user_input = user_input.replace("×", "*").replace("÷", "/")
    user_input = re.sub(r'(\d)(\()', r'\1*(', user_input)   
    user_input = user_input.replace(")(", ")*(")            
    try:
        result = eval(user_input)
        print("Result:", result)
    except Exception as e:
        print("Invalid Expression!")

