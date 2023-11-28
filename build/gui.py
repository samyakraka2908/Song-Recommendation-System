from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\Coding\Python\Song Recommendation System\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def get_spotify_track_id(track_name, artist_name, sp):
    query = f"track:{track_name} artist:{artist_name}"
    results = sp.search(q=query, type='track', limit=1)

    if results['tracks']['items']:
        return results['tracks']['items'][0]['id']
    else:
        return None


def get_related_tracks(track_id, sp, num_recommendations=5):
    recommendations = sp.recommendations(seed_tracks=[track_id], limit=num_recommendations)

    related_tracks = []
    for track in recommendations['tracks']:
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        related_tracks.append((track_name, artist_name))

    return related_tracks


def on_submit():
    track_name = entry_song.get()
    artist_name = entry_artist.get()

    input_track_id = get_spotify_track_id(track_name, artist_name, sp)

    if input_track_id:
        related_tracks = get_related_tracks(input_track_id, sp, num_recommendations=5)

        if related_tracks:
            result_text.config(state='normal')
            result_text.delete(1.0, 'end')
            result_text.insert('end', "Recommended tracks:\n")
            for i, (related_track_name, related_artist_name) in enumerate(related_tracks, start=1):
                result_text.insert('end', f"{i}. {related_track_name} by {related_artist_name}\n")
            result_text.config(state='disabled')
        else:
            result_text.config(state='normal')
            result_text.delete(1.0, 'end')
            result_text.insert('end', "No related tracks found.")
            result_text.config(state='disabled')
    else:
        result_text.config(state='normal')
        result_text.delete(1.0, 'end')
        result_text.insert('end', "Input song not found on Spotify.")
        result_text.config(state='disabled')

client_id = 'e2e2c03bbb7049c5becef160bb7342f0'
client_secret = '42f1cb8319c34c758462550e099c366e'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

window = Tk()

window.geometry("1920x1080")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    480.0,
    540.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1440.0,
    540.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1439.0,
    692.0,
    image=image_image_3
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=291.0,
    y=859.0,
    width=379.0,
    height=114.0
)

canvas.create_text(
    338.0,
    879.0,
    anchor="nw",
    text="Submit",
    fill="#FFFFFF",
    font=("Candal", 48 * -1)
)

canvas.create_text(
    440.0,
    32.0,
    anchor="nw",
    text="Song Recommendation System",
    fill="#FFFFFF",
    font=("Inter", 80 * -1)
)

canvas.create_text(
    67.0,
    349.0,
    anchor="nw",
    text="Enter Song name:\n",
    fill="#000000",
    font=("Candal", 48 * -1)
)

canvas.create_text(
    68.0,
    540.0,
    anchor="nw",
    text="Enter Artist name:\n",
    fill="#000000",
    font=("Candal", 48 * -1)
)

canvas.create_text(
    1031.0,
    349.0,
    anchor="nw",
    text="Your Recommendations:",
    fill="#FFFFFF",
    font=("Candal", 48 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    480.5,
    466.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=106.0,
    y=411.0,
    width=749.0,
    height=108.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    480.5,
    679.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=106.0,
    y=624.0,
    width=749.0,
    height=108.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    375.0,
    70.0,
    image=image_image_4
)

entry_song = Entry(window, font=("Candal", 45))
entry_song.place(x=150, y=430)

entry_artist = Entry(window, font=("Candal", 45))
entry_artist.place(x=150, y=640)

# Submit button
submit_button = Button(window, text="Submit", command=on_submit, font=("Candal", 30))
submit_button.place(x=405, y=875)

# Result text area
result_text = Text(window, wrap="word", font=("Candal", 16), state='disabled', height=20, width=55)
result_text.place(x=1100, y=450)

window.resizable(False, False)
window.mainloop()
