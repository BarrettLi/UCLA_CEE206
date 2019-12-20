import numpy as np
import matplotlib.pyplot as plt

damp = [80, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

fnames = ["outputs/baro{}.out".format(_) for _ in damp]
res = []
x = [_ * 10 for _ in range(4000)]

for name in fnames:
    with open(name, "r") as fd:
        lines = fd.readlines()
        i = 0
        temp = []
        while i < len(lines):
            if(lines[i].startswith("Step Temp PotEng Press Volume")):
                i = i + 1
                for _ in range(2000):
                    info = lines[i].split()
                    # print(info[0])
                    temp.append(float(info[3]))
                    if float(info[1]) > 1000:
                        print(name, len(temp)*10)
                    i = i + 1
            else:
                i = i + 1
        res.append(temp)
        print("{} done! {} lines processed!".format(name, len(temp)))

for i in range(1, len(res)):
    plt.plot(x, res[i], label="param={}".format(damp[i]))
    plt.xlabel("steps")
    plt.ylabel("Pressure")
plt.xlim(15000, 40000)
plt.title("Effect of damping parameters")
plt.legend()
plt.show()

# print(res[0][2000: 2500])
