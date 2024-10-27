import reflex as rx
from typing import List, TypedDict
import google.generativeai as genai
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

# gemini
genai.configure(api_key=GEMINI_API_KEY)
model_json = genai.GenerativeModel(
    "gemini-1.5-flash-002",
    generation_config={"response_mime_type": "application/json"},
)

# flux.1 schnell
client = OpenAI(
    api_key=TOGETHER_API_KEY,
    base_url="https://api.together.xyz/v1",
)


# Define the structure for ingredients
class Ingredient(TypedDict):
    item: str
    amount: int | float
    unit: str


# Define the structure for recipe
class Recipe(TypedDict):
    title: str
    description: str
    prepTime: str
    cookTime: str
    servings: int
    calories: int
    ingredients: List[Ingredient]
    instructions: List[str]


def generate_recipe_image(user_prompt):
    response = client.images.generate(
        prompt=user_prompt,
        model="black-forest-labs/FLUX.1-schnell",
        n=1,
    )
    return response.data[0].url


def generate_recipe(user_prompt):
    PROMPT = f"""
    You are an expert at generating recipe based on user prompt.
    Create a recipe in JSON format based on user prompt below. Dont use cups for measurement. Use only metric units.

    Note: If the user provides a list of ingredients like (tomato, onion, spinach etc) recommend the most appropriate recipe that can be made with those ingredients.


    json schema example:

    {{
        "title": "Healthy Breakfast Omelette",
        "description": "A light and nutritious omelette packed with vegetables.",
        "prepTime": "5 minutes",
        "cookTime": "10 minutes",
        "servings": 1,
        "calories": 250,
        "ingredients": [
        {{"item": "Eggs", "amount": 2, "unit": ""}},
        {{"item": "Milk", "amount": 20, "unit": "ml"}},
        {{"item": "Cream", "amount": 20, "unit": "ml"}},
        ],
        "instructions": [
            "Whisk eggs and milk together in a bowl. Season with salt and pepper.",
            "Heat olive oil in a non-stick pan over medium heat.",
            "Add onion and cook until softened, about 2 minutes.",
            "Add mushrooms and bell pepper, and cook for another 3-4 minutes until slightly tender.",
            "Stir in spinach and cook until wilted, about 1 minute.",
            "Pour egg mixture into the pan.",
            "Cook until the edges are set, then gently lift the edges to allow uncooked egg to flow underneath.",
            "Cook until the omelette is set but still slightly moist, about 3-4 minutes more.",
            "Fold the omelette in half and serve immediately.",
        ],
    }}

    USER RECIPE REQUEST: {user_prompt}
    """
    response = model_json.generate_content(PROMPT).text
    response = json.loads(response)
    return response


def recalculate_recipe(recipe_json: Recipe, servings: int):
    """Recalculates recipe ingredient amounts based on the desired number of servings.

    Args:
        recipe_json: A JSON string or Python dictionary representing the recipe.
        servings: The desired number of servings.

    Returns:
        A new dictionary with the updated ingredient amounts, or None if input is invalid.
    """

    try:
        if isinstance(recipe_json, str):
            recipe = json.loads(recipe_json)
        elif isinstance(recipe_json, dict):
            recipe = recipe_json
        else:
            return None  # Handle invalid input type

        original_servings = recipe.get("servings", 1)  # default to 1 if missing

        if original_servings <= 0 or servings <= 0:
            return None  # Handle invalid serving sizes.

        scaling_factor = servings / original_servings

        for ingredient in recipe["ingredients"]:
            if "amount" in ingredient and isinstance(
                ingredient["amount"], (int, float)
            ):
                ingredient["amount"] = round(
                    ingredient["amount"] * scaling_factor, 1
                )  # round to 1 decimal

        recipe["servings"] = servings  # update servings in the recipe

        return recipe

    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error processing recipe: {e}")
        return None


recipe_data: Recipe = {
    "title": "Healthy Breakfast Omelette",
    "description": "A light and nutritious omelette packed with vegetables.",
    "prepTime": "5 minutes",
    "cookTime": "10 minutes",
    "servings": 1,
    "calories": 250,
    "ingredients": [
        {"item": "Eggs", "amount": 2, "unit": ""},
        {"item": "Milk", "amount": 20, "unit": "ml"},
        {"item": "Cream", "amount": 20, "unit": "ml"},
        {"item": "Uranium", "amount": 20, "unit": "ml"},
    ],
    "instructions": [
        "Whisk eggs and milk together in a bowl. Season with salt and pepper.",
        "Heat olive oil in a non-stick pan over medium heat.",
        "Add onion and cook until softened, about 2 minutes.",
        "Add mushrooms and bell pepper, and cook for another 3-4 minutes until slightly tender.",
        "Stir in spinach and cook until wilted, about 1 minute.",
        "Pour egg mixture into the pan.",
        "Cook until the edges are set, then gently lift the edges to allow uncooked egg to flow underneath.",
        "Cook until the omelette is set but still slightly moist, about 3-4 minutes more.",
        "Fold the omelette in half and serve immediately.",
    ],
}


class State(rx.State):
    recipe: Recipe = recipe_data
    user_prompt: str = ""
    is_generating: bool = False
    recipe_img_url: str = ""
    serving_slider: int = 1
    default_serving_size: int = 0

    def set_end(self, value: list[int]):
        self.serving_slider = value[0]

    def handle_serving(self):
        new_recipe = recalculate_recipe(self.recipe, self.serving_slider)
        if new_recipe is not None:
            self.recipe = new_recipe

    def set_query(self, query: str):
        self.user_prompt = query

    def start_generation(self):
        self.is_generating = True

    def handle_submit(self):
        self.recipe: Recipe = generate_recipe(self.user_prompt)
        # self.recipe: Recipe = recipe_data
        self.default_serving_size = self.recipe["servings"]
        self.serving_slider = self.recipe["servings"]
        img_url = generate_recipe_image(self.user_prompt)
        if img_url is not None:
            self.recipe_img_url = img_url
        self.is_generating = False
        return rx.redirect("/recipe")

    @rx.var
    def ingredients(self) -> List[Ingredient]:
        return self.recipe["ingredients"]

    @rx.var
    def instructions(self) -> List[str]:
        return self.recipe["instructions"]
