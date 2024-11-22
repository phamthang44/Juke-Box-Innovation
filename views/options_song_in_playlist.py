from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QLineEdit, QFrame, QPushButton, QListWidget, QListWidgetItem, QHBoxLayout, QScrollBar, QAbstractItemView, QMessageBox

from PySide6.QtCore import Qt, QSize
from models.Song import Song
from utils.helper import Helper
from controllers.PlayListController import PlayListController
import sys


class OptionSong(QWidget):
    def __init__(self, songs, ui, main_window):
        self.songs = songs
        self.ui = ui
        self.main_window = main_window
        super().__init__()
        self.setGeometry(800, 300, 500, 230)
        self.setWindowFlags(Qt.FramelessWindowHint)
        #self.playlist = Helper.load_playlist()
        # Main layout
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)   
        layout.setSpacing(0)  
        # Frame 1: Display the current playlist name
        self.name_frame = QFrame()
        self.name_frame.setStyleSheet("background-color: #1e1e1e;")
        name_layout = QVBoxLayout(self.name_frame)
        self.name_frame.setContentsMargins(0, 0, 0, 0)
    
        self.current_name_label = QLabel("Library")
        self.current_name_label.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")
        name_layout.addWidget(self.current_name_label)

        # Frame 2 : list to show song in playlist 
        self.list_show_song_frame = QFrame()
        self.list_show_song_frame.setStyleSheet("background-color: #000000;")
        list_layout = QVBoxLayout(self.list_show_song_frame)
        self.list_show_song_frame.setContentsMargins(0, 0, 0, 0)
        
        self.list_show_song = QListWidget()
        self.list_show_song.setStyleSheet("background-color: transparent;")
        self.list_show_song.setFixedHeight(400)
        list_layout.addWidget(self.list_show_song)
        
        # Frame 3: Input new playlist name
        self.input_frame = QFrame()
        self.input_frame.setContentsMargins(0, 0, 0, 0)
        
        self.input_frame.setStyleSheet("background-color: #1e1e1e")
        input_layout = QVBoxLayout(self.input_frame)

        self.id_song_input = QLineEdit()
        self.id_song_input.setPlaceholderText("Enter ID of song...")
        self.id_song_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #555555;
                background-color: #292929;
                color: white;
                font-weight:bold;
            }
        """)
        self.name_playlist = QLineEdit()
        self.name_playlist.setPlaceholderText("Enter Name of other Playlist You want to remove song")
        self.name_playlist.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #555555;
                background-color: #292929;
                color: white;
                font-weight:bold;
            }
        """)
        input_layout.addWidget(self.id_song_input)
        input_layout.addWidget(self.name_playlist)
        # Button to change the playlist name
        self.remove = QPushButton("Remove")
        self.remove.setStyleSheet("""
            QPushButton {
                background-color: #1DB954;
                font-weight:bold;
                color: white;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #1ed760;
            }
        """)

        input_layout.addWidget(self.remove)

        # Close button
        self.close_button = QPushButton("Close")
        self.close_button.setStyleSheet("""
            QPushButton {
                background-color: #292929;
                color: white;
                font-weight:bold;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #444444;
            }
        """)
        input_layout.addWidget(self.close_button)

        # Add frames to the main layout
        layout.addWidget(self.name_frame)
        layout.addWidget(self.input_frame)
        layout.addWidget(self.list_show_song_frame)
        # Close button action
        self.close_button.clicked.connect(self.close)
        #self.remove.clicked.connect(self.update_playlist_name)
        
        scrollbar_list_item = QScrollBar()
        scrollbar_list_item.setStyleSheet("""   
            QScrollBar:vertical {
                border: none;
                background: gray;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {                                  
                background: #535353;
                min-height: 30px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: #B3B3B3;
            }
            QScrollBar::sub-line:vertical {
                height: 0px;
            }
            QScrollBar::sub-line:vertical:hover {
                background-color: gray;
            }
            QScrollBar::sub-line:vertical:pressed {
                background-color: #484848;
            }
            
            QScrollBar::add-line:vertical {
                height: 0px;
            }
            QScrollBar::add-line:vertical:hover {
                background-color: gray;
            }
            QScrollBar::add-line:vertical:pressed {
                background-color: #484848;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
                border: none;
            }
        """)
        self.list_show_song.setVerticalScrollBar(scrollbar_list_item)
        self.list_show_song.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        
        self.display_song_items()
        
        self.remove.clicked.connect(self.execute_remove_song_from_playlist)
        
    def create_song_item_in_short(self, song_id, title):
        
        new_item = QListWidgetItem()
        new_item.setSizeHint(QSize(0, 40))
        self.list_show_song.addItem(new_item)

        central_widget = QWidget()
        layout = QHBoxLayout(central_widget)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        # Frame that stores the ID
        number_frame = QFrame()
        number_frame.setFixedSize(30, 30)
        number_label = QLabel(f"{song_id}")
        number_label.setStyleSheet("color: #807e7e; font-size: 20px; font-weight: 600;")
        number_layout = QVBoxLayout(number_frame)  # Add a layout to the number_frame
        number_layout.addWidget(number_label)
        number_layout.setContentsMargins(0, 0, 0, 0)  # Optional: to ensure proper alignment

        layout.addWidget(number_frame)

        # Frame for song title and artist text
        text_frame = QFrame()
        text_layout = QVBoxLayout()
        text_layout.setContentsMargins(20, 0, 0, 0)  # Vertical padding
        text_layout.setSpacing(2)  # Space between title and artist

        title_label = QLabel(title)
        title_label.setStyleSheet("color: #ffffff; font-weight: bold; font-size: 20px;")

        text_layout.addWidget(title_label)
        text_frame.setLayout(text_layout)  # Assign the layout to the text_frame
        layout.addWidget(text_frame)

        # Add the central widget to the QListWidgetItem
        self.list_show_song.setItemWidget(new_item, central_widget)
        
    def display_song_items(self):
        
        for song in self.songs:
            self.create_song_item_in_short(song.id_song, song.name_song)
        
    def refresh_song_items(self):
        self.list_show_song.clear()
        keyword = self.name_playlist.text()
        controller = PlayListController(self.ui, self.main_window)
        chosen_playlist = controller.get_playlist_by_name(keyword)
        song_ids = controller.get_song_ids(chosen_playlist)
        unique_song_ids = list(set(song_ids))
        song_objects = controller.get_songs_by_ids(unique_song_ids)
        for song in list(set(song_objects)):
            self.create_song_item_in_short(song.id_song, song.name_song)    
    
    def set_current_playlist_name(self, name):

        """Set the current playlist name."""
        self.current_name_label.setText(f"Current Playlist: {name}")

    def execute_remove_song_from_playlist(self):
        
        keyword = self.name_playlist.text()
        
        controller = PlayListController(self.ui, self.main_window)
        chosen_playlist = controller.get_playlist_by_name(keyword)
        
        if chosen_playlist is None:
            print(f"No playlist found with the name '{keyword}'")
            #QMessageBox.information(self,"Error","There is no playlist chosen!")
            QMessageBox.warning(self,"Error",f"There is no playlist same with {keyword}!")
            return  # Exit early if no playlist is found
        song_id = int(self.id_song_input.text())
        
        if song_id < 1 and song_id > 46:
            QMessageBox.warning(self,"Error",f"Out of bound with your {song_id}!")
            return
        
        if song_id not in chosen_playlist.songs:
            print(f"No playlist found with the name '{keyword}'")
            #QMessageBox.information(self,"Error","There is no playlist chosen!")
            QMessageBox.warning(self,"Error",f"Your {song_id} you input does not have in {keyword}!")
            return  # Exit early if no playlist is found 
            
        chosen_playlist.remove_song(song_id)
        QMessageBox.information(self, "Successful", f"You just removed the song with ID {song_id} from {keyword}")
        Helper.save_playlists_to_csv(controller.playlists)
        
        self.refresh_song_items()
        self.main_window.show_playlist(chosen_playlist)
        self.main_window.display_song_items_1(chosen_playlist)
        return chosen_playlist
        
