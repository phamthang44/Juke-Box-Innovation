# #here is the place that 
import csv
import io
import sys
from models.Song import Song
from models.PlayList import PlayList
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import pandas as pd
import os
class Helper:
    #    def conver_integer_number(input):
    @staticmethod
    def input_name(name):
        pass
    def input_integer(number, msg, errormsg, inbound, outbound):
        pass
    def input_string(keyword):
        pass
    def input_path(path):
        pass
    #     return songs
    @staticmethod
    def load_data():
        songs = []

        df = pd.read_csv(r'utils\data.csv')
        for _, row in df.iterrows():
            song = Song(id_song=int(row['id_song']), name_song=row['name'], artists=row['artist'], rating=row['rating'], release_year=row['year'], genre=row['genre'], duration=row['duration'], album=row['album'])
            songs.append(song)

        return songs #songs will belong to Library not list !!!
    
    @staticmethod
    def load_song_by_id(song_id):
        all_songs = Helper.load_data()
        for song in all_songs:
            if song.id_song == song_id:
                return song
        return None  # Nếu không tìm thấy bài hát
    @staticmethod
    def load_playlist(file_path=r"utils\playlist.csv"):
        """Load playlists from CSV and return as PlayList objects."""
        playlists = []
        
        try:
            if not os.path.exists(file_path):
                print(f"File {file_path} does not exist.")
                return playlists
            
            # Read CSV into DataFrame
            df = pd.read_csv(file_path)
            
            # Process each row in the DataFrame
            for _, row in df.iterrows():
                # Convert songs to a list of integers
                songs = row['songs']
                songs_list = list(map(int, songs.split(','))) if isinstance(songs, str) else []
                
                # Create the PlayList object
                playlist = PlayList(
                    id_playlist=int(row['id_playlist']),
                    name_playlist=row['playlist_name'],
                    image_path=row['image_path'],
                    description=row['desc'],
                    songs=songs_list
                )
                playlists.append(playlist) #The object contains songs, but the songs in data.csv are numbers, so they need to point to the correct song object, not a number.
                
        except Exception as e:
            print(f"Error loading playlists from CSV: {e}")
        
        return playlists
    
    @staticmethod
    def save_playlists_to_csv(playlists, file_path=r"utils\playlist.csv"): #this method will save as well 
        try:
            # Filter out playlists that are not deleted (deleted playlists will not be in this list)
            data = {
                "id_playlist": [playlist.id_playlist for playlist in playlists],
                "playlist_name": [playlist.name_playlist for playlist in playlists],
                "image_path": [playlist.image_path for playlist in playlists],
                "desc": [playlist.description for playlist in playlists],
                "songs": [",".join(map(str, playlist.songs)) for playlist in playlists]
            }

            df = pd.DataFrame(data)

            # Record all data to CSV (do not delete old data, just add additional data)
            df.to_csv(file_path, index=False)
            print(f"Playlists saved to {file_path} successfully.")
        except Exception as e:
            print(f"Error saving playlists to CSV: {e}")
     
       
    @staticmethod
    def save_playlist(playlists, file_path=r"utils\playlist.csv"): #this method for create playlist to save
        
        if os.path.exists(file_path):
            
            existing_df = pd.read_csv(file_path)
            existing_ids = existing_df['id_playlist'].tolist()
        else:
            existing_ids = []

        # Filter new playlists, only add playlists whose ids do not exist in the file
        new_playlists = [playlist for playlist in playlists if playlist.id_playlist not in existing_ids]
        
        # Create new DataFrame for playlists that are not in the CSV file
        data = {
            "id_playlist": [int(playlist.id_playlist) for playlist in new_playlists],
            "playlist_name": [playlist.name_playlist for playlist in new_playlists],
            "image_path": [playlist.image_path for playlist in new_playlists],
            "desc": [playlist.description for playlist in new_playlists],
            "songs": [",".join(map(str, playlist.songs)) for playlist in new_playlists]  # Joining song IDs as string
        }
        df = pd.DataFrame(data)

        # If the file already exists, write to the CSV file without adding column headers
        if os.path.exists(file_path):
            df.to_csv(file_path, mode='a', header=False, index=False)
        else:
            # If file does not exist, write all data including headers
            df.to_csv(file_path, index=False)
        
# songs = Helper.load_data('data.csv')
# for song in songs: 
#     print(song)