# author CJP 09/26/21
text = input("please enter radius ")
radius = int(text)

text = input("please enter a height ")
height = int(text)

volume = 3.14 * (radius ** 2) * height
print(volume)

sa = (2 * 3.14 * (radius ** 2)) + (2 * 3.14 * radius * height)
print(sa)