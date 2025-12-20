def pin_criteria(atm_pin):
    return (len(atm_pin) == 3 or len(atm_pin) == 4) and atm_pin.isdigit()

def get_stored_pin():
    with open("account.txt", "r") as f:
        for line in f:
            if line.startswith("PIN="):
                return line.strip().split("=")[1]

def check_pin(atm_pin):
    return atm_pin == get_stored_pin()

attempt = 3

while attempt>0:
    atm_pin = input("Enter your pin no: ")
    if not pin_criteria(atm_pin):
        print("Enter your pin consists of 3 to 4 digits")
        continue
    if check_pin(atm_pin):
        print("Your PIN is correct")
        break 
    else:
        attempt -=1
        print(f"Try Again, Attempts left out{attempt}")
else:
    print("Your Bank account is locked")