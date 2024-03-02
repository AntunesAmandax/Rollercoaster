print("Welcome to the rollercoaster!")
while True:
    height = int(input("What is your height in cm?"))
    if height >= 120:
        print("You can ride the rollercoaster!")
    else:
        print("Sorry, you have to grow taller before you can ride.")

    Resposta = input("Want to try again? Type 'yes' or 'no'.")
    if Resposta.lower() == "no":
        print("OK. Have a good day!")
        break
    elif Resposta.lower() != "yes":
        print("Invalid input. Please type 'yes' or 'no'.")
        
       

   




