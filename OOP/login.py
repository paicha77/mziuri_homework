class Login:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def see_credentials(self):
        return (self.__username, self.__password)


l = Login("nika123", "mypassword")
print(l.see_credentials())

# N2

class Account:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def login(self, username, password):
        if username == self.__username and password == self.__password:
            print("Login successful")
        else:
            print("Wrong credentials")

    def change_password(self, new_password):
        self.__password = new_password

    def show_username(self):
        return self.__username


acc = Account("nika123", "1234")
acc.login("nika123", "1234")
acc.change_password("abcd")
print(acc.show_username())