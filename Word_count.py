def j(a):
    new_map = {} 
    for item in list(a.split()):
        if item in new_map:
            new_map[item] += 1
        else:
            new_map[item] = 1
    return new_map
    
print(j('testing i am just testing i'))