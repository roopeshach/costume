#text file based system for costume rental

import os
from costume import Costume
from rent import Rent

#menu based costume rental system   
def menu():
    print("1. Add a new costume")
    print("2. View all costumes")
    print("3. Rent a costume")
    print("4. View all rentals")
    print("5. Return rental")
    print("6. Exit\n")
    choice = input("What would you like to do? ")
    return choice

def add_costume():
    name = input("What is the name of the costume? ")
    brand = input("What is the brand of the costume? ")
    price = input("What is the price of the costume? ")
    stock = input("How many are in stock? ")
    id = Costume.get_next_id()
    costume = Costume(id, name, brand, price, stock)
    costume.write_to_file()
    print(costume)

def view_costumes():
    costumes = Costume.read_from_file()
    #display as table with borders and
    print("{:<5} {:<20} {:<20} {:<20} {:<20}".format("ID", "Name", "Brand", "Price", "Stock\n"))
    for costume in costumes:
        print("{:<5} {:<20} {:<20} {:<20} {:<20}".format(costume.id, costume.name, costume.brand, costume.price, costume.stock + "\n"))

def rent_costume():
    customer = input("What is the name of the customer? ")
    rent_date = input("What is the rent date? ")
    days = input("How many days is the rental? ")
    # limit days to 1-5
    while int(days) < 1 or int(days) > 5:
        print("Invalid number of days")
        days = input("How many days is the rental? ")
    
    costume_id = input("What is the id of the costume? ")
    costume = Costume.get_costume_by_id(costume_id)
    if costume is None:
        print("No costume found with this id")
        return
    if int(costume.stock) == 0:
        print("No stock available")
        return
    costume.stock = int(costume.stock) - 1
    costume.update_stock(costume_id, costume.stock)

    id = Rent.get_next_id()
    status = "Rented"
    rent = Rent(id, costume.name, costume.id, customer, rent_date, days, status)
    rent.write_to_file()
    rent.display_invoice()




#main function with exception handling
def return_rental():
    id = input("What is the id of the rental? ")
    rent = Rent.get_rent_by_id(id)
    if rent is None:
        print("No rental found with this id\n")
        return
    rent.status = "Returned"
    rent.update_status(id, rent.status)
    costume = Costume.get_costume_by_id(rent.costume_id)
    costume.stock = int(costume.stock) + 1
    costume.update_stock(costume.id, costume.stock)
    print("Rental returned\n\n")


def main():
    while True:
        # try:
        choice = menu()
        if choice == "1":
            add_costume()
        elif choice == "2":
            view_costumes()
        elif choice == "3":
            rent_costume()
        elif choice == "4":
            Rent.get_all_rents()
        elif choice == "5":
            return_rental()
        elif choice == "6":
            break
        else:
            print("Invalid choice")
        # except Exception as e:
        #     print(e)
        #     print("Invalid choice")
        #     continue    
        
if __name__ == "__main__":
    main()
    print("Thanks for using our costume rental system")