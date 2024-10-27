import reflex as rx
from typing import List, TypedDict
import google.generativeai as genai
import os
import json

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# gemini api config
genai.configure(api_key=GEMINI_API_KEY)
model_json = genai.GenerativeModel(
    "gemini-1.5-flash-002",
    generation_config={"response_mime_type": "application/json"},
)


def generate_recipe(user_prompt):
    PROMPT = f"""
    You are an expert at generating recipe based on user prompt.
    Create a recipe in JSON format based on user prompt below. Dont use cups for measurement. Use only metric units.


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


# Define the structure for ingredients
class Ingredient(TypedDict):
    item: str
    amount: int
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

    def set_query(self, query: str):
        self.user_prompt = query

    def handle_submit(self):
        self.recipe: Recipe = generate_recipe(self.user_prompt)
        return rx.redirect("/recipe")

    @rx.var
    def ingredients(self) -> List[Ingredient]:
        return self.recipe["ingredients"]

    @rx.var
    def instructions(self) -> List[str]:
        return self.recipe["instructions"]
