# author CJP 09/26/21
text = input("please enter number of free throws scored ")
freeThrowsScored = int(text)

text = input("please enter number of short baskets scored ")
shortBasketsScored = int(text)

text = input("please enter number of long baskets scored ")
longBasketsScored = int(text)

totalpoints = (1 * freeThrowsScored) + (2 * shortBasketsScored) + (3 * longBasketsScored)
print(totalpoints)