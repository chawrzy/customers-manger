from classes import user_manger , menu
import sys
um = user_manger()
m = menu()
while True:
        print("--- welcome to restaurant ---")
        print("if you have not sing in it will automatically create new account for you!")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username != "admin" and password != "admin":
            if um.check_user(username, password):
                print(f"welcome back {username}")
            else:
                print("your account is created")

        if username != "admin" and password != "admin":
            while True:
                print("-----------------------------------------")
                print("how can i help you?")
                print("[1] show your info\n[2] show your order history\n[3] order new food\n[4] logout\n[5] quit")
                user_input = int(input("Enter your choice: "))
                print("-----------------------------------------")
                match user_input:
                    case 1 :
                        print("i will show your info")
                        user_info = um.show_user(username , password)
                        print(f"username: {user_info['username']}\ntotal price: {user_info['totally']}$")

                    case 2 :
                        print("i will show your order history")
                        print(um.history_user(username , password ))

                    case 3 :
                        print("ok! you want to order new food")
                        print(m.show_menu())
                        user_food_order = int(input("Enter your food code : "))
                        user_food_order_count = int(input("how many orders do you have? : "))
                        um.user_update(username , password , user_food_order , user_food_order_count)
                        print("Your order has been placed!")

                    case 4 :
                        break
                    case 5:
                        sys.exit()

        else:
            while True:
                print("-----------------------------------------")
                print("--- admin panel ---")
                print("how can i help you?")
                print("[1] show total ordered\n[2] top customers\n[3] show menu\n[4] logout\n[5] quit")
                user_input = int(input("Enter your choice: "))
                print("-----------------------------------------")
                match user_input:
                    case 1 :
                        print("[1] show all food total\n[2] show specific total")
                        admin_input = int(input("Enter your choice: "))
                        match admin_input:
                            case 1 :
                                print(m.total_ordered_food(0))
                            case 2 :
                                print(m.show_menu())
                                food_total_input = int(input("Enter your food code : "))
                                print(m.total_ordered_food(food_total_input))
                    case 2 :
                        i = 0
                        for keys , values in um.top_user().items():
                            print(f"{keys}: {values}$")
                            i += 1
                            if i == 3 :
                                break
                    case 3 :
                        m.show_menu()
                    case 4:
                        break
                    case 5 :
                        sys.exit()