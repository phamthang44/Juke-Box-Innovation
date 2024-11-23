
from datetime import timedelta
class Song:
    id_counter_song = 0
    def __init__(self, id_song, name_song, artists, rating, release_year, genre, duration, album):
        # if id_song is None:
        #     self.id_song = self.generate_id_playlist()
        # else:
        # # Đảm bảo id_song always is an integer 
        self.id_song = id_song
        # Increment the counter and assign it as the song ID
        self.name_song = name_song
        self.artists = artists
        self.rating = rating
        self.release_year = release_year
        self.genre = genre
        self.duration = duration # Duration in seconds
        self.album = album
        self.is_playing = False
    
    @classmethod
    def generate_id_playlist(cls):
        cls.id_counter_song += 1
        return cls.id_counter_song
    
    
    def get_album(self):
        return self.album
    
    def get_name(self):
        return self.name_song
    
    def get_rating(self):
        return self.rating

    def get_release_year(self):
        return self.release_year
    
    def get_genre(self):
        return self.genre
    
    def play(self):
        self.is_playing = True
        print(f"{self.get_name()} is playing.")
        
    def pause(self):
        self.is_playing = False
        print(f"{self.get_name()} is paused")
    
    def stop(self):
        self.is_playing = False
        print(f"{self.get_name()} is stopped")
    
    
    
    def get_duration(self):
        # Create a timedelta object from the duration in seconds
        time_delta = timedelta(seconds=self.duration)
        
        # Extract total minutes and remaining seconds
        total_minutes = time_delta.total_seconds() // 60  # Total minutes
        remaining_seconds = time_delta.total_seconds() % 60  # Remaining seconds
        
        return f"{int(total_minutes):02}:{int(remaining_seconds):02}"
    
    def get_info(self): #sau này đổi thành kiểu phù hợp với UI 
        artist_names = ' '.join(self.artists)
        return f"title: {self.name_song}, artist: {artist_names}, duration: {self.get_duration()}, release year: {self.release_year}"
        
    def __str__(self): #sau này đổi thành kiểu phù hợp với UI 
        artist_names = ' '.join(self.artists)
        return f"title: {self.name_song}, artist: {artist_names}, duration: {self.get_duration()}, release year: {self.release_year}"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # DRAFT AREA 
# if __name__ == "__main__":
#     test1 = Song("c", "tac_gia", 5, 2001, "romantic", 300)
#     test2 = Song("b", "tac_gia2", 4, 2002, "love", 250)
#     test3 = Song("a", "tac_gia3", 3, 2003, "test", 430)
#     test4 = Song("test4", "tac_gia4", 2, 2004, "ridiculous", 180)
#     test5 = Song("test5", "tac_gia5", 1, 2005, "not-have", 200)

#     #print(test1.get_info())
#     playlist_test = PlayList("Favorite", "Hello World")
#     playlist_test.add_song(test1)
#     playlist_test.add_song(test2)
#     playlist_test.add_song(test3)
#     #print(playlist_test.get_info())
#     #print(playlist_test.get_info())
    
#     #mỗi song trong list songs thì nó sẽ có 
#      #playlist_test.get_songs() -> return a list of songs in playlist instance 
#     print("Before sorting")
#     print(playlist_test.display_songs())
#     print("\n")
#     #print("here is the song:")
#     #playlist_test.find_song(4)
#     print("\nAfter sorting")
#     playlist_test.sort_song_by_name()
#     print(playlist_test.display_songs())
#      #playlist_test.get_songs() -> return a list of songs in playlist instance 
  
#     #ID ascending
#     #print(playlist_test.display_sorted_songs())    
    
    
    