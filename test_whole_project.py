from models.PlayList import PlayList
from models.Song import Song

def test_song_object():
    song1 = Song(1, "test", "test1", 5, 2020, "test", 200, "album test")
    song2 = Song(2, "test1", "test1", 5, 2020, "test", 200, "album test")
    song3 = Song(3, "test2", "test1", 5, 2020, "test", 200, "album test")
    song4 = Song(4, "test3", "test1", 5, 2020, "test", 200, "album test")
    song5 = Song(5, "test4", "test1", 5, 2020, "test", 200, "album test")
    
    assert song1 is not None
    assert song2 is not None
    assert song3 is not None
    assert song4 is not None
    assert song5 is not None
    
    assert song1.name_song == "test"
    assert song2.name_song == "test1"
    
def test_library():
    song1 = Song(1, "test", "test1", 5, 2020, "test", 200, "album test")
    song2 = Song(2, "test1", "test1", 5, 2020, "test", 200, "album test")
    song3 = Song(3, "test2", "test1", 5, 2020, "test", 200, "album test")
    song4 = Song(4, "test3", "test1", 5, 2020, "test", 200, "album test")
    song5 = Song(5, "test4", "test1", 5, 2020, "test", 200, "album test")
    
    library = []
    

    library.append(song1)
    library.append(song2)
    library.append(song3)
    library.append(song4)
    library.append(song5)
    
    assert len(library) == 5
    assert library[0].name_song == "test"
    
def test_playlist():
    playlist = PlayList()
    
    assert playlist is not None
    
def test_name_playlist():
    playlist = PlayList()
    name_playlist = playlist.name_playlist
    assert name_playlist is not None
    
def test_description_playlist():
    playlist = PlayList()
    description = playlist.description
    assert description is not None

def test_add_song():
    song = Song(1, "test", "test1", 5, 2024, "test", 300, "test album")
    playlist = PlayList()
    
    playlist.songs.append(song)
    
    assert song is not None
    assert len(playlist.songs) == 1
    
def test_remove_song():
    song = Song(1, "test", "test1", 5, 2024, "test", 300, "test album")
    playlist = PlayList()
    
    assert song is not None
    playlist.songs.append(song)
    
    assert playlist.songs != []
    playlist.songs.remove(song)
    assert len(playlist.songs) == 0

def test_non_empty_songs_playlist():
    playlist = PlayList()
    song = Song(1, "test", "test1", 5, 2024, "test", 300, "test album")
    song1 = Song(1, "test", "test1", 5, 2024, "test", 300, "test album")
    song2 = Song(1, "test", "test1", 5, 2024, "test", 300, "test album")
    song3 = Song(1, "test", "test1", 5, 2024, "test", 300, "test album")
    song4 = Song(1, "test", "test1", 5, 2024, "test", 300, "test album")
    
    playlist.songs.append(song)
    playlist.songs.append(song1)
    playlist.songs.append(song2)
    playlist.songs.append(song3)
    playlist.songs.append(song4)
    
    test_songs = []
    assert playlist.get_songs() != test_songs
    
def test_empty_songs_playlist():
    playlist = PlayList()
    test_songs = []
    assert playlist.songs == test_songs
    

def test_search_song_playlist():
    playlist = PlayList()
    song = Song(1, "test", "test1", 5, 2024, "test", 300, "test album")
    song1 = Song(1, "test", "test1", 5, 2024, "test", 300, "test album")
    song2 = Song(1, "test", "test1", 5, 2024, "test", 300, "test album")
    song3 = Song(1, "test", "test1", 5, 2024, "test", 300, "test album")
    song4 = Song(1, "test", "test1", 5, 2024, "test", 300, "test album")
    
    playlist.songs.append(song)
    playlist.songs.append(song1)
    playlist.songs.append(song2)
    playlist.songs.append(song3)
    playlist.songs.append(song4)
    
    assert len(playlist.songs) == 5
    songs = playlist.songs
    keyword = "test"
    def find_song(keyword, songs):
        for i,song in enumerate(songs):
            if song.name_song == keyword:
                return song
    song_test = find_song(keyword, songs)
    assert song_test is not None
    
