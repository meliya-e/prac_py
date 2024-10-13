def Pareto(*pairs):
    for i in pairs:
        for j in pairs:
            if (i[0] >= j[0] and i[1] >= j[1]) and (i[0] > j[0] or i[1] > j[1]):
                pairs = [x for x in pairs if j != x]
    return pairs

import sys
exec(sys.stdin.read())

