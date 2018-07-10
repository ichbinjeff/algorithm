def permutation(numstr):
    rst = []
    level = []
    dfs(rst, level, numstr)
    return rst

def dfs(rst, level, numstr):
    if len(level) == len(numstr):
        rst.append(level[:])
    for s in numstr:
        if s.lower() in level or s.upper() in level:
            continue

        level.append(s.lower())
        dfs(rst, level, numstr)
        level.pop()

        level.append(s.upper())
        dfs(rst, level, numstr)
        level.pop()



print permutation("abc")