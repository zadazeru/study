from subprocess import list2cmdline


def sum_def(a, b, c):
    return a, b, c


x = [1, 5, 7]
print(*x)

num = range(2, 6)
print(list(num))
args = [2, 7]
num = range(*args)
print(num)

countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
fin, sw, no, de, *ic = countries
print(fin, sw, no, de, ic)
