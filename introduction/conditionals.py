print("*"*20+"Sign in"+"*"*20)

username=input("username=")
password=input("password=")

print("Successfully signed in!")
print("Log in!")

username1=input("username=")
password1=input("password=")

if(username==username1 and password==password1):
    print("Successfully logged in!")
elif(username!=username1 and password==password1):
    print("Wrong username!")
elif(username==username1 and password!=password1):
    print("Wrong password")
else:
    print("Fucking fish memory detected!")
