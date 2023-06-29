word_to_guess = "cumbias"
user_option = ""
display_word = "_ "*len(word_to_guess)
user_chars = []
hang_person =['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']


print("<<<<<<<<<<<<>>>>>>>>>>>>\n")
print("Bienvenidos al ahorcadito\n")
print(f"{display_word}\n")
print(hang_person[-1])

while user_option != "3":
    print("Adivina la palabra si quieres vivir\n")
    print("1. Adivinar")
    print("2. Resultados")
    print("3. Salir")

    user_option =input("Indica una opción\n")

    if user_option == "1":
        exit_game = False
        while not exit_game:
            print("Intenta adivinar una letra o la palabra completa\n")
            print("Escribe salir para volver al menú principal")
            user_guess = input()
            guess_word = ""

        #Si el usuario ingreso una letra 
            if len(user_guess) == 1:
            #si no es una letra nueva, se agrega al listado de letras intentatas
                if not user_guess in user_chars:
                    user_chars.append(user_guess)

                if  (user_guess in word_to_guess):
                    print("Adivinaste la letra")
                    for char in word_to_guess:
                        if char in user_chars:
                            guess_word += char
                        else:
                            guess_word += "_ "
                    print(guess_word)
                else:
                    print("Esa letra no está en la palabra")
                    print(hang_person[len(user_chars)])

             # Si el usuario intento una palabra
            elif user_guess == "salir":
                exit = True           
            
                 #Si la palabra del usuario es la misma
            if (user_guess == word_to_guess):
                print ("¡Ganaste!")
                exit ()
            else:
                print ("No no no")
                print ("Perdiste y te quemaras en el infierno por los siglos de los siglos")
                print(hang_person(-1))
                exit ()

    elif user_option == 2:
         print (f"Has intentado las siguientes letras:{user_chars}")
    elif user_option == "3" :
        print ("chausito")