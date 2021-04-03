
from project.software.software import Software


class Hardware:


    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type  # string ("Heavy" or "Power")
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        occup_cap = sum([s.capacity_consumption for s in self.software_components])
        occup_mem = sum ( [s.memory_consumption for s in self.software_components] )
        if self.capacity >=software.capacity_consumption+ occup_cap and self.memory>=software.memory_consumption+occup_mem:
            self.software_components.append(software)
        else:
            raise Exception ("Software cannot be installed")

    #     If there is enough capacity and memory, add the software object to the software_components.
    #     Otherwise, raise Exception with message "Software cannot be installed"

    # def install(self, software: Software):
    #     if self.capacity < sum([s.capacity_consumption for s in self.software_components]) + software.capacity_consumption \
    #             or self.memory < sum([s.memory_consumption for s in self.software_components]) + software.memory_consumption:
    #         raise Exception('Software cannot be installed')

    def uninstall(self, software:Software):
        if software in self.software_components:
            self.software_components.remove(software)

    # @property
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self, value):
    #     self._name = value
    #
    # @property
    # def type(self):
    #     return self._type
    #
    # @type.setter
    # def type(self, value):
    #     self._type = value
    #
    # @property
    # def capacity(self):
    #     return self._capacity
    #
    # @capacity.setter
    # def capacity(self, value):
    #     self._capacity =value
    #
    # @property
    # def memory(self):
    #     return self._memory
    #
    # @memory.setter
    # def memory(self, value):
    #     self._memory=value
