from project.hardware.hardware import Hardware

class PowerHardware (Hardware):
    def __init__(self,  name, capacity_s, memory_s):
        super ().__init__ ( name , type = "Power" ,capacity= int(0.25*capacity_s), memory = int(1.75*memory_s))

