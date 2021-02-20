class Library:

    def __init__(self):
        self.user_records  = []
        self.books_available = {}
        self.rented_books = {} 


    def add_user(self, user):
        if user not in self.user_records:
            self.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"


    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        self.user_records.remove(user)


    def change_username(self, user_id: int, new_username: str):
        if user_id not in [user.user_id for user in self.user_records]:
            return f"There is no user with id = {user_id}!"
        user = [user for user in self.user_records if user.user_id == user_id][0]
        if user.username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"
        user.username = new_username
        return f"Username successfully changed to: {user.username} for userid: {user.user_id}"