while True :
    print("Choose one of item : \n1)Encrypt\n2)Decrypt\n3)Exit")
    item = input("Enter one item : ")

    if item == "1" or item == "1)Encrypt" or item == "Encrypt".lower() :
        simple_text = input("Enter your text : ")
        encrypted_text = ""
        for char in simple_text :
            code = ((ord(char) * 5) + 16) * 7
            encrypted_text += chr(code)
        print ("Encryted Text : " , encrypted_text)


    elif item == "2" or item == "2)Decrypt" or item == "Decrypt".lower() :
       encrypted_text = input("Enter your encrypted text : ") 
       simple_text = ""
       for char in encrypted_text :
           decode = ((ord(char) // 7 )- 16) // 5 
           simple_text += chr(decode)
       print("Decrypted Text : " , simple_text)   
        
        
    elif item == "3" or item == "3)Exit" or item == "Exit" :
        print("GoodBye")
        break

    else :
        print("Wrong Item Is Chosen!")
        break