sandwich_orders = ['tuna sandwich', 'ham sandwich', 'cheese sandwich', 'veggie sandwich', 'with cheese']
finished_sandwiches = []

for sandwich in sandwich_orders:
  print(f"I made your {sandwich}")
  finished_sandwiches.append(sandwich)

print("\nThe following sandwiches were made:")
for sandwich in finished_sandwiches:
  print(sandwich
#17.2
sandwich_orders = ['tuna sandwich', 'ham sandwich', 'cheese sandwich', 'veggie sandwich', 'with cheese', 'with cheese', 'with cheese']
finished_sandwiches = []

print("We are all out of cheese! Sorry, no more 'with cheese' sandwiches.")

while 'with cheese' in sandwich_orders:
  sandwich_orders.remove('with cheese')

for sandwich in sandwich_orders:
  print(f"I made your {sandwich}")
  finished_sandwiches.append(sandwich)

print("\nThe following sandwiches were made:")
for sandwich in finished_sandwiches:
  print(sandwich)
  #17.3
  dream_vacations = []

while True:
  vacation = input("Where would you like to go for vacation? (Enter 'quit' to finish): ")
  if vacation.lower() == 'quit':
    break
  dream_vacations.append(vacation)

print("\nDream vacations:")
for vacation in dream_vacations:
  print(vacation)