# l = []
# for i in range(3, 8):
#     l.append(i)
# l.pop(0)
# l.pop(3)

# print(l[:-1])
# print(l[:1])

#<------------------->

# l = []
# for i in range(10, 21):
#     l.append(i)
# print(l)

#<------------------->

# l = [1 if i <= 2 else 2 if 3 <= i <= 5 else 3 for i in range(9)]
# print(l)

#<------------------->

# l = [1, 2, 1] + [1, 2, 3] * 2
# print(l)

#<------------------->

# l = [1, 2, 3, 4]
# answer = []

# answer += [sum(l)]
# print(answer)

#<------------------->

# l = [[1, 2, 3], [1, 2, 2, 2, 3], [1, 2, 2, 2, 2, 2, 3]]
# quantity = []

# for i in l:
#     for j in i:
#         amount_of_twos = i.count(2)
#     quantity.append(amount_of_twos)
# print(quantity)

#<------------------->

# [1], [1, 2, 2, 2, 3], [1], [1, 2, 2, 2, 2, 2, 3], [1]

# l = [[1], [1, 2, 3], [1], [1, 2, 2, 2, 3], [1], [1, 2, 2, 2, 2, 2, 3], [1]]
# indexes_of_lists_without_2 = []

# for i, val in enumerate(l):
#     if 2 not in val:
#         indexes_of_lists_without_2.append(i)
# print(indexes_of_lists_without_2)

#<------------------->

t = (1, 2, 3, 4, 5)
t = list(t)
t.append(3)
t = tuple(t)
print(t)
        
            

