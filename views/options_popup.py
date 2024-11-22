from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QLineEdit, QFrame, QPushButton
from PySide6.QtCore import Qt

import sys


import sys


class OpenOptions(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Playlist Name")
        self.setGeometry(400, 300, 400, 230)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # Main layout
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)   
        layout.setSpacing(0)  
        # Frame 1: Display the current playlist name
        self.name_frame = QFrame()
        self.name_frame.setStyleSheet("background-color: #1e1e1e;")
        name_layout = QVBoxLayout(self.name_frame)
        self.name_frame.setContentsMargins(0, 0, 0, 0)
    
        self.current_name_label = QLabel("Current Playlist: ")
        self.current_name_label.setStyleSheet("color: white; font-size: 16px;")
        name_layout.addWidget(self.current_name_label)

        # Frame 2: Input new playlist name
        self.input_frame = QFrame()
        self.input_frame.setContentsMargins(0, 0, 0, 0)
        
        self.input_frame.setStyleSheet("background-color: #1e1e1e")
        input_layout = QVBoxLayout(self.input_frame)

        self.new_name_input = QLineEdit()
        self.new_name_input.setPlaceholderText("Enter new playlist name...")
        self.new_name_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #555555;
                background-color: #292929;
                color: white;
                font-weight:bold;
            }
        """)
        input_layout.addWidget(self.new_name_input)

        # Button to change the playlist name
        self.update_name_button = QPushButton("Update Playlist Name")
        self.update_name_button.setStyleSheet("""
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

        input_layout.addWidget(self.update_name_button)

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

        # Close button action
        self.close_button.clicked.connect(self.close)
        self.update_name_button.clicked.connect(self.update_playlist_name)
    def set_current_playlist_name(self, name):
        """Set the current playlist name."""
        self.current_name_label.setText(f"Current Playlist: {name}")

    def update_playlist_name(self):
        self.current_name_label.setText(f"Current Playlist: {self.new_name_input.text().strip()}")
        self.close()
        return self.new_name_input.text().strip()

    def get_current_playlist_name(self):
        current_name = self.current_name_label
        return current_name


        