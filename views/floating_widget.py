from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QLabel
from PySide6.QtCore import Qt

class FloatingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Playlist")
        self.setGeometry(400, 400, 1100, 300)

        # Main layout for the widget
        layout = QVBoxLayout(self)

        # Scroll Area
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("background-color: #2C2C2C; border: none;")
        self.scroll_area.setContentsMargins(0, 0, 0, 0)
        
        # Container for the scroll area content
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_widget.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)
        # Label inside the scroll area
        self.label = QLabel(
            """
            Our recommendations help you find audio you’ll enjoy, whether that’s an old favorite or a new song or show you never knew you’d be into. 
            Our editors around the globe have extensive knowledge about music and culture, and make sure our playlists are created with the best listener 
            experience in mind. Our personalized recommendations are tailored to your unique taste, taking into account a variety of factors, such as what 
            you’re listening to and when, the listening habits of people who have similar taste in music and podcasts, and the expertise of our music and 
            podcast specialists. In some cases, commercial considerations may influence our recommendations, but listener satisfaction is our priority 
            and we only ever recommend content we think you’ll want to hear. Our recommendations rely on signals from you, so keep on listening to the songs 
            and podcasts you love!"""
        )
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("""
            font-family: "Promo";
            font-weight: 550;
            font-size: 15px;
            color: white;

        """)

        # Add label to the content layout
        content_layout.addWidget(self.label)

        # Set the scroll area content
        self.scroll_area.setWidget(content_widget)

        # Add scroll area to the main layout
        layout.addWidget(self.scroll_area)
