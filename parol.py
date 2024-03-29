import random

def genirated_password(pass_len = 10):
    password_simvol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    generated_password = ""

    for i in range(pass_len):
        generated_password += random.choice(password_simvol)
    return generated_password


