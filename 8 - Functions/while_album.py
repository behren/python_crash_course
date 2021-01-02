def make_album(artist_name, album_title, tracks=0):
    
    album_dict = {
        "Artist": artist_name, 
        "Title": album_title
        }

    if tracks:
        album_dict["tracks"] = tracks

    return album_dict


artist_prompt = "\nWho's the artist? "
album_prompt = "Please name an album. "

print("Enter 'q' or 'quit' to exit at any time.")

while True:
    artist = input(artist_prompt)
    if artist == "q" or artist == "quit":
        break

    title = input(album_prompt)
    if title == "q" or title == "quit":
        break

    album = make_album(artist, title)
    print(f"\n{album}")

print("\nThanks for taking the survey.")