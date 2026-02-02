import numpy as np

MaxN = 1000000
test_case = []
test_case.append(np.sort(np.random.uniform(-1e6, 1e6, MaxN)))
test_case.append(np.sort(np.random.uniform(-1e6, 1e6, MaxN))[::-1])
for i in range(3):
    test_case.append(np.random.uniform(-1e6, 1e6, MaxN))
for i in range(5):
    test_case.append(np.random.randint(-1_000_000, 1_000_000, MaxN))
with open("input.txt", "w") as f:
    for a in test_case:
        f.write(" ".join(map(str, a)))
        f.write("\n")
