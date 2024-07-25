import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x150")

        mixer.init()

        self.playing = False

        self.create_widgets()

    def create_widgets(self):
        self.select_button = tk.Button(self.root, text="Select Folder", command=self.select_folder)
        self.select_button.pack(pady=10)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.songs = [os.path.join(self.folder_path, song) for song in os.listdir(self.folder_path) if song.endswith('.mp3')]
            self.current_song_index = 0
            if self.songs:
                self.play_music()

    def play_music(self):
        if not self.playing:
            if self.songs:
                mixer.music.load(self.songs[self.current_song_index])
                mixer.music.play()
                self.playing = True

    def pause_music(self):
        if self.playing:
            mixer.music.pause()
            self.playing = False

    def stop_music(self):
        if self.playing:
            mixer.music.stop()
            self.playing = False

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
