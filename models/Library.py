# models/Library.py

from utils.helper import Helper
from datetime import timedelta

class Library:
    def __init__(self, main_window, name_library="Library"):
        self.songs = Helper.load_data()  # Danh sách toàn bộ bài hát
        self.main_window = main_window
        self.name_library = name_library
    def find_song(self, keyword: str):
        # results = [song for song in self.songs if keyword.lower() in song.get_name().lower()]
        # return results
        for song in self.songs:
            if keyword.lower() in song.get_name().lower():  # Tìm kiếm không phân biệt hoa thường
                #print(song)  # Tự động gọi __str__ khi in đối tượng
                return song

        return None
    
    def add_song_into_playlist(self, song_id, playlist: list):
        playlist.append(song_id)
    
    def get_total_durations(self):
        
        durations = 0
        for song in self.songs:
            durations += song.duration
            
        # Create a timedelta object from the duration in seconds
        time_delta = timedelta(seconds=durations)
        
        # Extract total minutes and remaining seconds
        total_minutes = time_delta.total_seconds() // 60  # Total minutes
        remaining_seconds = time_delta.total_seconds() % 60  # Remaining seconds
        
        return f"{int(total_minutes):02}:{int(remaining_seconds):02}"
        
    def sort_by_name_ascending(self):
        self.songs.sort(key=lambda x: x.name_song)
        self.main_window.display_song_items_library(self.songs)
    
    def sort_by_name_descending(self):
        self.songs.sort(key=lambda x: x.name_song, reverse=True)
        self.main_window.display_song_items_library(self.songs)
    
    def sort_by_artist_ascending(self):
        self.songs.sort(key=lambda x: x.artists)
        self.main_window.display_song_items_library(self.songs)
    
    def sort_by_artist_descending(self):
        self.songs.sort(key=lambda x: x.artists, reverse=True)
        self.main_window.display_song_items_library(self.songs)
        
    def sort_by_album_ascending(self):
        self.songs.sort(key=lambda x: x.album)
        self.main_window.display_song_items_library(self.songs)
    
    def sort_by_album_descending(self):
        self.songs.sort(key=lambda x: x.album, reverse=True)
        self.main_window.display_song_items_library(self.songs)
    
    def get_all_songs(self):
        return self.songs

    def get_songs_search(self, keyword):
        found_songs = []
        for song in self.songs:
            if keyword in song.name_song.strip().lower().replace(" ", "") or keyword in song.artists.strip().lower().replace(" ", "") or keyword in song.album.strip().lower().replace(" ", ""):
                found_songs.append(song)
            
        return found_songs