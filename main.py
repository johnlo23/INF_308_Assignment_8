class User:

    def __init__(self, user_name):
        self.user_details = {'user': user_name,
                             'name_first': None,
                             'name_last': None,
                             'eyes': None,
                             'hair': None,
                             'city': None,
                             'state': None
                             }

    def set_user_name(self, user_name):
        self.user_details['user'] = user_name

    def set_name_first(self, name_first):
        self.user_details['name_first'] = name_first

    def set_name_last(self, name_last):
        self.user_details['name_last'] = name_last

    def set_eyes(self, eyes):
        self.user_details['eyes'] = eyes

    def set_hair(self, hair):
        self.user_details['hair'] = hair

    def set_city(self, city):
        self.user_details['city'] = city

    def set_state(self, state):
        self.user_details['state'] = state

    def add_details(self, details):
        self.set_user_name(details[0])
        self.set_name_first(details[1])
        self.set_name_last(details[2])
        self.set_eyes(details[3])
        self.set_hair(details[4])
        self.set_city(details[5])
        self.set_state(details[6])

    def get_location(self):
        return f"{self.user_details['city']} {self.user_details['state']}"

    def get_name(self):
        return f"{self.user_details['name_first']} {self.user_details['name_last']}"

    def show_details(self):
        print(f"User: {self.user_details['user']}")
        print(f"Name: {self.get_name()}")
        print(f"Eyes: {self.user_details['eyes']}")
        print(f"Hair: {self.user_details['hair']}")
        print(f"Location: {self.get_location()}")


class UserList:

    def __init__(self):
        self.user_list = list()

    def add_user(self, name, details):
        self.user_list.append({'name': name, 'details': User(name)})
        self.user_list[-1]['details'].add_details(details)

    def find_user(self, name):
        for i in range(0, len(self.user_list)):
            if self.user_list[i]['name'].lower() == name.lower():
                return i
        return None

    def sort_user_list(self):
        self.user_list.sort(key=lambda name: name['name'])


class PickMenu:

    def __init__(self, menu_details):
        self.menu_name = menu_details['title']
        self.menu_items = menu_details['items']

    def show_menu(self):
        print(self.menu_name)
        print("- - - - - - - -")
        for i in range(0, len(self.menu_items)):
            print(f"{str(i + 1)}. {self.menu_items[i]}")

    def get_menu_response(self):
        # loop until user gives valid menu response
        while True:
            # Ask user for menu number
            response = input("Enter the number of your menu choice: ").strip()
            # Check if response string is an integer
            if response.isdigit():
                # Check if response is a valid menu integer
                if (int(response) - 1) in range(0, len(self.menu_items)):
                    return int(response)

            # User did not enter valid integer response
            print(f"Please enter a menu choice between 1 and {len(self.menu_items)}.")
            print()


def get_name():
    while True:
        name = input("Enter a new user name: ").strip()
        if len(name) > 0:
            return name
        else:
            print("The user name cannot be blank.")
            print()


def get_details(name):
    # Get user information
    print("Name details")
    first = input("Enter the first name: ").strip()
    last = input("Enter the last name: ").strip()
    print()

    print("Personal description")
    eyes = input("Enter the eye color: ").strip()
    hair = input("Enter the hair color: ").strip()
    print()

    print("Location")
    city = input("Enter the city name: ").strip()
    state = input("Enter the state abbreviation: ").strip()
    print()
    return name, first, last, eyes, hair, city, state


def menu_action(menu_choice, user_list):
    # 1. Add a new user
    if menu_choice == 1:
        add_user(user_list, get_name())
        print()

    # 2. Show user information
    elif menu_choice == 2:
        show_user_list(user_list)
        print()

    # 3. Sort user list
    elif menu_choice == 3:
        sort_user_list(user_list)
        print()

    # 4. Quit
    elif menu_choice == 4:
        app_quit()


def add_user(user_list_obj, name):
    # Check if name is already in the user list. use list comprehension
    if name.lower() in [x['name'].lower() for x in user_list_obj.user_list]:
        print('Sorry, that name is already taken.')
    else:
        user_list_obj.add_user(name, get_details(name))


def show_user_list(user_list_obj):
    user_menu_tuple = [x['name'] for x in user_list_obj.user_list]
    user_menu_name = 'User List'
    user_menu_details = {'title': user_menu_name, 'items': user_menu_tuple}
    user_menu = PickMenu(user_menu_details)
    user_menu.show_menu()

    user_choice = user_menu.get_menu_response() - 1
    print()
    user_list_obj.user_list[user_choice]['details'].show_details()


def sort_user_list(user_list_obj):
    user_list_obj.sort_user_list()


def app_quit():
    print("Goodbye")
    quit()


def main():
    user_list = UserList()

    # Sample Data
    user_list.add_user('John23', ('John23', 'John', 'Logiudice', 'brown', 'brown', 'Wala Wala', 'WA'))
    user_list.add_user('RollyPanda', ('RollyPanda', 'Gandolph', 'Verspasian', 'hazel', 'blonde', 'Portland', 'OR'))
    user_list.add_user('Jandra2001', ('Jandra2001', 'Jandra', 'De La Cruz', 'green', 'brown', 'La Jolla', 'CA'))

    main_menu_tuple = ('Add a new user', 'Show user information', 'Sort user list', 'Quit')
    main_menu_name = 'Main Menu'
    main_menu_details = {'title': main_menu_name, 'items': main_menu_tuple}
    main_menu = PickMenu(main_menu_details)

    while True:
        main_menu.show_menu()
        print()
        user_choice = main_menu.get_menu_response()
        print()

        menu_action(user_choice, user_list)


if __name__ == '__main__':
    main()
