fruits = ["banana", "apple", "watermelon" , "pineapple", "strawberries"]

while True:
 user_option = input("ingrese un número entre 0 y 4 para elegir su fruta, q para salir:")
    
 if user_option == "q":
    break
 try:
     print(fruits[int(user_option)])
 except IndexError:
     print("por favor ingresa un número del 0 al 4.")
 except ValueError as valueeror:
    print("porfavor ingresa un número", valueeror) 