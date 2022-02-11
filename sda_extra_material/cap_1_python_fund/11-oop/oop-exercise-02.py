class User:
    def __init__(self, name):
        self.name = name
        self.__password = ""

    @property
    def password(self):
        if len(self.__password) == 0:
            return ""
        secret = self.__password[0]
        for i in range(len(self.__password) - 2):
            secret += "*"
        secret += self.__password[-1]
        return secret

    # For those looking to learn new things - this can be also achieved using List Comprehensions
    # @property
    # def password(self):
    #     if len(self.__password) == 0:
    #         return ""
    #     secret = [ch for ch in self.__password]
    #     secret[1:-1] = ["*" for _ in range(len(secret) - 2)] # Primul si ultimul caracter din secret nu sunt suprascrise datorita folosirii unui index pozitiv si unul negativ
    #     return "".join(secret)

    @password.setter
    def password(self, new_pass):
        if len(new_pass) < 6:
            for i in range(6 - len(new_pass)):
                new_pass += "#"
        self.__password = new_pass

    # For those looking to learn new things - this can be also achieved using List Comprehensions
    # @password.setter
    # def password(self, new_pass):
    #     self.__password = f"{new_pass:*<6}"

    @password.deleter
    def password(self):
        if len(self.__password) >10000:
            del self.__password


u = User("John")
u.password = "s"
print(u.password)
u.password = "L0nger passwords ArE M0r3 Secure 0r s0 th3y s@y!"
print(u.password)
del(u.password)
print(u.password)
