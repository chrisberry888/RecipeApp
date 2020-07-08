import re
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



def add_recipes():
    recipes = open("D:\Git_Repositories\RecipeApp\\recipe_file.txt", "w")
    while True:
        another_recipe = input("Another recipe? Y/N ")
        if re.match("(N|n)o*", another_recipe):
            print("Done!")
            break
        recipes.write("<recipe>\n")
        
        name = input("Recipe name? ")
        recipes.write("<name>%s</name>\n" % name)
        
        servings = input("Servings? ")
        recipes.write("<servings>%s</servings>\n" % servings)
        
        recipes.write("<spices>\n")
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
            recipes.write("%s, %s; " % (spice, amount))
        recipes.write("\n</spices>\n")
        
        recipes.write("<ingredients>\n")
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
            recipes.write("%s, %s; " % (ingredient, amount))
        recipes.write("\n</ingredients>\n")
        
        recipes.write("<steps>\n")
        steps = []
        count = 1
        print("If no more steps, press enter")
        while True:
            step = input("Step: ")
            if step == "":
                break
            steps.append(step)
            recipes.write("<%d>%s</%d>\n" % (count, step, count))
            count += 1
        recipes.write("</steps>\n")
        
            
        recipes.write("</recipe>\n")
        
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
        
        
    recipes.close()
    
    
    




def driver(){
    
    
}

cred = credentials.Certificate("D:\Secret_keys\super_secret_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

driver()