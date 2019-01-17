"""
This is the store module and supports all the ReST actions for the
STORE collection
"""

# System modules
from datetime import datetime
from copy import copy

# 3rd party modules
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
PRODUCTS = {
    "Hat": {
        "title": "Hat",
        "inventory_count": 2,
        "timestamp": get_timestamp(),
        "price": 4.65,
    },
    "Glove": {
        "title": "Glove",
        "inventory_count": 7,
        "timestamp": get_timestamp(),
        "price": 3.65,
    },
    "Baseball": {
        "title": "Baseball",
        "inventory_count": 130,
        "timestamp": get_timestamp(),
        "price": 1.05,
    },
    "Bag": {
        "title": "Bag",
        "inventory_count": 0,
        "timestamp": get_timestamp(),
        "price": 20.57,
    }
}
 
cart = {"total_cost" : 0,}

def see_all(in_stock = False):
    """
    This function responds to a request for /api/store
    with the complete lists of products
    :return:        json string of list of products
    """
    # Go through the list and remove all products with inventory < 1
    if in_stock == True:
        in_stock = {}
        for key in PRODUCTS:
            if PRODUCTS[key]["inventory_count"] > 0:
                in_stock[key] = PRODUCTS[key]
        return [in_stock[key] for key in sorted(in_stock.keys())]
    else:
         # Create the list of products from our data
         return PRODUCTS

def search(title):
    """
    This function responds to a request for /api/store/{title}
    with the complete lists of products
    :return:        json string of the product
    """
    if title in PRODUCTS:
       return [PRODUCTS[title]]
    else:
       abort(
           404,"{title} is not available".format(title=title)
       )
def purchase(title, amount = 1):
    """
    This function responds to a request for /api/purchase/{title}
    with a response message
    :return:       a response code
    """
    # Check if the product is in the store
    if title in PRODUCTS:
        # Check if the product has at least {amount} of inventory
        if PRODUCTS[title]["inventory_count"] - amount >= 0:
            PRODUCTS[title]["inventory_count"] -= amount
            return make_response(
            "{amount} of {title} purchased!".format(title=title, amount=amount), 200
            )
        elif PRODUCTS[title]["inventory_count"] > 0:
           return make_response(
           "You can't buy {amount} of {title} there are only {in_stock} in stock!".format(amount=amount, title=title, in_stock = PRODUCTS[title]["inventory_count"]), 200
            )
        else:
            abort(
            404,"{title} is out of stock.".format(title=title)          
            )
    else:
        abort(
             404,"{title} is not available".format(title=title)
            ) 

def view_cart():
    """
    This function responds to a request for /api/cart
    with the complete cart
    :return:        json string of list of products
    """
    #Find the total cost
    total_cost = 0
    for keys in cart:
        if keys == "total_cost":
            pass
        else:
            total_cost += cart[keys]["inventory_count"] * cart[keys]["price"]
    if total_cost > 0: 
       cart["total_cost"] = total_cost
    # return all the items in the cart
    return cart

def cart_add(title, amount = 1):
    """
    This function responds to a request for /api/cart/add/{title}
    with a response message
    :return:       a response code
    """
    # Check if the product is in the store
    if title in PRODUCTS:
        # Check if the product has at least {amount} of inventory
        if PRODUCTS[title]["inventory_count"] - amount >= 0:
            # Check if the title has been added to the cart yet
            if title not in cart:
                cart[title] = copy(PRODUCTS[title])
                cart[title]["inventory_count"] = amount
                return make_response(
                "{amount} of {title} added to cart!".format(title=title, amount=amount), 200
            ) 
            elif cart[title]["inventory_count"] + amount <= PRODUCTS[title]["inventory_count"]:
                cart[title]["inventory_count"] = amount + cart[title]["inventory_count"]
                return make_response(
                "{amount} of {title} added to cart!".format(title=title, amount=amount), 200
            )
            else:
                return make_response(
                "You can't add {amount} of {title} to cart as there are only {available} available!".format(amount=amount, title=title, available = PRODUCTS[title]["inventory_count"] - cart[title]["inventory_count"]), 200
            )

        elif PRODUCTS[title]["inventory_count"] > 0:
           return make_response(
           "You can't add {amount} of {title} to cart as there are only {in_stock} in stock!".format(amount=amount, title=title, in_stock = PRODUCTS[title]["inventory_count"]), 200
            )
        else:
            abort(
            404,"{title} is out of stock.".format(title=title)          
            )
    else:
        abort(
             404,"{title} is not available".format(title=title)
            ) 
 
def clear_cart():
    cart.clear()
    cart["total_cost"] = 0
    return make_response(
        "Cart successfully cleared", 200
        )

def purchase_cart():
    for keys in cart:
       if keys == "total_cost": 
           pass
       else: 
           PRODUCTS[keys]["inventory_count"] -= cart[keys]["inventory_count"]
    cart.clear()
    return make_response(
        "Cart purchased", 200
        ) 



