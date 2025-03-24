def my_zip(l1,l2):
    r =[]
    for i in range(len(l1)):
        r.append((l1[i],l2[i]))

    return r

groups = ['HOT', 'Seventeen', 'Black Pink', 'NJZ']
# ratings = [1, 2, 4, 3, 100]
ratings = [1, 2, 4, 3]

#group_rating = list(zip(groups, ratings))
#print(group_rating)
print(my_zip(groups, ratings))