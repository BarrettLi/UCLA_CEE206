import pandas as pd

CHUNCK_SIZE = 40

data = []

for param in range(10, 2501):
    with open("output/thermo{}.out".format(param)) as fd:
        print("reading thermo{}.out".format(param))
        seen = False
        lines = fd.readlines()
        observation = [param]
        for i in range(len(lines)):
            line = lines[i]
            if line.startswith("   20000") and seen is True:
                j = i
                while j < len(lines) and len(lines[j].split()) == 7:
                    observation.append(float(lines[j].split()[1]))
                    j = j + CHUNCK_SIZE
                break
            elif line.startswith("   20000"):
                seen = True
        data.append(observation)
        print("done")
columns = ["damp"]
for i in range(101):
    columns.append("temp{}".format(i))

fd = pd.DataFrame(data, columns=columns)
fd.to_csv("data/thermo.csv", index=False)
# print(fd)