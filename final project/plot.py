import pandas as pd
import matplotlib.pyplot as plt

CHUNCK_SIZE = 40

thermo = []

with open("output/thermo1000.out") as fd:
    print("reading thermo1000.out")
    seen = False
    lines = fd.readlines()
    for i in range(len(lines)):
        line = lines[i]
        if line.startswith("   20000") and seen is True:
            j = i
            while j < len(lines) and len(lines[j].split()) == 7:
                thermo.append(float(lines[j].split()[1]))
                j = j + 1
            break
        elif line.startswith("   20000"):
            seen = True
    print("done")

data = []

with open("output/thermo1000.out") as fd:
    print("reading thermo100.out")
    seen = False
    lines = fd.readlines()
    for i in range(len(lines)):
        line = lines[i]
        if line.startswith("   20000") and seen is True:
            j = i
            while j < len(lines) and len(lines[j].split()) == 7:
                data.append(float(lines[j].split()[1]))
                j = j + CHUNCK_SIZE
            break
        elif line.startswith("   20000"):
            seen = True
    print("done")
x1 = [_ for _ in range(20000, 60001, 10)]
x2 = [_ for _ in range(20000, 60001, 400)]

fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Data Encoding')
ax1.plot(x1, thermo)
ax1.set(xlabel="Time Stamp", ylabel="Temperature")
ax2.plot(x2, data)
ax2.set(xlabel="Time Stamp", ylabel="Temperature")
plt.show()