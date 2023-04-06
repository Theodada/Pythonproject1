# This program uses a nested for loop to check each number between 2 and 10 to see if
# it's prime. If a number is divisible by any other number between 2 and itself then ' \
# it's not prime. If it's not divisible by any number between 2 and itself, then it's ' \
# prime and the program prints it out
for num in range(2, 10):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)