import os

# AIRBNB - BATANGAS (A small house rental project, that has similar features to airbnb )
 
# Features - View Available Properties for Rent
#          - Check-In and Check-Out of Properties
#          - View Current Bookings
#          - Manage Account Balance
#          - User Property Listing and Management:
#               - Add own property for rent
#               - Modify existing owned property details
#               - Delete property from available rentals
#               - View All Owned Properties Available for rent


user_accounts = {}

#DICTIONARY FOR THE LIST OF PROPERTIES AVAILABLE TO RENT (NAME, DESCRIPTION, PRICE PER NIGHT, LOCATION, AVAILABILITY, AND THE HOST)
available_rentals = [
    {'name': 'Condo Unit (4D - 4th floor)', 'description': '\nPartially furnished condo unit with balcony and elevator with majestic view of Batangas City. \n The room can accomodate 2 pax. The price indicated here is per person per night. \nBefore booking, kindly update number of guests. The system will automatically compute the amount you have to pay.', 'price_per_night': 13, 'location': 'Kumintang Ibaba, Batangas', 'availability': {'Monday': True, 'Tuesday': True, 'Wednesday': True, 'Thursday': True, 'Friday': True, 'Saturday': True, 'Sunday': True}, 'host': 'Rosie'},
    {'name': 'M&R Apartment Batangas City', 'description': '\n A three-unit apartment, one will be used as a transient house. Located at Mirata Compound, Sitio Lamao, Barangay Libjo, Batangas City\n Few meters away from the mainroad. Free-road parking. Quiet and safe place. Good for 2 guest only. \nPETS NOT ALLOWED', 'price_per_night': 15, 'location': 'Libjo, Batangas', 'availability': {'Monday': True, 'Tuesday': True, 'Wednesday': True, 'Thursday': False, 'Friday': False, 'Saturday': True, 'Sunday': True}, 'host': 'Rhobert'},
    {'name': 'Anyayahan Apartment - 3rd', 'description': '\n -no available description-', 'price_per_night': 19, 'location': 'Batangas', 'availability': {'Monday': False, 'Tuesday': False, 'Wednesday': False, 'Thursday': False, 'Friday': False, 'Saturday': False, 'Sunday': False}, 'host': 'Juana'},
    {'name': 'Invite-Reyes Apartment', 'description': 'Not suited for toddlers & wheelchair-user due to steep stairs. Not so far to Jollibee & Euphrasia. \nCCTV. WiFi. AC. 3CR/showerrooms. French veranda. Dirty kitchen. These are not provided: towels, toilet paper, soap, shampoo', 'price_per_night': 26, 'location': 'Batangas', 'availability': {'Monday': True, 'Tuesday': True, 'Wednesday': True, 'Thursday': False, 'Friday': True, 'Saturday': True, 'Sunday': True}, 'host': 'Jovita'},
    {'name': 'JMS Transient House - Kathniel', 'description': '\nA comfortable room in a garden with free wifi, tv, aircon. Best for travelers looking for very affordable accommodation for a night. \nValue for money is at its best! Our guests satisfaction is our priority. Book now!', 'price_per_night': 29, 'location': 'Wawa, Batangas', 'availability': {'Monday': True, 'Tuesday': True, 'Wednesday': True, 'Thursday': True, 'Friday': True, 'Saturday': True, 'Sunday': True}, 'host': 'Kath'},
    {'name': '3rd Floor Modern Apartment LUXE Unit 1', 'description': '\nThis one bedroom apartment is on the 3rd floor of a new building. There is parking on the ground floor and a laundromat who will deliver your laundry to your apartment. \nThe apartment is designed for comfort with old artwork, vintage and new furniture. The bathroom and kitchen area is made with Italian marble. \nThis area is walking distance to the Capitol building, Lyceum, NBI, BIR and other points of interests. \nOutside, public transportation and eating options are plenty. ', 'price_per_night': 40, 'location': 'Batangas', 'availability': {'Monday': True, 'Tuesday': True, 'Wednesday': True, 'Thursday': True, 'Friday': True, 'Saturday': False, 'Sunday': False}, 'host': 'Claudio'},
    {'name': 'Summer Promo Stylish Studio', 'description': '\n If you are looking for comfortable living, leisure and convenient work space in the city, this studio type condo might be the perfect fit for you.\nUpon entering the unit, you can feel the comfort of the seater perfect for study, work space or just simply for relaxing while watching your favorite Netflix movie. \nThe kitchenette is fully equipped with sink, basic appliances and utensils for light cooking. Feel the warmth of home and indulge on the complimentary snacks and drinks. \nBefore you snooze down and rest , you can enjoy the scenic view of the hotels garden and swimming pool. \nThe toilet and bath are separate with personal care items for your convenience and just across it is the dresser for your clothes, shoes and personal items.', 'price_per_night': 39, 'location': 'Batangas', 'availability': {'Monday': True, 'Tuesday': True, 'Wednesday': True, 'Thursday': True, 'Friday': True, 'Saturday': True, 'Sunday': True}, 'host': 'Kristine Joy'},
    {'name': 'Mel C Place', 'description': '\nKeep it simple at this peaceful and centrally-located place.', 'price_per_night': 114, 'location': 'Batangas', 'availability': {'Monday': False, 'Tuesday': False, 'Wednesday': True, 'Thursday': True, 'Friday': True, 'Saturday': True, 'Sunday': True}, 'host': 'Mel'},
    {'name': 'Pontefino Prime Townhouse ', 'description': '\nYour home away from home. This townhouse is located midway malls, schools, hospitals and prime areas. \nPerfect for everyone planning to stay in the city.', 'price_per_night': 88, 'location': 'Batangas', 'availability': {'Monday': True, 'Tuesday': True, 'Wednesday': True, 'Thursday': True, 'Friday': True, 'Saturday': True, 'Sunday': True}, 'host': 'Kristine'},
    {'name': 'Mamas Place', 'description': '\nMamas Place is conveniently located in Batangas Uptown, you are welcome and you and your safety are always our priority.', 'price_per_night': 35, 'location': 'Alangilan, Batangas', 'availability': {'Monday': True, 'Tuesday': True, 'Wednesday': True, 'Thursday': True, 'Friday': False, 'Saturday': False, 'Sunday': False}, 'host': 'Noriel'},
    {'name': 'Sofies Home', 'description': '\nEnjoying a central location in Batangas City!, We offer our home to be your home with 24 hour security services, WIFI, Smart TV, Cable, Netflix and Free Pool Access registered guest only.\n 5 guests, 3 bedrooms, 3 beds, 3 baths', 'price_per_night': 58, 'location': 'Batangas', 'availability': {'Monday': False, 'Tuesday': True, 'Wednesday': True, 'Thursday': True, 'Friday': False, 'Saturday': True, 'Sunday': True}, 'host': 'Lyn'},
    {'name': 'Marife Apartments', 'description': '\nThis stylish and spacious place is in the heart of Batangas. Near SM Mall and Resturants that may cater your liking. \nVery accessible and secured location.', 'price_per_night': 34, 'location': 'Batangas', 'availability': {'Monday': True, 'Tuesday': True, 'Wednesday': False, 'Thursday': False, 'Friday': False, 'Saturday': True, 'Sunday': True}, 'host': 'Marife'},
    {'name': 'Celes Guest House', 'description': '\nThis is the best place for your family to get together. Quiet and comfortable place to stay with.\n Has 2 bedrooms and 1 bathroom, can accomodate 2 guests in total', 'price_per_night': 44, 'location': 'Batangas', 'availability': {'Monday': True, 'Tuesday': True, 'Wednesday': True, 'Thursday': True, 'Friday': True, 'Saturday': True, 'Sunday': True}, 'host': 'Celeste Marie'},
    {'name': 'Loming Barako Home Batangas City 3BR', 'description': '\nFeel like home in this spacious & quiet house, located in a subdivision in Batangas City with 24/7 security guard and roving time to time along the premises,\n near in SM Batangas City, Church and restaurants. \nMinimalist home with 3 bedrooms, 3 beds, 1 powder room & 1 CR/Shower', 'price_per_night': 62, 'location': 'Batangas City', 'availability': {'Monday': True, 'Tuesday': True, 'Wednesday': True, 'Thursday': True, 'Friday': True, 'Saturday': True, 'Sunday': True}, 'host': 'Cherie Marie'},
    {'name': 'White Llabin - Cozy Glass House', 'description': '\nExperience ultimate gatherings at our aesthetic home rental in San Isidro, Batangas City! Enjoy a refreshing dip in the mini pool, showcase your vocal talents with the karaoke setup, or simply unwind in the spacious garden. \nIdeal for family celebrations, the property is conveniently located just 8 minutes away from SM Batangas City and other attractions. Create lasting memories in a home crafted for family joy and togetherness', 'price_per_night': 261, 'location': 'Batangas', 'availability': {'Monday': True, 'Tuesday': False, 'Wednesday': True, 'Thursday': True, 'Friday': True, 'Saturday': True, 'Sunday': True}, 'host': 'Christian'},
    {'name': 'Nature Lodge', 'description': '\n You will love the stylish decor of this charming place to stay. \n16+ guests, 4 bedrooms, 9 beds, 9 shared baths', 'price_per_night': 265, 'location': 'Batangas', 'availability': {'Monday': False, 'Tuesday': False, 'Wednesday': False, 'Thursday': False, 'Friday': False, 'Saturday': False, 'Sunday': False}, 'host': 'JOEL'},
    {'name': 'Emmanuel private pool house', 'description': '\nLooking for a place comfortable ,a touch of luxury? Emanuel pool place is perfect  place for you . \nA relaxing place for staycation,birthday events,family gathering for friends and family bonding. \nLocated @ Road 4 stay labak  batangas city', 'price_per_night': 143, 'location': 'Batangas', 'availability': {'Monday': True, 'Tuesday': True, 'Wednesday': True, 'Thursday': True, 'Friday': True, 'Saturday': True, 'Sunday': True}, 'host': 'Armi'},
    {'name': 'Lian Beach & Pool private resort', 'description': '\n Reconnect with loved ones in this family-friendly place. 8 guests, 1 bedroom, 2 beds, 1 bath', 'price_per_night': 106, 'location': 'Batangas', 'availability': {'Monday': False, 'Tuesday': False, 'Wednesday': False, 'Thursday': False, 'Friday': True, 'Saturday': True, 'Sunday': True}, 'host': 'Gk Keets'},
    {'name': 'House of Mother -Nordic Style bungalow', 'description': '\nIt is not a hotel with 5star service but guests will experience the quiet/secured place to stay while attending business on-site meetings/functions, \nenjoy recreational and leisure activities, and, satisfy craving for food and easy access to get basic necessities while away from home.', 'price_per_night': 100, 'location': 'Tacad, Batangas', 'availability': {'Monday': True, 'Tuesday': True, 'Wednesday': True, 'Thursday': True, 'Friday': True, 'Saturday': True, 'Sunday': True}, 'host': 'Jane Smith'},
    {'name': 'Cozy Stay in Batangas City (Unit L)', 'description': '\nWelcome to our spacious 2-bedroom apartment, perfect for families or groups of friends. Our fully air-conditioned space features two comfortable beds and can accommodate up to four people. \nYou will also have access to a smart TV with Netflix and fast wifi. Our location is conveniently situated in the city center, just minutes walk away from the SM mall and 15 mins drive to Batangas Pier. \nCome stay with us and experience the best of the city in comfort and style.', 'price_per_night': 47, 'location': 'Batangas', 'availability': {'Monday': True, 'Tuesday': True, 'Wednesday': True, 'Thursday': True, 'Friday': True, 'Saturday': True, 'Sunday': True}, 'host': 'Ellen'},
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  

#REGISTER USER
def register():
    clear_screen()  
    while True:
        print("-REGISTER USER-")
        username = input("\nEnter username: ")
        password = input("Enter Password (must be at least 8 characters long): ")
        if len(password) >= 8:
            user_accounts[username] = {
                'username': username,
                'password': password,
                'money': 0,
                'properties': []
            }
            print("Sign up successful!")
            break
        else:
            print("Password must be 8 characters long.")

#LOG-IN USER
def user_log_in():
    clear_screen()  
    while True:
        print("-LOG-IN USER-")
        username = input("\nEnter your username: ")
        password = input("Enter your password: ")
        if username in user_accounts and user_accounts[username]['password'] == password:
            print("Log in successful!")
            logged_in_menu(username)
            break
        else:
            print("Wrong username or password.")

#THE AIRBNB - BATANGAS MAIN MENU
def logged_in_menu(username):
    clear_screen()  
    while True:
        print("\nAIRBNB - BATANGAS MAIN MENU")
        print(f'\nLogged in as {username}')
        print(f'Current balance: ${user_accounts[username]["money"]}')
        print("Today is Monday.")  
        print("""
            1. View Available House Rentals 
            2. Check-In
            3. Check-Out
            4. View Bookings
            5. Account Balance
            6. User Property Listing and Management
            7. Logout
            """)
        try:
            choice = int(input("Enter a number: "))
            if choice == 1:
                view_available_rentals()
            elif choice == 2:
                checkin(username)
            elif choice == 3:
                checkout(username)
            elif choice == 4:
                bookings(username)
            elif choice == 5:
                balance(username)
            elif choice == 6:
                properties(username)
            elif choice == 7:
                main()
                break
            else:
                print("Enter a valid input.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#VIEW THE DETAILS OF AVAILABLE PROPERTIES FOR RENT
def view_available_rentals():
    clear_screen()  
    print("Available Rentals: Sorted Price From Low to High")
    for index, rental in enumerate(available_rentals):
        name = rental['name']
        price = rental['price_per_night']
        location = rental['location']
        print(f"{index + 1:2}. {name: <40} - Price per night: ${price:<5}, Location: {location}")

    try:
        choice = int(input("Enter the number of the property you want to view details (or enter 0 to go back): "))
        if choice == 0:
            return
        rental = available_rentals[choice - 1]

        print("\nProperty Details:")
        print(f"\nName: {rental['name']}")
        print(f"Description: {rental['description']}")
        print(f"Host: {rental['host']}")
        print(f"Price per night: ${rental['price_per_night']}")
        print(f"Location: {rental['location']}")
        print("\nAvailability:")
        for day, available in rental['availability'].items():
            print(f"{day}: {'Available' if available else 'Not Available'}")
    except (IndexError, ValueError):
        print("Invalid property number.")

#CHECK IN 
def checkin(username):
    clear_screen()  
    print("Available Properties:")
    for index, rental in enumerate(available_rentals):
        print(f"{index + 1}. {rental['name']}")

    try:
        choice = int(input("Enter the number of the property you want to check-in (or enter 0 to go back): "))
        if choice == 0:
            return
        rental = available_rentals[choice - 1]
        nights = int(input("Enter number of nights: "))
        checkin_day = input("Enter the day you want to check in (e.g., Monday): ").capitalize()
        total_cost = nights * rental['price_per_night']

        # Check availability for each night starting from the chosen check-in day
        current_day_index = list(rental['availability'].keys()).index(checkin_day)
        for i in range(nights):
            day_index = (current_day_index + i) % 7
            day = list(rental['availability'].keys())[day_index]
            if not rental['availability'][day]:
                print(f"Property not available on {day}.")
                return

        if total_cost > user_accounts[username]['money']:
            print("Insufficient balance.")
        else:
            user_accounts[username]['money'] -= total_cost

            # Update availability for each night starting from the chosen check-in day
            for i in range(nights):
                day_index = (current_day_index + i) % 7
                day = list(rental['availability'].keys())[day_index]
                rental['availability'][day] = False

            user_accounts[username]['properties'].append((rental, checkin_day, nights))
            print("Check-in successful!")
    except (IndexError, ValueError):
        print("Invalid property number or input.")

#CHECK OUT
def checkout(username):
    clear_screen()  
    print("Your Bookings:")
    for index, (property, checkin_day, nights) in enumerate(user_accounts[username]['properties']):
        print(f"{index + 1}. {property['name']} - Checked in on {checkin_day}, {nights} nights")
    try:
        choice = int(input("Enter the number of the property you want to check-out (or enter 0 to go back): "))
        if choice == 0:
            return
        rental, checkin_day, nights = user_accounts[username]['properties'][choice - 1]

        # Calculate the days stayed
        current_day_index = list(rental['availability'].keys()).index(checkin_day)
        days_stayed = [list(rental['availability'].keys())[(current_day_index + i) % 7] for i in range(nights)]

        # Calculate the refund amount based on the number of nights stayed
        refund_amount = (nights - len(days_stayed)) * rental['price_per_night']

        # Ask user for early checkout or based on paid nights
        checkout_choice = input("Do you want to check out early? (yes/no): ").lower()
        if checkout_choice == 'yes':
            # If user wants to check out early, update availability for checkin day
            rental['availability'][checkin_day] = True
            user_accounts[username]['money'] += refund_amount  # Refund the remaining nights
            print("Check-out successful! Refund amount: $", refund_amount)
        elif checkout_choice == 'no':
            # If user wants to check out based on paid nights, proceed with normal checkout
            # Update availability status for each night
            for day in days_stayed:
                rental['availability'][day] = True
            
            # Remove the property from user's bookings
            user_accounts[username]['properties'].remove((rental, checkin_day, nights))
            print("Check-out successful!")
        else:
            print("Invalid choice.")
    except (IndexError, ValueError):
        print("Invalid property number or input.")


#VIEW CURRENT BOOKINGS 
def bookings(username):
    clear_screen()  
    print("Your Bookings:")
    for index, (property, checkin_day, nights) in enumerate(user_accounts[username]['properties']):
        print(f"{index + 1}. {property['name']} - Checked in on {checkin_day}, {nights} nights")
        print("Days stayed:")
        current_day_index = list(property['availability'].keys()).index(checkin_day)
        days_stayed = [list(property['availability'].keys())[(current_day_index + i) % 7] for i in range(nights)]
        print(", ".join(days_stayed))

#ADD BALANCE TO USER
def balance(username):
    clear_screen()  
    print(f"Current balance: ${user_accounts[username]['money']}")
    choice = input("Do you want to top up your account? (yes/no): ").lower()
    if choice == 'yes':
        try:
            amount = int(input("Enter amount to top up: "))
            user_accounts[username]['money'] += amount
            print("Top up successful!")
        except ValueError:
            print("Invalid input. Amount must be a number.")
    elif choice != 'no':
        print("Invalid input. Please enter 'yes' or 'no'.")

#USER PROPERTY LISTING AND MANAGEMENT MENU
def properties(username):
    clear_screen()  
    print("User Property Listing and Management")
    print("1. Add Property")
    print("2. Modify Property")
    print("3. Delete Property")
    print("4. View Owned Properties")
    print("5. Back to Main Menu")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_property(username)
        elif choice == 2:
            modify_property(username)
        elif choice == 3:
            delete_property(username)
        elif choice == 4:
            view_own_properties(username)
        elif choice == 5:
            logged_in_menu(username)
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

#ADD USER PROPERTY
def add_property(username):
    while True:
        clear_screen()
        print("Adding a New Property")
        name = input("Enter property name: ")
        description = input("Enter property description: ")
        price_per_night = float(input("Enter price per night: "))
        location = input("Enter property location: ")

        # True initially
        availability = {day: True for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}

        # Add the property to available_rentals list
        available_rentals.append({
            'name': name,
            'description': description,
            'price_per_night': price_per_night,
            'location': location,
            'availability': availability,
            'host': username
        })
        print("Property added successfully.")
        
        input("Press Enter to continue.")
        properties(username)
        break

#MODIFY USER PROPERTY
def modify_property(username):
    clear_screen()
    print("Modifying Property")
    print("Your Properties:")
    user_properties = [property for property in available_rentals if property['host'] == username]
    for index, property in enumerate(user_properties):
        print(f"{index + 1}. {property['name']}")

    try:
        choice = int(input("Enter the number of the property you want to modify (or enter 0 to go back): "))
        if choice == 0:
            return
        property_index = available_rentals.index(user_properties[choice - 1])
        property = available_rentals[property_index]

        # Only allow modification of description, price_per_night, and location
        description = input("Enter new property description (leave blank to keep existing): ")
        if description:
            property['description'] = description

        price_per_night = input("Enter new price per night (leave blank to keep existing): ")
        if price_per_night:
            property['price_per_night'] = float(price_per_night)

        location = input("Enter new property location (leave blank to keep existing): ")
        if location:
            property['location'] = location

        print("Property modified successfully.")
    except (IndexError, ValueError):
        print("Invalid property number or input.")

#DELETE USER PROPERTY
def delete_property(username):
    clear_screen()
    print("Deleting Property")
    print("Your Properties:")
    user_properties = [property for property in available_rentals if property['host'] == username]
    for index, property in enumerate(user_properties):
        print(f"{index + 1}. {property['name']}")

    try:
        choice = int(input("Enter the number of the property you want to delete (or enter 0 to go back): "))
        if choice == 0:
            return
        property_index = available_rentals.index(user_properties[choice - 1])
        del available_rentals[property_index]
        print("Property deleted successfully.")
    except (IndexError, ValueError):
        print("Invalid property number or input.")

#VIEW OWN PROPERTY
def view_own_properties(username):
    clear_screen()
    print("Your Listed Properties:")
    user_properties = [property for property in available_rentals if property['host'] == username]
    for index, property in enumerate(user_properties):
        print(f"{index + 1}. Property Name: {property['name']}")
        print(f"   Description: {property['description']}")
        print(f"   Location: {property['location']}")
        print(f"   Price per Night: ${property['price_per_night']}")
        print("   Availability:")
        for day, available in property['availability'].items():
            print(f"      {day}: {'Available' if available else 'Not Available'}")
        print()  

    input("Press Enter to go back.")
    properties(username)


def main():
    while True:
        clear_screen()  
        print("Welcome to User Log-in and Sign-up Page")
        print("1. REGISTER USER")
        print("2. LOG IN USER")
        print("3. EXIT")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                register()
            elif choice == 2:
                user_log_in()
            elif choice == 3:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
