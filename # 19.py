# 19.1
def city_country(city, country):
    return f"{city}, {country}"

print(city_country("Santiago", "Chile"))
print(city_country("Tokyo", "Japan"))
print(city_country("Paris", "France"))

# 19.2
def make_album(artist, album):
    return {"artist": artist, "album": album}

album1 = make_album("Artist1", "Album1")
album2 = make_album("Artist2", "Album2")
album3 = make_album("Artist3", "Album3")

print(album1)
print(album2)
print(album3)

# 19.3
def make_album(artist, album, tracks=None):
    album_dict = {"artist": artist, "album": album}
    if tracks:
        album_dict["tracks"] = tracks
    return album_dict

album4 = make_album("Artist4", "Album4", 12)
print(album4)

# 19.4
while True:
    artist = input("Enter artist (or 'q' to quit): ")
    if artist == 'q':
        break
    album = input("Enter album: ")
    
    album_dict = make_album(artist, album)
    print(album_dict)

# 19.5
def show_messages(messages):
    for message in messages:
        print(message)

messages = ["Message 1", "Message 2", "Message 3"]
show_messages(messages)

# 19.6
def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

sent_messages = []
send_messages(messages, sent_messages)
print("Sent messages:", sent_messages)
print("Remaining messages:", messages)

# 19.7
messages = ["Message 1", "Message 2", "Message 3"]
sent_messages = []
send_messages(messages[:], sent_messages)
print("Sent messages:", sent_messages)
print("Original messages:", messages)
