def func(strs,dicts):
    res = []
    ls = list(strs)
    res.append("")
    count = 0
    for s in ls:
        if s in dicts:
            count += 1
            tmp = []
            for c in dicts[s]:
                 tmp+= list(map(lambda x:x+c,res))
            res = tmp
        else:
            res = list(map(lambda x:x+s,res))
    if count==0:
        return None
    return res