# while True:
#     input_text = """
# What would you like ? (expresso/latte/cappuccino):
# 1.report
# 2.latte
# 3.expresso
# 4.cappuccino

#     """

# choice = input("What would you like ? (expresso/latte/cappucinno):")

is_machine_on = True

while is_machine_on:
    choice = input("What would you like ? (expresso/latte/cappucinno):")
    if choice.lower() == "off":
        is_machine_on = False

