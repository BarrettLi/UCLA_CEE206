import os

def fix_param(damp):
    with open("input/Kr_thermostat.in") as fd:
        text = fd.read()
        text = text.replace("damping_factor", "{}.0".format(damp))
    with open("input/temp.in", "w") as fd:
        fd.write(text)

def run():
    for i in range(1000, 2501):
        print("damping factor = {}".format(i))
        fix_param(i)
        print("running...")
        os.system("lmp_serial -in input/temp.in > output/thermo{}.out".format(i))

if __name__ == "__main__":
    run()
        
     