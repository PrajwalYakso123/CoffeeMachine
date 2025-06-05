# while True:
#     input_text = """
# What would you like ? (expresso/latte/cappuccino):
# 1.report
# 2.latte
# 3.expresso
# 4.cappuccino

#     """

# choice = input("What would you like ? (expresso/latte/cappucinno):")
from resources_db import machine_resources as resources

def get_resources_report():
    print(f"water: {resources.get('water', ' ')}ml")
    print(f"milk: {resources.get('milk', ' ')}ml")
    print(f"coffee: {resources.get('coffee', ' ')}gm")
    print(f"money: ${resources.get('money', ' ')}")

is_machine_on = True

while is_machine_on:
    choice = input("What would you like ? (expresso/latte/cappucinno):")
    if choice.lower() == "off":
        is_machine_on = False

    elif choice.lower() == "report":
        get_resources_report()

