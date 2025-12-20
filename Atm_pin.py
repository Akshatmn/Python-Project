# # name = input("Enter your name")
# # print(f"Welcome {name}, to this adventure!")

# # answer = input("You are on a dirt road, you can got to left or right, Which way would you like to go").lower()


# # pwd = input("What is the master password: ")

# # def view():
# #     with open('password.txt','r') as f:
# #         for line in r.readlines()

# # def add():
# #     name = input("Account Name: ")
# #     newpwd =input("password: ")

# #     with open('password.txt','a') as f:
# #         f.write(name + " " + newpwd)


# # while True:
# #     mode = input("Would you like to add a new pasword or view existing OR press q to quit: " ).lower()

# #     if mode == "q":
# #         break

# #     if mode == "view":
# #         view()
# #     elif mode == "add":
# #         add()
# #     else:
# #         print("Invalid mode.")
# #         continue



# import random 
# OPERATOR = []
# MIN_OPERAND = 3
# MAX_OPERAND = 12

# def generate_problem():
#     left = random.randint(MIN_OPERAND, MAX_OPERAND)
#     right = random.randint(MIN_OPERAND, MAX_OPERAND)


# import random

# def play():
#     user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
#     computer = random.choice(['r', 'p', 's'])

#     print(f"Computer chose: {computer}")

#     if user == computer:
#         return "It's a tie"
    
#     if is_win(user, computer):
#         return "You won!"
    
#     return "Sorry, you lost"


# def is_win(player, opponent):
#     # return True if player wins
#     # r > s, s > p, p > r
#     if (player == 'r' and opponent == 's') or \
#        (player == 's' and opponent == 'p') or \
#        (player == 'p' and opponent == 'r'):
#         return True
#     return False


# print(play())



im