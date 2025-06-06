from resources_db import machine_resources as resources
from resources_db import COFFEE_MENU
def get_resources_report():
    print(f"water: {resources.get('water', ' ')}ml")
    print(f"milk: {resources.get('milk', ' ')}ml")
    print(f"coffee: {resources.get('coffee', ' ')}gm")
    print(f"money: ${resources.get('money', ' ')}")
    
def is_resource_sufficient(choice):
    is_resource_suff = True
    for ingred, qty in COFFEE_MENU.get(choice, {}).get("ingredients", " ").items():
        if resources.get(ingred, 0) <= qty:
            print(f"We don't have enough {ingred}. Try another choice.")
            is_resource_suff = False
    return is_resource_suff

    