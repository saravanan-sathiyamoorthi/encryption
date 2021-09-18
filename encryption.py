class Encryption:
    def __init__(self, message, key, user):
        self.message = message.lower()
        self.key = key
        self.user = user
        encrypting = dict(zip(self.key, self.key[::-1]))
        encrypted_message = "".join(encrypting[letters] for letters in message)
        # noinspection PyRedundantParentheses
        print(f"Encrypted Message - ", (encrypted_message))
        decrypted_message = "".join(encrypting[letters] for letters in encrypted_message)
        # noinspection PyRedundantParentheses
        print(f"Decrypted Message - ", (decrypted_message))
        print(f''+self.user+" exited Successfully")


def encrypt(userid):
    user = userid
    Encryption_message = input("Enter Your message : ")
    E_key = open("key.key", "rb")
    Encryption_key = E_key.read().decode('utf-8')
    E_key.close()
    Encryption(Encryption_message, Encryption_key, user)
