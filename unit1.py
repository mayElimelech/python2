class unit1:
    def make_double(self,my_letter):
        return my_letter*2
    def double_letter(self,my_str):
        return ''.join(map(self.make_double,my_str))
    def check_div(self,number):
        return number%4==0
    def four_dividers(self,number):
        return list(filter(self.check_div,range(1,number+1)))

    def sum_of_digits(self,number):
        return sum(map(int, str(number)))

    def intersection(self,list_1, list_2):
        return list(set(list_1) & set(list_2))

    def is_prime(self,number):
        return all(number % i != 0 for i in range(2, number-1))

    def is_funny(self,string):
        return all(ch == 'h' or ch == 'a' for ch in string)

    def check_pass(self,password):
        return ''.join(chr(ord(ch) + 2) if ch.isalpha() else ch for ch in password)

    def tar151(self,namefile):
        f1=open(namefile,"r")
        return max(name.strip() for name in f1)

    def tar152(self,namefile):
        f1=open(namefile,"r")
        return sum(len(name.strip()) for name in f1)

    def tar153(self,namefile):
        f1 = open(namefile, "r")
        minLength = min(len(name.strip()) for name in f1)
        f1 = open(namefile, "r")
        return '\n'.join([name.strip() for name in f1 if len(name.strip()) == minLength])
    def tar154(self,namefile):
        f1=open(namefile)
        f2=open("name_length.txt", "w")
        for name in f1:
            f2.write(str(len(name.strip())) + "\n")

    def tar155(self):
        name_length = int(input("Enter name length: "))
        f1= open("task1.txt")
        names = [name.strip() for name in f1 if len(name.strip()) == name_length]
        print('\n'.join(names))


if __name__ == '__main__':
    unit =unit1()
    print(unit.double_letter("python"))
    print(unit.four_dividers(9))
    print(unit.sum_of_digits(104))
    print(unit.intersection([1, 2, 3, 4], [8, 3, 9]))
    print(unit.is_prime(42))
    print(unit.is_funny("hahahaaahaha"))
    print(unit.check_pass( "sljmai ugrf rfc ambc: lglc dmsp mlc rum"))
    print(unit.tar151("task1.txt"))
    print(unit.tar152("task1.txt"))
    print(unit.tar153("task1.txt"))
    unit.tar154("task1.txt")
    unit.tar155()