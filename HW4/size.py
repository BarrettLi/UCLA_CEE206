import matplotlib.pyplot as plt
import numpy as np

s = [3, 4, 5, 6, 7, 8]
atoms = [ _ **3 * 4 for _ in s]
fnames = ["outputs/size{}.out".format(str(_)) for _ in s]

ave_eng = []
std = []

for index in range(len(fnames)):
    with open(fnames[index], "r") as fd:
        lines = fd.readlines()
        i = 0
        temp = []
        while i < len(lines):
            if lines[i].startswith("Step Temp PotEng Press"):
                i = i + 1
                while lines[i].split()[0].isdigit():
                    temp.append(float(lines[i].split()[1]))
                    
                    if lines[i].split()[0] == "221182":
                        tot_eng = float(lines[i].split()[2])
                        ave_eng.append(tot_eng/atoms[index])
                    
                    i = i + 1
            else:
                i = i + 1
        std.append(temp)
    print("size{}.out is processed".format(s[index]))
print(len(ave_eng))
print(np.array(std).shape)

plt.plot(atoms, np.absolute(ave_eng))
plt.title("# of atoms vs. average energy")
plt.xlabel("# of atoms")
plt.ylabel("Average energy")
plt.show()

plt.plot(atoms, np.std(std, axis=1))
plt.title("# of atoms vs. std of temperature")
plt.xlabel("# of atoms")
plt.ylabel("std of temperature")
plt.show()