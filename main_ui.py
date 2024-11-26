import time
import webbrowser
from views.options_popup import OpenOptions
from utils.helper import Helper
from models.Library import Library
from controllers.PlayListController import PlayListController
from sklearn.cluster import KMeans
from models.Song import Song
import numpy as np
import cv2

# from views.ui_view_list_widget import Ui_MainWindow
# from PySide6.QtCore import Signal, Qt, QThread 
import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QEventLoop, QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter, QPainterPath,
    QPalette, QPixmap, QRadialGradient, QTransform, QAction, QScreen)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget, QLabel, QAbstractItemView, QMenu, QScrollBar, QScrollArea, QDialog, QListView, QStackedLayout)
from PySide6.QtCore import Signal, Qt, QThread

import weakref
from views.ui_view_list_widget import Ui_MainWindow
from views.tooltipManager import TooltipManager
from utils.menu import Menu
import ctypes
from views.options_song_in_playlist import OptionSong, OptionSong2

class HoverFrame(QFrame):
    hovered = Signal(bool)
    pressed = Signal(bool)
    selected = Signal(bool)

    def __init__(self, id, parent=None):
        super().__init__(parent)
        self.id = id  # A unique identifier for the frame
        self.is_hovered = False
        self.is_selected = False
        self.play_button = QPushButton("▶", self)
        self.update_style()
        
    def _is_deleted(self):
        try:
            # Try to access a Qt property to check if widget still exists
            self.isVisible()
            return False
        except RuntimeError:
            return True
        
    def enterEvent(self, event):
        self.hovered.emit(True)
        if not self.is_selected:
            self.setStyleSheet("background-color: #1f1f1f;")  # Hover style

        super().enterEvent(event)

    def leaveEvent(self, event):
        self.hovered.emit(False)
        if not self.is_selected:
            self.setStyleSheet("background-color: #121212;")  # Default style

        super().leaveEvent(event)

    def mousePressEvent(self, event):
        self.pressed.emit(True)
        self.setStyleSheet("background-color: #333333;")  # Pressed style
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.pressed.emit(False)
        if event.button() == Qt.LeftButton:
            self.is_selected = not self.is_selected  # Toggle selection
            self.update_style()
            self.selected.emit(self.is_selected)  # Emit signal
        super().mouseReleaseEvent(event)

    def set_hovered(self, hovered):
        """Sets the hover state and updates style."""
        self.is_hovered = hovered
        self.update_style()

    def set_selected(self, selected):
        """Sets the selected state and updates style."""
        if self.is_selected != selected:
            self.is_selected = selected
            if not self._is_deleted():
                self.update_style()
            self.selected.emit(selected)
    
    def update_style(self):
        """Updates the style based on hover and selected states."""
        if not self._is_deleted():
            style = "background-color: #282828;" if self.is_selected else "background-color: #121212;"
            self.setStyleSheet(style)
        if self.is_selected:
            self.setStyleSheet("background-color: #3d3d3d;")  # Selected color
        elif self.is_hovered:
            self.setStyleSheet("background-color: #1f1f1f;")  # Hovered color
        else:
            self.setStyleSheet("background-color: #121212;")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(r"icons\spotify_icon.ico"))
        self.setWindowTitle("JukeBox")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.initial_size = self.size()
        self.is_maximized = False
        self.selected_frame = None
        self.current_playlist = None
        self.current_playing_frame = None  # To track the currently playing frame (song)
        self.current_playing_button = None  # To track the play button of the currently playing song
        
        self.frames = weakref.WeakSet()
        self.library = Library(self)
        
        
        
        #ControllerPlayList
        self.controller_playlist = PlayListController(self.ui,self) 
        self.tooltip_manager = TooltipManager(self)
        self.tooltip_manager.attach(self.ui.play_btn_in_playlist, "Play the list")
        self.tooltip_manager.attach(self.ui.remove_playlist_from_library, "Remove From Your Library")
        self.tooltip_manager.attach(self.ui.expand_btn, "Expand Your Library")
        self.tooltip_manager.attach(self.ui.expand_button, "Collapse Your Library")
        self.tooltip_manager.attach(self.ui.create_playlist, "Create playlist")
        self.tooltip_manager.attach(self.ui.sort_btn_playlist, "Sort by")
        self.tooltip_manager.attach(self.ui.button_home, "Move To Home Page")
        self.tooltip_manager.attach(self.ui.search_btn_2, "Search in your Library")
        self.tooltip_manager.attach(self.ui.search_btn_playlist, "Search in list")
        self.tooltip_manager.attach(self.ui.moreoptions, "More options")
        self.tooltip_manager.attach(self.ui.pushButton_3, "Durations")
       # self.ui.button_inside_floating.clicked.connect(controller_playlist.create_playlist)
        
       #test playlist id = 1 coi show songs khong ?
        self.playlists = Helper.load_playlist()
        self.controller_playlist.set_playlists(self.playlists)
        self.ui.remove_playlist_from_library.clicked.connect(self.on_remove_playlist_clicked)
        
        self.ui.hide_window_btn.clicked.connect(self.hide_window)
        self.ui.maximize_btn.clicked.connect(self.maximize)
        self.mouse_press_pos = None  # To track mouse position
        self.mouse_dragging = False  # To track if the window is being dragged
        self.ui.close_btn.clicked.connect(self.close_window) 
         
        self.ui.create_playlist.clicked.connect(self.menu_popup)
        self.ui.listButton.clicked.connect(self.menu_popup_sort)
        self.ui.search_bar_2.textChanged.connect(self.controller_playlist.search_by_name_playlist)
        self.ui.moreoptions.clicked.connect(self.menu_popup_more_options)
        
        self.ui.search_area_playlist.textChanged.connect(self.search_songs)
        self.ui.play_btn_in_playlist.clicked.connect(self.open_youtube_link)
        # Add HoverFrame to the QStackLayout
        
        self.ui.sort_btn_playlist.clicked.connect(self.menu_popup_sorting)
        
        self.ui.searchPlaceHolder.textChanged.connect(self.search_songs_library)
        self.ui.button_home.clicked.connect(self.show_library)
        self.show_library(self.library)
        #self.setup_playlist_connections()
        self.refresh_playlist_items()
        self.display_list_items_2()
        
        self.center_window()
    
    def display_song_items_library(self, library): 
        self.ui.list_show_song_in_playlist.clear()
        
        self.hide_no_results_found()
        try:
            # Get the list of Song objects from the library
            song_objects = self.library.get_all_songs() 
        
            for idx, song in enumerate(song_objects, start=1):
                # Ensure song is a Song object with expected attributes
                self.create_song_item(
                    title=song.name_song, 
                    artist=song.artists, 
                    album=song.album,
                    release_year=song.release_year,
                    duration=song.get_duration(), 
                    pic=r"image\default-playlist.png", 
                    idx=idx
                )
        except Exception as e:
            print(f"Error displaying songs: {e}")
    
    def search_songs_library(self):
        if self.current_playlist:
            self.current_playlist = None
        keyword = self.ui.searchPlaceHolder.text().strip().lower().replace(" ", "")  

        # Proceed with search if a valid playlist is selected
        object_songs = self.library.get_songs_search(keyword)
    
        # Clear the current list of songs (QListWidget)
        self.ui.list_show_song_in_playlist.clear()

        if object_songs:
            # Display the found songs
            self.hide_no_results_found()
            for idx, song in enumerate(object_songs, start=1):
                self.create_song_item(
                    title=song.name_song, 
                    artist=song.artists, 
                    album=song.album,
                    release_year=song.release_year,
                    duration=song.get_duration(), 
                    pic=r"image\default-playlist.png", 
                    idx=idx
                )
            
        else:
            # If no songs are found, show the "No results found" label
            self.add_no_results_label_songs_playlist()
            if keyword == "":
                self.hide_no_results_found()
                self.show_library(self.library)
    
    def show_library(self, library):
        self.current_playlist = None
        selected_frame = self.selected_frame() if self.selected_frame else None
            
            # Deselect the previous frame if it exists and is not deleted
        if selected_frame and not selected_frame._is_deleted():
            selected_frame.set_selected(False)
            
        self.hide_no_results_found()
        # new_search_area_playlist = self.ui.search_area_playlist
        # new_search_area_playlist.textChanged.connect(self.search_songs_library)
        self.ui.list_show_song_in_playlist.clear()
        self.display_song_items_library(library)
        # Hide and remove the placeholder if it exists
        self.ui.main_content.setStyleSheet(generate_gradient_css(r"image\default-library.png"))
        
        self.ui.image_label.setScaledContents(True)
        self.ui.image_label.setWordWrap(False)
        self.ui.image_label.setMargin(4)
        # Create rounded image
        
        pixmap = QPixmap(r"image\default-library.png")
        
        # Scale pixmap to desired size
        scaled_pixmap = pixmap.scaled(160, 160, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        
        # Create mask for rounded corners
        target = QPixmap(scaled_pixmap.size())
        target.fill(Qt.transparent)
        
        path = QPainterPath()
        path.addRoundedRect(target.rect(), 8, 8)  # radius = 25 for circular image
        
        painter = QPainter(target)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, scaled_pixmap)
        painter.end()
        
        # Set the rounded image to label
        
        self.ui.image_label.setPixmap(target)
        
        self.ui.image_label.setText("")
        self.ui.public_playlist.setText(QCoreApplication.translate("MainWindow", u"Public Library", None))
        self.ui.name_playlist_label.setText(QCoreApplication.translate("MainWindow", u"Library", None))
        
        
        self.ui.time_total.setText(QCoreApplication.translate("MainWindow", convert_time(self.library.get_total_durations()), None))
        self.ui.play_btn_in_playlist.setText("")
        self.ui.search_area_playlist.setText("")
        self.ui.search_area_playlist.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  search song in library", None))
        self.ui.search_btn_playlist.setText("")
        self.ui.sort_btn_playlist.setText("")
        self.ui.label_2.setText(QCoreApplication.translate("MainWindow", u"#", None))
        self.ui.pushButton.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.ui.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Album", None))
        self.ui.pushButton_3.setText("")
        self.ui.search_area_playlist.hide()
        self.ui.search_btn_playlist.hide()
        self.ui.remove_playlist_from_library.hide()
        self.ui.moreoptions.hide()
    
    
    def init_hover_frame(self, hover_frame, play_button):
        # This is where we can add more functionality for handling hover and selection behavior
        # Example: Connect hover events to show/hide the play button
        self.play_button.setVisible(False)  # Initially hide the play button

        # Example of adding hover and selection handling to the frame (in case you are creating items dynamically)
        def handle_hovered(is_hovered):
            self.play_button.setVisible(is_hovered)
        
        # Assuming you create a HoverFrame here or elsewhere  # You can pass any ID
        hover_frame.hovered.connect(handle_hovered)
    
    def menu_popup_sorting(self):
        global_position = self.ui.second_area_playlist.mapToGlobal(QPoint(850, 0))
        self.menu = Menu()
        self.menu.add_menu_item("Sort by Name (Ascending)", self.library.sort_by_name_ascending)
        self.menu.add_menu_item("Sort by Name (Descending)", self.library.sort_by_name_descending)
        self.menu.add_menu_item("Sort by artists (Ascending)", self.library.sort_by_artist_ascending)
        self.menu.add_menu_item("Sort by artists (Descending)", self.library.sort_by_artist_descending)
        self.menu.add_menu_item("Sort by Album (Ascending)", self.library.sort_by_album_descending)
        self.menu.add_menu_item("Sort by Album (Descending)", self.library.sort_by_album_descending)
        self.menu.show_menu(global_position)
    
    def menu_popup_more_options(self):
        global_position = self.ui.second_area_playlist.mapToGlobal(QPoint(160, 22))
        self.menu = Menu()
        self.menu.add_menu_item("✅ Remove From Your Library", self.on_remove_playlist_clicked)
        self.menu.add_menu_item("Recommendations", self.controller_playlist.open_recommendations)
        self.menu.add_menu_item("Rename the playlist and add link youtube", lambda: self.controller_playlist.on_clicked_rename_popup(self.current_playlist.name_playlist))
        self.menu.add_menu_item("Change the image of Playlist", self.controller_playlist.change_image_path)
        self.menu.show_menu(global_position)
    
    def menu_popup_sort(self):
        # Create the menu
        global_position = self.ui.widgets_with_full.mapToGlobal(QPoint(300, 50))
        self.menu = Menu(self)
        self.menu.add_menu_item("Sort by Alphabetical ascending", self.controller_playlist.sort_by_name_ascending)
        self.menu.add_menu_item("Sort by Alphabetical descending", self.controller_playlist.sort_by_name_descending)
        
        # Show the menu
        self.menu.show_menu(global_position)
        
    def show_playlists_search(self, playlists):
        self.ui.list_avatar_item_2.clear()
        if playlists == []:
            self.add_no_results_label()
            return  # No need to continue if no playlists are found
        # Iterate over the playlists and create a list item for each
        for playlist in playlists:
            list_title = playlist.name_playlist
            desc = playlist.description
            pic = playlist.image_path
            id_playlist = playlist.id_playlist  # Ensure to get the id from the playlist data
            self.create_list_item(list_title, desc, pic, id_playlist)
            
            
        
        get_name_playlist = self.ui.search_bar_2.text().lower().strip().replace(" ", "")
        selected_playlist = self.controller_playlist.get_playlist_by_name(get_name_playlist)
        if selected_playlist:
            self.show_playlist(selected_playlist)
        else:
            return    
        
    def menu_popup(self):
        self.menu = QMenu(self)
        create_playlist_action = QAction("Create a new playlist", self)     
        create_playlist_action.triggered.connect(self.controller_playlist.create_playlist)
        self.menu.addAction(create_playlist_action)
        
        self.menu.popup(self.ui.widgets_with_full.mapToGlobal(QPoint(300, 50)))
        self.menu.setStyleSheet("""
            QMenu {
                background-color: #282828;
                border: none;
                color: white;
            }
            
            QMenu::item {
                padding: 10px 20px;
            }
            QMenu::item:hover {
                background-color: #3e3e3e;
            }                    
            QMenu::item:selected {
                background-color: #4e4e4e;
            }

            QMenu::submenu {
                background-color: #282828;
            }
            QMenu::submenu:hover {
                background-color: #3e3e3e;
            }    
        """)      
        
    def center_window(self):
        # Get the screen geometry
        screen = QScreen.availableGeometry(QApplication.primaryScreen())
        # Calculate the center point
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        # Move the window to the center
        self.move(x, y)
        
    def hide_window(self):
        self.showMinimized()
        
    def maximize(self):
        if self.is_maximized:
            self.showNormal()
            self.resize(self.initial_size)
            self.is_maximized = False
        else:
            self.showMaximized()
            self.is_maximized = True 
    def mousePressEvent(self, event): 
        if event.button() == Qt.LeftButton:
            self.offset = QPoint(event.position().x(),event.position().y())
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:

            self.move(self.pos() + QPoint(event.scenePosition().x(),event.scenePosition().y()) - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

    def close_window(self):
        exit()
    
    def set_selected_frame(self, hover_frame):
        # Tạo tham chiếu yếu tới hover_frame
        self.selected_frame = weakref.ref(hover_frame)
    
    def set_selected_playing_frame(self, hover_frame):
        self.current_playing_frame = weakref.ref(hover_frame)
    
    def on_item_selected_1(self, hover_frame, selected):
        """
        Handle playlist selection.
        When a playlist is selected, it updates the UI to show that playlist's songs.
        """
        self.hide_no_results_found()
        try:
            # Dereference the selected frame if it exists
            selected_frame = self.selected_frame() if self.selected_frame else None
            
            # Deselect the previous frame if it exists and is not deleted
            if selected_frame and not selected_frame._is_deleted():
                selected_frame.set_selected(False)
            
            if selected:  # If this playlist is being selected
                # Update the selected frame reference
                
                self.selected_frame = weakref.ref(hover_frame)
                
                # Get the playlist ID from the hover frame
                playlist_id = hover_frame.id

                # Fetch the playlist from the controller using the ID
                selected_playlist = self.controller_playlist.get_playlist(playlist_id)
                
                self.on_playlist_selected(selected_playlist)
                if selected_playlist:
                    # Display the selected playlist
                    self.show_playlist(selected_playlist)
                    
                    # Display the songs from the selected playlist
                    self.display_song_items_1(selected_playlist)
                else:
                    print("Playlist not found.")
            else:
                # If the item is deselected, reset the selected frame
                self.selected_frame = None
                
        except Exception as e:
            print(f"Error in playlist selection: {e}")


    def on_song_selected(self, hover_frame, selected):
        try:
            # Get the currently selected song frame (if it exists)
            if hasattr(self, 'selected_song_frame'):
                # Dereference the weakref to get the actual object
                selected_song_frame = self.selected_song_frame() if isinstance(self.selected_song_frame, weakref.ref) else self.selected_song_frame
            else:
                selected_song_frame = None
            
            # If the song is being selected
            if selected:
                # Deselect the previously selected song (if exists)
                if selected_song_frame and hasattr(selected_song_frame, 'set_selected'):
                    selected_song_frame.set_selected(False)
                    selected_song_frame.setStyleSheet("background-color: #121212;")  # Reset the style of the previously selected song
                
                # Store the newly selected song frame using weakref (avoid circular references)
                self.selected_song_frame = weakref.ref(hover_frame)
                
                # Apply the selection style to the new song
                hover_frame.set_selected(True)
                hover_frame.setStyleSheet("background-color: #383838;")  # Highlight the selected song frame
                
                # Optionally, store additional information such as song ID
                song_id = hover_frame.id
                # Additional logic for the selected song (e.g., update UI, play the song, etc.)
                #print(f"Song selected with ID: {song_id}")
            
            else:
                # If deselected, clear the selected frame reference and reset its style
                if hover_frame == selected_song_frame:
                    self.selected_song_frame = None
                    hover_frame.setStyleSheet("background-color: #121212;")  # Reset the style of the deselected song frame
                
        except Exception as e:
            print(f"Error in song selection: {e}")

    def on_item_selected(self, hover_frame, selected):
        """
        Handle single item selection with moving highlight
        """
        try:
            # Get previously selected frame
            selected_frame = self.selected_frame() if self.selected_frame else None
            
            # If there's a previously selected frame, deselect it
            if selected_frame and not selected_frame._is_deleted():
                selected_frame.set_selected(False)
                #selected_frame.setStyleSheet("background-color: #2b2727;")  # Reset style
            
            # When item is clicked (selected)
            if selected:
                # Update selected frame reference
                self.selected_frame = weakref.ref(hover_frame)
                
                # Highlight newly selected item
                hover_frame.set_selected(True)
                hover_frame.setStyleSheet("background-color: #383838;")  # Selected style
                
                # Get the playlist ID and update content
                playlist_id = hover_frame.id
                selected_playlist = self.controller_playlist.get_playlist(playlist_id)
                
                if selected_playlist:
                    self.current_playlist = selected_playlist
                    self.display_song_items_1(selected_playlist)
                    
            else:
                self.selected_frame = None
                #hover_frame.setStyleSheet("background-color:  #383838;")  # Reset style
                
        except Exception as e:
            print(f"Error in item selection: {e}")

    
    def setup_playlist_connections(self):
        """
        Connect click events for playlist items.
        """
        # Assuming you have a list widget for playlists called list_playlists
        self.ui.list_avatar_item_2.itemClicked.connect(self.on_item_selected_1)
      
    def on_remove_playlist_clicked(self):
        """Handle the remove playlist button click."""
        try:
            # Check if a playlist is selected
            if hasattr(self, 'current_playlist') and self.current_playlist:
                # Pass the selected playlist to the controller for removal
                playlist_id = self.current_playlist.id_playlist
                self.controller_playlist.remove_playlist(playlist_id)
                
                # Optionally, update the UI to remove the playlist from the list
                self.refresh_playlist_items()
                self.display_list_items_2()
            else:
                print("No playlist selected for removal.")
        except Exception as e:
            print(f"Error in removing playlist: {e}")    
    
    def on_clicked_open_option_2_song(self, current_playlist):
        try:
            #create instance of OptionSong Widget
            if current_playlist is None:
                current_playlist = self.library.get_all_songs() #songs object not IDs
                self.open_songs_options_2 = OptionSong2(current_playlist, self.ui, self)
                
                self.open_songs_options_2.show()

            elif current_playlist is not None:
                songs_ids = current_playlist.songs
                songs_objects = list(set(self.controller_playlist.get_songs_by_ids(songs_ids)))
            
                self.open_songs_options_2 = OptionSong2(songs_objects, self.ui, self)
                self.open_songs_options_2.set_current_playlist_name_option2(current_playlist.name_playlist)
                self.open_songs_options_2.show() #test open widget

            else:
                print("There is no current Playlist")
        except:
            print("There is unexpected error in option 2")
            
    def on_clicked_open_option_1_song(self, current_playlist):
        try:
        #create instance of OptionSong Widget
            if current_playlist is None:
                current_playlist = self.library.get_all_songs() #songs object not IDs
                
                self.open_songs_options = OptionSong(current_playlist, self.ui, self)
                
                self.open_songs_options.show()

            elif current_playlist is not None:
                songs_ids = current_playlist.songs
                songs_objects = list(set(self.controller_playlist.get_songs_by_ids(songs_ids)))
            
                self.open_songs_options = OptionSong(songs_objects, self.ui, self)
                self.open_songs_options.set_current_playlist_name(current_playlist.name_playlist)
                self.open_songs_options.show() #test open widget

            else:
                print("There is no current Playlist")
        except:
            print("There is unexpected error in option 1")
            
    def on_item_hovered(self, hovered_frame, hovered):
        # Update hover state for the frame
        hovered_frame.set_hovered(hovered)         
# test area
    def clear_selection(self):
        """Clear current selection safely"""
        if self.selected_frame and not self.selected_frame._is_deleted():
            self.selected_frame.set_selected(False)
        self.selected_frame = None

    def cleanup_frames(self):
        """Remove any deleted frames from tracking"""
        self.frames = weakref.WeakSet(frame for frame in self.frames 
                                    if not frame._is_deleted())
        
    def create_rounded_image_label(image_path, radius=5):  # Đặt radius nhỏ hơn
        # Tạo QLabel và load hình ảnh từ đường dẫn
        label = QLabel()
        pixmap = QPixmap(image_path)
        
        if pixmap.isNull():
            print(f"Error: Unable to load image at {image_path}")
            return label
        
        # Tạo một QPixmap mới với kích thước giống hình gốc và nền trong suốt
        target = QPixmap(pixmap.size())
        target.fill(Qt.transparent)
        
        # Tạo một QPainterPath để bo tròn góc nhẹ
        path = QPainterPath()
        path.addRoundedRect(target.rect(), radius, radius)  # Sử dụng radius nhỏ hơn
        
        # Vẽ hình ảnh lên QPixmap với hiệu ứng bo tròn
        painter = QPainter(target)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setClipPath(path)  # Áp dụng path bo tròn
        painter.drawPixmap(0, 0, pixmap)  # Vẽ ảnh gốc lên target
        painter.end()
        
        # Đặt hình ảnh đã bo tròn vào QLabel
        label.setPixmap(target)
    
        return label

    def add_placeholder_to_main_content(self):
        # Clear any existing widgets
            # Check if placeholder already exists
        if hasattr(self, 'placeholder') and self.placeholder and not self.placeholder.isHidden():
            return  # Placeholder is already present

        # Clear any existing widgets in the layout
        layout = self.ui.main_content.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # Create and add the placeholder
        self.placeholder = QLabel("No content available.")
        self.placeholder.setStyleSheet("color: gray; font-style: italic; font-size: 16px;")
        self.placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.placeholder)
    
     
    def show_playlist(self, selected_playlist):
        # Hide and remove the placeholder if it exists
        if selected_playlist is None:
            self.add_no_results_label()
            return
        self.ui.main_content.setStyleSheet(generate_gradient_css(selected_playlist.image_path))
        
        self.ui.image_label.setScaledContents(True)
        self.ui.image_label.setWordWrap(False)
        self.ui.image_label.setMargin(4)
        # Create rounded image
        
        pixmap = QPixmap(selected_playlist.image_path)
        
        # Scale pixmap to desired size
        scaled_pixmap = pixmap.scaled(160, 160, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        
        # Create mask for rounded corners
        target = QPixmap(scaled_pixmap.size())
        target.fill(Qt.transparent)
        
        path = QPainterPath()
        path.addRoundedRect(target.rect(), 8, 8)  # radius = 25 for circular image
        
        painter = QPainter(target)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, scaled_pixmap)
        painter.end()
        
        # Set the rounded image to label
        
        self.ui.image_label.setPixmap(target)
        
        self.ui.image_label.setText("")
        self.ui.public_playlist.setText(QCoreApplication.translate("MainWindow", u"Public Playlist", None))
        self.ui.name_playlist_label.setText(QCoreApplication.translate("MainWindow", selected_playlist.name_playlist, None))
        
        self.songs_ids = self.current_playlist.get_songs()
        if self.songs_ids is None:
            return
        self.songs_objects = list(set(self.controller_playlist.get_songs_by_ids(self.songs_ids)))
        
        self.ui.time_total.setText(QCoreApplication.translate("MainWindow", convert_time(selected_playlist.total_durations(self.songs_objects)), None))
        self.ui.play_btn_in_playlist.setText("")
        self.ui.remove_playlist_from_library.setText("")
        self.ui.moreoptions.setText("")
        self.ui.search_area_playlist.setText("")
        self.ui.search_area_playlist.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  search song in playlist", None))
        self.ui.search_btn_playlist.setText("")
        self.ui.sort_btn_playlist.setText("")
        self.ui.label_2.setText(QCoreApplication.translate("MainWindow", u"#", None))
        self.ui.pushButton.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.ui.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Album", None))
        self.ui.pushButton_3.setText("")
        self.ui.search_btn_playlist.show()
        self.ui.remove_playlist_from_library.show()
        self.ui.moreoptions.show()

    def show_playlist_by_id(self, playlist_id):
        # Lấy playlist từ controller bằng ID
        selected_playlist = self.controller_playlist.get_playlist(playlist_id)
        
        # Nếu playlist tồn tại, gọi hàm `show_playlist` để hiển thị nó
        if selected_playlist:
            self.show_playlist(selected_playlist)
        else:
            print(f"Playlist with ID {playlist_id} not found.")              
    
    def on_playlist_selected(self, playlist):
        # When a playlist is selected, update current_playlist
        self.current_playlist = playlist
    
    def search_songs(self):
        keyword = self.ui.search_area_playlist.text().strip().lower().replace(" ", "")  # Lấy từ khóa tìm kiếm từ QLineEdit
        # Clear the current list of songs (QListWidget)
        """Search songs in the current playlist based on the keyword entered."""
        # Check if current_playlist is None
        #keyword = self.ui.searchPlaceHolder.text().strip().lower().replace(" ", "")
        if self.current_playlist is None:
            self.add_no_results_label_songs_playlist()
            return  # handle this case differently, like showing a message to the user
        ids = self.controller_playlist.get_song_ids(self.current_playlist)
        # Proceed with search if a valid playlist is selected
        object_songs = self.controller_playlist.get_songs_by_ids(ids)
        found_songs = self.current_playlist.find_songs(keyword, object_songs)
        
        # Clear the current list of songs (QListWidget)
        self.ui.list_show_song_in_playlist.clear()

        if found_songs:
            # Display the found songs
            self.hide_no_results_found()
            for idx, song in enumerate(found_songs, start=1):
                self.create_song_item(
                    title=song.name_song, 
                    artist=song.artists, 
                    album=song.album,
                    release_year=song.release_year,
                    duration=song.get_duration(), 
                    pic=r"image\default-playlist.png", 
                    idx=idx
                )
            
        else:
            # If no songs are found, show the "No results found" label
            self.add_no_results_label_songs_playlist()
            if keyword == "":
                self.hide_no_results_found()
                self.display_song_items_1(self.current_playlist)
    
    def display_search_results(self, songs):
        """Hiển thị kết quả tìm kiếm lên giao diện"""
        self.ui.list_show_song_in_playlist.clear()

        if not songs:
            # Nếu không có bài hát nào tìm thấy
            
            self.add_no_results_label_songs_playlist()
        else:
            self.hide_no_results_found()
            # Nếu có bài hát, hiển thị chúng
            for song in songs:
                self.create_song_item(
                    title=song.name_song,
                    artist=song.artists,
                    album=song.album,
                    release_year=song.release_year,
                    duration=song.get_duration(),
                    pic=r"image\default-playlist.png",
                    idx=song.id_song
                )
    
    def add_no_results_label_songs_playlist(self):
        # Remove any previous layout in main_content

        self.ui.list_show_song_in_playlist.clear()
        # Check if the "No results found" label already exists
        existing_label = self.ui.main_content.findChild(QLabel, "no_results_label")
        if existing_label:
                # If the label exists, just show it again
                existing_label.show()
        else:
            label = QLabel("No results found", self.ui.main_content)
            label.setObjectName("no_results_label")
            label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            label.setStyleSheet("""
                QLabel {
                    border : none;
                    background-color: #121212;
                    font-size: 24px;
                    text-align: center;
                    font-weight: bold;
                    color: white;
                }                    
            """)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)

            # Create a new layout for main_content
            layout = QVBoxLayout(self.ui.list_show_song_in_playlist)
            layout.addStretch(1)
            layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addStretch(1)

            # Apply the new layout to main_content
            self.ui.main_content.setLayout(layout)
            
            # Optionally, set label width equal to list_show_song_in_playlist
            label.setFixedWidth(self.ui.list_show_song_in_playlist.width())
    
    def hide_no_results_found(self):
        # Tìm label nếu đã tồn tại và ẩn nó
        existing_label = self.ui.main_content.findChild(QLabel, "no_results_label")
        
        if existing_label:
            existing_label.hide()
    
    def add_no_results_label(self):
    # Check if the layout is already present in icon_name_widget
        layout = self.ui.icon_name_widget.layout()
        # Search for the "No results found" label in the layout
        no_results_label = None
        
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if isinstance(widget, QLabel) and widget.text() == "No results found":
                no_results_label = widget
                break
        
        # If the label doesn't exist, create it
        if not no_results_label:
            no_results_label = QLabel("No results found", self.ui.icon_name_widget)
            
            no_results_label.setStyleSheet("""
                color: white;
                font-style: italic;
                padding: 20px;
                font-size: 20px;
            """)
            
            no_results_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
            layout.addWidget(no_results_label)
            
            
        
        # Ensure the layout contains the QListWidget if not already present
        if isinstance(self.ui.icon_name_widget, QListWidget):
            self.ui.icon_name_widget.setLayout(layout)  # If not, we add the QListWidget
        
    def clear_no_results_label(self):
        """
        Clears the 'No results found' label if present.
        """
        layout = self.ui.icon_name_widget.layout()
        
        # Search for the "No results found" label in the layout
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if isinstance(widget, QLabel) and widget.text() == "No results found":
                layout.removeWidget(widget)  # Remove the label
                widget.deleteLater()  # Optionally delete it to free memory
                break       
            
    def show_playlists_search(self, playlists):
        self.ui.list_avatar_item_2.clear()
        if playlists == []:
            self.add_no_results_label()
            return  # No need to continue if no playlists are found
        # Iterate over the playlists and create a list item for each
        for playlist in playlists:
            list_title = playlist.name_playlist
            desc = playlist.description
            pic = playlist.image_path
            id_playlist = playlist.id_playlist  # Ensure to get the id from the playlist data
            self.create_list_item(list_title, desc, pic, id_playlist)
            
            
        
        get_name_playlist = self.ui.search_bar_2.text().lower().strip().replace(" ", "")
        selected_playlist = self.controller_playlist.get_playlist_by_name(get_name_playlist)
        if selected_playlist:
            self.show_playlist(selected_playlist)
        else:
            return
    
    def refresh_playlist_items_by_sorting_1(self, playlists):
        self.ui.list_avatar_item_2.clear()
        for playlist in playlists:
            list_title = playlist.name_playlist
            desc = playlist.description
            pic = playlist.image_path
            id_playlist = playlist.id_playlist  # Ensure to get the id from the playlist data
            self.create_list_item(list_title, desc, pic, id_playlist)
    
    def refresh_playlist_items_by_sorting_2(self, playlists):
        self.ui.list_avatar_item.clear()
       
        for playlist in playlists:
            pic = playlist.image_path
            idx = playlist.id_playlist
            self.create_list_item_shorten(pic, idx)
    
    def display_list_items_2(self):
        self.ui.list_avatar_item.clear()
        self.playlists = Helper.load_playlist()
              
        for playlist in self.playlists:
            pic = playlist.image_path
            idx = playlist.id_playlist
            self.create_list_item_shorten(pic, idx)
            
    def refresh_playlist_items(self):
        self.ui.list_avatar_item_2.clear()
        self.playlists = Helper.load_playlist()
        for playlist in self.playlists:
            list_title = playlist.name_playlist
            desc = playlist.description
            pic = playlist.image_path
            id_playlist = playlist.id_playlist  # Ensure to get the id from the playlist data
            self.create_list_item(list_title, desc, pic, id_playlist)
        
    
    def create_list_item_shorten(self, pic, idx):
        new_item_shorten = QListWidgetItem()
        new_item_shorten.setSizeHint(QSize(0, 70))
        self.ui.list_avatar_item.addItem(new_item_shorten)
        
        central_widget_2 = QWidget()
        layout_2 = QHBoxLayout(central_widget_2)
        layout_2.setSpacing(0)
        layout_2.setContentsMargins(0, 0, 0, 0)
        
        hover_frame_2 = HoverFrame(id=idx)
        hover_frame_2.update_style()
        hover_frame_2.setStyleSheet("background-color: #121212;")
        hover_frame_2.setFrameShape(QFrame.Shape.NoFrame)
        hover_frame_2.setMaximumHeight(100)
        
        layout_2.addWidget(hover_frame_2)
        
        # Set layout for main_frame
        main_frame_layout_2 = QHBoxLayout(hover_frame_2)
        main_frame_layout_2.setContentsMargins(0, 0, 0, 0)
        
        # Left image frame
        image_frame = QFrame(hover_frame_2)
        image_layout = QHBoxLayout(image_frame)
        image_layout.setContentsMargins(0, 0, 0, 0)
        
        # Create rounded image
        image_label = QLabel(image_frame)
        pixmap = QPixmap(pic)
        
        # Scale pixmap to desired size
        scaled_pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        
        # Create mask for rounded corners
        target = QPixmap(scaled_pixmap.size())
        target.fill(Qt.transparent)
        
        path = QPainterPath()
        path.addRoundedRect(target.rect(), 8, 8)  # radius = 25 for circular image
        
        painter = QPainter(target)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, scaled_pixmap)
        painter.end()
        
        # Set the rounded image to label
        image_label.setPixmap(target)
        image_label.setMaximumSize(50, 50)
        
        image_frame.setStyleSheet("""
            QFrame {
                background-color: transparent;
            }                         
        """)
        image_layout.addWidget(image_label)
        main_frame_layout_2.addWidget(image_frame)
        
        self.ui.list_avatar_item.setItemWidget(new_item_shorten, central_widget_2)
        hover_frame_2.set_hovered(False)  # Start with non-hovered state
        hover_frame_2.selected.connect(lambda selected: self.on_item_selected_1(hover_frame_2, selected))

        # Restore the selected state for the item if it is the currently selected one
        if hover_frame_2 == self.selected_frame:
            hover_frame_2.set_selected(True)
        
    def create_list_item(self, title, desc, pic, idx):
        # Create QListWidgetItem
        new_item = QListWidgetItem()
        new_item.setSizeHint(QSize(0, 100))
        self.ui.list_avatar_item_2.addItem(new_item)

        # Create custom widget for the QListWidgetItem
        central_widget = QWidget()
        layout = QHBoxLayout(central_widget)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        
        # Main frame with layout
        hover_frame = HoverFrame(id=idx)
        hover_frame.update_style()  # Set initial style
        hover_frame.setStyleSheet("background-color: #121212;")
        hover_frame.setFrameShape(QFrame.Shape.NoFrame)
        hover_frame.setMaximumHeight(100)

        
        
        # Set layout for main_frame
        main_frame_layout = QHBoxLayout(hover_frame)
        main_frame_layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(hover_frame)

        # Left image frame
        image_frame = QFrame(hover_frame)
        image_layout = QHBoxLayout(image_frame)
        image_layout.setContentsMargins(3, 0, 0, 0)
        # Create rounded image
        image_label = QLabel(image_frame)
        pixmap = QPixmap(pic)
        
        # Scale pixmap to desired size
        scaled_pixmap = pixmap.scaled(90, 90, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        
        # Create mask for rounded corners
        target = QPixmap(scaled_pixmap.size())
        target.fill(Qt.transparent)
        
        path = QPainterPath()
        path.addRoundedRect(target.rect(), 8, 8)  # radius = 25 for circular image
        
        painter = QPainter(target)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, scaled_pixmap)
        painter.end()
        
        # Set the rounded image to label
        image_label.setPixmap(target)
        image_label.setMaximumSize(90, 90)
        
        image_layout.addWidget(image_label)
        main_frame_layout.addWidget(image_frame)

        
        # Set horizontal stretch for image_frame
        image_frame.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        
        
        image_frame.setStyleSheet("background-color: transparent; border-radius: 40px;")
        main_frame_layout.addWidget(image_frame, 1)
        
        # Right text frame
        text_frame = QFrame(hover_frame)
        text_layout = QVBoxLayout(text_frame)
        text_layout.setContentsMargins(0, 0, 0, 0)
        title_label = QLabel(text_frame)
        title_label.setText(f"   {title}")
        title_label.setStyleSheet("color: #ffffff; font-weight: 800; font-size: 20px;")
        desc_label = QLabel(text_frame)
        desc_label.setText(f"   {desc}")
        desc_label.setStyleSheet("color: #a8a8a8; font-weight: 500; font-size: 15px;")
        text_layout.addWidget(title_label)
        text_layout.addWidget(desc_label)
        main_frame_layout.addWidget(text_frame)


        # Set horizontal stretch for text_frame
        text_frame.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        text_frame.setStyleSheet("background-color: transparent;")
        main_frame_layout.addWidget(text_frame, 6)

        
        layout.addWidget(hover_frame)
        self.ui.list_avatar_item_2.setItemWidget(new_item, central_widget)
        # Track this frame for hover linking
        
        hover_frame.set_hovered(False)  # Start with non-hovered state
        hover_frame.selected.connect(lambda selected: self.on_item_selected_1(hover_frame, selected))

        # Restore the selected state for the item if it is the currently selected one
        if hover_frame == self.selected_frame:
            hover_frame.set_selected(True)
            playlist_id = hover_frame.id

    def on_more_options_song_clicked(self):
        global_position = self.ui.list_show_song_in_playlist.mapToGlobal(QPoint(800, 5))
        self.menu = Menu()

        # Use playlist IDs or names for comparison
        current_playlist = self.current_playlist

        if current_playlist is None:
            
            #current_playlist = self.library.get_all_songs()
            self.menu.add_menu_item("Add Song To Your List", lambda :self.on_clicked_open_option_2_song(current_playlist))
            
        # elif current_playlist == all_songs_playlist:
            
        #     self.menu.add_menu_item("Add Song To Your List", lambda :self.on_clicked_open_option_2_song(self.current_playlist))
       
        elif current_playlist is not None:
            
            self.menu.add_menu_item("Add Song To Your List", lambda :self.on_clicked_open_option_2_song(current_playlist))
            self.menu.add_menu_item("Remove From Your List", lambda :self.on_clicked_open_option_1_song(current_playlist))
            


                    
        self.menu.show_menu(global_position)
        
    
    def create_song_item(self, title, artist, album, duration, release_year, pic, idx):
        # Create QListWidgetItem
        new_item = QListWidgetItem()
        new_item.setSizeHint(QSize(0, 55))
        self.ui.list_show_song_in_playlist.addItem(new_item)
        
        # Create central widget and main layout
        central_widget = QWidget()
        layout = QHBoxLayout(central_widget)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Main hover frame
        hover_frame = HoverFrame(id=idx)
        hover_frame.update_style()
        hover_frame.setStyleSheet("background-color: #2b2727;")
        hover_frame.setFrameShape(QFrame.Shape.NoFrame)
        hover_frame.setMaximumHeight(55)
        
        # Main frame layout with consistent spacing
        main_frame_layout = QHBoxLayout(hover_frame)
        main_frame_layout.setContentsMargins(10, 0, 10, 0)  # Consistent outer margins
        main_frame_layout.setSpacing(15)  # Consistent spacing between all elements
        layout.addWidget(hover_frame)
        
        
        
        # Number ID with fixed width
        number_frame = QFrame(hover_frame)
        number_frame.setFixedSize(20,20)
        stack_layout = QStackedLayout(number_frame)
        
        #stack_layout = QHBoxLayout(number_frame)
        stack_layout.setContentsMargins(0,0,0,0)
        stack_layout.setSpacing(0)
        #number_layout = QHBoxLayout(stack_layout)
        #number_layout.setContentsMargins(0, 0, 0, 0)
        number_label = QLabel(f"{idx}")
        number_label.setStyleSheet("color: #807e7e; font-size: 14px; font-weight: 600;")
        #number_label.setFixedWidth(30)  # Fixed width for consistency
        #number_layout.addWidget(stack_layout)

        play_button = QPushButton("▶")
        play_button.setMaximumWidth(25)
        play_button.setStyleSheet("""
            QPushButton {
                padding: 0px;
                margin-top: 5px;
                color: #d8d8d8;
                font-size: 20px;
            }
            QPushButton:hover {
                color: #d5d5d6; 
            }
            QPushButton:pressed {
                color: white; 
            }
        """)
        
        stack_layout.addWidget(play_button)
        stack_layout.addWidget(number_label)
        stack_layout.setCurrentWidget(number_label)
        
        main_frame_layout.addWidget(number_frame)
        # Image frame with fixed size
        image_frame = QFrame(hover_frame)
        image_layout = QHBoxLayout(image_frame)
        image_layout.setContentsMargins(0, 0, 0, 0)
        image_label = QLabel(image_frame)
        image_label.setPixmap(QPixmap(pic))
        image_label.setScaledContents(True)
        image_label.setFixedSize(50, 50)
        image_layout.addWidget(image_label)
        main_frame_layout.addWidget(image_frame)

        # Title and artist frame with flexible width
        text_frame = QFrame(hover_frame)
        text_layout = QVBoxLayout(text_frame)
        text_layout.setContentsMargins(0, 5, 0, 5)  # Vertical padding
        text_layout.setSpacing(2)  # Space between title and artist
        
        title_label = QLabel(title)
        title_label.setStyleSheet("color: #ffffff; font-weight: bold; font-size: 14px;")
        
        artist_label = QLabel(artist)
        artist_label.setStyleSheet("color: #a8a8a8; font-weight: 500; font-size: 12px;")
        
        text_layout.addWidget(title_label)
        text_layout.addWidget(artist_label)
        text_frame.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        main_frame_layout.addWidget(text_frame)

        # Album frame with fixed width
        album_frame = QFrame(hover_frame)
        album_layout = QHBoxLayout(album_frame)
        album_layout.setContentsMargins(0, 0, 0, 0)
        album_frame.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        album_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)  # Set left alignment
        album_label = QLabel(album)
        album_label.setStyleSheet("""
            QLabel {
                color: #a8a8a8;
                font-weight: 900;
                font-size: 14px;
                text-align: center;  
            }             
            QLabel:hover {
                font-size: 16px;
                color: #fff;
            }
        """)
        album_label.setFixedWidth(200)  # Fixed width for consistency
        album_layout.addWidget(album_label)
        main_frame_layout.addWidget(album_frame)
        
        
        # Release year frame with fixed width
        release_year_frame = QFrame(hover_frame)
        release_year_layout = QHBoxLayout(release_year_frame)
        release_year_layout.setContentsMargins(0, 0, 0, 0)
        release_year_label = QLabel(str(release_year))
        release_year_label.setStyleSheet("""
            QLabel {
                color: #a8a8a8;
                font-weight: 700;
                font-size: 14px;
                text-align: center;
            }             
            QLabel:hover {
                font-size: 16px;
                color: #fff;
            }
        """)
        release_year_label.setFixedWidth(60)  # Fixed width for consistency
        release_year_layout.addWidget(release_year_label)
        main_frame_layout.addWidget(release_year_frame)

        self.more_options_songs = QPushButton("●●●")
        
        # icon_more_options_songs = QIcon()

        # icon_more_options_songs.addFile(r"icons/more-horizontal.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        # more_options_songs.setIcon(icon_more_options_songs)
        # more_options_songs.setIconSize(QSize(20, 20))
        
        self.more_options_songs.setStyleSheet("""
            QPushButton {
                color: gray;
                font-weight: 700;
                font-size: 12px;
                text-align: center;
                padding: 5px;
            }             
            QPushButton:hover {
                color: #fff;
            }
            QPushButton:pressed {
                color: #e8e8e8;
            }
        """)
        self.more_options_songs.setFixedWidth(30)
        main_frame_layout.addWidget(self.more_options_songs, 0, Qt.AlignmentFlag.AlignVCenter)

        # Duration frame with fixed width
        duration_frame = QFrame(hover_frame)
        duration_layout = QHBoxLayout(duration_frame)
        duration_layout.setContentsMargins(0, 0, 0, 0)
        duration_label = QLabel(duration)
        duration_label.setStyleSheet("""
            QLabel {
                color: #a8a8a8;
                font-weight: 700;
                font-size: 14px;
                text-align: center;
            }             
            QLabel:hover {
                font-size: 16px;
                color: #fff;
                font-weight: 800;
                text-decoration: underline;
            }
        """)
        duration_label.setFixedWidth(60)  # Fixed width for consistency
        duration_layout.addWidget(duration_label)
        main_frame_layout.addWidget(duration_frame)
        # Set the custom widget for the QListWidgetItem
        self.ui.list_show_song_in_playlist.setItemWidget(new_item, central_widget)

        is_playing = False

        # Handle button press to play/pause song
        def on_play_button_clicked():
            self.open_youtube_link()
            if self.current_playing_button:
                # Make sure the button is still valid before accessing
                
                try:
                    # Reset the previous button and its style
                    self.current_playing_button.setText("▶")
                    self.current_playing_button.setStyleSheet("""
                        QPushButton {
                            padding: 0px;
                            margin-top: 5px;
                            color: #d8d8d8;
                            font-size: 20px;
                        }
                        QPushButton:hover {
                            color: #d5d5d6;
                        }
                        QPushButton:pressed {
                            color: white;
                        }
                    """)

                    # Reset the previous playing frame
                    if self.current_playing_frame:
                        self.current_playing_frame.set_selected(False)
                except RuntimeError:
                    # The button or frame may have been deleted, clear the reference
                    self.current_playing_button = None
                    #self.current_playing_frame = None
                    
            if self.current_playing_frame:
                try:
                    # Reset the previous frame selection
                    self.current_playing_frame.set_selected(False)
                except AttributeError:
                    # Frame reference is invalid; clear it
                    self.current_playing_frame = None
                    
            # Update the new playing button and frame
            self.current_playing_button = play_button
            self.current_playing_frame = hover_frame
       
            self.current_playing_button.setText("||")  # Change text to pause
            self.current_playing_button.setStyleSheet("""
                QPushButton {
                    padding: 0px;
                    margin: 0px;
                    border: none;
                    font-size: 20px;
                    font-weight: bold;
                    color: #1ed760 ;
                    width: 15px;  
                    height: 15px;  
                }
                QPushButton:hover {
                    color: #35cd6b;
                }
                QPushButton:pressed {
                    color: green;
                }
            """)
            
            # Highlight the new frame and update its selection
            hover_frame.set_selected(True)
            
            
            nonlocal is_playing  # Use the is_playing variable to track the state
            is_playing = not is_playing
            

            if is_playing:
                title_label.setStyleSheet("""
                    color: #1ed760;  
                    font-weight: bold; 
                    font-size: 14px;                   
                """)
                
            else:
                title_label.setStyleSheet("""
                    color: #ffffff;  
                    font-weight: bold; 
                    font-size: 14px;                   
                """)
                self.current_playing_button.setText("▶")  # Change button text back to play
                self.current_playing_button.setStyleSheet("""
                    QPushButton {
                        padding: 0px;
                        margin-top: 5px;
                        color: #d8d8d8;
                        font-size: 20px;
                    }
                    QPushButton:hover {
                        color: #d5d5d6;
                    }
                    QPushButton:pressed {
                        color: white;
                    }
                """)
            
                hover_frame.set_selected(False)
                stack_layout.setCurrentWidget(play_button)  # Keep the play button visible
       
        
        # Connect the button's click event to the toggle function
        play_button.clicked.connect(on_play_button_clicked)
        
        # Handle more options in song like add remove 
        
        self.more_options_songs.clicked.connect(self.on_more_options_song_clicked)
        # Connect hover and selection handling
        hover_frame.set_hovered(False)
        hover_frame.selected.connect(lambda selected: self.on_song_selected(hover_frame, selected))
    
        #self.init_hover_frame(hover_frame, play_button)
        # Toggle play button visibility based on hover
        # Modify hover logic to switch stack layout widgets for this item
        hover_frame.hovered.connect(lambda is_hovered: stack_layout.setCurrentWidget(play_button if is_hovered else number_label))


        
        if hover_frame == self.selected_frame:
            hover_frame.set_selected(True)
            #hover_frame.selected.connect(lambda selected: self.on_song_selected(hover_frame, selected))
            
            # if hover_frame == self.selected_frame:
            #     hover_frame.set_selected(True)
    
    
    def update_song_hover_style(self, hover_frame, is_hovered):
        if not hover_frame.is_selected:
            hover_frame.setStyleSheet(
                "background-color: #383838;" if is_hovered else "background-color:  #383838;"
            )
            
    def get_selected_song(self):
        if hasattr(self, 'selected_song_frame') and self.selected_song_frame:
            return self.selected_song_frame.id
        return None
                
    def create_songs_items(self, selected_playlist): 
        self.ui.list_show_song_in_playlist.clear()  # Clear existing items in the list
        songs_items = []  # List to hold the song items
        for idx, song in enumerate(selected_playlist, start=1):
            # Extract song information
            title = song.name_song
            artist = song.artists
            album = song.album
            release_year = song.release_year
            duration = song.get_duration()

            # Create the song item and add it to the list
            self.create_song_item(title, artist, album, release_year, duration, idx, song)
            songs_items.append(song)

        return songs_items
                
        # Usage example:

    def display_song_items_1(self, playlist): 
        self.ui.list_show_song_in_playlist.clear()
        self.hide_no_results_found()
        try:
            # Get the list of Song objects from the playlist
            song_ids = self.controller_playlist.get_song_ids(playlist)
            unique_song_ids = list(set(song_ids))
            song_objects = self.controller_playlist.get_songs_by_ids(unique_song_ids)  # Assuming get_songs() returns song IDs
            seen_songs = set()
            unique_songs = []
            
            for song in song_objects:
                if song.id_song not in seen_songs:
                    seen_songs.add(song.id_song)
                    unique_songs.append(song)
            # Iterate over each Song object
            for idx, song in enumerate(unique_songs, start=1):
                # Ensure song is a Song object with expected attributes
                self.create_song_item(
                    title=song.name_song, 
                    artist=song.artists, 
                    album=song.album,
                    release_year=song.release_year,
                    duration=song.get_duration(), 
                    pic=r"image\default-playlist.png", 
                    idx=idx
                )
        except Exception as e:
            print(f"Error displaying songs: {e}")
            
    #test this function in the future will implement to the real App if I have more time
    def on_playlist_button_clicked(self):
        """
        Handles sequential playback of songs in the playlist.
        Assumes `self.current_playlist` contains the frames of the playlist being played.
        """

        if not self.current_playlist:
            print("No playlist selected or playlist is empty.")
            return

        # Initialize playback variables
        self.current_song_index = 0
        self.song_timer = QTimer()  # Timer for controlling playback duration

        def play_next_song():
            if self.current_song_index < len(self.current_playlist.get_songs()):
                song_id = self.current_playlist.get_songs()[self.current_song_index]
                # Retrieve the actual song object by its ID (assuming you have a method for this)
                current_song = self.controller_playlist.find_song_by_id(song_id)  # Replace with your actual function to get the song object
                
                # Now access the frame and play_button of the song object (assuming current_song has these attributes)
                if current_song:
                    current_frame = current_song.frame  # Assuming each song has a 'frame' that represents the song's UI
                    current_button = current_song.play_button  # Assuming each song has a play button
                    
                    # Mark the song as selected
                    current_frame.set_selected(True)
                    current_button.setText("||")  # Show pause button
                    print(f"Playing song {self.current_song_index + 1}")

                    # Now start the timer for the next song
                    song_duration = current_song.duration  # Duration in seconds, adjust as needed
                    self.song_timer.start(song_duration * 1000)  # Start the timer for the next song

                    # Update the current playing song index
                    self.selected_frame = weakref.ref(current_frame)  # Store as weak reference
                    self.current_song_index += 1  # Move to the next song
                else:
                    print(f"Song with ID {song_id} not found.")
            else:
                # Playback completed
                print("Playlist finished.")
                self.song_timer.stop()
                self.selected_frame = None  # Clear selected frame

        # Connect the timer to the function
        self.song_timer.timeout.connect(play_next_song)
        #start with the first
        play_next_song()

    def open_youtube_link(self):
        webbrowser.open(r"https://www.youtube.com/watch?v=hLQl3WQQoQ0&list=PLNHrmMB_UE7pn_JsXU3Ae8W8N_mGfpyri")


    
