import os
from datetime import datetime

def system_menu():
    print("-------------------RESTAURANT RESERVATION SYSTEM----------------")
    print("                             System Menu                        ")
    print("a. Make Reservation")
    print("b. View Reservations")
    print("c. Update Reservation")
    print("d. Delete Reservation")
    print("e. Generate Report")
    print("f. Exit")
    print("---------------------------------------------------------------")

def make_reservation(reservations,directory):
    os.system('cls' if os.name == 'nt' else 'clear') 
    reservations = []
    print("Make Reservation")
    while True:
        try:
            name = input("Name: ")
            if not name:
                raise ValueError("Name cannot be empty")
            if not name.isalpha():
                raise ValueError("Name cannot contain number or special character")
            if len(name) < 3:
                raise ValueError("Name too short")
            break
        except ValueError as e:
            print(f"Invalid input. {e}")

    while True:
        try:
            date = input("Date (e.g., Jan 30, 2023): ")
            if not date:
                raise ValueError("Date cannot be empty")

            datetime.strptime(date, '%b %d, %Y')
            break
        except ValueError as e:
            print(f"Invalid input. {e}")

    while True:
        try:
            time = input("Time (e.g., 08:00 AM): ")

            if not time:
                raise ValueError("Time cannot be empty")

            datetime.strptime(time, '%I:%M %p')
            break
        except ValueError as e:
            print(f"Invalid input. {e}") 

    while True:
        try:
            num_adults = int(input("Enter Number of Adults: "))
            if num_adults < 0:
                raise ValueError("Number of adults cannot be negative.")
            if num_adults >= 10000:
                raise ValueError("Number too long.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            num_children = int(input("Enter Number of Children: "))
            if num_children < 0:
                raise ValueError("Number of children cannot be negative.")
            if num_children >= 10000:
                raise ValueError("Number too long.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    subtotal = (num_adults * 500) + (num_children * 250)

    last_id = 0
    file_path = os.path.join(directory, "reservations.txt")
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            for line in file:
                last_id = int(line.split('|')[0])

    reservation_id = last_id + 1
    reservation = {
        'id': reservation_id,
        'name': name,
        'date': date,
        'time': time,
        'num_adults': num_adults,
        'num_children': num_children,
        'subtotal': subtotal
    }

    reservations.append(reservation)
    save_to_file(reservations, directory)

    print("\nReservation added successfully!\n")
    input("Press Enter to continue...")

def save_to_file(reservations, directory):
    file_path = os.path.join(directory, "reservations.txt")
    with open(file_path, "a") as file:
        for reservation in reservations:
            file.write(f"{reservation['id']}|{reservation['date']}|{reservation['time']}|{reservation['name']}|{reservation['num_adults']}|{reservation['num_children']}|{reservation['subtotal']}\n")

def view_reservations(reservations,directory):
    reservations = load_from_file(directory)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("View Reservations\n")

    file_path = os.path.join(directory, "reservations.txt")

    if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
        print("--No reservations found.--\n")
        input("Press Enter to continue...")
        return

    print("{:<5} {:<20} {:<12} {:<25} {:<8} {:<8}".format("ID", "Date", "Time", "Name", "Adults", "Children"))
    print("-" * 85)

    for reservation in reservations:
        print("{:<5} {:<20} {:<12} {:<25} {:<8} {:<8}".format(
            reservation['id'],
            reservation['date'],
            reservation['time'],
            reservation['name'],
            reservation['num_adults'],
            reservation['num_children']
        ))

    print("\n Press Enter to back to menu...")
    input()

def update_file(reservation, directory):
    file_path = os.path.join(directory, "reservations.txt")
    reservations = load_from_file(directory)

    with open(file_path, "w") as file:
        for r in reservations:
            if r['id'] == reservation['id']:
                file.write(f"{reservation['id']}|{reservation['date']}|{reservation['time']}|{reservation['name']}|{reservation['num_adults']}|{reservation['num_children']}|{reservation['subtotal']}\n")
            else:
                file.write(f"{r['id']}|{r['date']}|{r['time']}|{r['name']}|{r['num_adults']}|{r['num_children']}|{r['subtotal']}\n")

def update_reservation(reservations, directory):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Update Reservation\n")
    reservations = load_from_file(directory)
    file_path = os.path.join(directory, "reservations.txt")

    if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
        print("--No reservations found.--\n")
        input("Press Enter to continue...")
        return

    print("{:<5} {:<20} {:<12} {:<25} {:<8} {:<8}".format("ID", "Date", "Time", "Name", "Adults", "Children"))
    print("-" * 85)

    for reservation in reservations:
        print("{:<5} {:<20} {:<12} {:<25} {:<8} {:<8}".format(
            reservation['id'],
            reservation['date'],
            reservation['time'],
            reservation['name'],
            reservation['num_adults'],
            reservation['num_children']
        ))

    try:
        update_id = int(input("\nEnter the ID of the reservation you want to update: "))
    except ValueError:
        print("Invalid input. Please enter a valid ID.")
        input("Press Enter to continue...")
        return

    reservation_found = False
    for reservation in reservations:
        if reservation['id'] == update_id:
            reservation_found = True
            print("\nExisting Reservation Details:")
            print("{:<5} {:<15} {:<12} {:<20} {:<8} {:<8}".format("ID", "Date", "Time", "Name", "Adults", "Children"))
            print("-" * 85)
            print("{:<5} {:<15} {:<12} {:<20} {:<8} {:<8}".format(
                reservation['id'],
                reservation['date'],
                reservation['time'],
                reservation['name'],
                reservation['num_adults'],
                reservation['num_children']
            ))
            print("-" * 85)

            print("\nEnter New Details:")

            while True:
                try:
                    name = input("Name: ")
                    if not name:
                        raise ValueError("Name cannot be empty")
                    if not name.isalpha():
                        raise ValueError("Name cannot contain number or special character")
                    if len(name) < 3:
                        raise ValueError("Name too short")
                    break
                except ValueError as e:
                    print(f"Invalid input. {e}")

            while True:
                try:
                    date = input("Date (e.g., Jan 30, 2023): ")
                    if not date:
                        raise ValueError("Date cannot be empty")

                    datetime.strptime(date, '%b %d, %Y')
                    break
                except ValueError as e:
                    print(f"Invalid input. {e}")

            while True:
                try:
                    time = input("Time (e.g., 08:00 AM): ")

                    if not time:
                        raise ValueError("Time cannot be empty")

                    datetime.strptime(time, '%I:%M %p')
                    break
                except ValueError as e:
                    print(f"Invalid input. {e}") 

            while True:
                try:
                    num_adults = int(input("Enter Number of Adults: "))
                    if num_adults < 0:
                        raise ValueError("Number of adults cannot be negative.")
                    if num_adults >= 10000:
                        raise ValueError("Number too long.")
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            while True:
                try:
                    num_children = int(input("Enter Number of Children: "))
                    if num_children < 0:
                        raise ValueError("Number of children cannot be negative.")
                    if num_children >= 10000:
                        raise ValueError("Number too long.")
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            subtotal = (num_adults * 500) + (num_children * 250)

            reservation['date'] = date
            reservation['time'] = time
            reservation['name'] = name
            reservation['num_adults'] = num_adults
            reservation['num_children'] = num_children
            reservation['subtotal'] = subtotal

            update_file(reservation, directory)

            print("\nReservation updated successfully!\n")
            view_reservations(reservations,directory)

    if not reservation_found:
        print(f"No reservation found with ID {update_id}.\n")
        input("Press Enter to continue...")

def delete_file(reservation, directory):
    file_path = os.path.join(directory, "reservations.txt")
    reservations = load_from_file(directory)

    with open(file_path, "w") as file:
        for r in reservations:
            if r['id'] != reservation['id']:
                file.write(f"{r['id']}|{r['date']}|{r['time']}|{r['name']}|{r['num_adults']}|{r['num_children']}|{r['subtotal']}\n")

def delete_reservation(reservations, directory):
    os.system('cls' if os.name == 'nt' else 'clear')
    reservations = load_from_file(directory)
    print("Delete Reservation\n")

    file_path = os.path.join(directory, "reservations.txt")

    if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
        print("--No reservations found.--\n")
        input("Press Enter to continue...")
        return

    print("{:<5} {:<20} {:<12} {:<25} {:<8} {:<8}".format("ID", "Date", "Time", "Name", "Adults", "Children"))
    print("-" * 85)

    for reservation in reservations:
        print("{:<5} {:<20} {:<12} {:<25} {:<8} {:<8}".format(
            reservation['id'],
            reservation['date'],
            reservation['time'],
            reservation['name'],
            reservation['num_adults'],
            reservation['num_children']
        ))

    try:
        delete_id = int(input("\nEnter the ID of the reservation you want to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid ID.")
        input("Press Enter to continue...")
        return

    reservation_found = False

    for reservation in reservations:
        if reservation['id'] == delete_id:
            reservation_found = True
            print("\nReservation to Delete:")
            print("{:<5} {:<15} {:<12} {:<20} {:<8} {:<8}".format("ID", "Date", "Time", "Name", "Adults", "Children"))
            print("-" * 85)
            print("{:<5} {:<15} {:<12} {:<20} {:<8} {:<8}".format(
                reservation['id'],
                reservation['date'],
                reservation['time'],
                reservation['name'],
                reservation['num_adults'],
                reservation['num_children']
            ))
            print("-" * 85)

            confirmation = input("Do you really want to delete this reservation? (yes/no): ").lower()
            if confirmation == 'yes':
                print(f"\nReservation with ID {delete_id} deleted successfully!\n")
                delete_file(reservation, directory)
                view_reservations(reservations,directory)
            else:
                print(f"\nDeletion of reservation with ID {delete_id} canceled.\n")
                return

    if not reservation_found:
        print(f"No reservation found with ID {delete_id}.\n")
        input("Press Enter to continue...")

def generate_report(reservations, directory):
    os.system('cls' if os.name == 'nt' else 'clear')

    report_title = "---------------------------------------REPORT---------------------------------------"
    print(f"{report_title}")
    print("{:<2} {:<18} {:<8} {:<25} {:<6} {:<9} {:<4}".format("ID", "Date", "Time", "Name", "Adults", "Children", "Subtotal"))

    reservations = load_from_file(directory)
    if not reservations:
        print("\nNo reservations found.\n")
        input("Press Enter to continue...")
        return

    total_adults = 0
    total_children = 0
    grand_total = 0

    for i, reservation in enumerate(reservations, start=1):
        print(f"{i:<2} {reservation['date']:<18} {reservation['time']:<8} {reservation['name']:<25} {reservation['num_adults']:<6} {reservation['num_children']:<9} {reservation['subtotal']:.2f}")
        total_adults += reservation['num_adults']
        total_children += reservation['num_children']
        grand_total += reservation['subtotal']

    print(f"\nTotal number of adults: {total_adults}")
    print(f"Total number of Kids: {total_children}")
    print(f"Grand Total: PHP {grand_total:.2f}")
    
    print("----------------------------------nothing follows----------------------------------")

    print("\nPress Enter to back to the menu...")
    input()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    directory = os.getcwd()
    if not os.path.exists(directory):
        os.makedirs(directory)
    reservations = []
    while True:
        system_menu()
        choice = input("Enter your choice: ").lower()

        if choice == 'a':
            make_reservation(reservations,directory)
        elif choice == 'b':
            view_reservations(reservations, directory)
        elif choice == 'c':
            update_reservation(reservations, directory)
        elif choice == 'd':
            delete_reservation(reservations,directory)
        elif choice == 'e':
            generate_report(reservations,directory)
        elif choice == 'f':
            save_to_file(reservations,directory)
            print("Thank you for using the RESERVATION SYSTEM!")
            break
        else:
            input("Invalid choice. Please try again.")
            os.system('cls' if os.name == 'nt' else 'clear') 

def load_from_file(directory):
    file_path = os.path.join(directory, "reservations.txt")
    
    if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
        return []
    
    reservations = []
    with open(file_path, 'r') as file:
        # next(file)
        for line in file:
            # print(line)
            id, date, time, name, adults, children, subtotal = line.strip().split('|')
            reservation = {
                'id': int(id),
                'date': date,
                'time': time,
                'name': name,
                'num_adults': int(adults),
                'num_children': int(children),
                'subtotal': float(subtotal)
            }
            reservations.append(reservation)
    
    return reservations

if __name__ == "__main__":
    main()
