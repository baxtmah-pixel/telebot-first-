import random 
def passgen(less_password):
    password = ""
    symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    for i in range(less_password):
        password += random.choice(symbols)
    return password

