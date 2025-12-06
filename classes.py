

import pandas as pd

res = "./csv/restaurant.csv"
pri = r"C:\Users\hesam\Desktop\PY\pyprj1\csv\prices.csv"
columns = [
    "username", "password", "Pizza", "Burger", "Pasta", "Sushi", "Kebab", "taco",
    "Salad", "Steak", "Sandwich", "Fried Chicken", "qorme sabzi", "rice", "fish", "total"
]
class user_manger():

    def file(self):
        return pd.read_csv(res)

    def create_user(self, username, password):

        values = [username, password] + ["0"] * (len(columns) - 2)
        user_line = ",".join(values) + "\n"

        with open(res, "a", newline="") as f:
            f.write(user_line)
        return values

    def check_user(self, username, password):
        df = self.file()
        for info in df.itertuples():
            if info.username != username and info.password != password:
                self.create_user(username, password)
                return False
        return True

    def user_update(self , username, password , food_code , food_count):
        df = self.file()
        m = menu()
        food = m.convert_to_food(food_code)
        price = m.food_to_pricec(food)
        df[food] = df[food].astype(int)
        df.loc[(df["username"] == username) & (df["password"] == password), food] += food_count
        df.loc[(df["username"] == username) & (df["password"] == password), "total"] += food_count*price
        df.to_csv(res , index = False)

    def user_dict(self, username, password):
        df = self.file()
        for info in df.itertuples():
            if info.username == username and info.password == password:
                return info._asdict()

    def show_user(self, username, password):
        df = self.file()
        for info in df.itertuples():
            if info.username == username and info.password == password:
                return {
                    "username": info.username,
                    "totally": info.total
                }

    def history_user(self, username, password):
        df = self.file()
        foods = pd.read_csv(pri)
        foods_list = foods.columns.tolist()
        user_info = self.user_dict(username, password)
        food_history_dict = {}
        for key, value in user_info.items():
            if key in foods_list:
                food_history_dict[key] = value
        food_history_str = ""
        m = menu()
        for key , values in food_history_dict.items():
            food_history_str += f"{key} : {values} * {m.food_to_pricec(key)}\n"
        return food_history_str

class menu():
    def show_menu(self):
        df = pd.read_csv(pri)
        menu = ""
        i = 0
        for head in df.head():
            menu += f"[{i}] {head} : {df[head].loc[0]}$\n"
            i += 1
        return menu

    def food_to_pricec(self, food):
        df = pd.read_csv(pri)
        return df[food].loc[0]

    def convert_to_food(self, food_code):
        match food_code:
            case 0:
                return "Pizza"
            case 1:
                return "Burger"
            case 2:
                return "Pasta"
            case 3:
                return "Sushi"
            case 4:
                return "Kebab"
            case 5:
                return "taco"
            case 6:
                return "Salad"
            case 7:
                return "Steak"
            case 8:
                return "Sandwich"
            case 9:
                return "Fried Chicken"
            case 10:
                return "qorme sabzi"
            case 11:
                return "rice"
            case 12:
                return "fish"
            case _:
                return "invalid food code"