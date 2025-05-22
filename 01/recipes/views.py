from django.shortcuts import render
from django.http import Http404
from .models import Recipe

recipes = [
    {
        "name": "蔥爆牛肉",
        "slug": "beef-stir-fry",
        "template": "beef_stir_fry.html",
        "ingredients": ["牛肉","蔥"],
        "image": "image/beef-stir-fry.png",
    },
    {
        "name": "番茄炒蛋",
        "slug": "tomato-egg",
        "template": "tomato-egg.html",
        "ingredients": ["蛋", "西紅柿"],
        "image": "image/tomato-eggs.jpg",
    },
    {
        "name": "麻油雞",
        "slug": "sesame-chicken",
        "template": " sesame-chicken.html",
        "ingredients": ["雞肉"],
        "image": "./image/sesame-chicken.jpg",
    },
    {
        "name": "紅燒茄子",
        "slug": "braised-eggplant",
        "template": " eggplant.html",
        "ingredients": ["茄子"],
        "image": "image/eggplant.jpg",
    },
    {
        "name": "蘑菇濃湯",
        "slug": "mushroom-soup",
        "template": " mushroom0.html",
        "ingredients": ["蘑菇"],
        "image": "image/mushroom-soup.jpg",
    },
    {
        "name": "清蒸魚",
        "slug": "steamed-fish",
        "template": " steamed-fish.html",
        "ingredients": ["魚肉"],
        "image": "image/steamed-fish.jpg",
    },
    {
        "name": "韓式泡菜豆腐鍋",
        "slug": "kimchi-stew",
        "template": " kimchi-stew.html",
        "ingredients": ["豆腐", "泡菜"],
        "image": "image/kimchi-stew.jpg",
    },
    {
        "name": "奶油蘑菇義大利麵",
        "slug": "pasta",
        "template": " pasta.html",
        "ingredients": ["麵", "蘑菇", "奶油"],
        "image": "image/pasta.jpg",
    },
    {
        "name": "紅燒豆腐",
        "slug": "braised-tofu",
        "template": " braised-tofu.html",
        "ingredients": ["豆腐"],
        "image": "image/braised-tofu.jpg",
    },
    {
        "name": "香蔥炒蝦仁",
        "slug": "shrimp-stir-fry",
        "template": " shrimp-stir-fry.html",
        "ingredients": ["蝦仁", "蔥"],
        "image": "image/shrimp-stir-fry.jpg",
    },
    {
        "name": "蝦仁蛋羹",
        "slug": "shrimp-egg-custard",
        "template": " shrimp-egg-custard.html",
        "ingredients": ["蝦仁", "蛋"],
        "image": "image/shrimp-egg-custard.jpg",
    },
    {
        "name": "蒜炒青菜",
        "slug": "boiled-vegetables",
        "template": " boiled-vegetables.html",
        "ingredients": ["青江菜"],
        "image": "image/boiled-vegetables.jpg",
    },
    {
        # error
        "name": "咖哩雞肉飯",
        "slug": "curry", 
        "template": " curry-chicken-rice.html",
        "ingredients": ["雞肉", "咖哩塊"],
        "image": "image/curry-chicken-rice.jpg"
    },
    {
        "name": "炒高麗菜",
        "slug": "stir-fried-vegetables",
        "template": " stir-fried-vegetables.html",
        "ingredients": ["高麗菜"],
        "image": "image/stir-fried-vegetables.jpg",
    },
    {
        "name": "三杯雞",
        "slug": "three-cup-chicken",
        "template": " three-cup-chicken.html",
        "ingredients": ["雞肉"],
        "image": "image/three-cup-chicken.jpg",
    },
    {
        "name": "魚香茄子",
        "slug": "yuxiang-eggplant",
        "template": " yuxiang-eggplant.html",
        "ingredients": ["茄子"],
        "image": "image/yuxiang-eggplant.jpg",
    },
    {
        "name": "蒜蓉蝦",
        "slug": "garlic-shrimp",
        "template": " garlic-shrimp.html",
        "ingredients": ["蝦仁"],
        "image": "image/garlic-shrimp.jpg",
    },
    {
        "name": "宮保雞丁",
        "slug": "kung-pao-chicken",
        "template": " kung-pao-chicken.html",
        "ingredients": ["雞肉"],
        "image": "image/kung-pao-chicken.jpg",
    },
    {
        "name": "螞蟻上樹",
        "slug": "ants-climbing-tree",
        "template": " ants-climbing-tree.html",
        "ingredients": ["粉絲", "豬肉"],
        "image": "image/ants-climbing-tree.jpg",
    },
    {
        "name": "糖醋排骨",
        "slug": "sweet-and-sour-pork",
        "template": " sweet-and-sour-pork.html",
        "ingredients": ["豬肉"],
        "image": "image/sweet-and-sour-pork.jpg",
    },
    {
        "name": "滷肉飯",
        "slug": "braised-pork-rice",
        "template": " braised-pork-rice.html",
        "ingredients": ["豬肉", "米"],
        "image": "image/braised-pork-rice.jpg",
    },
    {
        "name": "肉燥麵",
        "slug": "minced-pork-noodles",
        "template": " minced-pork-noodles.html",
        "ingredients": ["豬肉", "麵"],
        "image": "image/minced-pork-noodles.jpg",
    },
    {
        "name": "薑絲蛤蜊湯",
        "slug": "clam-soup",
        "template": " clam-soup.html",
        "ingredients": ["蛤蜊", "薑"],
        "image": "image/clam-soup.jpg",
    },
    {
        "name": "薯泥蛋沙拉",
        "slug": "Mashed_Potato_Egg_Salad",
        "template": " Mashed_Potato_Egg_Salad.html",
        "ingredients": ["蛋", "馬鈴薯"],
        "image": "image/Mashed_Potato_Egg_Salad.jpg",
    },
    {
        "name": "川味椒麻涼麵",
        "slug": "Sichuan_Spicy_Sesame_Noodles",
        "template": " Sichuan_Spicy_Sesame_Noodles.html",
        "ingredients": ["麵", "雞肉"],
        "image": "image/Sichuan_Spicy_Sesame_Noodles.jpg",
    },
    {
        "name": "拔絲地瓜",
        "slug": "candied-sweet-potato",
        "template": " candied_sweet_potato.html",
        "ingredients": ["地瓜"],
        "image": "image/candied_sweet_potato.jpg",
    },
    {
        "name": "泰式涼拌薄荷肉",
        "slug": "Thai_style_cold_mint_meat",
        "template": " Thai_style_cold_mint_meat.html",
        "ingredients": ["豬肉", "薄荷"],
        "image": "image/Thai_style_cold_mint_meat.jpg",
    },
    {
        "name": "番茄鯖魚蔬菜麵",
        "slug": "Tomato_mackerel_vegetable_noodles",
        "template": " Tomato_mackerel_vegetable_noodles.html",
        "ingredients": ["鯖魚罐頭", "高麗菜", "麵"],
        "image": "image/Tomato_mackerel_vegetable_noodles.jpg",
    },
    {
        "name": "皮蛋瘦肉粥",
        "slug": "century-egg-lean-pork-congee",
        "template": " Century_egg_and_lean_pork_congee.html",
        "ingredients": ["米", "皮蛋", "豬肉"],
        "image": "image/Century_egg_and_lean_pork_congee.jpg",
    },
    {
        "name": "鮑魚粥",
        "slug": "abalone-porridge",
        "template": " abalone_Porridge.html",
        "ingredients": ["鮑魚", "豬肉", "米"],
        "image": "image/abalone_porridge.jpg",
    },
    {
        "name": "青椒炒肉絲",
        "slug": "stir-fried-pork-with-green-pepper",
        "template": " Stir_fried_pork_with_green_pepper.html",
        "ingredients": ["豬肉", "牛肉", "青椒"],
        "image": "image/Stir_fried_pork_with_green_pepper.jpg",
    },
    {
        "name": "東坡肉",
        "slug": "Dongpo_pork",
        "template": " Dongpo_pork.html",
        "ingredients": ["豬肉"],
        "image": "image/Dongpo_pork.jpg",
    },
    {
        "name": "梅菜扣肉",
        "slug": "Braised_Pork_Belly_with_Preserved_Mustard_Greens",
        "template": " Braised_Pork_Belly.html",
        "ingredients": ["豬肉"],
        "image": "image/Braised_Pork_Belly_with_Preserved_Mustard_Greens.jpg",
    },
{
        "name": "玉米火腿炒蛋",
        "slug": "corn-ham-scrambled-eggs",
        "template": " Corn_ham.html",
        "ingredients": ["玉米", "火腿", "蛋"],
        "image": "image/Corn_ham_and_scrambled_eggs.jpg",
    },
{
        "name": "蝦醬空心菜",  
        "slug": "water-spinach-with-shrimp-paste",
        "template": " Water_spinach.html",
        "ingredients": ["空心菜"],
        "image": "image/Water_spinach_with_shrimp_paste.jpg",
    },
{
        "name": "蒜炒空心菜",
        "slug": "stir-fried-water-spinach-with-garlic",
        "template": " Stir-fried_water.html",
        "ingredients": ["空心菜"],
        "image": "image/Stir-fried_water_spinach_with_garlic.jpg",
    },
{
        "name": "蒜香奶油烤馬鈴薯",
        "slug": "Garlic_butter_roasted_potatoes",
        "template": " Garlic_butter.html",
        "ingredients": ["馬鈴薯"],
        "image": "image/Garlic_butter_roasted_potatoes.jpg",
    },
{
        "name": "韓式涼拌海帶",
        "slug": "Korean_style_cold_seaweed_salad",
        "template": " Korean_style_cold.html",
        "ingredients": ["海帶"],
        "image": "image/Korean_style_cold_seaweed_salad.jpg",
    },
{
        "name": "狼牙土豆",
        "slug": "Wolf_Tooth_Potato",
        "template": " Wolf_Tooth_Potato.html",
        "ingredients": ["馬鈴薯"],
        "image": "image/Wolf_Tooth_Potato.jpg",
    },
{
        "name": "紫菜豆腐湯",
        "slug": "Seaweed_and_Tofu_Soup",
        "template": " Seaweed_and_Tofu.html",
        "ingredients": ["豆腐", "紫菜"],
        "image": "image/Seaweed_and_Tofu_Soup.jpg",
    },
{
        "name": "紫菜蛋花湯",
        "slug": "Seaweed_and_Egg_Soup",
        "template": " Seaweed_and_Egg.html",
        "ingredients": ["紫菜", "蛋"],
        "image": "image/Seaweed_and_Egg_Soup.jpg",
    },
{
        "name": "玉米濃湯",
        "slug": "Cream_of_corn_soup",
        "template": " Cream_of_corn.html",
        "ingredients": ["玉米"],
        "image": "image/Cream_of_corn_soup.jpg",
    },
{
        "name": "南瓜濃湯",
        "slug": "Pumpkin_soup",
        "template": " Pumpkin_soup.html",
        "ingredients": ["南瓜"],
        "image": "image/Pumpkin_soup.jpg",
    },
{
        "name": "脆炒南瓜絲",
        "slug": "Crispy_Fried_Pumpkin_Strips",
        "template": " Crispy_Fried_Pumpkin_Strips.html",
        "ingredients": ["南瓜"],
        "image": "image/Crispy_Fried_Pumpkin_Strips.jpg",
    },
{
        "name": "蒜蓉魷魚",
        "slug": "Garlic_Squid",
        "template": " Garlic_Squid.html",
        "ingredients": ["魷魚"],
        "image": "image/Garlic_Squid.jpg",
    },
{
        "name": "可樂鷄翅",
        "slug": "Coca-Cola_Chicken_Wings",
        "template": " Coca-Cola_Chicken_Wings.html",
        "ingredients": ["鷄翅"],
        "image": "image/Coca-Cola_chicken_wings.jpg",
    },
{
        "name": "椒麻雞",
        "slug": "Mala_Chicken",
        "template": " Mala_Chicken.html",
        "ingredients": ["鷄肉"],
        "image": "image/Mala_Chicken.jpg",
    },
{
        "name": "馬鈴薯燉牛肉",
        "slug": "Beef_stew_with_potatoes",
        "template": " Beef_stew_with_potatoes.html",
        "ingredients": ["馬鈴薯", "牛肉"],
        "image": "image/Beef_stew_with_potatoes.jpg",
    },
{
        "name": "涼拌土豆絲",
        "slug": "Cold_mixed_potato_shreds",
        "template": " Cold_mixed_potato_shreds.html",
        "ingredients": ["馬鈴薯"],
        "image": "image/Cold_mixed_potato_shreds.jpg",
    },
{
        "name": "香菇蛤蜊鷄湯",
        "slug": "Mushroom_clam_and_chicken_soup",
        "template": " Mushroom_clam_and_chicken_soup.html",
        "ingredients": ["蘑菇", "蛤蜊", "鷄肉"],
        "image": "image/Mushroom_clam_and_chicken_soup.jpg",
    },
]