def clear_layout(widget):
    """Clear the existing layout of the widget."""
    layout = widget.layout()
    if layout:
        for i in range(layout.count()):
            child = layout.itemAt(i).widget()
            if child:
                child.deleteLater()  # Delete child widget
        layout.deleteLater()  # Delete the layout itself   
    
from sklearn.cluster import KMeans
import numpy as np
import cv2
def extract_two_dominant_colors(image_path):
    """Trích xuất 2 màu chủ đạo từ ảnh và trả về 2 màu dạng QColor."""
    # Đọc ảnh và chuyển sang RGB
    image = cv2.imread(image_path)
    if image is None:
        print(f"Không thể đọc ảnh từ {image_path}")
        return None, None

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Reshape ảnh thành 1 chiều để áp dụng K-means
    pixels = image_rgb.reshape(-1, 3)

    # Sử dụng KMeans từ scikit-learn
    kmeans = KMeans(n_clusters=2, random_state=0)
    kmeans.fit(pixels)

    # Lấy các màu sắc chủ đạo từ KMeans
    centers = kmeans.cluster_centers_

    # Chuyển đổi các giá trị màu thành đối tượng QColor
    color1 = QColor(int(centers[0][0]), int(centers[0][1]), int(centers[0][2]))
    color2 = QColor(18,18,18)

    return color1, color2

