from PySide6.QtWidgets import QMenu
from PySide6.QtGui import QAction
class Menu(QMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
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

    def add_menu_item(self, label, callback=None, enabled=True):
        """
        Add a single menu item with the given label and callback function.
        """
        action = QAction(label, self)
        if callback:
            action.triggered.connect(callback)
        action.setEnabled(enabled)
        self.addAction(action)
        
    def add_separator(self):
        """
        Add a separator line to the menu.
        """
        self.addSeparator()
        
    def show_menu(self, position):
        """
        Show the menu at the given global position.
        """
        self.popup(position)
        
    def add_submenu(self, label, submenu):
        """
        Add a submenu to the current menu.
        :param label: The text for the submenu.
        :param submenu: A QMenu or Menu object to use as the submenu.
        """
        submenu_action = self.addMenu(submenu)
        submenu_action.setTitle(label)