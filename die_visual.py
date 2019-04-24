from die import Die
import matplotlib.pyplot as plt

# Create a D6
die = Die()

# Make some rolls and store it in a list
results = []
for roll in range(10):
    result = die.roll()
    results.append(result)

print(results)

labels = []
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
    labels.append(str(value))

height = die.num_sides
    
plt.bar(labels, frequencies)
plt.xticks(labels)
plt.show()

