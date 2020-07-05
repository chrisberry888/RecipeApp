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
        print("If no more spices, press enter")
        while True:
            spice = input("Spice: ")
            if spice == "":
                break
            amount = input("amount: ")
            recipes.write("%s, %s; " % (spice, amount))
        recipes.write("\n</spices>\n")
        
        recipes.write("<ingredients>\n")
        print("If no more ingredients, press enter")
        while True:
            ingredient = input("Ingredient: ")
            if ingredient == "":
                break
            amount = input("amount: ")
            recipes.write("%s, %s; " % (ingredient, amount))
        recipes.write("\n</ingredients>\n")
        
        recipes.write("<steps>\n")
        count = 1
        print("If no more steps, press enter")
        while True:
            step = input("Step: ")
            if step == "":
                break
            recipes.write("<%d>%s</%d>\n" % (count, step, count))
            count += 1
        recipes.write("</steps>\n")
        
            
        recipes.write("</recipe>\n")
        
        
    recipes.close()
    
cred = credentials.Certificate("D:\Git_Repositories\RecipeApp\super_secret_key.json")
firebase_admin.initialize_app(cred)


db = firestore.client()

#add_recipes()

doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

doc_ref = db.collection(u'users').document(u'aturing')
doc_ref.set({
    u'first': u'Alan',
    u'middle': u'Mathison',
    u'last': u'Turing',
    u'born': 1912
})


users_ref = db.collection(u'users')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
  
  
  

