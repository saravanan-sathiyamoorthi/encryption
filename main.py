# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.

import encryption as encryption


class Login:
    def __init__(self, userId, pin):
        self.id = userId
        self.pin = pin
        if self.id == 'saro' and self.pin == '141314':
            print(f'' + self.id + " Entered Successfully!")
            try:
                encryption.encrypt(self.id)
            except:
                print("Unable to access the encryption")

        else:
            print("Unauthorized access! Unable to proceed")


if __name__ == '__main__':
    UserId = input("Enter Your Username : ")
    Pin = input("Enter Your Pin : ")
    Login(UserId, Pin)
