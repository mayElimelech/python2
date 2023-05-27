import string
class UnderAge(Exception):
    def __str__(self):
        return "under age"
class UsernameContainsIllegalCharacter(Exception):

    def __init__(self, char, index):
        self.char = char
        self.index = index
    def __str__(self):
        return f"The username contains an illegal character '{self.char}' at index {self.index}."

class UsernameTooShort(Exception):
        def __str__(self):
            return "The username is too short."

class UsernameTooLong(Exception):
        def __str__(self):
            return "The username is too long."

class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character."


class PasswordMissingCharacterUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class PasswordMissingCharacterLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class PasswordMissingCharacterDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class PasswordMissingCharacterSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


class PasswordTooShort(Exception):
        def __str__(self):
            return "The password is too short."

class PasswordTooLong(Exception):
        def __str__(self):
            return "The password is too long."
class unit3:
    def read_file(self,file_name):
        try:
            f1= open(file_name, 'r')
            text = f1.read()
            return f"__CONTENT_START__\n{text}\n__CONTENT_END__\n"
        except FileNotFoundError:
            return "__CONTENT_START__\n__NO_SUCH_FILE__\n__CONTENT_END__\n"



    def send_invitation(self,name, age):
        try:
            if int(age) < 18:
                raise UnderAge
            else:
                print("You should send an invite to " + name)
        except UnderAge as e:
            print(e)


    def illigal_userName(self,username):
        for char in username:
            if char.isalpha() == False and char.isalnum() == False and char != "_":
                return char#illigal
        return -1
    def illigal_password(self,password):
        countUpper=0
        countLower=0
        countpunctuation=0
        countdigit=0
        for char in password:
            if(char.isupper()):
                countUpper+=1
            if(char.islower()):
                countLower +=1
            if(char in string.punctuation):
                countpunctuation +=1
            if(char.isdigit()):
                countdigit+=1
        if(countUpper==0):
            return "upper"
        if (countLower == 0):
            return "lower"
        if (countdigit == 0):
            return "digit"
        if (countpunctuation == 0):
            return "punctuation"

        return "ok"


    def check_input(self,username, password):
        # Checking username
        try:
            if len(username) < 3:
                raise UsernameTooShort
            elif len(username) > 16:
                raise UsernameTooLong
            elif self.illigal_userName(username)!= -1 :
                    raise UsernameContainsIllegalCharacter(self.illigal_userName(username),username.find(self.illigal_userName(username)))

            # Checking password
            if len(password) < 8:
                raise PasswordTooShort
            elif len(password) > 40:
                raise PasswordTooLong
            elif self.illigal_password(password)!="ok":
                if(self.illigal_password(password)=="upper"):
                    raise  PasswordMissingCharacterUppercase
                if (self.illigal_password(password) == "lower"):
                    raise PasswordMissingCharacterLowercase
                if (self.illigal_password(password) == "digit"):
                    raise PasswordMissingCharacterDigit
                if (self.illigal_password(password) == "punctuation"):
                    raise PasswordMissingCharacterSpecial

            print("OK")
        except (UsernameTooShort, UsernameTooLong, UsernameContainsIllegalCharacter, PasswordTooShort,
                PasswordTooLong,PasswordMissingCharacter,PasswordMissingCharacterUppercase,PasswordMissingCharacterLowercase,PasswordMissingCharacterSpecial,PasswordMissingCharacterDigit) as e:
            print(e)




if __name__ == '__main__':
    unit =unit3()
    print(unit.read_file("task1.txt"))
    print(unit.send_invitation("may",17))
    # Testing the inputs
    unit.check_input("1", "2")
    unit.check_input("0123456789ABCDEFG", "2")
    unit.check_input("A_a1.", "12345678")
    unit.check_input("A_1", "2")
    unit.check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    unit.check_input("A_1", "abcdefghijklmnop")
    unit.check_input("A_1", "ABCDEFGHIJLKMNOP")
    unit.check_input("A_1", "ABCDEFGhijklmnop")
    unit.check_input("A_1", "4BCD3F6h1jk1mn0p")
    unit.check_input("A_1", "4BCD3F6.1jk1mn0p")