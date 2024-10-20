s = input()
arr = []
arr.append(s)
while (s := input()):
    arr.append(s)
    if len(s) == s.count("#"):
        break

w = len(arr)
gas = sum(i.count(".") for i in arr)
water = sum(i.count("~") for i in arr)
def fun(gas, water):
    res = ["#" * len(arr)]
    while gas >= w - 2:
        i = f"#{"." * (w - 2)}#"
        gas -= w - 2
        res.append(i)

    while water >= 0:
        i = f"#{"~" * (w - 2)}#"
        water -= w - 2
        res.append(i)
    res.append("#" * len(arr))
    return res

for i in fun(gas, water):
    print(i)
if gas > water:
    r = 20 * round(gas/ (gas + water))
    g = 20
else:
    g = 20 * round(water/ (gas + water))
    r = 20

print(f"{"." * 10:<{g}} {gas}/{gas + water}")
print(f"{"~" * 20:<{r}} {water}/{gas + water}")


import sys
exec(sys.stdin.read())

