class User:
    def __init__(self, id, name, access_level='user'):
        self._id = id
        self._name = name
        self.__access_level = access_level

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_access_level(self):
        return self.__access_level

    def set_access_level(self, level):
        self.__access_level = level

    def __repr__(self):
        return f"Пользователь('{self.get_id()}', '{self.get_name()}', '{self.get_access_level()}')"


class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name, 'admin')
        self._users = []

    def add_user(self, user):
        if isinstance(user, User) and user not in self._users:
            self._users.append(user)
            print(f"Добавление {user}")
        else:
            print(f"Не удалось добавить пользователя: {user}")

    def remove_user(self, user):
        if user in self._users:
            self._users.remove(user)
            print(f"Удаление {user}")
        else:
            print(f"Не удалось удалить пользователя: {user}")

    def list_users(self):
        return self._users

    def __repr__(self):
        return f"Администратор('{self.get_id()}', '{self.get_name()}', '{self.get_access_level()}')"


# Создание администратора
admin = Admin(1, "Admin1")

# Создание пользователей
user1 = User(2, "User1")
user2 = User(3, "User2")
user3 = User(4, "User3")

# Добавление пользователей
admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

# Попытка добавить того же пользователя
admin.add_user(user1)

# Удаление пользователя
admin.remove_user(user2)

# Попытка удалить несуществующего пользователя
admin.remove_user(user2)

# Список пользователей
print("Список пользователей:")
for user in admin.list_users():
    print(user)

# Обновление уровня доступа пользователя
user1.set_access_level('superuser')
print(user1)