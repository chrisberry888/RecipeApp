import re
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def add_recipes():
    
    while True:
        another_recipe = input("Another recipe? Y/N ")
        if re.match("(N|n)o*", another_recipe):
            print("Done!")
            break
        
        
        name = input("Recipe name? ")
        
        
        servings = input("Servings? ")
        
        
        
        spices = []
        spices_amounts = []
        print("If no more spices, press enter")
        while True:
            spice = input("Spice: ")
            if spice == "":
                break
            amount = input("amount: ")
            spices.append(spice)
            spices_amounts.append(amount)
            
        
        
        
        ingredients = []
        ingredients_amounts = []
        print("If no more ingredients, press enter")
        while True:
            ingredient = input("Ingredient: ")
            if ingredient == "":
                break
            amount = input("amount: ")
            ingredients.append(ingredient)
            ingredients_amounts.append(amount)
            
        steps = []
        
        print("If no more steps, press enter")
        while True:
            step = input("Step: ")
            if step == "":
                break
            steps.append(step)
            
            
        
        new_recipe = {
            u'name': name,
            u'serving_size': servings,
            u'spices': spices,
            u'spices_amounts': spices_amounts,
            u'ingredients': ingredients,
            u'ingredients_amounts': ingredients_amounts,
            u'steps': steps
        }
        
        db.collection(u'recipes').document(name).set(new_recipe)








def driver():
    while True:
        ans = input(
            '''Select function:
            \n1) Add Recipes
            \n0) Quit\n''')
        if ans == "1":
            add_recipes()
        elif ans == "0":
            break
        else:
            print("invalid input")


cred = credentials.Certificate("D:\Secret_keys\super_secret_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

driver()