def generate_gradient_css(image_path):
    """Tạo gradient CSS với 2 màu chủ đạo từ ảnh."""
    # Trích xuất 2 màu chủ đạo từ ảnh
    color1, color2 = extract_two_dominant_colors(image_path)

    # Chuyển đổi màu sắc từ QColor sang mã hex
    color1_hex = color1.name()
    color2_hex = color2.name()

    # Tạo CSS gradient
    gradient_css = f"""
    background: qlineargradient(
        x1: 0, y1: 0, 
        x2: 0, y2: 0.44, 
        stop: 0 {color1_hex}, 
        stop: 1 {color2_hex}
    );
    border-radius: 4px;
    """
    return gradient_css


def convert_time(minute_second):
    # Split the input string into minutes and seconds
    minutes, seconds = map(int, minute_second.split(':'))
    
    # Calculate hours and remaining minutes
    hours = minutes // 60  # Divide by 60 to get the number of hours
    minutes = minutes % 60  # Get the remaining minutes after dividing by 60

    # Return the formatted string as {hour:minute:second}
    return f"{hours:02}:{minutes:02}:{seconds:02}"



# if __name__ == "__main__":
    

#     app = QApplication([])
#     app_icon = QIcon()
#     app_icon.addFile(r"icons\spotify_icon.ico", QSize(30,30))
#     app.setWindowIcon(app_icon)
    
    
#     window = MainWindow()
#     window.show()
#     app.exec()
   