# while True:
#     input_text = """
# What would you like ? (expresso/latte/cappuccino):
# 1.report
# 2.latte
# 3.expresso
# 4.cappuccino

#     """

# choice = input("What would you like ? (expresso/latte/cappucinno):")
from utils import get_resources_report, is_resource_sufficient

is_machine_on = True

while is_machine_on:
    choice = input("What would you like ? (expresso/latte/cappucinno):")
    if choice.lower() == "off":
        is_machine_on = False

    elif choice.lower() == "report":
        get_resources_report()
    else:
        if choice not in ["latte", "Cappuccino", "espresso"]:
            print(f"sorry!! {choice} is not appropriate. Select Correctly")
        else:
            if is_resource_sufficient(choice):
                pass

            # print(choice)