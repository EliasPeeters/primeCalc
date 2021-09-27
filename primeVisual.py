import matplotlib.pyplot as plt

primes = []
with open('data.txt') as my_file:
    for line in my_file:
        prime = line.split('\n')[0]
        primes.append(int(prime))

blocklength = 1000

biggestBlock = round((primes[len(primes)-1]/blocklength)+0.49)

x = []
y = []

for number in range(biggestBlock+1):
    x.append(number*100)
    y.append(0)


for number in primes:
    block = round((number/blocklength)+0.49)
    y[block] = y[block]+1
    # print(block)


# plotting the points
x.pop(0)
y.pop(0)

y.pop(len(y)-1)
x.pop(len(x)-1)

plt.figure(figsize=(10, 5), dpi=500)
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()
