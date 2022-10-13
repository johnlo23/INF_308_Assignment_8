

class User:

    def __init__(self, user_name):
        self.user_details = {'user' : user_name,
                             'name_first' : None,
                             'name_last' : None,
                             'eyes' : None,
                             'hair' : None,
                             'city' : None,
                             'state' : None
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

    def add_details(self, user_name, name_first, name_last,
                    eyes, hair, city, state):
        self.set_user_name(user_name)
        self.set_name_first(name_first)
        self.set_name_last(name_last)
        self.set_eyes(eyes)
        self.set_hair(hair)
        self.set_city(city)
        self.set_state(state)

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

    # Add a new user
    def add_details(self):
        print()

class User_List:

    def __init__(self):
        self.user_list = list()

    def add_user(self, name):
        self.user_list.append({'name': name, 'details':User(name)})

    def find_user(self, name):
        for i in range(0, len(self.user_list)):
            if self.user_list[i]['name'].lower() == name.lower():
                return i
        return None

    def sort_user_list(self):
        self.user_list.sort(key=lambda name: name['name'])

    def show_user_list(self):
        print("User list")
        print('- - - - - -')

        # Iterate through the list of users
        for i in range(0, len(self.user_list)):
            # Print line number and user name
            print(f"{i+1}. {self.user_list[i]}")
    

class Menu:

    main_menu_tuple = ('Add a new user', 'Show user information', 'Sort user list', 'Quit')
    main_menu_name = 'Main Menu'
    def __init__(self):
        user_choice = None

    def show_menu(self):
        print(self.main_menu_name)
        print("- - - - - - - -")
        for i in range(0, len(self.main_menu_tuple)):
            print(f"{str(i+1)}. {self.main_menu_tuple[i]}")
            
    def get_menu_response(self):
        # loop until user gives valid menu response
        while True:
            # Ask user for menu number
            response = input("Enter the number of your menu choice: ").strip()
            # Check if response string is an integer
            if response.isdigit():
                # Check if response is a valid menu integer
                if (int(response) - 1) in range(0, len(self.main_menu_tuple)):
                    return int(response)

            # User did not enter valid integer response
            print(f"Please enter a menu choice between 1 and {len(self.main_menu_tuple)}.")
            print()
    
    def menu_action(self, menu_choice):
        if menu_choice == 1:
            print('1')
        elif menu_choice == 2:
            print('2')

        elif menu_choice == 3:
            print('3')

        elif menu_choice == 4:
            print('4')
            
    def add_user(self, user_list_obj, name):
        user_list_obj.add_user(name)

    def show_user_list(self, user_list_obj):
        user_list_obj.show_user_list()

    def sort_user_list(self, user_list_obj):
        user_list_obj.sort_user_list()

    def app_quit(self):
        print("Goodbye")
        quit()

def main():
    user_list = User_List()
    main_menu = Menu()

    main_menu.show_menu()
    print()
    user_choice = main_menu.get_menu_response()
    print()
    
    main_menu.menu_action(user_choice)


if __name__ == '__main__':
    main()
