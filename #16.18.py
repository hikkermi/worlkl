# 6.1
toppings = []
while True:
    topping = input("Введите дополнение для пиццы (или 'quit' для завершения): ")
    if topping.lower() == 'quit':
        break
    print(f"Дополнение '{topping}' включено в заказ.")
    toppings.append(topping)

# 16.2
age = int(input("Введите ваш возраст: "))
if age < 3:
    print("Билет бесплатный.")
elif 3 <= age <= 12:
    print("Стоимость билета $10.")
else:
    print("Стоимость билета $15.")

# 16.3
active = True
while active:
    topping = input("Введите дополнение для пиццы (или 'quit' для завершения): ")
    if topping.lower() == 'quit':
        break
    print(f"Дополнение '{topping}' включено в заказ.")

# 18.1
def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Alice in Wonderland")

# 18.2
def make_shirt(size, text):
    print(f"Футболка размера {size} с текстом: {text}")

make_shirt("M", "Hello, World!")
make_shirt(text="Python is awesome", size="L")

# 18.3
def make_shirt(size="L", text="I love Python"):
    print(f"Футболка размера {size} с текстом: {text}")

make_shirt()
make_shirt("S", "Keep Coding")

# 18.4
def describe_city(city, country="USA"):
    print(f"{city} is in {country}")

describe_city("New York")
describe_city("Reykjavik", "Iceland")
describe_city("Tokyo", "Japan")

# 18.5
def car_rental():
    car = input("Какую машину вы бы хотели взять напрокат? ")
    print(f"Вы хотите взять напрокат машину: {car}")

car_rental()
