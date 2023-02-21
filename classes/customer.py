from csv import DictReader

class Customer: 
    def __init__(self, **kwargs) -> None:
        self.id = kwargs['id']
        self.account_type = kwargs['account_type']
        self.first_name = kwargs['first_name']
        self.last_name = kwargs['last_name']
        self.current_video_rentals = kwargs['current_video_rentals']

    @classmethod 
    def load_customers_from_csv(cls) :
        customer_list = []
        with open('./data/customers.csv') as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                new_customer = cls(**row)
                customer_list.append(new_customer)
        return customer_list

    def update_current_video_rentals(self, new_current_video_rentals):
        self.current_video_rentals = new_current_video_rentals
        
    def __str__(self) -> str:
         return f"Id: {self.id} -- Account type: {self.account_type} -- First name: {self.first_name} -- Last name: {self.last_name}"
        