class Gym:

    def __init__(self):
        self.customers =[]
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)
        # – add the customer in the customer list, if the customer is not already in it

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)
    # – add the trainer to the trainers list, if the trainer is not already in it

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)
    # – add the equipment to the equipment list, if the equipment is not already in it

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)
    # – add the plan to the plans list, if the plan is not already in it

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)
    # – add the subscription in the subscriptions list, if the subscription is not already in it

    def subscription_info(self, subscription_id:int):
        subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer = [c for c in self.customers if c.id == subscription.customer_id][0]
        trainer = [t for t in self.trainers if t.id == subscription.trainer_id][0]
        plan = [p for p in self.plans if p.trainer_id == trainer.id][0]
        equipment = [e for e in self.equipment if e.id == plan.equipment_id][0]
        return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"

