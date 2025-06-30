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
    "gemini-2.5-flash",
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


def create_image_prompt(user_prompt: str) -> str:
    """Convert user recipe prompt into an optimized image generation prompt.

    Args:
        user_prompt: The user's recipe request/description

    Returns:
        A formatted prompt optimized for food image generation
    """
    base_prompt = """Professional food photography of"""

    style_elements = """
    high-end restaurant presentation,
    soft natural lighting,
    shallow depth of field,
    garnished and styled,
    vibrant colors,
    shot from a 45-degree angle,
    on a rustic wooden table,
    4k quality, ultra detailed
    """

    # Clean up user prompt and remove cooking instructions
    cleaned_prompt = user_prompt.lower()
    cleaned_prompt = (
        cleaned_prompt.split("recipe")[0]
        if "recipe" in cleaned_prompt
        else cleaned_prompt
    )
    cleaned_prompt = (
        cleaned_prompt.split("how to")[0]
        if "how to" in cleaned_prompt
        else cleaned_prompt
    )

    # Construct final prompt
    image_prompt = f"{base_prompt} {cleaned_prompt}, {style_elements}"

    return image_prompt.strip()


def generate_recipe_image(user_prompt):
    formatted_prompt = create_image_prompt(user_prompt)
    response = client.images.generate(
        prompt=formatted_prompt,
        model="black-forest-labs/FLUX.1-kontext-dev",
        n=1,
    )
    return response.data[0].url


def generate_recipe(user_prompt, is_ingredient_search=False, cuisine=None):
    base_prompt = """
    You are an expert at generating recipe based on user prompt.
    Create a recipe in JSON format based on user prompt below. Dont use cups for measurement. Use only metric units.
    """

    if is_ingredient_search:
        ingredient_prompt = f"""
        Given these ingredients and {cuisine} cuisine preference, recommend the most appropriate recipe:
        Ingredients: {user_prompt}

        Note: The recipe should primarily use the provided ingredients and be influenced by {cuisine} cooking style.
        """
        PROMPT = base_prompt + ingredient_prompt
    else:
        PROMPT = (
            base_prompt
            + f"""
        Note: If the user provides a list of ingredients like (tomato, onion, spinach etc) recommend the most appropriate recipe that can be made with those ingredients.

        USER RECIPE REQUEST: {user_prompt}
        """
        )

    PROMPT += """
    json schema example:
    {
        "title": "Healthy Breakfast Omelette",
        "description": "A light and nutritious omelette packed with vegetables.",
        "prepTime": "5 minutes",
        "cookTime": "10 minutes",
        "servings": 1,
        "calories": 250,
        "ingredients": [
        {"item": "Eggs", "amount": 2, "unit": ""},
        {"item": "Milk", "amount": 20, "unit": "ml"},
        {"item": "Cream", "amount": 20, "unit": "ml"}
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
            "Fold the omelette in half and serve immediately."
        ]
    }
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
    cuisine: str = ""
    active_tab: str = "tab1"

    def set_end(self, value: list[int]):
        self.serving_slider = value[0]

    def set_cuisine(self, cuisine: str):
        self.cuisine = cuisine

    def set_active_tab(self, tab: str):
        self.active_tab = tab

    def handle_serving(self):
        new_recipe = recalculate_recipe(self.recipe, self.serving_slider)
        if new_recipe is not None:
            self.recipe = new_recipe

    def set_query(self, query: str):
        self.user_prompt = query

    def start_generation(self):
        self.is_generating = True

    def handle_submit(self):
        is_ingredient_search = self.active_tab == "tab2"
        self.recipe: Recipe = generate_recipe(
            self.user_prompt,
            is_ingredient_search=is_ingredient_search,
            cuisine=self.cuisine if is_ingredient_search else None,
        )
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
