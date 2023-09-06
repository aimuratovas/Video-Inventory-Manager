# Write your solution here!
from classes.video import Video

video = Video('== Welcome to Video Inventory Manager! ==')

print(video.name)

prompt = """ 
What would you like to do? 
Options:
    1. View store video inventory
    2. View store customers
    3. View customer rented videos
    4. Add new customer
    5. Rent video
    6. Return video
    7. Exit
"""

while(True):

    try: 
        mode = int(input(prompt))
    except ValueError:
        print('invalid input, please enter a valid number ')
        continue

    if mode == 1:
        video.view_video_inventory()
        
    elif mode == 2:
        video.view_all_customers()
   
    elif mode == 3:
        try:
            id = input('Please enter the cusomer\'s ID \n')
        except ValueError:
            print('invalid input, please enter a valid id number ')
        print(video.view_customer_rented_videos(id))

    elif mode == 4:
        new_customer = {}
        new_customer['id'] = input('Id: ')
        new_customer['account_type'] = input('Account type. Choose from sx, px, sf, pf: ')
        new_customer['first_name'] = input('First name: ')
        new_customer['last_name'] = input('Last name: ')
        new_customer['current_video_rentals']= ""

        video.add_customer(new_customer)
    elif mode == 5:
        video_title = input('Enter video title: ')
        customer_id = input('Enter customer id: ')
        print(video.rent_video_to_customer(video_title, customer_id))

    elif mode == 6:
        customer_id = input('Enter customer id: ')
        video_title = input('Enter video title: ')
        print(video.return_video_from_customer(customer_id, video_title))

    elif mode == 7:
        break     