# Nutrition data per 100g serving (average values)
# Source: USDA FoodData Central & nutritional databases
NUTRITION_MAP = {
    # EXISTING FOODS
    "pizza": {"calories": 266, "protein_g": 11, "fat_g": 10, "carbs_g": 33, "sugar_g": 4},
    "hamburger": {"calories": 250, "protein_g": 13, "fat_g": 9, "carbs_g": 30, "sugar_g": 5},
    "french_fries": {"calories": 312, "protein_g": 3, "fat_g": 15, "carbs_g": 41, "sugar_g": 0},
    "hot_dog": {"calories": 290, "protein_g": 10, "fat_g": 18, "carbs_g": 23, "sugar_g": 4},
    "fried_rice": {"calories": 163, "protein_g": 3, "fat_g": 5, "carbs_g": 26, "sugar_g": 1},
    "steak": {"calories": 271, "protein_g": 25, "fat_g": 19, "carbs_g": 0, "sugar_g": 0},
    "donuts": {"calories": 452, "protein_g": 5, "fat_g": 25, "carbs_g": 51, "sugar_g": 21},
    "ramen": {"calories": 188, "protein_g": 5, "fat_g": 7, "carbs_g": 27, "sugar_g": 1},
    "spaghetti_bolognese": {"calories": 160, "protein_g": 7, "fat_g": 6, "carbs_g": 20, "sugar_g": 5},
    "sushi": {"calories": 145, "protein_g": 7, "fat_g": 4, "carbs_g": 24, "sugar_g": 2},
    "tacos": {"calories": 226, "protein_g": 10, "fat_g": 12, "carbs_g": 20, "sugar_g": 2},
    "apple_pie": {"calories": 237, "protein_g": 2, "fat_g": 11, "carbs_g": 34, "sugar_g": 19},
    "waffles": {"calories": 291, "protein_g": 6, "fat_g": 14, "carbs_g": 35, "sugar_g": 10},
    "chocolate_cake": {"calories": 389, "protein_g": 6, "fat_g": 17, "carbs_g": 56, "sugar_g": 37},
    "caesar_salad": {"calories": 190, "protein_g": 7, "fat_g": 13, "carbs_g": 11, "sugar_g": 2},
    "ice_cream": {"calories": 207, "protein_g": 3, "fat_g": 11, "carbs_g": 24, "sugar_g": 21},
    "pancakes": {"calories": 227, "protein_g": 6, "fat_g": 6, "carbs_g": 37, "sugar_g": 9},
    "grilled_cheese_sandwich": {"calories": 320, "protein_g": 12, "fat_g": 18, "carbs_g": 28, "sugar_g": 4},
    
    # NEWLY ADDED - DESSERTS & BAKED GOODS
    "tiramisu": {"calories": 240, "protein_g": 4, "fat_g": 13, "carbs_g": 27, "sugar_g": 20},
    "cheesecake": {"calories": 321, "protein_g": 6, "fat_g": 23, "carbs_g": 25, "sugar_g": 19},
    "carrot_cake": {"calories": 350, "protein_g": 4, "fat_g": 16, "carbs_g": 50, "sugar_g": 32},
    "red_velvet_cake": {"calories": 378, "protein_g": 4, "fat_g": 18, "carbs_g": 52, "sugar_g": 38},
    "chocolate_mousse": {"calories": 189, "protein_g": 3, "fat_g": 13, "carbs_g": 16, "sugar_g": 13},
    "bread_pudding": {"calories": 195, "protein_g": 5, "fat_g": 8, "carbs_g": 26, "sugar_g": 15},
    "creme_brulee": {"calories": 233, "protein_g": 4, "fat_g": 16, "carbs_g": 18, "sugar_g": 17},
    "panna_cotta": {"calories": 201, "protein_g": 3, "fat_g": 14, "carbs_g": 16, "sugar_g": 15},
    "cannoli": {"calories": 300, "protein_g": 6, "fat_g": 17, "carbs_g": 32, "sugar_g": 18},
    "baklava": {"calories": 334, "protein_g": 5, "fat_g": 16, "carbs_g": 43, "sugar_g": 25},
    "churros": {"calories": 380, "protein_g": 5, "fat_g": 18, "carbs_g": 50, "sugar_g": 22},
    "beignets": {"calories": 350, "protein_g": 6, "fat_g": 16, "carbs_g": 47, "sugar_g": 18},
    "macarons": {"calories": 400, "protein_g": 6, "fat_g": 20, "carbs_g": 50, "sugar_g": 45},
    "cup_cakes": {"calories": 305, "protein_g": 3, "fat_g": 13, "carbs_g": 45, "sugar_g": 32},
    "strawberry_shortcake": {"calories": 225, "protein_g": 3, "fat_g": 10, "carbs_g": 32, "sugar_g": 20},
    
    # PASTA & ITALIAN
    "spaghetti_carbonara": {"calories": 175, "protein_g": 8, "fat_g": 8, "carbs_g": 18, "sugar_g": 1},
    "lasagna": {"calories": 135, "protein_g": 8, "fat_g": 5, "carbs_g": 14, "sugar_g": 3},
    "ravioli": {"calories": 170, "protein_g": 7, "fat_g": 6, "carbs_g": 23, "sugar_g": 2},
    "gnocchi": {"calories": 130, "protein_g": 3, "fat_g": 1, "carbs_g": 27, "sugar_g": 1},
    "risotto": {"calories": 140, "protein_g": 3, "fat_g": 5, "carbs_g": 21, "sugar_g": 1},
    
    # ASIAN FOODS
    "pad_thai": {"calories": 140, "protein_g": 5, "fat_g": 5, "carbs_g": 19, "sugar_g": 4},
    "pho": {"calories": 92, "protein_g": 6, "fat_g": 2, "carbs_g": 13, "sugar_g": 2},
    "dumplings": {"calories": 186, "protein_g": 8, "fat_g": 6, "carbs_g": 25, "sugar_g": 2},
    "gyoza": {"calories": 200, "protein_g": 9, "fat_g": 8, "carbs_g": 23, "sugar_g": 2},
    "spring_rolls": {"calories": 150, "protein_g": 4, "fat_g": 5, "carbs_g": 23, "sugar_g": 3},
    "samosa": {"calories": 262, "protein_g": 5, "fat_g": 13, "carbs_g": 32, "sugar_g": 2},
    "bibimbap": {"calories": 121, "protein_g": 5, "fat_g": 3, "carbs_g": 20, "sugar_g": 3},
    "takoyaki": {"calories": 155, "protein_g": 6, "fat_g": 7, "carbs_g": 18, "sugar_g": 2},
    "peking_duck": {"calories": 337, "protein_g": 19, "fat_g": 28, "carbs_g": 0, "sugar_g": 0},
    "edamame": {"calories": 121, "protein_g": 11, "fat_g": 5, "carbs_g": 10, "sugar_g": 2},
    
    # MEXICAN
    "nachos": {"calories": 312, "protein_g": 7, "fat_g": 18, "carbs_g": 31, "sugar_g": 2},
    "chicken_quesadilla": {"calories": 210, "protein_g": 11, "fat_g": 10, "carbs_g": 19, "sugar_g": 2},
    "breakfast_burrito": {"calories": 195, "protein_g": 9, "fat_g": 8, "carbs_g": 22, "sugar_g": 2},
    "huevos_rancheros": {"calories": 150, "protein_g": 9, "fat_g": 8, "carbs_g": 11, "sugar_g": 3},
    
    # SANDWICHES & BREADS
    "club_sandwich": {"calories": 240, "protein_g": 15, "fat_g": 11, "carbs_g": 21, "sugar_g": 3},
    "pulled_pork_sandwich": {"calories": 280, "protein_g": 18, "fat_g": 14, "carbs_g": 20, "sugar_g": 4},
    "lobster_roll_sandwich": {"calories": 320, "protein_g": 17, "fat_g": 18, "carbs_g": 23, "sugar_g": 3},
    "french_toast": {"calories": 216, "protein_g": 7, "fat_g": 8, "carbs_g": 29, "sugar_g": 10},
    "garlic_bread": {"calories": 350, "protein_g": 8, "fat_g": 16, "carbs_g": 44, "sugar_g": 3},
    "bruschetta": {"calories": 150, "protein_g": 4, "fat_g": 6, "carbs_g": 21, "sugar_g": 2},
    
    # SALADS
    "greek_salad": {"calories": 106, "protein_g": 3, "fat_g": 8, "carbs_g": 7, "sugar_g": 4},
    "caprese_salad": {"calories": 160, "protein_g": 8, "fat_g": 12, "carbs_g": 4, "sugar_g": 3},
    "beet_salad": {"calories": 88, "protein_g": 2, "fat_g": 5, "carbs_g": 10, "sugar_g": 7},
    "seaweed_salad": {"calories": 70, "protein_g": 2, "fat_g": 4, "carbs_g": 8, "sugar_g": 4},
    
    # BREAKFAST
    "omelette": {"calories": 154, "protein_g": 11, "fat_g": 12, "carbs_g": 1, "sugar_g": 1},
    "eggs_benedict": {"calories": 215, "protein_g": 12, "fat_g": 14, "carbs_g": 11, "sugar_g": 2},
    "deviled_eggs": {"calories": 147, "protein_g": 6, "fat_g": 13, "carbs_g": 1, "sugar_g": 0},
    
    # MEATS & SEAFOOD
    "chicken_wings": {"calories": 203, "protein_g": 18, "fat_g": 14, "carbs_g": 0, "sugar_g": 0},
    "chicken_curry": {"calories": 104, "protein_g": 8, "fat_g": 5, "carbs_g": 7, "sugar_g": 3},
    "baby_back_ribs": {"calories": 290, "protein_g": 22, "fat_g": 22, "carbs_g": 0, "sugar_g": 0},
    "beef_carpaccio": {"calories": 120, "protein_g": 21, "fat_g": 3, "carbs_g": 1, "sugar_g": 0},
    "beef_tartare": {"calories": 140, "protein_g": 20, "fat_g": 6, "carbs_g": 1, "sugar_g": 0},
    "filet_mignon": {"calories": 227, "protein_g": 24, "fat_g": 14, "carbs_g": 0, "sugar_g": 0},
    "pork_chop": {"calories": 231, "protein_g": 23, "fat_g": 15, "carbs_g": 0, "sugar_g": 0},
    "prime_rib": {"calories": 310, "protein_g": 25, "fat_g": 23, "carbs_g": 0, "sugar_g": 0},
    "grilled_salmon": {"calories": 139, "protein_g": 23, "fat_g": 5, "carbs_g": 0, "sugar_g": 0},
    "fish_and_chips": {"calories": 265, "protein_g": 13, "fat_g": 14, "carbs_g": 23, "sugar_g": 1},
    "fried_calamari": {"calories": 175, "protein_g": 15, "fat_g": 8, "carbs_g": 10, "sugar_g": 0},
    "crab_cakes": {"calories": 210, "protein_g": 12, "fat_g": 13, "carbs_g": 12, "sugar_g": 1},
    "sashimi": {"calories": 127, "protein_g": 20, "fat_g": 5, "carbs_g": 0, "sugar_g": 0},
    "scallops": {"calories": 69, "protein_g": 12, "fat_g": 1, "carbs_g": 3, "sugar_g": 0},
    "mussels": {"calories": 86, "protein_g": 12, "fat_g": 2, "carbs_g": 4, "sugar_g": 0},
    "oysters": {"calories": 68, "protein_g": 7, "fat_g": 2, "carbs_g": 4, "sugar_g": 0},
    "tuna_tartare": {"calories": 132, "protein_g": 23, "fat_g": 4, "carbs_g": 0, "sugar_g": 0},
    "ceviche": {"calories": 89, "protein_g": 13, "fat_g": 2, "carbs_g": 5, "sugar_g": 2},
    "escargots": {"calories": 90, "protein_g": 16, "fat_g": 1, "carbs_g": 2, "sugar_g": 0},
    "foie_gras": {"calories": 462, "protein_g": 12, "fat_g": 44, "carbs_g": 2, "sugar_g": 0},
    
    # SOUPS
    "french_onion_soup": {"calories": 57, "protein_g": 2, "fat_g": 2, "carbs_g": 8, "sugar_g": 4},
    "clam_chowder": {"calories": 103, "protein_g": 4, "fat_g": 5, "carbs_g": 11, "sugar_g": 2},
    "miso_soup": {"calories": 40, "protein_g": 2, "fat_g": 1, "carbs_g": 5, "sugar_g": 1},
    "hot_and_sour_soup": {"calories": 45, "protein_g": 3, "fat_g": 2, "carbs_g": 5, "sugar_g": 1},
    "lobster_bisque": {"calories": 95, "protein_g": 4, "fat_g": 6, "carbs_g": 7, "sugar_g": 2},
    
    # SIDES & APPETIZERS
    "onion_rings": {"calories": 411, "protein_g": 5, "fat_g": 24, "carbs_g": 44, "sugar_g": 4},
    "macaroni_and_cheese": {"calories": 164, "protein_g": 6, "fat_g": 8, "carbs_g": 18, "sugar_g": 2},
    "poutine": {"calories": 510, "protein_g": 13, "fat_g": 27, "carbs_g": 54, "sugar_g": 2},
    "falafel": {"calories": 333, "protein_g": 13, "fat_g": 18, "carbs_g": 32, "sugar_g": 2},
    "hummus": {"calories": 166, "protein_g": 8, "fat_g": 10, "carbs_g": 14, "sugar_g": 0},
    "guacamole": {"calories": 160, "protein_g": 2, "fat_g": 15, "carbs_g": 9, "sugar_g": 1},
    "cheese_plate": {"calories": 350, "protein_g": 22, "fat_g": 28, "carbs_g": 2, "sugar_g": 1},
    
    # COMPLEX DISHES
    "paella": {"calories": 175, "protein_g": 9, "fat_g": 5, "carbs_g": 23, "sugar_g": 2},
    "shrimp_and_grits": {"calories": 180, "protein_g": 11, "fat_g": 8, "carbs_g": 16, "sugar_g": 1},
    "croque_madame": {"calories": 295, "protein_g": 15, "fat_g": 16, "carbs_g": 23, "sugar_g": 3},
    
    # FROZEN DESSERTS
    "frozen_yogurt": {"calories": 127, "protein_g": 4, "fat_g": 4, "carbs_g": 20, "sugar_g": 17},
}
