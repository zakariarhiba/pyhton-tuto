# If hiya b7al ila kant wa7ad exp s7i7a dir lina/ Else  ila makanch dackchi s7i7 dir lina dakchi li f else

x = 21
y = 20

#  (==, !=, >, <, >=, <=) -had symboles 3la 9bl comparaison

#if syntax
if x > y:
  print(f'{x} is greater than {y}')

# If/else syntax
if x > y:
  print(f'{x} is greater than {y}')
else:
  print(f'{y} is greater than {x}')  

# elif hadi kandiroha ila 3dna bzzf d conditions
if x > y:
  print(f'{x} is greater than {y}')
elif x == y:
  print(f'{x} is equal to {y}')  
else:
  print(f'{y} is greater than {x}')  



# (and, or, not) - hado kan5dmo bihom b7al et ou

# and syntax
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

# or syntax
if x > 2 or x <= 10:
    print(f'{x} is greater than 2 or less than or equal to 10')

# not kandiroha bach tnfi lina b7al ila kant l7aja true katrodha false
if not(x == y):
  print(f'{x} is not equal to {y}')