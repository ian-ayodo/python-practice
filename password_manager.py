import hashlib
password = input("Enter a password : ")
hashed_password = hashlib.sha512(password.encode()).hexdigest()
with open(r"files/password.txt","wb") as p:
    p.write(hashed_password.encode())

with open(r"files/password.txt","rb") as p:
    print(p.read().decode())
