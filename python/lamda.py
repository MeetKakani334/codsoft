name = lambda x,y:x+y

result = name(5,4)
print(result)

number = [1,2,3,4,5]
doubeled = list(map(lambda X:X%2==0,number))
print(doubeled)