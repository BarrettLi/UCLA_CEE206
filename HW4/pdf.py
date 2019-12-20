import numpy as np
import matplotlib.pyplot as plt
import os

def read(names):
    for name in names: 
        os.system("lmp_serial -in inputs/Kr_pdf_{}.in > outputs/pdf_{}.out".format(name, name))
        dis = []
        pdf = []
        print("{} simulation done!".format(name))
        with open("pdf.dat") as fd:
            lines = fd.readlines()
            for line in lines:
                comp = line.split()
                if len(comp) == 4 and comp[0].isdigit():
                    dis.append(float(comp[1]))
                    pdf.append(float(comp[2]))
        
        plt.plot(dis, pdf, label=name)
        print("{} plotting done!".format(name))
    
    plt.plot(dis, [1 for _ in range(len(dis))], '--')
    plt.title("pair distribution function")
    plt.xlabel("distance")
    plt.ylabel("pdf")
    plt.legend()

    plt.show()

read(["crystal", "gas", "glass", "liquid"])