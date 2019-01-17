# Shopify
Shopify Summer Development Challenge

# Setup

Hello to whoever is looking at this!

You'll need (at least) Python 3.5, Flask (run on version 1.02), Connexion (2.20) and (optionally) swagger-ui to run this web server API

# Instructions

Once the code is pulled, you can run $ python3 server.py to boot up the webpage for the API
You wil be able to find the webpage at localhost:5000
All the API components can be found under localhost:5000/api, with swagger-ui documentation at localhost:5000/api/ui

# Challenge steps

The code starts with a base of data (under PRODUCTS in store.py) that can be played around with at the source code level
This data (like in a real marketplace) cannot be added from the API (if you wish to change it, it should be fairly simple to edit from store.py)

Passing in in_stock = True shows only items that are in stock

Purchase accepts an argument for # of items wishing to be purchased

Cart can either be added to, cleared, or a "purchase" can be made, and the items will be removed from the store 
