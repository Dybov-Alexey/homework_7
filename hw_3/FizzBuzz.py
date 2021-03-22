fizzbuzz = lambda n: print(f'FizzBuzz') if n % 3 == 0 and n % 5 == 0 else print(end='') \
    or print(f'Fizz') if n % 3 == 0 else print(end='') or print(f'Buzz') if n % 5 == 0 \
    else print(end='') or print(f'{n}')
for n in range(0, 101):
    fizzbuzz(n)