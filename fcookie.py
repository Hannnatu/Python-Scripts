import random

# Dictionary of fortune messages based on user input
fortunes = {
    "love": [
        "Love is just around the corner. 💖",
        "Open your heart, and love will find you. 💕",
        "Someone special is thinking of you. 💌"
    ],
    "money": [
        "Unexpected wealth is coming your way. 💰",
        "A financial opportunity will knock soon. 💵",
        "Save wisely, and riches will follow. 💎"
    ],
    "happiness": [
        "True happiness comes from within. ��",
        "A smile is the key to a joyful life. 😄",
        "You will find happiness in the little things. 🌼"
    ],
    "success": [
        "Your hard work will soon pay off. 🚀",
        "Great achievements are ahead. 🌟",
        "Stay persistent, success is near. 🎯"
    ],
    "friendship": [
        "A new friend will bring joy to your life. 👫",
        "Loyal friends are your greatest treasure. 💖",
        "Kindness will strengthen your friendships. 🤗"
    ]
}

# Default fortune if the word isn't in the dictionary
default_fortunes = [
    "Your future is bright! ✨",
    "A great surprise awaits you. 🎁",
    "Change is coming—embrace it! 🌱"
]

# Get user input
word = input("Enter one word for your fortune: ").strip().lower()

# Pick a random fortune based on input or use a default
fortune = random.choice(fortunes.get(word, default_fortunes))

# Display the fortune
print(f"\n🥠 Fortune Cookie Message: {fortune}")

