# for loop ila bghina nb9aw f kola element mn list, tuple, dictionary, set, string

people = ['zakaria', 'saad', 'Simo', 'ahmed']

# for loop syntax
for person in people:
  print(f'Current Person: {person}')

# Break kandiroha bach n5orjo mn loop
for person in people:
  if person == 'Sara':
    break
  print(f'Current Person: {person}')

# Continue bach idoz ldawra taliya
for person in people:
  if person == 'Sara':
    continue
  print(f'Current Person: {person}')

# range kandiro fih ch7al mn mera bghina dor loop
for i in range(len(people)):
  print(people[i])

for i in range(0, 11):
  print(f'Number: {i}')

# While loops kat5dm ila kant condition true bili katwli false katw9af

count = 0
while count < 10:
  print(f'Count: {count}')
  count += 1