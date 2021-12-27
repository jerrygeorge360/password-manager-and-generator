import random
import  string
lenght=int(input('Length of password\n'))
sitename=input('site name\n')


class PasswordGenerator:
    def __init__(self):
        self.number=string.digits
        self.alphabets=string.ascii_lowercase
        self.capital=string.ascii_uppercase
        self.symbols=string.punctuation
        self.combine=self.number + self.alphabets+self.capital +self.symbols
        self.sitename=sitename.upper()

        self.real=random.sample(self.combine,lenght)
        self.password=''.join(self.real)


        self.filesent()

    def filesent(self):
        with open('password.txt','a',encoding='utf-8') as f:
            f.write(f'{self.sitename}:\n{self.password}\n\n')


passwordgenerator=PasswordGenerator()