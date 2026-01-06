import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't eggs tell jokes? They'd crack each other up!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the bicycle fall over? It was two-tired!"
]

def get_random_joke():
    return random.choice(jokes)

if __name__ == "__main__":
    print(get_random_joke())