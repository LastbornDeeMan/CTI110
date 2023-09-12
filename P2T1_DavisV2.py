import matplotlib.pyplot as plt

"""
# Collect the data
print("Enter Pokeman Data")
print("Day 1:", end="")
day1 = int(input())
print("Day 2:", end="")
day2 = int(input())
print("Day 3:", end="")
day3 = int(input())
"""
# New version
data = [] # empty list
num_days = int(input("How many days? "))
for day in range(num_days):
  print("Day ", day, ":", end="")
  today = int(input())
  data.append(today) # add it to the end of the list

# put the dat in a list
# print min and max
print("Best Day:", max(data))
print("Worst Day:", min(data))
# don't do total and average yet
# TODO: Graph the real data
fig, ax = plt.subplots()
ax.plot(range(num_days), data)
plt.title("Pokeman Data")
plt.xlabel('day #')
plt.ylabel('pokemans collected')
plt.show()
