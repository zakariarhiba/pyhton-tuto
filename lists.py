#list hiya varrible li kijma3 des values
# les values i9dro ikono ayi 7aja b7al int float str bool

ar9am = [1,2,3,4,5]
names = ['zakaria','ahmed','saad','oussama']

#ila bghina ghi value mn list
print(names[1])

#ila bghina ch7al fiha mn value
print(len(ar9am))

#ila bghina nzido f list
names.append('ali')

#nm7iw mn list 
names.remove('saad')
print(names)

#ila bghina nzido wlkn f position li bghina
names.insert(2,'saad')
print(names)

#nm7iw  b pop
names.pop(2)

#nglbo list
names.reverse()

#n5rb9 list
names.sort()

#nglbo o n5rb9ha
names.sort(reverse=True)

#nbdlo value
names[1] = 'Rhiba'
print(names)
