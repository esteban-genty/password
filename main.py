import hashlib

password = input("Saisissez votre password : ")

# Vérifie si le password à 8 carractères
if (len(password) <= 8):
    print("Il doit contenir au moins huit caractères.")

# Vérifie si le password à une majuscule
elif not any(char.isupper() for char in password):
    print("Il doit contenir au moins une lettre majuscule.")
    
# Vérifie si le password à une minuscule
elif not any(char.islower() for char in password):
    print("Il doit contenir au moins une lettre minuscule.")
    
# Vérifie si le password à un chiffre
elif not any(char.isdigit() for char in password):
    print("Il doit contenir au moins un chiffre.")

# Vérifie si le password à un caractères spécial : (!, @, #, $, %, ^, &, *).
elif not any(char in ['!', '@', '#', '$', '%', '^', '&', '*'] for char in password):
    print("Il doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
    
else:
    print("Valid Password.")
    # Encrypt le pasword
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    print (password_hash)