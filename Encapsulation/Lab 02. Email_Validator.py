class EmailValidator:
    def __init__(self, min_length , mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains =domains

    def __validate_name(self, name):
        if len(name)>=self.min_length:
            return True
        return False

    def __validate_mail(self, mail):
        if mail in self.mails:
            return True
        return False

    def __validate_domain(self, domain):
        if domain in self.domains:
            return True
        return False

    def validate(self, email):
        current_name = email.split ( '@' )[0]
        current_mail = email.split ( '@' )[1]
        current_domain = current_mail.split ( '.' , maxsplit=1)[1]
        current_mail = current_mail.split ( '.' )[0]
        if self.__validate_name(current_name) and self.__validate_mail(current_mail) and self.__validate_domain(current_domain):
            return True
        return False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
