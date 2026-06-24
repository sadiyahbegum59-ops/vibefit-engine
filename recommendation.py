import random

def recommend_outfit(occasion, style, mood):

    try:
        options = OUTFIT_DATABASE[occasion][style][mood]

        selected = random.choice(options)

        return f"Recommended Outfit: {selected}"

    except KeyError:

        return "No exact match found. Try changing preferences."
