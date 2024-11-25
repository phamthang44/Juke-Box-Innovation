from models.PlayList import PlayList
from utils.helper import Helper
from views.floating_widget import FloatingWidget
from views.options_popup import OpenOptions
from datetime import timedelta
from PySide6.QtWidgets import QFileDialog
from PIL import Image
class PlayListController():
    def __init__(self, ui, main_window):
        self.ui = ui
        self.main_window = main_window
        self.playlists = Helper.load_playlist() #list chứa 1 đống object PlayList() 
        # mà một object PlayList() chứa thêm object Songs 
        self.all_songs = Helper.load_data()
        self.floating_test = FloatingWidget()
        self.open_menus_options = OpenOptions()
    def get_all_playlist(self):
        return self.playlists
    
    def sort_by_name_ascending(self):
        self.playlists.sort(key=lambda x: x.name_playlist) #key argument to specify the attribute of list in playlists
        
        self.main_window.refresh_playlist_items_by_sorting_1(self.playlists)
        self.main_window.refresh_playlist_items_by_sorting_2(self.playlists)
        
    def sort_by_name_descending(self):
        self.playlists.sort(key=lambda x: x.name_playlist, reverse=True)
        self.main_window.refresh_playlist_items_by_sorting_1(self.playlists)
        self.main_window.refresh_playlist_items_by_sorting_2(self.playlists)
        
    def search_by_name_playlist(self):
        
        keyword = self.ui.search_bar_2.text().strip()
        playlists_search = []  # List to store matching playlists
        result = "Not Found"
        text_for_show = ""
        
        for playlist_info in self.playlists:
            if (
                keyword.lower() in playlist_info.name_playlist.lower()
                or keyword.lower() in playlist_info.description.lower()
            ):
                playlists_search.append(playlist_info)

        if playlists_search:
            self.main_window.clear_no_results_label()
            self.main_window.show_playlists_search(playlists_search)
        else:
        # Show "No Results Found" label in the list
            self.main_window.show_playlists_search(playlists_search)
            
    def get_playlist(self, playlist_id):
        for playlist in self.playlists:
            if playlist.id_playlist == playlist_id:
                return playlist
        return None
    
    def get_playlist_by_object(self, playlist):
        for playlist in self.playlists:
            if playlist == playlist:
                return playlist
        return None
       
    def get_playlist_by_name(self, name_playlist):
        
        for playlist in self.playlists:
            if playlist.name_playlist.lower().strip().replace(" ", "") == name_playlist.lower().strip().replace(" ", ""):
                return playlist
        return None
    
    def remove_playlist(self, playlist_id):
        playlist_object = self.get_playlist(playlist_id)
        try:
            # Remove the playlist from the internal list of playlists
            self.playlists.remove(playlist_object)
            
            # Now, save the updated playlists to CSV without affecting the songs of other playlists
            Helper.save_playlists_to_csv(self.playlists)
            
            print(f"Playlist with ID {playlist_object.id_playlist} removed from internal list.")
            # after removing, show the playlist with ID 1
            self.main_window.show_playlist_by_id(1)  # call function to show playlist with ID = 1
        except ValueError:
            print("Playlist not found.")
        except Exception as e:
            print(f"Error removing playlist: {e}")
    
            
    def set_playlists(self, playlists):
        """
        Lưu danh sách playlist vào controller.
        """
        self.playlists = playlists
     
    def create_playlist(self):
        existed_playlists = self.playlists
        new_playlist = PlayList()
        
        existing_ids = {playlist.id_playlist for playlist in existed_playlists}
        
        existing_names = {playlist.name_playlist for playlist in existed_playlists}
        # check and create new ID
        while new_playlist.id_playlist in existing_ids:
            new_playlist.id_playlist = PlayList.generate_id_playlist()  # create new ID if existing 

        # check and create new name of playlist if existing 
        while new_playlist.name_playlist in existing_names:
            new_playlist.name_playlist = f"New Playlist #{len(existing_names) + 1}"  # change the name if already had 
            
        self.playlists.append(new_playlist)
        Helper.save_playlist(self.playlists)
        self.main_window.refresh_playlist_items()
        self.main_window.display_list_items_2()
        return new_playlist
    
    def open_recommendations(self):
        self.floating_test.show()
        
     #it means input an songs list like (1,2,3) because in csv file that store songs object dạng ID, so it need to call if ID == ID of real Song object will return object not number!
     
    def get_song_ids(self, playlist):
        if playlist:
            return playlist.songs
            
    def find_song_by_id(self, song_id):
        """Retrieve a Song object by its ID."""
        for song in self.all_songs:  # Giả sử self.all_songs chứa danh sách toàn bộ bài hát
            if song.id_song == song_id:
                return song
        return None
    
    def get_songs_by_ids(self, song_ids): # must be input as a songs like helper class 
        """Fetch the Song objects based on their IDs."""

        song_objects = []
        for playlist in self.playlists:
            for song_id in playlist.songs:
                if song_id in song_ids:
                    song = self.find_song_by_id(song_id)
                    if song:
                        song_objects.append(song)    
        return song_objects

    def on_clicked_rename_popup(self, current_name_playlist):
        self.open_menus_options.show()
        # test = self.open_menus_options.set_current_playlist_name(current_name_playlist)
        self.open_menus_options.set_current_playlist_name(current_name_playlist)
        
        #check is current name need something after change by button 
        self.open_menus_options.update_name_button.clicked.connect(
    lambda: self.on_playlist_name_updated(self.open_menus_options.update_playlist_name())
)
        



        
    def on_playlist_name_updated(self, updated_name):
        if updated_name:
            print(f"Updated Playlist Name: {updated_name}")
            # Here you can proceed with further processing, like renaming the playlist
            self.rename_playlist(updated_name)
        else:
            print("No name entered.")
    
    def rename_playlist(self, name):
        try:
            # Get the updated name from the input
            updated_name = name
            
            # Ensure a playlist is selected
            if hasattr(self.main_window, 'current_playlist') and self.main_window.current_playlist:
                current_playlist = self.main_window.current_playlist
                
                # Update the playlist's name
                current_playlist.name_playlist = updated_name
                
                # Save the updated playlists to CSV
                Helper.save_playlists_to_csv(self.playlists)
                
                # Optionally, update the UI to reflect the new name
                self.main_window.refresh_playlist_items()
                self.main_window.display_list_items_2()
                self.main_window.show_playlist_by_id(1)
                
                print(f"Playlist renamed to '{updated_name}'.")
            else:
                print("No playlist selected for renaming.")
        except Exception as e:
            print(f"Error in renaming playlist: {e}")
    
    
    def change_image_path(self):
        
            
        file_path, _ = QFileDialog.getOpenFileName(None, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")

        try:
            # Get the updated name from the input
            updated_image = file_path
            if updated_image == "":
                updated_image = r"image\default-playlist.png"
            # Ensure a playlist is selected
            if hasattr(self.main_window, 'current_playlist') and self.main_window.current_playlist:
                current_playlist = self.main_window.current_playlist
                
                # Update the playlist's name
                current_playlist.image_path = updated_image
                
                # Save the updated playlists to CSV
                Helper.save_playlists_to_csv(self.playlists)
                
                # Optionally, update the UI to reflect the new name
                self.main_window.refresh_playlist_items()
                self.main_window.display_list_items_2()
                self.main_window.show_playlist_by_id(1)
                
                print("Playlist image has been changed!'.")
            else:
                print("No playlist selected for renaming.")
        except Exception as e:
            print(f"Error in renaming playlist: {e}")

            

        
        
    #it means input an songs list like (1,2,3) because in csv file that store songs object dạng ID, so it need to call if ID == ID of real Song object will return object not number!    
    # def get_songs_by_ids(self, playlist_id, song_ids):
    #     """Fetch the Song objects for a given playlist, based on their IDs."""
    #     # Find the playlist by ID
    #     playlist = self.get_playlist(playlist_id)
    #     if playlist:
    #         return playlist.get_songs_by_ids(song_ids)
    #     return []  # Return an empty list if playlist is not found

