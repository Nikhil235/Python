import random

# Random value from 0 to 1
value = random.random()
print(value)

# Random floating value from 1 t 10
value_1 = random.uniform(1, 10)
print(value_1)
# change the arguments if you want different outputs

# Random value - Whole number - can change arguments
value_2 = random.randint(1, 6)
print(value_2)

# Random value from list of values
greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
value_3 = random.choice(greetings)
print(value_3 + ', Nikhil!')

# Random multiple values from list of values
colors = ['red', 'green', 'black']
results = random.choices(colors, weights=[18, 18, 2], k=10)
print(results)


# Random shuffle values form a list
deck = list(range(1, 53))
random.shuffle(deck)
print(deck)

# sample methods -> pick only unique values
hand = random.sample(deck, k=5)
print(hand)

# Example ->
first_names = ['John', 'Jane', 'Corey', 'Travis',
               'Dave', 'Kurt', 'Sam', 'Steve', 'Tom', 'James']

last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson',
              'Davis', 'Stuart', 'Jefferson', 'Jocobs', 'Wright']

Street_names = ['Main', 'High', 'Pearl',
                'Maple', 'Park', 'oak', 'pine', 'cedar']

fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale',
               'bedrock', 'South  Park', 'Atlantis', 'hotride', 'fakeship']

states = ['AL', 'Ak', 'AZ', 'AR', 'CA', 'CO', 'CT',
          'DC', 'DE', 'Fl', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA']

for num in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)

    phone = (f'{random.randint(100, 999)} -555- {random.randint(1000,9999)}')

    Street_num = random.randint(100, 999)
    Street = random.choice(Street_names)
    city = random.choice(fake_cities)
    state = random.choice(states)
    zip_code = random.randint(10000, 99999)
    address = (f'{Street_num} {Street} St., {city} {state} {zip_code}')

    email = first.lower() + last.lower() + '@gmail.com'

    print(f'{first} {last}\n{phone}\n{address}\n{email}')
