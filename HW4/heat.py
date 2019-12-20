import matplotlib.pyplot as plt

def read(name):
    temp = []
    eng = []
    volume = []

    with open(name, "r") as fd:
        lines = fd.readlines()
        i = 0
        while i < len(lines):
            if lines[i].startswith("Step Temp PotEng Press Volume"):
                i = i + 1
                while lines[i].split()[0].isdigit():
                    info = lines[i].split()
                    temp.append(float(info[1]))
                    eng.append(abs(float(info[2])))
                    volume.append(float(info[4]))
                    i = i + 1
            else:
                i = i + 1
    
    return temp, eng, volume

temp_heat, eng_heat, volume_heat = read("outputs/heat.out")
print(len(temp_heat), len(eng_heat), len(volume_heat))
plt.scatter(temp_heat, eng_heat, label="heating")

temp_cool, eng_cool, _ = read("outputs/cool.out")
plt.scatter(temp_cool, eng_cool, label="cooling")
plt.title("temperature vs. potential energy")
plt.xlabel("temperature")
plt.ylabel("potential energy")
plt.legend()
plt.show()
