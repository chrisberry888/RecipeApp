def add_recipes():
    recipes = open("D:\Git_Repositories\RecipeApp\\recipe_file.txt", "w")
    while True:
        string = raw_input("Another recipe? Y/N")
        if string == "N" then:
            print("Done!")
            break
        recipes.write("<recipe>")
        string = raw_input("Recipe name?")
        recipes.write("<name>" + str + 
        recipes.write("</recipe>")
        
        
    recipes.close()
    
add_recipes()