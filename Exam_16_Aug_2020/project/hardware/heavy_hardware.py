from project.hardware.hardware import Hardware

class HeavyHardware(Hardware):
    def __init__(self,  name, capacity_s, memory_s):
        super ().__init__ ( name , type ="Heavy", capacity= int(2*capacity_s), memory = int(0.75*memory_s))



# l_software = HeavyHardware("HDD", 200, 200)
# print(l_software)

