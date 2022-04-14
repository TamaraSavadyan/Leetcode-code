import time
startTime = time.time()


def fizzBuzz(n):
    return ["FizzBuzz" if not i % 15 else "Buzz" if not i % 5 else "Fizz"
            if not i % 3 else str(i) for i in range(1, n + 1)]

print(fizzBuzz(16))
print((time.time() - startTime)*1000, 'ms')

startTime_2 = time.time()

def fizzBuzz2(n):
    l = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            l.append("FizzBuzz")
        elif i % 3 == 0:
            l.append("Fizz")
        elif i % 5 == 0:
            l.append("Buzz")
        else:
            l.append(str(i))
    return l


#fizzBuzz2(9999)
print((time.time() - startTime_2)*1000, 'ms')

