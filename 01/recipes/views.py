from django.shortcuts import render
from django.http import Http404
from .models import Recipe

recipes = [
    {
        "name": "蔥爆牛肉",
        "slug": "beef-stir-fry",
        "template": "recipes/beef_stir_fry.html",
        "ingredients": ["牛肉","蔥"],
        "image": "image/beef-stir-fry.png",
    },
    {
        "name": "番茄炒蛋",
        "slug": "tomato-egg",
        "template": "recipes/tomato-egg.html",
        "ingredients": ["蛋", "西紅柿"],
        "image": "image/tomato-eggs.jpg",
        "url" : "http://127.0.0.1:8000/recipe/"
    },
    {
        "name": "麻油雞",
        "slug": "sesame-chicken",
        "template": "recipes/sesame-chicken.html",
        "ingredients": ["雞肉"],
        "image": "./image/sesame-chicken.jpg",
    },
    {
        "name": "紅燒茄子",
        "slug": "braised-eggplant",
        "template": "recipes/eggplant.html",
        "ingredients": ["茄子"],
        "image": "image/eggplant.jpg",
    },
    {
        "name": "蘑菇濃湯",
        "slug": "mushroom-soup",
        "template": "recipes/mushroom0.html",
        "ingredients": ["蘑菇"],
        "image": "image/mushroom-soup.jpg",
    },
    {
        "name": "清蒸魚",
        "slug": "steamed-fish",
        "template": "recipes/steamed-fish.html",
        "ingredients": ["魚肉"],
        "image": "image/steamed-fish.jpg",
    },
    {
        "name": "韓式泡菜豆腐鍋",
        "slug": "kimchi-stew",
        "template": "recipes/kimchi-stew.html",
        "ingredients": ["豆腐", "泡菜"],
        "image": "image/kimchi-stew.jpg",
    },
    {
        "name": "奶油蘑菇義大利麵",
        "slug": "pasta",
        "template": "recipes/pasta.html",
        "ingredients": ["麵", "蘑菇", "奶油"],
        "image": "image/pasta.jpg",
    },
    {
        "name": "紅燒豆腐",
        "slug": "braised-tofu",
        "template": "recipes/braised-tofu.html",
        "ingredients": ["豆腐"],
        "image": "image/braised-tofu.jpg",
    },
    {
        "name": "香蔥炒蝦仁",
        "slug": "shrimp-stir-fry",
        "template": "recipes/shrimp-stir-fry.html",
        "ingredients": ["蝦仁", "蔥"],
        "image": "image/shrimp-stir-fry.jpg",
    },
    {
        "name": "蝦仁蛋羹",
        "slug": "shrimp-egg-custard",
        "template": "recipes/shrimp-egg-custard.html",
        "ingredients": ["蝦仁", "蛋"],
        "image": "image/shrimp-egg-custard.jpg",
    },
    {
        "name": "蒜炒青菜",
        "slug": "boiled-vegetables",
        "template": "recipes/boiled-vegetables.html",
        "ingredients": ["青江菜"],
        "image": "image/boiled-vegetables.jpg",
    },
    {
        # error
        "name": "咖哩雞肉飯",
        "slug": "curry", 
        "template": "recipes/curry-chicken-rice.html",
        "ingredients": ["雞肉", "咖哩塊"],
        "image": "image/curry-chicken-rice.jpg"
    },
    {
        "name": "炒高麗菜",
        "slug": "stir-fried-vegetables",
        "template": "recipes/stir-fried-vegetables.html",
        "ingredients": ["高麗菜"],
        "image": "image/stir-fried-vegetables.jpg",
    },
    {
        "name": "三杯雞",
        "slug": "three-cup-chicken",
        "template": "recipes/three-cup-chicken.html",
        "ingredients": ["雞肉"],
        "image": "image/three-cup-chicken.jpg",
    },
    {
        "name": "魚香茄子",
        "slug": "yuxiang-eggplant",
        "template": "recipes/yuxiang-eggplant.html",
        "ingredients": ["茄子"],
        "image": "image/yuxiang-eggplant.jpg",
    },
    {
        "name": "蒜蓉蝦",
        "slug": "garlic-shrimp",
        "template": "recipes/garlic-shrimp.html",
        "ingredients": ["蝦仁"],
        "image": "image/garlic-shrimp.jpg",
    },
    {
        "name": "宮保雞丁",
        "slug": "kung-pao-chicken",
        "template": "recipes/kung-pao-chicken.html",
        "ingredients": ["雞肉"],
        "image": "image/kung-pao-chicken.jpg",
    },
    {
        "name": "螞蟻上樹",
        "slug": "ants-climbing-tree",
        "template": "recipes/ants-climbing-tree.html",
        "ingredients": ["粉絲", "豬肉"],
        "image": "image/ants-climbing-tree.jpg",
    },
    {
        "name": "糖醋排骨",
        "slug": "sweet-and-sour-pork",
        "template": "recipes/sweet-and-sour-pork.html",
        "ingredients": ["豬肉"],
        "image": "image/sweet-and-sour-pork.jpg",
    },
    {
        "name": "滷肉飯",
        "slug": "braised-pork-rice",
        "template": "recipes/braised-pork-rice.html",
        "ingredients": ["豬肉", "米"],
        "image": "image/braised-pork-rice.jpg",
    },
    {
        "name": "肉燥麵",
        "slug": "minced-pork-noodles",
        "template": "recipes/minced-pork-noodles.html",
        "ingredients": ["豬肉", "麵"],
        "image": "image/minced-pork-noodles.jpg",
    },
    {
        "name": "薑絲蛤蜊湯",
        "slug": "clam-soup",
        "template": "recipes/clam-soup.html",
        "ingredients": ["蛤蜊", "薑"],
        "image": "image/clam-soup.jpg",
    },
    {
        "name": "薯泥蛋沙拉",
        "ingredients": ["蛋", "馬鈴薯"],
        "image": "image/Mashed_Potato_Egg_Salad.jpg",
    },
    {
        "name": "川味椒麻涼麵",
        "ingredients": ["麵"],
        "image": "image/Sichuan_Spicy_Sesame_Noodles.jpg",
    },
    {
        "name": "拔絲地瓜",
        "ingredients": ["地瓜"],
        "image": "image/candied_sweet_potato.jpg",
    },
    {
        "name": "泰式涼拌薄荷肉",
        "ingredients": ["豬肉", "薄荷"],
        "image": "image/Thai_style_cold_mint_meat.jpg",
    },
    {
        "name": "番茄鯖魚蔬菜麵",
        "ingredients": ["鯖魚罐頭", "高麗菜", "麵"],
        "image": "image/Tomato_mackerel_vegetable_noodles.jpg",
    },
    {
        "name": "皮蛋瘦肉粥",
        "ingredients": ["米", "皮蛋", "豬肉"],
        "image": "image/Century_egg_and_lean_pork_congee.jpg",
    },
    {
        "name": "鮑魚粥",
        "ingredients": ["鮑魚", "豬肉", "米"],
        "image": "image/abalone_porridge.jpg",
    },
    {
        "name": "青椒炒肉絲",
        "ingredients": ["豬肉", "牛肉", "青椒"],
        "image": "image/Stir_fried_pork_with_green_pepper.jpg",
    },
    {
        "name": "東坡肉",
        "ingredients": ["豬肉"],
        "image": "image/Dongpo_pork.jpg",
    },
    {
        "name": "梅菜扣肉",
        "ingredients": ["豬肉"],
        "image": "image/Braised_Pork_Belly_with_Preserved_Mustard_Greens.jpg",
    },
{
        "name": "玉米火腿炒蛋",
        "ingredients": ["玉米", "火腿", "蛋"],
        "image": "image/Corn_ham_and_scrambled_eggs.jpg",
    },
{
        "name": "蝦醬空心菜",
        "ingredients": ["空心菜"],
        "image": "image/Water_spinach_with_shrimp_paste.jpg",
    },
{
        "name": "蒜炒空心菜",
        "ingredients": ["空心菜"],
        "image": "image/Stir-fried_water_spinach_with_garlic.jpg",
    },
{
        "name": "蒜香奶油烤馬鈴薯",
        "ingredients": ["馬鈴薯"],
        "image": "image/Garlic_butter_roasted_potatoes.jpg",
    },
{
        "name": "韓式涼拌海帶",
        "ingredients": ["海帶"],
        "image": "image/Korean_style_cold_seaweed_salad.jpg",
    },
{
        "name": "狼牙土豆",
        "ingredients": ["馬鈴薯"],
        "image": "image/Wolf_Tooth_Potato.jpg",
    },
{
        "name": "紫菜豆腐湯",
        "ingredients": ["豆腐", "紫菜"],
        "image": "image/Seaweed_and_Tofu_Soup.jpg",
    },
{
        "name": "紫菜蛋花湯",
        "ingredients": ["紫菜", "蛋"],
        "image": "image/Seaweed_and_Egg_Soup.jpg",
    },
{
        "name": "玉米濃湯",
        "ingredients": ["玉米"],
        "image": "image/Cream_of_corn_soup.jpg",
    },
{
        "name": "南瓜濃湯",
        "ingredients": ["南瓜"],
        "image": "image/Pumpkin_soup.jpg",
    },
{
        "name": "脆炒南瓜絲",
        "ingredients": ["南瓜"],
        "image": "image/Crispy_Fried_Pumpkin_Strips.jpg",
    },
{
        "name": "蒜蓉魷魚",
        "ingredients": ["魷魚"],
        "image": "image/Garlic_Squid.jpg",
    },
{
        "name": "可樂鷄翅",
        "ingredients": ["鷄翅"],
        "image": "image/Coca-Cola_chicken_wings.jpg",
    },
{
        "name": "椒麻雞",
        "ingredients": ["鷄肉"],
        "image": "image/Mala_Chicken.jpg",
    },
{
        "name": "馬鈴薯燉牛肉",
        "ingredients": ["馬鈴薯", "牛肉"],
        "image": "image/Beef_stew_with_potatoes.jpg",
    },
{
        "name": "涼拌土豆絲",
        "ingredients": ["馬鈴薯"],
        "image": "image/Cold_mixed_potato_shreds.jpg",
    },
{
        "name": "香菇蛤蜊鷄湯",
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
    vegetable_items = ["空心菜", "小白菜", "青江菜", "高麗菜","玉米", "馬鈴薯", "茄子", "海帶", "紫菜", "西紅柿","南瓜"]
    seafood_items = ["魚肉","鯖魚", "魷魚", "蝦仁", "鮑魚", "蛤蜊"]
    other_items = ["米", "麵", "豆腐", "蛋", "粉絲", "蘑菇"]

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


