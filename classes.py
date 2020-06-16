# classe hiya b7al object katjma3 fiha wa7d objet wlkn b function  
# o bma3ayer dealo , ma3loma kolchi f python rah objet

#class syntax
class user:
    #hada constructor b7al lwasf dealo
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    # db nsyab function kayna f class
    # bnsnba l self darori kadar wa5a maykonch 7ta parameter
    def is_who(self):
        return f'His name is {self.name} and he is {self.age}'
    

# db ghi 3tina lwasf deal l class wlkn ba9i masybna objet
# kansayboh b7al haka
zakaria = user('Zakaria RHIBA','zakariarhiba@gmail.com',18)

#dik self kan3awdoha b smiya deal class li drti f kola blasa
print(zakaria.is_who())

