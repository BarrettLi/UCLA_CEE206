import matplotlib.pyplot as plt
lx = []
stress = []
energy = []
filename = "elastic.out"
with open(filename, "r+") as f:
	lines = f.readlines()
	for i in range(len(lines)):
		line = lines[i]
		if(line.startswith("Step TotEng")):
			ne = lines[i+1]
			vars = ne.split()
			if(int(vars[0]) > 10):
				lx.append(float(vars[-1]))
				stress.append(-1 * float(vars[4]))
				energy.append(float(vars[1]))
# print(lx)
# print(stress)
# print(energy)
dx = [_ - lx[0] for _ in lx]
# print(dx)

plt.plot(dx, stress)
plt.title("Strain-Stress Curve")
plt.xlabel("Strain(%)")
plt.ylabel("Stress(ev/Angstrom)")
plt.show()
print(max(stress))
        # if line[:5] == "anim ":
        #     ne = lines[i + 1] # you may want to check that i < len(lines)
        #     print ' ne ',ne,'\n'
	
