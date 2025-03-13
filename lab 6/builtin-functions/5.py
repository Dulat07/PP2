def all_elements_true(tup):
    return all(tup)


tup1 = (True, True, True,True,True)
tup2 = (True, False, True,False,True)

print(all_elements_true(tup1)) 
print(all_elements_true(tup2)) 