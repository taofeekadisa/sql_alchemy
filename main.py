from models import Base, Customer, Vendor, Admin, Order, OrderItem, product_promotion, Product, Category

from models import Payment, Cart, CartItem, Shipping, CustomerAddress, Inventory, Review, Promotion
from database import engine, session
import pprint

Base.metadata.create_all(engine)

#Create Customer

# user1 = Customer(
#     first_name = "Daniel",
#     last_name = "Alaga",
#     username = "danla",
#     email = "dan@dan.com",
#     phone_number = "+23565485",
#     password_hash = "mypass"
# )

# user2 = Customer(
#     first_name = "Mike",
#     last_name = "Kone",
#     username = "kona",
#     email = "kon@dan.com",
#     phone_number = "+23565485654",
#     password_hash = "mypass2"
# )

# session.add_all([user1, user2])
# session.commit()


# user5 = Customer(
#     first_name = "Ade",
#     last_name = "Kunle",
#     username = "kunle.ade",
#     email = "ade@dan.com",
#     phone_number = "+23565485894",
#     password_hash = "mypass3"
# )

kona = session.query(Customer).filter_by(email='kon@dan.com').first()

# useraddress3 = CustomerAddress (
#     residence_number = 101,
#     customer = user3,
#     street = "Olasunkanmi Street",
#     city = "Lagos",
#     postal_code = "1200-101",
#     country = "Nigeria",
#     description = "Na my addres be this o"
# )

# useraddress4 = CustomerAddress (
#     residence_number = 190,
#     customer = kona,
#     street = "Johnson Street",
#     city = "Lagos",
#     postal_code = "14568-90",
#     country = "Nigeria",
#     description = "Na my forth address be this o"
# )

# useraddress5 = CustomerAddress (
#     residence_number = 190,
#     customer = kona,
#     street = "Johnson Street",
#     city = "Lagos",
#     postal_code = "14568-90",
#     country = "Nigeria",
#     description = "Na my forth address be this o"
# )

# session.add_all([useraddress4, useraddress5])
# session.commit()


# Create product category

# cat1 = Category(
#     name = "big appliances",
#     parentcategory = "appliances"
# )

# cat2 = Category(
#     name = "small appliances",
#     parentcategory = "appliances"
# )

# cat3 = Category(
#     name = "home appliances",
#     parentcategory = "appliances"
# )

# session.add_all([cat1, cat2, cat3])
# session.commit()

# Create vendors

vendor1 = Vendor(
    first_name = "xys",
    last_name = "enterprises",
    username = "xyz_enterprise",
    email = "xyz@dan.com",
    phone_number = "+2356546",
    address = "123, Alaba international market",
    password_hash = "mypass"
)

vendor2 = Vendor(
    first_name = "Mike",
    last_name = "electronics",
    username = "mike_igwe",
    email = "mike.igwe@dan.com",
    phone_number = "+235564654",
    address = "125, computer village, Ikeja, Lagos",
    password_hash = "mypass2"
)

session.add_all([vendor1, vendor2])
session.commit()

# #Add an expense
# user1_expense = Expenses(
#     user_id = 1,
#     title = "Trip to lasgidi",
#     description = "My ntrip to lasgidi",
#     amount = 200202.54
# )
# session.add(user1_expense)
# session.commit()


# # #Read all  Users
# users = session.query(User).all()
# for user in users:
#     print(user)
    
# # #Read single user
# user = session.query(User).filter_by(id=1).first()
# pprint.pprint(user.expenses)

# expense = session.query(Expenses).filter_by(id=1).first()
# print(expense.user)

# # #Update single user
# user = session.query(User).filter_by(id=2).first()

# user.city = "Enugu"
# user.country = "Nigeria"
# user.phone_number = "+23454565467"

# session.commit()

# #Delete Users
# user = session.query(User).filter_by(id=3).first()

# session.delete(user)
# session.commit()




    



# print(users)