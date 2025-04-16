# Sets Intro
my_set = {1, 2, 3, 4, 5}
print("my_set: ", my_set)

my_set = set([1, 2, 3, 4, 5])
print("my_set: ", my_set)

my_set.add(6)
print("my_set: ", my_set)

my_set.update([3, 4, 5, 6])
print("my_set: ", my_set)

my_set.remove(3)
print("my_set: ", my_set)

other_set = {3, 4, 5, 6}
print("other_set: ", other_set)

union_set = my_set.union(other_set)
print("union_set: ", union_set)

intersection_set = my_set.intersection(other_set)
print("intersection_set: ", intersection_set)

difference_set = my_set.difference(other_set)
print("difference_set: ", difference_set)

if "hello" in my_set:
    print("Found hello in my_set")
