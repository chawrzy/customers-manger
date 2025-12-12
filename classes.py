import pandas as pd
from selenium.webdriver.support.expected_conditions import none_of

res = "./csv/restaurant.csv"
pri = "./csv/prices.csv"
columns = [
    "username", "password", "Pizza", "Burger", "Pasta", "Sushi", "Kebab", "taco",
    "Salad", "Steak", "Sandwich", "Chicken", "qorme", "rice", "fish", "total"
]
foods_list = [
    "Pizza", "Burger", "Pasta", "Sushi", "Kebab", "taco",
    "Salad", "Steak", "Sandwich", "Chicken", "qorme", "rice", "fish"
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
            if info.username == username and info.password == password:
                return True
        self.create_user(username, password)
        return False

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

    def top_user(self):
        df = self.file()
        result = {}
        for name, total in zip(df["username"], df["total"]):
            result[name] = total
        result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1] , reverse=True)}
        return result

class menu():
    def show_menu(self):
        df = pd.read_csv(pri)
        menu = ""
        i = 1
        for head in df.head():
            menu += f"[{i}] {head} : {df[head].loc[0]}$\n"
            i += 1
        return menu

    def food_to_pricec(self, food):
        df = pd.read_csv(pri)
        return df[food].loc[0]

    def total_ordered_food(self, food_code):
        df = user_manger().file()
        dfp = pd.read_csv(pri)
        total_dict = {}
        total_income = 0
        for food in foods_list:
            total_dict[food] = int(df[food].sum())
        total_dict = dict(sorted(total_dict.items(), key=lambda item: item[1]))
        if food_code == 0:
            total_str = ""
            for key, value in total_dict.items():
                total_str += f"{key} : {value} * {int(dfp[key].iloc[0])}$\n"
                total_income += value * int(dfp[key].iloc[0])
            return f"{total_str}-----------------\ntotal incoming : {total_income}$"
        else :
            food_name = self.convert_to_food(food_code)
            total_count = total_dict[food_name]
            price = int(dfp[food_name].iloc[0])
            return f"{food_name} * {price} : {total_count * price}$"

    def convert_to_food(self, food_code):
        match food_code:
            case 1:
                return "Pizza"
            case 2:
                return "Burger"
            case 3:
                return "Pasta"
            case 4:
                return "Sushi"
            case 5:
                return "Kebab"
            case 6:
                return "taco"
            case 7:
                return "Salad"
            case 8:
                return "Steak"
            case 9:
                return "Sandwich"
            case 10:
                return "Chicken"
            case 11:
                return "qorme"
            case 12:
                return "rice"
            case 13:
                return "fish"
            case _:
                return "invalid food code"