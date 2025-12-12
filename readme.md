
## 📁 File Structure

- **res** → Path to the restaurant CSV file
- **pri** → Path to the price CSV file
- **columns** → All columns inside the restaurant file
- **food_list** → List of all foods available

# 👤 `user_manger` Class
Handles all user-related operations.

### `file()`
Reads and returns the restaurant CSV file as a Pandas DataFrame.

### `create_user()`
Creates a new user with a username and password.
New users start with zero orders for all foods:

| username | password | Pizza | Burger | Pasta | Sushi | Kebab | taco | Salad | Steak | Sandwich | Chicken | qorme | rice | fish | total |
|:--------|:--------:|:-----:|:------:|:-----:|:-----:|:-----:|:----:|:-----:|:-----:|:--------:|:-------:|:-----:|:----:|:----:|------:|
| new user | new password | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

### `user_check()`
Checks if the user exists in the restaurant file.
Returns `True` or `False`.

### `user_update()`
Updates the user’s row after ordering food.

### `user_dict()`
Returns a dictionary with all user information.

### `show_user()`
Shows and returns the user information.

### `history_user()`
Returns a string of the user’s order history.

### `top_user`
Returns a dict of top customers as price

# 📦 `menu` Class
Handles menu display and price data.

### `show_menu()`
Returns the restaurant menu.

### `food_to_price(food_name)`
Returns the price of the given food.

### `convert_to_food(code)`
Converts a food code (1–13) to the corresponding food name.

### `total_ordered_food(code)`
- If `code == 0`: returns totals for all foods + total price.
- If `code != 0`: returns totals for the selected food.
"""