from django.shortcuts import render

def recipe_detail(request, slug):
    for recipe in recipes:
        if recipe["slug"] == slug:
            template = recipe.get("template")
            if not template:
                raise Http404("Template not specified for this recipe.")
            return render(request, template, {"recipe": recipe})
    raise Http404("Recipe not found")

def select_ingredients(request):
    # 食材分類資料
    meat_items = ["雞肉","鷄翅", "豬肉", "牛肉", "羊肉", "火腿", "培根"]
    vegetable_items = ["空心菜", "小白菜", "青江菜", "高麗菜","玉米", "馬鈴薯", "茄子", "海帶", "紫菜", "西紅柿","南瓜","地瓜"]
    seafood_items = ["魚肉","鯖魚", "魷魚", "蝦仁", "鮑魚", "蛤蜊"]
    other_items = ["米", "麵", "豆腐", "蛋", "粉絲", "蘑菇", "皮蛋", "鯖魚罐頭"]

    context = {
        'meat_items': meat_items,
        'vegetable_items': vegetable_items,
        'seafood_items': seafood_items,
        'other_items': other_items,
    }
    return render(request, 'recipes/select_ingredients.html', context)


def recipe_results(request):
    selected_ingredients = request.GET.getlist('ingredients')  # 使用者勾選的食材
    recommended_recipes = []

    for recipe in recipes:
        recipe_ingredients = recipe["ingredients"]
        if any(ingredient in recipe_ingredients for ingredient in selected_ingredients):
            recommended_recipes.append(recipe)

    context = {
        'recipes': recommended_recipes,
        'selected_ingredients': selected_ingredients,
    }
    return render(request, 'recipes/recipe_results.html', context)




