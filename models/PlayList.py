from datetime import timedelta
class PlayList:
    #class variable to keep count number
    _counter = 0
    id_counter = 0
    
    def __init__(self, id_playlist=None, name_playlist=None, image_path=r"image\default-playlist.png",  description=r"Favorite Playlist",songs=None):
        if id_playlist is None:
            self.id_playlist = self.generate_id_playlist()
        else:
        # Ensure id_playlist always is an integer 
            self.id_playlist = int(id_playlist)  
        # self.id_playlist = id_playlist
        self.songs = songs if songs is not None else [] #List as numbers
        self.songs_playlist = [] #library of songs 
        if name_playlist is None:
            name_playlist = self.generate_playlist_name()
        self.name_playlist = name_playlist 
        self.description = description 
        self.image_path = image_path

        
    def __str__(self):
        song_list = "\n".join(str(s) for s in self.songs_playlist)
        return f"{self.name_playlist:}\n{song_list}"
    
    @classmethod
    def generate_id_playlist(cls):
        cls.id_counter += 1
        return cls.id_counter
    
    @classmethod
    def generate_playlist_name(cls): #auto increment name with number

        cls._counter += 1
        return f"New Playlist #{cls._counter}"    
    
    @classmethod
    def reset_counter(cls):
        #Reset the playlist counter - useful for testing
        cls._counter = 0
        
    # hàm này bị sai hết về mặt logic từ 41 tới hết do songs_playlist là 1 list nhưng chứa dạng số (ID của Song object thật) 
    def add_song_1(self, song):
        self.songs_playlist.append(song)
    
    def add_song(self, song_id): 
        try:
            if song_id is not None:
                if song_id in self.songs:
                    return f"Your song with ID {song_id} has been in list"
                else:
                    self.songs.append(song_id)
            else:
                print("Playlist not found.")
        except:
            print("Unexpected Error")

    def remove_song(self, song_id): #input number ID of song object real just remove the number not object 
        try:
            if song_id is not None:
                if song_id in self.songs:
                    self.songs.remove(song_id)
            else:
                print("Playlist not found.")
        except:
            print("Unexpected Error")
       
    def get_name_playlist(self):
        return self.name_playlist
    
    def clear_songs(self):
        self.songs_playlist.clear()
    
    def get_image_path(self):
        return r"{self.image_path}"
    
    def get_total_duration_test(self):
        return f"1:02:03"
    
    def total_durations(self, songs):
        total_duration = 0
        for song in songs: #list store songs_ids 
            total_duration += song.duration
        time_delta = timedelta(seconds=total_duration)
        total_minutes = time_delta.total_seconds() // 60  # Total minutes
        remaining_seconds = time_delta.total_seconds() % 60  # Remaining seconds
        
        return f"{int(total_minutes):02}:{int(remaining_seconds):02}"
    
    def get_info(self): #test first, after fixing will return another way not in this way
        
        return {
            "name": self.get_name_playlist(),
            "number_of_songs": len(self.songs_playlist),
            "duration" : self.total_durations()
        }        
        
    def get_songs(self): # Return the list of Song IDs ( interger list (1, 2, 3,..))
        return self.songs
    
    def display_songs(self):
        for index, song in enumerate(self.songs_playlist, start=1):
            print(f"ID: {index}, {song.get_info()}")
        return #sau này print sẽ change with hàm mà set_text look like  prototype để show text lên 
    
    
    
    def sort_song_by_name(self):
        return self.songs_playlist.sort(key=lambda song: song.get_name())
    
    def __iter__(self):
        # Trả về iterator cho danh sách bài hát
        return iter(self.songs_playlist)
    
    def find_songs(self, keyword, songs):
        """Find song by name, album, artists"""
        if keyword == "":
            return None
        
        songs_found = []
        
        for song in songs:
            if (keyword in song.name_song.strip().lower().replace(" ", "") or
                keyword in song.artists.strip().lower().replace(" ", "") or
                keyword in song.album.strip().lower().replace(" ", "")):
                songs_found.append(song)
        
        return list(set(songs_found))
    
    def __lt__(self, other):
        return self.name_playlist < other.name_playlist