class OptionSong2(OptionSong):
    def __init__(self, songs, ui, main_window):
        super().__init__(songs, ui, main_window)
        
        self.name_playlist.setPlaceholderText("Enter Name of other Playlist You want to add song")

        # Button to change the playlist name
        
        self.remove.setText("Add")
        self.remove.clicked.disconnect()
        self.remove.clicked.connect(self.execute_add_song_to_playlist)
        
    def set_current_playlist_name_option2(self, name):

        """Set the current playlist name."""
        self.current_name_label.setText(f"Current Playlist: {name}")
        
    def execute_add_song_to_playlist(self):

        keyword = self.name_playlist.text()
        
        controller = PlayListController(self.ui, self.main_window)
        chosen_playlist = controller.get_playlist_by_name(keyword)
        
        if chosen_playlist is None:
            print(f"No playlist found with the name '{keyword}'")
            #QMessageBox.information(self,"Error","There is no playlist chosen!")
            QMessageBox.warning(self,"Error",f"There is no playlist same with {keyword}!")
            return  # Exit early if no playlist is found
        song_id = int(self.id_song_input.text())
        
        if song_id < 1 and song_id > 46:
            QMessageBox.warning(self,"Error",f"Out of bound with your {song_id}!")
            return
        
        # if song_id not in chosen_playlist.songs:
        #     print(f"No playlist found with the name '{keyword}'")
        #     #QMessageBox.information(self,"Error","There is no playlist chosen!")
        #     QMessageBox.warning(self,"Error",f"Your {song_id} you input does not have in {keyword}!")
        #     return  # Exit early if no playlist is found 
            
        chosen_playlist.add_song(song_id)
        QMessageBox.information(self, "Successful", f"You just added the song with ID {song_id} from {keyword}")
        Helper.save_playlists_to_csv(controller.playlists)
        
        self.refresh_song_items()
        self.main_window.show_playlist(chosen_playlist)
        self.main_window.display_song_items_1(chosen_playlist)
        return chosen_playlist