# Password generator - TASK 3
import random
import string

length = int(input("Enter length of password to be generated: "))

password = ""
for i in range(length):
    password += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
print(password) 
