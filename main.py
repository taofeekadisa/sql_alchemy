from models import Base, User, Expenses
from database import engine, session
import pprint

Base.metadata.create_all(engine)

# #Create user

# user1 = User(
#     first_name = "Desayo",
#     last_name = "Labaeka",
#     country = "Nigeria",
#     city = "Lagos",
#     phone_number = "+23216545",
#     password = "mypass"
#     # expenses = [user1_expense]
# )

# # user2 = User(
# #     first_name = "John",
# #     last_name = "Doe",
# #     country = "Ghana",
# #     city = "Accra",
# #     phone_number = "+2331233",
# #     password = "mypass"
# # )

# session.add(user1)
# session.commit()


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
user = session.query(User).filter_by(id=1).first()
pprint.pprint(user.expenses)

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