def aesthetic_score(style, mood):

    score = 50

    if style == "minimalist":
        score += 20

    if mood == "confident":
        score += 30

    return score
