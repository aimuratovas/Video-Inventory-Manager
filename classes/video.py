from classes.customer import Customer
from classes.inventory import Inventory


class Video:
    def __init__(self, name):
        self.name = name
        self.inventories = Inventory.load_video_inventory_from_csv()
        self.customers = Customer.load_customers_from_csv()
    
    def view_video_inventory(self):
        for item in self.inventories:
            print("Title: " + item.title + " -- Copies available: " + item.copies_available + "\n")

    def view_all_customers(self):
        for item in self.customers:
            print("Id: " + item.id + " -- Name: " + item.first_name + "\n")

    def view_customer_rented_videos(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                if customer.current_video_rentals == "":
                    return "Customer does not have rented videos"
                
                customer_ls = customer.current_video_rentals.split("/")
                print("Current rented videos: \n")
                for item in customer_ls:
                    print(item + '\n')
                return ""
        return 'No customer found by given id'
    
    def add_customer(self, new_customer):
        for customer in self.customers:
            if customer.id == new_customer["id"]:
                print("Id already exists. Enter different id.")
                return ""

        account_types = ['sx', 'px', 'sf', 'pf']
        if new_customer["account_type"] not in account_types:
            print(new_customer["account_type"] + " is not valid account type. Please enter valid one")
            return ""

        self.customers.append(Customer(**new_customer))
        print("New customer entry is created. Updated new customer list: ")
        
        for item in self.customers:
            print(str(item))
        return self.customers
    
    def rent_video_to_customer(self, video_title, customer_id):
        ls = []
        for inventory in self.inventories: 
            if inventory.title == video_title:
                count_copies_available = inventory.copies_available
                if count_copies_available == 0:
                    return "No video copies available to rent"
                ls.append(inventory)
                break
        
        if len(ls) != 1:
            return "No inventory found for given video title"
        
        for customer in self.customers:
            if customer.id == customer_id:
                if customer.account_type == "sx":
                    count_sx = len(customer.current_video_rentals.split('/'))
                    if customer.current_video_rentals == "":
                     count_sx = 0
                    if count_sx >= 1: 
                        return "Out of limit. Can't rent a video"
                    else:
                        return self.update_customer_and_inventory_rent_video(customer, inventory)

                elif customer.account_type == "px":
                    check_px = len(customer.current_video_rentals.split('/'))  
                    if check_px >= 3:
                        return "Out of limit. Can't rent a video" 
                    else:
                        return self.update_customer_and_inventory_rent_video(customer, inventory)

                elif customer.account_type == "sf":
                    check_sf = len(customer.current_video_rentals.split('/'))  
                    if check_sf >= 1: 
                        return "Out of limit. Can't rent a video" 
                    else:
                        if  inventory.rating == "R":
                            return "Cannot rent R rated video"
                        else:
                            return self.update_customer_and_inventory_rent_video(customer, inventory) 

                elif customer.account_type == "pf":
                    check_pf = len(customer.current_video_rentals.split('/')) 
                    if check_pf >= 3:
                        return "Out of limit. Can't rent a video"  
                    else:
                        if  inventory.rating == "R":
                            return "Cannot rent R rated video"
                        else:
                            return self.update_customer_and_inventory_rent_video(customer, inventory)
        return ""

    def update_customer_and_inventory_rent_video(self, customer, inventory):
        updated_video_rentals = customer.current_video_rentals + "/" + inventory.title
        if customer.current_video_rentals == "":
            updated_video_rentals = inventory.title
        
        updated_inventory_copies = int(inventory.copies_available) - 1

        inventory.update_copies_available(str(updated_inventory_copies))
        customer.update_current_video_rentals(updated_video_rentals)

        print("Rented video. Updated customer and inventory.")

    def return_video_from_customer(self, customer_id, video_title):
        for customer in self.customers:
            if customer.id == customer_id:
                rentals_list = customer.current_video_rentals.split('/')
                for title in rentals_list: 
                    if video_title == title: 
                        rentals_list.remove(title)
                        updated_rental_list = ("/").join(rentals_list)
                        customer.update_current_video_rentals(updated_rental_list)
                        print("Updated customer video rentals: " + self.view_customer_rented_videos(customer_id))
        
        for inventory in self.inventories: 
            if inventory.title == video_title:
                updated_inventory_copies = int(inventory.copies_available) + 1
                inventory.update_copies_available(str(updated_inventory_copies))
                print("Updated inventory available copies: " + str(inventory))
        return ""

