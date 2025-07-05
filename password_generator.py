import random
import string

def generate_password(length, numbers, uppercase, lowercase, special):
    #generates a password with customized options
 
    #defining the character sets
    uppercase_ch = string.ascii_uppercase if uppercase else ''
    lowercase_ch = string.ascii_lowercase if lowercase else ''
    numbers_ch = string.digits if numbers else ''
    special_ch = string.punctuation if special else ''

    #combining the character set
    chars = uppercase_ch + lowercase_ch + numbers_ch + special_ch

    #the length of the password
    length = max(length,8)

    #genrating the password
    password = ''.join(random.choice(chars) for i in range(length))

    return password

password = generate_password(length=8,uppercase=True, lowercase=True, numbers=True, special=True)
print("Generating the Password...")
print(password)