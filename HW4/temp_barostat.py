import os

with open("./inputs/Kr_barostat.in", "r") as fd:
    text = fd.readlines()
para = [80.0]
for _ in range(1, 11):
    para.append(_ * 1000.0)

for p in para:
    with open("./inputs/temp_barostat.in", "w") as fd:
        for line in text:
            if(line.startswith("fix")):
                params = line.split()
                params[-1] = str(p) + '\n'
                new_line = " ".join(params)
            else:
                new_line = line
            fd.write(new_line)

    os.system("lmp_serial -in inputs/temp_barostat.in > outputs/baro{}.out".format(int(p)))