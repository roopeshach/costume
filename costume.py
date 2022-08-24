class Costume:
    def __init__(self, id, name, brand, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.brand = brand
        self.stock = stock

    def __str__(self):
        return f"{self.name} - Rs. {self.price}"
    
    def __repr__(self):
        return f"{self.name} - Rs. {self.price}"

    def remove_stock(self, amount):
        self.stock -= amount
        return self.stock
    
    def get_stock(self):
        return self.stock
    
    def get_price(self):
        return self.price
    
    def write_to_file(self):
        with open("costumes.txt", "a") as file:
            file.write(f"{self.id},{self.name},{self.brand},{self.price},{self.stock}\n")

    #auto increment id
    @staticmethod
    def get_next_id():
        with open("costumes.txt", "r") as file:
            lines = file.readlines()
            if len(lines) == 0:
                return 1
            else:
                ids = []
                for line in lines:
                    ids.append(int(line.split(",")[0]))
                return max(ids) + 1
    
    #read from file and return all costumes
    def read_from_file():
        with open("costumes.txt", "r") as file:
            lines = file.readlines()
            costumes = []
            for line in lines:
                id, name, brand, price, stock = line.strip().split(",")
                costumes.append(Costume(id, name, brand, price, stock))
            return costumes


    #delete from file by id 
    def delete_from_file( id):
        with open("costumes.txt", "r") as file:
            lines = file.readlines()    
            with open("costumes.txt", "w+") as file:
                for line in lines:
                    if line.split(",")[0] != id:
                        file.write(line)
            

                
    def get_costume_by_id( id):
        costumes = Costume.read_from_file()
        for costume in costumes:
            if int(costume.id) == int(id):
                return costume
        return None

    #update stock
    def update_stock(self, id, stock):
        costumes = Costume.read_from_file()
        with open("costumes.txt", "w+") as file:
            for costume in costumes:
                if int(costume.id) == int(id):
                    costume.stock = stock
                file.write(f"{costume.id},{costume.name},{costume.brand},{costume.price},{costume.stock}\n")