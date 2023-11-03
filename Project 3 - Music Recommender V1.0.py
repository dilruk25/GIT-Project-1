# Define a dictionary of moods and their corresponding song lists
moods = {
    "Happy": ["Uptown Funk", "Happy Now", "Dancing Queen", "Walking on Sunshine"],
    "Sad": ["Tears in Heaven", "Yesterday", "Hallelujah"],
    "Relaxed": ["Imagine", "What a Wonderful World", "Over the Rainbow"],
    "Angry": ["Highway to Hell", "Back in Black", "Iron Man"],
    "Energetic": ["Eye of the Tiger", "Lose Yourself", "Jump Around"],
    "Romantic": ["My Girl", "Can't Help Falling in Love", "At Last"],
    "Nostalgic": ["Bohemian Rhapsody", "Don't Stop Believin'", "I Will Always Love You"]
}

# Ask the mood
mood = input("What mood are you in today? (Happy, Sad, Relaxed, Angry, Energetic, Romantic, Nostalgic): ")

# Confirm the mood selection
mood_confirmation = input("Are you sure you're in a {} mood? (Y/N): ".format(mood))

# If the user doesn't confirm their mood selection, exit the program
if mood_confirmation != "Y":
    print("Okay, no problem. Maybe next time!")
    exit()

# Get the song list for the selected mood
song_list = moods[mood]

# Print the song list to the console
print("Here are some song recommendations for your mood:")
for song in song_list:
    print(song)
