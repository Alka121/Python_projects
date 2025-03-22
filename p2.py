import random
import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
# print(random.choice("hellow"))
pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

# List Comprehension [function for i in range(n)]
password = "".join([random.choice(charValues) for i in range (pass_len)])

# password = ""
# for i in range(pass_len):

#    password += random.choice(charValues)

print("Your rendom password is :" ,password)


