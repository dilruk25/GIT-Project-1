# Define a dictionary of moods and their corresponding song lists
mood_songs = {
    1: {
        "MoodName": "Happy",
        "Songs": ["Uptown Funk", "Happy Now", "Dancing Queen", "Walking on Sunshine"],
    },
    2: {"MoodName": "Sad", "Songs": ["Tears in Heaven", "Yesterday", "Hallelujah"]},
    3: {
        "MoodName": "Relaxed",
        "Songs": ["Imagine", "What a Wonderful World", "Over the Rainbow"],
    },
    4: {"MoodName": "Angry", "Songs": ["Highway to Hell", "Back in Black", "Iron Man"]},
    5: {
        "MoodName": "Energetic",
        "Songs": ["Eye of the Tiger", "Lose Yourself", "Jump Around"],
    },
    6: {
        "MoodName": "Romantic",
        "Songs": ["My Girl", "Can't Help Falling in Love", "At Last"],
    },
    7: {
        "MoodName": "Nostalgic",
        "Songs": [
            "Bohemian Rhapsody",
            "Don't Stop Believin'",
            "I Will Always Love You",
        ],
    },
}


# Display moods
def display_moods():
    welcome_text = """Hello there, What mood are you in today? 
                    1. Happy
                    2. Sad
                    3. Relaxed
                    4. Angry
                    5. Energetic
                    6. Romantic
                    7. Nostalgic
                    8. To exit
                    """
    print(welcome_text)


# Ask the user to choose a mood
display_moods()
mood = int(input("Choose (1, 2, 3, 4, 5, 6, 7, 8): "))

# Check if the selected mood is valid
if mood == 8:
    print("Have a good day...")
    exit()

if mood not in mood_songs:
    print("Invalid mood selection. Please choose a valid number.")
else:
    selected_mood = mood_songs[mood]
    selected_mood_name = selected_mood["MoodName"]  # Get the name of the selected mood
    song_list = selected_mood["Songs"]  # Get the song list for the selected mood

    # Ask for confirmation with the mood name
    mood_confirmation = input(
        f"Are you sure you're in a {selected_mood_name} mood? (Y/N): "
    )

    if mood_confirmation.upper() == "Y":
        # Print the song list to the console
        print(f"Here are some song recommendations for your {selected_mood_name} mood:")
        for song in song_list:
            print(song)
    else:
        print("Okay, no problem. Maybe next time!")
