import datetime
class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented  = False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        day, month, year = date.split('.')
        year = int(year)
        month = datetime.date(int(year), int(month), 1).strftime('%B')
        return cls( name, id, year, month, age_restriction)

    def __repr__(self):
        if self.is_rented:
            status = "rented"
        else:
            status = "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}"