def test_search_playlist():
    playlist1 = PlayList()
    playlist2 = PlayList()
    playlist3 = PlayList()
    
    test_list = []
    test_list.append(playlist1)
    test_list.append(playlist2)
    test_list.append(playlist3)
    
    keyword = playlist1.name_playlist
    def find_playlist(keyword, test_list):
        for i, playlist in enumerate(test_list):
            if playlist.name_playlist == keyword:
                return playlist
    playlist_test = find_playlist(keyword, test_list)
    
    assert playlist_test is not None
    
def test_total_duration():
    playlist = PlayList()
    song = Song(1, "test", "test1", 5, 2024, "test", 300, "test album")
    song1 = Song(1, "test", "test1", 5, 2024, "test", 300, "test album")
    
    playlist.songs.append(song)
    playlist.songs.append(song1)

    duration1 = song.duration
    duration2 = song1.duration
    
    
    def total_durations(duration1, duration2):
        return duration1 + duration2
    
    total_duration = total_durations(duration1, duration2)
    
    assert total_duration == 600
        

def test_song_object():
    song = Song(1, "test", "test1", 5, 2024, "test", 300, "test album")
    assert song is not None
    
def test_name_song():
    song = Song(1, "test", "test1", 5, 2024, "test", 300, "test album")
    assert song.name_song == "test"
    
def test_artist_song():
    song = Song(1, "test", "test1", 5, 2024, "test", 300, "test album")
    assert song.artists == "test1"

def test_year_song():
    song = Song(1, "test", "test1", 5, 2024, "test", 300, "test album")
    assert song.release_year == 2024

def test_duration_song():
    song = Song(1, "test", "test1", 5, 2024, "test", 300, "test album")
    assert song.duration == 300
    
def test_sort_song_playlist():
    playlist = PlayList()
    song = Song(1, "test2", "test1", 5, 2024, "test", 300, "test album")
    song1 = Song(1, "test5", "test1", 5, 2024, "test", 300, "test album")
    song2 = Song(1, "test1", "test1", 5, 2024, "test", 300, "test album")
    song3 = Song(1, "test3", "test1", 5, 2024, "test", 300, "test album")
    song4 = Song(1, "test4", "test1", 5, 2024, "test", 300, "test album")
    
    playlist.songs.append(song)
    playlist.songs.append(song1)
    playlist.songs.append(song2)
    playlist.songs.append(song3)
    playlist.songs.append(song4)
    
    assert playlist.songs == [song, song1, song2, song3, song4]
    sorted_songs = sorted(playlist.songs)
    assert sorted_songs == [song2, song, song3, song4, song1]

def test_sort_playlist():
    playlist1 = PlayList()
    playlist2 = PlayList()
    playlist3 = PlayList()
    
    test_list = []
    test_list.append(playlist1)
    test_list.append(playlist2)
    test_list.append(playlist3)
    
    assert test_list == [playlist1, playlist2, playlist3]
    sorted_list = sorted(test_list)
    
    assert sorted_list is not test_list
    
def test_remove_playlist():
    
    playlist1 = PlayList()
    playlist2 = PlayList()
    playlist3 = PlayList()
    
    test_list = []
    test_list.append(playlist1)
    test_list.append(playlist2)
    test_list.append(playlist3)
    assert len(test_list) == 3
    
    test_list.remove(playlist1)
    
    assert len(test_list) == 2
    
# test_non_empty_songs_playlist
# test_song_object()
# test_library()
# test_playlist()
# test_name_playlist()
# test_description_playlist()
# test_add_song()
# test_remove_song()
# test_search_song_playlist()
# test_search_playlist()
