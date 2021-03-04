class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name=name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals)>=self.__animal_capacity:
            return f"Not enough space for animal"
        if  self.__budget < price and len(self.animals)< self.__animal_capacity:
            return f"Not enough budget"
        self.animals.append(animal)
        self.__budget -=price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self,worker):
        if len(self.workers)>=self.__workers_capacity:
            return f"Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        workers = [worker for worker in self.workers if worker.name==worker_name]
        if not workers:
            return f"There is no {worker_name} in the zoo"
        worker = workers[0]
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salary_sum = sum([worker.salary for worker in self.workers])
        if salary_sum>=self.__budget:
            return f"You have no budget to pay your workers. They are unhappy"
        self.__budget -= salary_sum
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        tender_sum = sum([animal.get_needs() for animal in self.animals])
        if tender_sum>=self.__budget:
            return f"You have no budget to tend the animals. They are unhappy."
        self.__budget -= tender_sum
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget+=amount

    def animals_status(self):
        lions = [str(el) for el in self.animals if el.__class__.__name__=="Lion"]
        tigers = [str(el) for el in self.animals if el.__class__.__name__ == "Tiger"]
        cheetahs = [str(el) for el in self.animals if el.__class__.__name__ == "Cheetah"]
        new_line = "\n"

        res =f"You have {len(self.animals)} animals"+"\n"
        res +=f"----- {len(lions)} Lions:"+"\n"
        res +=f"{new_line.join(lions)}"+"\n"
        res +=f"----- {len(tigers)} Tigers:"+"\n"
        res +=f"{new_line.join(tigers)}"+"\n"
        res +=f"----- {len(tigers)} Cheetahs:"+"\n"
        res +=f"{new_line.join(cheetahs)}"
        return res


    def workers_status(self):
        keepers = [str ( el ) for el in self.workers if el.__class__.__name__ == "Keeper"]
        caretakers = [str ( el ) for el in self.workers if el.__class__.__name__ == "Caretaker"]
        vets = [str ( el ) for el in self.workers if el.__class__.__name__ == "Vet"]
        new_line = "\n"

        res =f"You have {len(self.workers)} workers"+"\n"
        res +=f"----- {len(keepers)} Keepers:"+"\n"
        res +=f"{new_line.join(keepers)}"+"\n"
        res +=f"----- {len(caretakers)} Caretakers:"+"\n"
        res +=f"{new_line.join(caretakers)}"+"\n"
        res +=f"----- {len(vets)} Vets:"+"\n"
        res +=f"{new_line.join(vets)}"
        return res

