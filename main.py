class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name

    def set_access_level(self, access_level):
        self.__access_level = access_level


class Admin(User):
    def __init__(self, user_id, name, admin_level):
        super().__init__(user_id, name, 'admin')
        self.__admin_level = admin_level
        self.__users = []

    def get_admin_level(self):
        return self.__admin_level

    def set_admin_level(self, admin_level):
        self.__admin_level = admin_level

    def add_user(self, user):
        if isinstance(user, User):
            self.__users.append(user)
            print(f"User {user.get_name()} added.")
        else:
            print("Invalid user. Cannot add to the list.")

    def remove_user(self, user_id):
        for user in self.__users:
            if user.get_user_id() == user_id:
                self.__users.remove(user)
                print(f"User {user.get_name()} removed.")
                return
        print("User not found.")

    def list_users(self):
        if self.__users:
            print("User List:")
            for user in self.__users:
                print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")
        else:
            print("No users in the list.")

# Пример использования:
admin = Admin(1, "Admin1", 5)
user1 = User(2, "User1")
user2 = User(3, "User2")

admin.add_user(user1)
admin.add_user(user2)
admin.list_users()

admin.remove_user(2)
admin.list_users()
