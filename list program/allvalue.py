def get_values(d):
    for v in d.values():
        if isinstance(v, dict):
            yield from get_values(v)
        else:
            yield v

my_own = {'1':'harsha','name':{'location':{'bangalore':{'marath','white'},'che':{1:{'hy','ra'}}}}}

print(list(get_values(my_own)))

mydict2 = {'1':'harsha','name':{'location':{'bangalore':{'marath','white'},'che':{1:{'hy','ra'}}}}}
nl = []
nl.append(mydict2['1'])
nl.append(mydict2['name']['location']['bangalore'])
nl.append(mydict2['che'][1])
print(nl)