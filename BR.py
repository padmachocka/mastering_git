def pick_temperature(tone: str) -> float:
    return {
        "warm": 0.4,
        "curious": 0.4,
        "confused": 0.3,
        "frustrated": 0.25,
        "urgent": 0.2,
        "cold": 0.2,
        "neutral": 0.25,
    }.get(tone, 0.25)
