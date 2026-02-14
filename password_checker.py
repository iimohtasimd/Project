import re

password = input("Enter the Passwrod: ")

score = 0

# Password Length
if len(password) >= 8:
    score += 1
else:
    print("Use at least 8 character")

# UpperCase(A-Z)
if re.search("[A-Z]",password):
    score += 1
else:
    print("Use at least one Uppper case letter")

# LowerCase(a-z)
if re.search("[a-z]",password):
    score += 1
else:
    print("Use at least one lower character")

# Numbers
if re.search("[0-9]",password):
    score += 1
else:
    print("Use at least one numbers")

# Special Symbols
if re.search("[!,@,#,$,%,^,&,*]",password):
    score += 1
else:
    print("Use at least on Symbol")

print("score:",score,"/5")

if score <= 2:
    print("Password Strengt: Weak")
elif  score <= 4:
    print("Password Strength: medium")
else:
    print("Password Strength: Strong")

