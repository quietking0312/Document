import random

data = []
for a in range(100000000):
    item = random.randint(0, 100000000)
    print(item)
    data.append(item)
with open("data.text", "w") as f:
    f.write(",".join([str(i) for i in data]))