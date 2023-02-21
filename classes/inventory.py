from csv import DictReader

class Inventory:
    def __init__(self, **kwargs) -> None:
        self.id = kwargs["id"]
        self.title = kwargs["title"]
        self.rating = kwargs["rating"]
        self.release_year = kwargs["release_year"]
        self.copies_available = kwargs["copies_available"]

    @classmethod
    def load_video_inventory_from_csv(cls):
        video_inventory_list = []
        with open('./data/inventory.csv') as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                new_list = cls(**row)
                video_inventory_list.append(new_list)
        return video_inventory_list

    def update_copies_available(self, new_copies_available):
        self.copies_available = new_copies_available
    
    def __str__(self) -> str:
         return f"Id: {self.id} -- Title: {self.title} -- Rating: {self.rating} -- Release year: {self.release_year} -- Copies available: {self.copies_available}"