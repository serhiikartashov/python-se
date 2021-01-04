list = ["a", 1.45, True, 6]
print(list)
# access by index, starts from 0
print(list[2])  # True

print(1.45 in list)  # True

for value in list:
    print(value)

colors = ["purple", "teal", "magenta", "crimson", "emerald"]

index = 0
while index < len(colors):
    print(f"{index}: {colors[index]}")
    index += 1

# list methods
colors.append("red")  # we can't append to exist list new array, only one item
print(colors)
colors.extend(["white", "blue"])
print(colors)
colors.insert(2, "Hi!")
print(colors)
colors.insert(-1, "The End!")
print(colors)
print(list)
list.clear()
print(list)
colors.pop()  # last
some_item = colors.pop(1)  # index 1
print(colors)
print(some_item)
colors.remove("red")
print(colors)
print(colors.index("white"))
print(colors.count("emerald"))  # count repeatable items
colors.reverse()
print(colors)
colors.sort()
print(colors)
print(' '.join(colors))  # join is a part of string, not list
# slicing
print(colors[1:])
print(colors[1:5])
print(colors[1:5:2])

# list comprehension
# [ __ for __ in __ ]
numbers = [1, 2, 3, 4, 5]
var = [x * 10 for x in numbers]
print(var)
friends = ['ashley', 'matt', "michael"]
# friends_ = [friend.title() for friend in friends]
friends_ = [friend.capitalize() for friend in friends]
print(friends_)
# list comprehension with condition
print([num * 2 if num % 2 == 0 else num / 2 for num in numbers])
phrase = "This is New Year! Yahooo!"
print(''.join(char for char in phrase if char not in "aeiou"))  # remove fall vowels

# nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[0][1])
print(nested_list[2][-1])

for l in nested_list:
    for val in l:
        print(val)
