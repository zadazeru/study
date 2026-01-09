import os
import sys
import getopt


n = 40
pattern = [[" " for _ in range(n)] for _ in range(n)]

for i in range(n):
    pattern[0][i] = "*"
    pattern[n - 1][i] = "*"
    pattern[i][0] = "*"
    pattern[i][n - 1] = "*"
    pattern[i][n // 2] = "*"
    pattern[i][i] = "*"
    pattern[i][n - i - 1] = "*"
    pattern[n // 2][i] = "*"

pattern[int(float(n) / 7.0)][int(float(n) / 4.0 + float(n) / 7.0)] = "*"
pattern[int(float(n) / 4.0 + float(n) / 7.0)][int(float(n) / 7.0)] = "*"
pattern[int(float(n) / 7.0)][int(float(n) - float(n) / 4.0 - float(n) / 7.0)] = "*"
pattern[int(float(n) / 4.0 + float(n) / 7.0)][int(float(n) - float(n) / 7.0)] = "*"
pattern[int(float(n) / 7.0)][int(float(n) / 2.0)] = "*"


pattern[int(float(n) - float(n) / 7.0 - 1)][int(float(n) / 4.0 + float(n) / 7.0)] = "*"
pattern[int(float(n) - float(n) / 4.0 - float(n) / 7.0)][int(float(n) / 7.0)] = "*"
pattern[int(float(n) - float(n) / 7.0 - 1)][
    int(float(n) - float(n) / 4.0 - float(n) / 7.0)
] = "*"
pattern[int(float(n) - float(n) / 4.0 - float(n) / 7.0)][
    int(float(n) - float(n) / 7.0)
] = "*"
pattern[int(float(n) - float(n) / 7.0 - 1)][int(float(n) / 2.0)] = "*"
for row in pattern:
    print(" ".join(row))

sys.exit(0)
