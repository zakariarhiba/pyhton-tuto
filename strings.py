
name = 'zakaria'
age = 18

#bach nbdlo mn int l string kandiro str(smiya d varible)
#example : age = str(age)

'''print('My name is ' + name )
   print('I am ' + age)            ''' 
#drna hado ''' 3la 9bl nbdaw comment fih bzzf deal les lines o kansaliw bihom

#bach ndiro print b le variables kanktbohom haka
#print('My name is {name} and I am {age}'.format(name=name,age=age))

#o n9dro ndiro 7ta had method wlkn ghi f les versions jdida 3++
#print(f'My name is {name} and I am {age}')

#hado chwiya deal tricks li t9dr dirhom b strings jrbhom

#1
s = 'hello world'
print(s.capitalize())


#2 tkbr l7orof uppercase
print(s.upper())

#3 tsghr l7orof
print(s.lower())

#4 Swap case
print(s.swapcase())

#5  ch7al fiha mn 7arf
print(len(s))

#6 katbdl lwla b taniya
print(s.replace('world', 'everyone'))

#7 t7sb
sub = 'h'
print(s.count(sub))

#8 wach kaybda b hello
print(s.startswith('hello'))

#9 wach kaysali b 'd'
print(s.endswith('d'))

#10 trodhom liste
print(s.split())

#11 t9lb 3la position dealo
print(s.find('r'))

#12 wach fih 7orof o ar9am
print(s.isalnum())

#13 wach kamlin 7orof
print(s.isalpha())

#14 wach kamlin ar9am
print(s.isnumeric())


