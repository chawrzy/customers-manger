from classes import user_manger , menu
um = user_manger()
m = menu()

print("--- welcome to restaurant ---")
print("if you have not sing in it will automatically create new account for you!")
username = input("Enter your username: ")
password = input("Enter your password: ")
if um.check_user(username, password):
    print(f"welcome back {username}")
else:
    print("your account is created")
while True:
    print("-----------------------------------------")
    print("how can i help you?")
    print("[1] show your info\n[2] show your order history\n[3] order new food\n[4] quit")
    user_input = int(input("Enter your choice: "))
    match user_input:
        case 1 :
            print("i will show your info")
            user_info = um.show_user(username , password)
            print(f"username: {user_info['username']}\ntotal price: {user_info['totally']}$")
            print("-----------------------------------------")
        case 2 :
            print("i will show your order history")
            print(um.history_user(username , password ))
            print("-----------------------------------------")
        case 3 :
            print("ok! you want to order new food")
            print(m.show_menu())
            user_food_order = int(input("Enter your food code : "))
            user_food_order_count = int(input("how many orders do you have? : "))
            um.user_update(username , password , user_food_order , user_food_order_count)
            print("Your order has been placed!")
            print("-----------------------------------------")
        case 4 :
            user_quit = input("Do you want to quit?:(y/n) ").lower()
            if user_quit == "y":
                break
