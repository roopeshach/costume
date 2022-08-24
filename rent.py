class Rent:
    def __init__(self, id, costume_name , costume_id, customer, rent_date, days, status):
        self.id = id
        self.costume_name = costume_name
        self.costume_id = costume_id
        self.customer = customer
        self.rent_date = rent_date
        self.days = days
        self.status = status
    def __str__(self):
        return f"{self.costume_name} - Rs. {self.costume_id}"
    
    def __repr__(self):
        return f"{self.costume_name} - Rs. {self.costume_id}"
    
    def get_costume_name(self):
        return self.costume_name
    
    def get_costume_id(self):
        return self.costume_id
    
    # auto increment id
    @staticmethod
    def get_next_id():
        with open("rent.txt", "r") as file:
            lines = file.readlines()
            if len(lines) == 0:
                return 1
            else:
                ids = []
                for line in lines:
                    ids.append(int(line.split(",")[0]))
                return max(ids) + 1
    
    # read from file and return all costumes
    @classmethod
    def read_from_file(cls):
        with open("rent.txt", "r") as file:
            lines = file.readlines()
            rents = []
            for line in lines:
                id, costume_name, costume_id, customer, rent_date, days, status = line.strip().split(",")
                rents.append(Rent(id, costume_name, costume_id, customer, rent_date, days, status))
            return rents


    # write to file
    def write_to_file(self):
        with open("rent.txt", "a") as file:
            file.write(f"{self.id},{self.costume_name},{self.costume_id},{self.customer},{self.rent_date},{self.days},{self.status}\n")
    
    # delete from file by id
    def delete_from_file(id):
        with open("rent.txt", "r") as file:
            lines = file.readlines()
            with open("rent.txt", "w+") as file:
                for line in lines:
                    if int(line.split(",")[0]) != int(id):
                        file.write(line)
    
    # update status
    def update_status(self, id, status):
        rents = Rent.read_from_file()
        with open("rent.txt", "w+") as file:
            for rent in rents:
                if int(rent.id) == int(id):
                    rent.status = status
                    file.write(f"{rent.id},{rent.costume_name},{rent.costume_id},{rent.customer},{rent.rent_date},{rent.days},{rent.status}\n")
                    return rent
        return None

    # get all rents
    def get_all_rents():
        rents = Rent.read_from_file()
        #print as table with borders
        print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("\nID", "Costume Name", "Costume ID", "Customer", "Rent Date", "Days", "Status\n"))
        for rent in rents:
            print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(rent.id, rent.costume_name, rent.costume_id, rent.customer, rent.rent_date, rent.days, rent.status))
        print("\n")
        print("Thank you for renting with us!")
        print("\n")

    #get rent by id
    def get_rent_by_id(id):
        rents = Rent.read_from_file()
        for rent in rents:
            if int(rent.id) == int(id):
                return rent
        return None
    

    #display invoice in List  format
    def display_invoice(self):

        print("Costume Rented\n")
        print("----------------------INVOICE-----------------------\n")

        print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "Costume Name", "Costume ID", "Customer", "Rent Date", "Days", "Status"))
        print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(self.id, self.costume_name, self.costume_id, self.customer, self.rent_date, self.days, self.status))
        print("\n")
        print("Thank you for renting with us!")
        print("Please return the costume on time!")
        print("Have a nice day!")
        print('\n')
