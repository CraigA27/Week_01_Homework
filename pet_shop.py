# WRITE YOUR FUNCTIONS HERE
import pdb
def get_pet_shop_name(pet_shop):
    pet_shop_name = pet_shop["name"]
    return pet_shop_name

def get_total_cash(pet_shop):
    cash_total = pet_shop["admin"]["total_cash"]
    return cash_total

def add_or_remove_cash(pet_shop, amount):
    cash = get_total_cash(pet_shop)
    pet_shop["admin"]["total_cash"] = cash + amount
    return (pet_shop["admin"]["total_cash"])

def get_pets_sold(pet_shop):
    sold_pets = pet_shop["admin"]["pets_sold"]
    return sold_pets

def increase_pets_sold(pet_shop, pet_sales):
    pet_shop["admin"]["pets_sold"] += pet_sales
    return (pet_shop["admin"]["pets_sold"])

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])
     

def get_pets_by_breed(pet_shop, named_breed):
    pet_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == named_breed:
            pet_breed.append(pet)
    return pet_breed
    

def find_pet_by_name(pet_shop, pet_name):
   for pet in pet_shop["pets"]:
    if pet["name"] == pet_name:
        return pet

def remove_pet_by_name(pet_shop, pet_name):
    found_pet = find_pet_by_name(pet_shop, pet_name)
    removed_pet = pet_shop["pets"].remove(found_pet)
    return removed_pet

def add_pet_to_stock(pet_shop, new_pet):
    count = get_stock_count(pet_shop)
    pet_shop["pets"] = count + len(new_pet)
    return pet_shop["pets"]


def get_customer_cash(customer):
    cash = customer["cash"]
    return cash


def remove_customer_cash(customer, amount):
    cash = get_customer_cash(customer)
    customer["cash"] = cash - amount
    return customer["cash"]


def get_customer_pet_count(customer):
    customer_pet_count = len(customer["pets"])
    return customer_pet_count

def add_pet_to_customer(customer, new_pet):
    add_pet = customer["pets"].append(new_pet)
    if customer["name"] == customer:
        add_pet
    return (customer["pets"])

def customer_can_afford_pet(customer, new_pet):
    customer_cash = get_customer_cash(customer)
    pet_cost = new_pet["price"]
    if customer_cash >= pet_cost:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop, pet, customer):
    if find_pet_by_name(pet_shop, pet) != None:
        if customer_can_afford_pet(customer, pet) == True:
            add_pet_to_customer(customer, pet)
            add_or_remove_cash(pet_shop, pet)
            increase_pets_sold(pet_shop, pet)
            get_total_cash(pet_shop)
        else:
            print("Insufficient funds")
    else:
        print("No such pet")        
    
    
    # get_customer_pet_count(customer)
    # get_pets_sold(pet_shop)
    # get_customer_cash(customer)
    # get_total_cash(pet_shop)
