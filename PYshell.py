#!/usr/bin/python3
import hashlib
import os

def encryptuser(user):
    encuser = hashlib.sha256(user.encode()).hexdigest()
    return encuser
def encryptpass(passw):
    encpass = hashlib.sha256(passw.encode()).hexdigest()
    return encpass

def startshell(userid):
    while True:
        shell = input("{0}@kali:~$ ".format(userid))
        if shell == "help":
            print("""
                    Welcome Kali Python Interctive Sh3ll~
                        help --> Shows this help menu
                        whoami --> shows user username
                        cmd --> start instance of windows Prompt
                        powershell --> start powershell
                        exit --> terminates the program
                        kali --> start KaliLinux Terminal instance.
                        -----Made with Lov3 by anii0101-----""")
                    
        elif shell == "exit":
            exit()
        elif shell == 'whoami':
            print(userid)
        else:
            os.system(shell)
    

def register():
    new_user = input("Enter username:")
    new_pass = input("Enter Password:")
    retype= input("enter retype password:")
    if retype != new_pass:
            print("Password not match [ ! ]")
            register()
    else:
        encoduser = encryptuser(new_user)
        encodpass = encryptpass(new_pass)
        with open("logindetails.txt","a") as loginwrite:
            loginwrite.write("{0}:{1}\n".format(encoduser,encodpass))
            print("\nRegistration Complete.please wait..")
            login()
        
def login():
    print("---------L0G1N-----------")
    username = input("Username:")
    password = input("Password:")
    USER_ENC = encryptuser(username)
    PASS_ENC = encryptpass(password)
    with open("logindetails.txt","r") as loginread:
        read = loginread.read()
        read = read.split("\n")
    if ('{0}:{1}'.format(USER_ENC,PASS_ENC)) in read:
        startshell(username)
    else:
        print("wrong creds ~ Try again.")
    
print(""" ~ Shell ~
            1.Login
            2.SignUp/register""")
choice = input("enter Choice:")

if choice == "1":
    login()
elif choice == "2":
    register()
else:
    print("Drunk? try again!")



