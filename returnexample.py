s_username="EMC"
s_password="123"

uname=input("Username:")
pwd=input("Password:")
def validate():
    if(s_username==uname and s_password==pwd):
        return True
    else:
        return False
print(validate())
     
