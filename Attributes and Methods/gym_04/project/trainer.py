class Trainer:
    count_id =0

    def __init__(self, name: str):
        self.name = name
        self.id=self.get_next_id()

    @staticmethod
    def get_next_id():
        Trainer.count_id+=1
        next_id = Trainer.count_id
        return next_id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"