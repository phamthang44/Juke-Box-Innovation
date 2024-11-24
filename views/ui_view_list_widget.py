# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'maingnVkdX.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################



from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QEventLoop, QTimer, QPropertyAnimation, QEasingCurve)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter, QPainterPath,
    QPalette, QPixmap, QRadialGradient, QTransform, QAction)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QToolButton, QGraphicsDropShadowEffect,
    QVBoxLayout, QWidget, QLabel, QAbstractItemView, QMenu, QScrollBar, QScrollArea, QDialog, QGraphicsScale, QGraphicsWidget, QGraphicsScene, QGraphicsView)

import cv2
import numpy as np

from PySide6.QtCore import Signal, Qt, QThread



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainOalQJR.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

class Ui_MainWindow(object):
        
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Juke Box")
        MainWindow.resize(1650, 900)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setStyleSheet("""
            QWidget {
                background-color: #000000;

            }
        """)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.main_header.sizePolicy().hasHeightForWidth())
        self.main_header.setSizePolicy(sizePolicy)
        self.main_header.setMaximumSize(QSize(2560, 50))
        self.main_header.setStyleSheet("""
            QFrame {
                background-color: #000000;
            }                               
        """)
        self.main_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 4, 0, 0)
        self.search_bar = QFrame(self.main_header)
        self.search_bar.setObjectName(u"search_bar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.search_bar.sizePolicy().hasHeightForWidth())
        self.search_bar.setSizePolicy(sizePolicy1)
        self.search_bar.setMaximumSize(QSize(2400, 60))
        self.search_bar.setStyleSheet(u"#search_bar {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QFrame {\n"
"	height: 60px;\n"
"	width: 700px;\n"
"}")
        self.search_bar.setFrameShape(QFrame.Shape.StyledPanel)
        self.search_bar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.search_bar)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.setting_container = QFrame(self.search_bar)
        self.setting_container.setObjectName(u"setting_container")
        self.setting_container.setMaximumSize(QSize(50, 50))
        self.setting_container.setStyleSheet(u"#setting_container {\n"
"	background-color: #000000;\n"
"}")
        self.setting_container.setFrameShape(QFrame.Shape.WinPanel)
        self.setting_container.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.setting_container)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.more_btn = QPushButton(self.setting_container)
        self.more_btn.setObjectName(u"more_btn")
        self.more_btn.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.more_btn.setStyleSheet(u"#more_btn {\n"
"	border:none;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(r"icons\spotify.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.more_btn.setIcon(icon)
        self.more_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.more_btn, 0, Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_6.addWidget(self.setting_container)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.home_frame = QFrame(self.search_bar)
        self.home_frame.setObjectName(u"home_frame")
        self.home_frame.setMaximumSize(QSize(50, 50))
        self.home_frame.setStyleSheet(u"#home_frame {\n"
"	border:none;\n"
"	border-radius: 20px;\n"
"}")
        self.home_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.home_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.home_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.button_home = QPushButton(self.home_frame)
        self.button_home.setObjectName(u"button_home")
        self.button_home.setEnabled(True)
        self.button_home.setMaximumSize(QSize(47, 42))
        self.button_home.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.button_home.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	padding: 19px;\n"
"	width: 3px;\n"
"	background-color: #1f1f1f;\n"
"	border-radius: 20px;\n"
"	margin-right: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 13px;\n"
"	background-color: #6a6a6a;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_home.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.button_home)


        self.horizontalLayout_6.addWidget(self.home_frame)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.searchFrame = QFrame(self.search_bar)
        self.searchFrame.setObjectName(u"searchFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.searchFrame.sizePolicy().hasHeightForWidth())
        self.searchFrame.setSizePolicy(sizePolicy2)
        self.searchFrame.setMaximumSize(QSize(1500, 46))
        self.searchFrame.setStyleSheet(u"#searchFrame {\n"
"	background-color: #1f1f1f;\n"
"\n"
"}\n"
"QFrame {\n"
"	border-radius: 20px;\n"
"}")
        self.searchFrame.setFrameShape(QFrame.Shape.WinPanel)
        self.searchFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.searchFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.searchBtn = QPushButton(self.searchFrame)
        self.searchBtn.setObjectName(u"searchBtn")
        sizePolicy1.setHeightForWidth(self.searchBtn.sizePolicy().hasHeightForWidth())
        self.searchBtn.setSizePolicy(sizePolicy1)
        self.searchBtn.setMaximumSize(QSize(50, 16777215))
        self.searchBtn.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.searchBtn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	padding: 10px;\n"
"   background-color: transparent"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"	padding: 13px;\n"
"	background-color: #6a6a6a;\n"
"	border-radius: 18px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(r"icons\icons8-search-512.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.searchBtn.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.searchBtn, 0, Qt.AlignmentFlag.AlignVCenter)

        self.searchPlaceHolder = QLineEdit(self.searchFrame)
        self.searchPlaceHolder.setPlaceholderText("What do you want to play?")
        self.searchPlaceHolder.setObjectName(u"searchPlaceHolder")
        self.searchPlaceHolder.setMaximumSize(QSize(400, 40))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        self.searchPlaceHolder.setFont(font)
        self.searchPlaceHolder.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.searchPlaceHolder.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.searchPlaceHolder.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.searchPlaceHolder.setStyleSheet(u"#searchPlaceHolder {\n"
"	background-color: #1f1f1f;\n"
"	color: gray;\n"
"	border-radius: 20px;\n"
"}")
        self.searchPlaceHolder.setFrame(True)

        self.horizontalLayout_5.addWidget(self.searchPlaceHolder)

        self.frame_2 = QFrame(self.searchFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_6.addWidget(self.searchFrame)


        self.horizontalLayout_2.addWidget(self.search_bar, 0, Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer_2 = QSpacerItem(300, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.top_right_btns = QFrame(self.main_header)
        self.top_right_btns.setObjectName(u"top_right_btns")
        self.top_right_btns.setMaximumSize(QSize(150, 16777215))
        self.top_right_btns.setStyleSheet(u"#top_right_btns {\n"
"	background-color: #000000\n"
"}")
        self.top_right_btns.setFrameShape(QFrame.Shape.WinPanel)
        self.top_right_btns.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.hide_window_btn = QPushButton(self.top_right_btns)
        self.hide_window_btn.setObjectName(u"hide_window_btn")
        self.hide_window_btn.setStyleSheet(u"#hide_window_btn {\n"
"	padding: 10px;\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #6d6d6d;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.hide_window_btn.setIcon(icon3)
        self.hide_window_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.hide_window_btn)

        self.maximize_btn = QPushButton(self.top_right_btns)
        self.maximize_btn.setObjectName(u"maximize_btn")
        self.maximize_btn.setStyleSheet(u"#maximize_btn {\n"
"   padding: 10px;\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #6d6d6d\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icons/square.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximize_btn.setIcon(icon4)
        self.maximize_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.maximize_btn)

        self.close_btn = QPushButton(self.top_right_btns)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setStyleSheet(u"#close_btn {\n"
"	padding: 10px;\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(250, 0, 0, 200);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icons/x.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon5)
        self.close_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.close_btn)


        self.horizontalLayout_2.addWidget(self.top_right_btns, 0, Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addWidget(self.main_header)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(9)
        sizePolicy3.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy3)
        self.main_body.setMaximumSize(QSize(2650, 1460))
        self.main_body.setStyleSheet(u"#main_body {\n"
"	background-color: #000000\n"
"}")
        self.main_body.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon_get_only_widget = QWidget(self.main_body)
        self.icon_get_only_widget.setVisible(False)
        self.icon_get_only_widget.setObjectName(u"icon_get_only_widget")
        self.icon_get_only_widget.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.icon_get_only_widget.sizePolicy().hasHeightForWidth())
        self.icon_get_only_widget.setSizePolicy(sizePolicy4)
        self.icon_get_only_widget.setMaximumSize(QSize(65, 16777215))
        self.icon_get_only_widget.setStyleSheet(u"background-color: #0f0f0f; \n"
"border-radius: 5px;")
        self.verticalLayout_2 = QVBoxLayout(self.icon_get_only_widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 0, 0, 0)
        self.widget = QWidget(self.icon_get_only_widget)
        self.widget.setObjectName(u"widget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy5)
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color: #121212;\n"
"}\n"
"QWidget:hover {\n"
"\n"
"	background-color: #6a6a6a;\n"
"}")
        self.horizontalLayout_8 = QHBoxLayout(self.widget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.expand_btn = QPushButton(self.widget)
        self.expand_btn.setObjectName(u"expand_btn")
        self.expand_btn.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: transparent;
                padding: 2px;
            }                           
        """)
        icon6 = QIcon()
        icon6.addFile(u"icons/before_expand_3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.expand_btn.setIcon(icon6)
        self.expand_btn.setCheckable(True)
        self.expand_btn.setAutoExclusive(False)
        self.expand_btn.setIconSize(QSize(30, 30))
        self.horizontalLayout_8.addWidget(self.expand_btn)


        self.verticalLayout_2.addWidget(self.widget)

        self.list_avatar_item = QListWidget(self.icon_get_only_widget)
        self.list_avatar_item.setObjectName(u"list_avatar_item")
        
        scrollbar_list_item = QScrollBar()
        scrollbar_list_item.setStyleSheet("""   
            QScrollBar:vertical {
                border: none;
                background: #121212;
                width: 4px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {                                  
                background: #535353;
                min-height: 30px;
                border-radius: 2px;
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
        self.list_avatar_item.setVerticalScrollBar(scrollbar_list_item)
        self.list_avatar_item.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        
        
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(9)
        sizePolicy6.setHeightForWidth(self.list_avatar_item.sizePolicy().hasHeightForWidth())
        self.list_avatar_item.setSizePolicy(sizePolicy6)
        self.list_avatar_item.setStyleSheet("""
            QListWidget {
                background-color: #0f0f0f;
            }
            
            QListWidget:selected {
                background-color: #2a2a2a;
            }
            
            QListWidget:pressed {
                background-color: #484848;
            }                                    
                                            
        """)

        self.verticalLayout_2.addWidget(self.list_avatar_item)


        self.horizontalLayout.addWidget(self.icon_get_only_widget)

        self.icon_name_widget = QWidget(self.main_body)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(7)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.icon_name_widget.sizePolicy().hasHeightForWidth())
        self.icon_name_widget.setSizePolicy(sizePolicy7)
        self.icon_name_widget.setMaximumSize(QSize(500, 16777215))
        self.icon_name_widget.setStyleSheet(u"background-color: #121212; \n"
"border-radius: 5px;\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widgets_with_full = QWidget(self.icon_name_widget)
        self.widgets_with_full.setObjectName(u"widgets_with_full")
        sizePolicy.setHeightForWidth(self.widgets_with_full.sizePolicy().hasHeightForWidth())
        self.widgets_with_full.setSizePolicy(sizePolicy)
        self.widgets_with_full.setStyleSheet(u"background-color: #121212;\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.widgets_with_full)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, 0, 0, 0)
        self.showLibraryFeatures = QFrame(self.widgets_with_full)
        self.showLibraryFeatures.setObjectName(u"showLibraryFeatures")
        sizePolicy.setHeightForWidth(self.showLibraryFeatures.sizePolicy().hasHeightForWidth())
        self.showLibraryFeatures.setSizePolicy(sizePolicy)
        self.showLibraryFeatures.setFrameShape(QFrame.Shape.WinPanel)
        self.showLibraryFeatures.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.showLibraryFeatures)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_2 = QWidget(self.showLibraryFeatures)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 1, 0)
        self.expand_button = QPushButton(self.widget_2)
        self.expand_button.setObjectName(u"expand_button")
        self.expand_button.setStyleSheet(u"QPushButton {\n"
"	margin-right: 100px;\n"
"   padding : 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	border-radius:2px;\n"
"	background-color:#6a6a6a;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icons/after_expand_3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.expand_button.setIcon(icon7)
        self.expand_button.setIconSize(QSize(30,30))
        self.horizontalLayout_9.addWidget(self.expand_button)
        
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)
        
        self.create_playlist = QPushButton(self.widget_2)
        self.create_playlist.setObjectName(u"create_playlist")
        self.create_playlist.setStyleSheet("""
            QPushButton {
                margin-right: 5px;
            }
            
            QPushButton:hover {
                padding: 5px;
                background-color: #686868;                               
            }
        """)
        
        
        
        
        icon8 = QIcon()
        icon8.addFile(u"icons/plus_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.create_playlist.setIcon(icon8)
        self.create_playlist.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.create_playlist)


        self.verticalLayout_6.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignTop)

        self.area_list_btn = QWidget(self.showLibraryFeatures)
        self.area_list_btn.setObjectName(u"area_list_btn")
        self.horizontalLayout_10 = QHBoxLayout(self.area_list_btn)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.listButton = QPushButton(self.area_list_btn)
        self.listButton.setObjectName(u"listButton")
        self.listButton.setStyleSheet("""
            QPushButton:hover {
                background-color: #686868;
                padding: 5px;
            }                              
        """)
        icon9 = QIcon()
        icon9.addFile(u"icons/list_icon_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.listButton.setIcon(icon9)
        self.listButton.setIconSize(QSize(25, 25))
        self.listButton.setCheckable(False)

        self.horizontalLayout_10.addWidget(self.listButton)


        self.verticalLayout_6.addWidget(self.area_list_btn)


        self.verticalLayout_5.addWidget(self.showLibraryFeatures)
        
        
        
        self.frame = QFrame(self.widgets_with_full)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy11)
        self.frame_3.setMaximumSize(QSize(50, 50))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        
        
        self.search_btn_2 = QPushButton(self.frame)
        self.search_btn_2.setObjectName(u"search_btn_2")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.search_btn_2.sizePolicy().hasHeightForWidth())
        self.search_btn_2.setSizePolicy(sizePolicy8)
        self.search_btn_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.search_btn_2.setStyleSheet("""
            QPushButton {
                padding:3px;
            }
            
            QPushButton:hover {
                background-color: #686868;
                padding: 5px;
            }           
        """)
        self.search_btn_2.setIcon(icon2)
        self.search_btn_2.setIconSize(QSize(40, 40))
        self.search_btn_2.setCheckable(True)
        self.search_btn_2.setAutoExclusive(False)

        self.horizontalLayout_13.addWidget(self.search_btn_2)


        self.horizontalLayout_12.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_12.addWidget(self.frame_6)

        self.search_bar_2 = QLineEdit(self.frame)
        self.search_bar_2.setObjectName(u"search_bar_2")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy12.setHorizontalStretch(5)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.search_bar_2.sizePolicy().hasHeightForWidth())
        self.search_bar_2.setSizePolicy(sizePolicy12)
        self.search_bar_2.setMaximumSize(QSize(250, 16777215))
        self.search_bar_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.search_bar_2.setStyleSheet(u"#search_bar_2 {\n"
"	background-color: #413e4c;\n"
"	color: #c6c5c9;\n"
"	text-align: center\n"
"\n"
"}\n"
"QLineEdit {\n"
"	border-radius: 3px;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #ffffff;\n"
"	border-radius: 3px;\n"
"}\n"
"QLineEdit {\n"
"	padding: 5px;\n"
"}")
        
        self.search_bar_2.setFrame(False)
        self.search_bar_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.search_bar_2.setDragEnabled(False)
        self.search_bar_2.setVisible(False)
        
        self.horizontalLayout_12.addWidget(self.search_bar_2)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy11.setHorizontalStretch(2)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy11)
        self.frame_7.setMaximumSize(QSize(50, 16777215))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_12.addWidget(self.frame_7)


        self.verticalLayout_5.addWidget(self.frame)


        self.verticalLayout_5.addWidget(self.frame)


        self.verticalLayout_3.addWidget(self.widgets_with_full)

        self.list_avatar_item_2 = QListWidget(self.icon_name_widget)
        scrollbar_list_item_2 = QScrollBar()
        scrollbar_list_item_2.setStyleSheet("""
            QScrollBar:vertical {
                border: none;
                background: #121212;
                width: 12px;
                margin: 0px 0px 0px 0px;
            }

            QScrollBar::handle:vertical {
                background: #535353;
                min-height: 30px;
                border-radius: 6px;
            }

            QScrollBar::handle:vertical:hover {
                background: #B3B3B3;
            }

            QScrollBar::add-line:vertical {
                height: 0px;
            }

            QScrollBar::sub-line:vertical {
                height: 0px;
            }

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
                border: none;
            }
        """)
        self.list_avatar_item_2.setVerticalScrollBar(scrollbar_list_item_2)
        self.list_avatar_item_2.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.list_avatar_item_2.setStyleSheet(u"""
             QListWidget {
                background-color: rgb(46, 46, 46);
             }
             QListWidget:hover {
                background-color: #1f1f1f;
             }
            
             QListWidget:selected {
                background-color: #2a2a2a;
             }
            
            
             QListWidget:pressed {
                background-color: #484848;
             }
         """)
        # QListWidgetItem(self.list_avatar_item_2)
        self.list_avatar_item_2.setObjectName(u"list_avatar_item_2")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(6)
        sizePolicy9.setHeightForWidth(self.list_avatar_item_2.sizePolicy().hasHeightForWidth())
        self.list_avatar_item_2.setSizePolicy(sizePolicy9)
        self.list_avatar_item_2.setStyleSheet(u"background-color: #121212")
        self.list_avatar_item_2.setFrameShape(QFrame.Shape.WinPanel)
        self.list_avatar_item_2.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_3.addWidget(self.list_avatar_item_2)


        self.horizontalLayout.addWidget(self.icon_name_widget)

        self.main_content = QFrame(self.main_body)
        self.main_content.setObjectName(u"main_content")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy13.setHorizontalStretch(13)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.main_content.sizePolicy().hasHeightForWidth())
        self.main_content.setSizePolicy(sizePolicy13)
        self.main_content.setStyleSheet(generate_gradient_css(r"image\test_image_playlist.png"))
        self.main_content.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_content.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.main_content)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.main_content)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy9.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy9)
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setStyleSheet(u"background-color : transparent;\n"
"border-radius: 3px;")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 658, 676))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.main_content_header = QFrame(self.scrollAreaWidgetContents)
        self.main_content_header.setObjectName(u"main_content_header")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(2)
        sizePolicy14.setHeightForWidth(self.main_content_header.sizePolicy().hasHeightForWidth())
        self.main_content_header.setSizePolicy(sizePolicy14)
        self.main_content_header.setStyleSheet(u"background-color: transparent;")
        self.main_content_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_content_header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.main_content_header)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.div_store_image = QFrame(self.main_content_header)
        self.div_store_image.setObjectName(u"div_store_image")
        sizePolicy4.setHeightForWidth(self.div_store_image.sizePolicy().hasHeightForWidth())
        self.div_store_image.setSizePolicy(sizePolicy4)
        self.div_store_image.setMaximumSize(QSize(200, 200))
        self.div_store_image.setStyleSheet(u"")
        self.div_store_image.setFrameShape(QFrame.Shape.StyledPanel)
        self.div_store_image.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.div_store_image)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(6, 6, 0, 0)
        self.image_label = QLabel(self.div_store_image)
        self.image_label.setObjectName(u"image_label")
        sizePolicy5.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy5)
        self.image_label.setMaximumSize(QSize(160, 160))
        self.image_label.setScaledContents(True)
        self.image_label.setWordWrap(False)
        self.image_label.setMargin(4)
        self.image_label.setStyleSheet(u"QLabel {\n"
"	border-radius: 60px;\n"
"}")
        pixmap = QPixmap(u"image/test_image_playlist.png")
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
        
        
        self.image_label.setPixmap(target)

        self.verticalLayout_9.addWidget(self.image_label)


        self.horizontalLayout_17.addWidget(self.div_store_image)

        self.show_info_header_right = QFrame(self.main_content_header)
        self.show_info_header_right.setObjectName(u"show_info_header_right")
        sizePolicy15 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy15.setHorizontalStretch(4)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.show_info_header_right.sizePolicy().hasHeightForWidth())
        self.show_info_header_right.setSizePolicy(sizePolicy15)
        self.show_info_header_right.setFrameShape(QFrame.Shape.StyledPanel)
        self.show_info_header_right.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.show_info_header_right)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 9, 0, 0)
        self.div_show_public_playlist = QFrame(self.show_info_header_right)
        self.div_show_public_playlist.setObjectName(u"div_show_public_playlist")
        sizePolicy.setHeightForWidth(self.div_show_public_playlist.sizePolicy().hasHeightForWidth())
        self.div_show_public_playlist.setSizePolicy(sizePolicy)
        self.div_show_public_playlist.setFrameShape(QFrame.Shape.StyledPanel)
        self.div_show_public_playlist.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.div_show_public_playlist)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.public_playlist = QLabel(self.div_show_public_playlist)
        self.public_playlist.setObjectName(u"public_playlist")
        self.public_playlist.setStyleSheet(u"QLabel {\n"
"	color: #fff;\n"
"	font-weight: 600;\n"
"	font-size: 12px;\n"
"	font-family : 'Promo';\n"
"}")

        self.horizontalLayout_14.addWidget(self.public_playlist)


        self.verticalLayout_8.addWidget(self.div_show_public_playlist)

        self.div_show_name_playlist = QFrame(self.show_info_header_right)
        self.div_show_name_playlist.setObjectName(u"div_show_name_playlist")
        sizePolicy16 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(3)
        sizePolicy16.setHeightForWidth(self.div_show_name_playlist.sizePolicy().hasHeightForWidth())
        self.div_show_name_playlist.setSizePolicy(sizePolicy16)
        self.div_show_name_playlist.setFrameShape(QFrame.Shape.StyledPanel)
        self.div_show_name_playlist.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.div_show_name_playlist)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.name_playlist_label = QLabel(self.div_show_name_playlist)
        self.name_playlist_label.setObjectName(u"name_playlist_label")
        self.name_playlist_label.setStyleSheet(u"QLabel {\n"
"	font-size: 55px;\n"
"	color: white;\n"
"	font-weight: 900;\n"
"	font-family: 'Promo';\n"
"}")

        self.horizontalLayout_15.addWidget(self.name_playlist_label)


        self.verticalLayout_8.addWidget(self.div_show_name_playlist)

        self.div_show_total_time = QFrame(self.show_info_header_right)
        self.div_show_total_time.setObjectName(u"div_show_total_time")
        sizePolicy.setHeightForWidth(self.div_show_total_time.sizePolicy().hasHeightForWidth())
        self.div_show_total_time.setSizePolicy(sizePolicy)
        self.div_show_total_time.setFrameShape(QFrame.Shape.StyledPanel)
        self.div_show_total_time.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.div_show_total_time)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.time_total = QLabel(self.div_show_total_time)
        self.time_total.setObjectName(u"time_total")
        self.time_total.setStyleSheet(u"QLabel {\n"
"	color: #999393;\n"
"	font-weight: 600;\n"
"	font-size: 12px;\n"
"	font-family : 'Promo';\n"
"}")

        self.horizontalLayout_16.addWidget(self.time_total)


        self.verticalLayout_8.addWidget(self.div_show_total_time)


        self.horizontalLayout_17.addWidget(self.show_info_header_right)


        self.verticalLayout_7.addWidget(self.main_content_header)

        self.second_area_playlist = QFrame(self.scrollAreaWidgetContents)
        self.second_area_playlist.setObjectName(u"second_area_playlist")
        sizePolicy14.setHeightForWidth(self.second_area_playlist.sizePolicy().hasHeightForWidth())
        self.second_area_playlist.setSizePolicy(sizePolicy14)
        self.second_area_playlist.setStyleSheet(u"background-color: transparent;")
        self.second_area_playlist.setFrameShape(QFrame.Shape.StyledPanel)
        self.second_area_playlist.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.second_area_playlist)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.div_show_features = QFrame(self.second_area_playlist)
        self.div_show_features.setObjectName(u"div_show_features")
        self.div_show_features.setFrameShape(QFrame.Shape.StyledPanel)
        self.div_show_features.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.div_show_features)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(3, 3, 3, 3)
        self.div_store_playbtn = QFrame(self.div_show_features)
        self.div_store_playbtn.setObjectName(u"div_store_playbtn")
        sizePolicy4.setHeightForWidth(self.div_store_playbtn.sizePolicy().hasHeightForWidth())
        self.div_store_playbtn.setSizePolicy(sizePolicy4)
        self.div_store_playbtn.setMaximumSize(QSize(60, 60))
        self.div_store_playbtn.setFrameShape(QFrame.Shape.StyledPanel)
        self.div_store_playbtn.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.div_store_playbtn)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.play_btn_in_playlist = QPushButton(self.div_store_playbtn)
        self.play_btn_in_playlist.setObjectName(u"play_btn_in_playlist")
        self.play_btn_in_playlist.setMaximumSize(QSize(50, 50))
        self.play_btn_in_playlist.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: #1ed760;
                border-radius: 25px;

            }
            QPushButton:hover {
                background-color: #35cd6b;
            } 
            QPushButton:pressed {
                background-color: #18ad4d;
            }                                        
        """)
        icon11 = QIcon()
        icon11.addFile(u"icons/play-button-arrowhead.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_btn_in_playlist.setIcon(icon11)
        self.play_btn_in_playlist.setIconSize(QSize(16, 16))

        self.horizontalLayout_21.addWidget(self.play_btn_in_playlist)


        self.horizontalLayout_23.addWidget(self.div_store_playbtn)

        self.div_store_options = QFrame(self.div_show_features)
        self.div_store_options.setObjectName(u"div_store_options")
        sizePolicy5.setHeightForWidth(self.div_store_options.sizePolicy().hasHeightForWidth())
        self.div_store_options.setSizePolicy(sizePolicy5)
        self.div_store_options.setFrameShape(QFrame.Shape.StyledPanel)
        self.div_store_options.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.div_store_options)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.remove_playlist_from_library = QPushButton(self.div_store_options)
        self.remove_playlist_from_library.setObjectName(u"remove_playlist_from_library")
        self.remove_playlist_from_library.setStyleSheet(u"QPushButton {\n"
"	padding: 4px;\n"
"	background-color: #1ed760;\n"
"	border: none;\n"
"	border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #35cd6b;\n"
"}"
"QPushButton:pressed {\n"
"	background-color: #18ad4d;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"icons/icons8-check-500.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.remove_playlist_from_library.setIcon(icon12)
        self.remove_playlist_from_library.setIconSize(QSize(16, 20))

        self.horizontalLayout_22.addWidget(self.remove_playlist_from_library)

        self.moreoptions = QPushButton(self.div_store_options)
        self.moreoptions.setObjectName(u"moreoptions")
        self.moreoptions.setStyleSheet("""
                QPushButton {
                    padding: 3px;
                    margin-left: 10px
                }                
                QPushButton:hover {
                    background-color: #686868;
                }               
        """)
        self.moreoptions.setIcon(icon)
        self.moreoptions.setIconSize(QSize(20, 20))
        self.moreoptions.setCheckable(True)

        self.horizontalLayout_22.addWidget(self.moreoptions)


        self.horizontalLayout_23.addWidget(self.div_store_options)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_6)

        self.search_area_playlist = QLineEdit(self.div_show_features)
        self.search_area_playlist.setObjectName(u"search_area_playlist")
        sizePolicy17 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(0)
        sizePolicy17.setHeightForWidth(self.search_area_playlist.sizePolicy().hasHeightForWidth())
        self.search_area_playlist.setSizePolicy(sizePolicy17)
        self.search_area_playlist.setMaximumSize(QSize(150, 30))
        self.search_area_playlist.setStyleSheet(u"QLineEdit {\n"
"	background-color: #413e4c;\n"
"	color: #c6c5c9;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ffffff;\n"
"	border-radius: 3px;\n"
"}")
        self.search_area_playlist.setDragEnabled(False)
        self.search_area_playlist.setVisible(False)
        
        self.horizontalLayout_23.addWidget(self.search_area_playlist)

        self.div_store_sub_features = QFrame(self.div_show_features)
        self.div_store_sub_features.setObjectName(u"div_store_sub_features")
        sizePolicy4.setHeightForWidth(self.div_store_sub_features.sizePolicy().hasHeightForWidth())
        self.div_store_sub_features.setSizePolicy(sizePolicy4)
        self.div_store_sub_features.setMaximumSize(QSize(95, 80))
        self.div_store_sub_features.setFrameShape(QFrame.Shape.StyledPanel)
        self.div_store_sub_features.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.div_store_sub_features)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.div_store_search_btn = QFrame(self.div_store_sub_features)
        self.div_store_search_btn.setObjectName(u"div_store_search_btn")
        self.div_store_search_btn.setMaximumSize(QSize(65, 50))
        self.div_store_search_btn.setFrameShape(QFrame.Shape.StyledPanel)
        self.div_store_search_btn.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.div_store_search_btn)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.search_btn_playlist = QPushButton(self.div_store_search_btn)
        self.search_btn_playlist.setObjectName(u"search_btn_playlist")
        self.search_btn_playlist.setMaximumSize(QSize(30, 30))
        self.search_btn_playlist.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #3a3844;\n"
"	border-radius: 15px;\n"
"}")
        self.search_btn_playlist.setCheckable(True)
        self.search_btn_playlist.setAutoExclusive(False)
        
        icon13 = QIcon()
        icon13.addFile(u"icons/icons8-search-512.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_btn_playlist.setIcon(icon13)
        
        self.horizontalLayout_19.addWidget(self.search_btn_playlist)


        self.horizontalLayout_18.addWidget(self.div_store_search_btn)

        self.div_store_sort = QFrame(self.div_store_sub_features)
        self.div_store_sort.setObjectName(u"div_store_sort")
        self.div_store_sort.setMaximumSize(QSize(50, 50))
        self.div_store_sort.setFrameShape(QFrame.Shape.StyledPanel)
        self.div_store_sort.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.div_store_sort)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.sort_btn_playlist = QPushButton(self.div_store_sort)
        self.sort_btn_playlist.setObjectName(u"sort_btn_playlist")
        self.sort_btn_playlist.setMaximumSize(QSize(30, 30))
        self.sort_btn_playlist.setStyleSheet("""
                QPushButton {
                    padding: 3px;
                }                
                QPushButton:hover {
                    border-radius: 15px;
                    background-color: #dde6e1;
                }                     
        """)
        icon14 = QIcon()
        icon14.addFile(u"icons/list_icon_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sort_btn_playlist.setIcon(icon14)

        self.horizontalLayout_20.addWidget(self.sort_btn_playlist)


        self.horizontalLayout_18.addWidget(self.div_store_sort)


        self.horizontalLayout_23.addWidget(self.div_store_sub_features)


        self.verticalLayout_10.addWidget(self.div_show_features)

        self.div_show_info_songs = QFrame(self.second_area_playlist)
        self.div_show_info_songs.setObjectName(u"div_show_info_songs")
        self.div_show_info_songs.setStyleSheet(u"")
        self.div_show_info_songs.setFrameShape(QFrame.Shape.StyledPanel)
        self.div_show_info_songs.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.div_show_info_songs)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_2 = QLabel(self.div_show_info_songs)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: #ffffff;\n"
"font-weight: 500; font-size: 15px;")

        self.horizontalLayout_24.addWidget(self.label_2)

        self.pushButton = QPushButton(self.div_show_info_songs)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton:hover {\n"
"	color: #999393;\n"
"}\n"
"QPushButton {\n"
"   font-size: 15px;\n"
"	font-weight: 600;\n"
"	border: none;\n"
"	padding: 10px;\n"
"	color: #ffffff;\n"
"}")

        self.horizontalLayout_24.addWidget(self.pushButton)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_7)

        self.pushButton_2 = QPushButton(self.div_show_info_songs)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton:hover {\n"
"	color: #999393;\n"

"}\n"
"QPushButton {\n"
"	font-weight: 600;\n"
"   font-size: 15px;\n"
"	border: none;\n"
"	padding: 10px;\n"
"	color: #ffffff;\n"
"}")

        self.horizontalLayout_24.addWidget(self.pushButton_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_8)

        self.pushButton_3 = QPushButton(self.div_show_info_songs)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(24, 24))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"   padding: 4px;\n"
"}\n"
"QPushButton:hover{\n"
"   border-radius: 9px;\n"
"   background-color: #383838;\n"
"\n"
"}")    
        
        icon15 = QIcon()
        icon15.addFile(r"icons\icons8-clock-500.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon15)
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setAutoRepeat(False)
        self.pushButton_3.setAutoExclusive(False)

        self.line = QFrame()
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setStyleSheet("background-color: #686868; height: 0px;")
        self.horizontalLayout_24.addWidget(self.pushButton_3)
        

        self.verticalLayout_10.addWidget(self.div_show_info_songs)
        self.verticalLayout_10.addWidget(self.line)

        self.verticalLayout_7.addWidget(self.second_area_playlist)

        self.list_show_song_in_playlist = QListWidget(self.scrollAreaWidgetContents)
        self.list_show_song_in_playlist.setObjectName(u"list_show_song_in_playlist")
        sizePolicy18 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy18.setHorizontalStretch(0)
        sizePolicy18.setVerticalStretch(5)
        sizePolicy18.setHeightForWidth(self.list_show_song_in_playlist.sizePolicy().hasHeightForWidth())
        self.list_show_song_in_playlist.setSizePolicy(sizePolicy18)
        self.list_show_song_in_playlist.setStyleSheet(u"background-color: transparent;;")

        
        scrollbar_show_songs_in_playlist = QScrollBar()
        scrollbar_show_songs_in_playlist.setStyleSheet("""   
            QScrollBar:vertical {
                border: none;
                background: #121212;
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
        self.list_show_song_in_playlist.setVerticalScrollBar(scrollbar_show_songs_in_playlist)
        self.list_show_song_in_playlist.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        
        self.verticalLayout_7.addWidget(self.list_show_song_in_playlist)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.main_content)


        self.verticalLayout.addWidget(self.main_body)

        self.main_footer = QFrame(self.centralwidget)
        self.main_footer.setObjectName(u"main_footer")
        sizePolicy.setHeightForWidth(self.main_footer.sizePolicy().hasHeightForWidth())
        self.main_footer.setSizePolicy(sizePolicy)
        self.main_footer.setMinimumSize(QSize(0, 100))
        self.main_footer.setMaximumSize(QSize(16777215, 16777215))
        self.main_footer.setStyleSheet("""
            QFrame {
                background-color: #000000;
                border-radius: 3px;
            }                               
        """)
        self.main_footer.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_footer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.main_footer)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        # self.frame_5 = QFrame(self.main_footer)
        # self.frame_5.setObjectName(u"frame_5")
        # self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        # self.frame_5.setFrameShadow(QFrame.Shadow.Raised)

        # self.horizontalLayout_11.addWidget(self.frame_5)

        # self.frame_4 = QFrame(self.main_footer)
        # self.frame_4.setObjectName(u"frame_4")
        # self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        # self.frame_4.setFrameShadow(QFrame.Shadow.Raised)

        # self.horizontalLayout_11.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.main_footer, 0, Qt.AlignmentFlag.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.expand_btn.clicked.connect(self.icon_name_widget.show)
        self.expand_btn.clicked.connect(self.icon_get_only_widget.hide)
        self.search_btn_2.toggled.connect(self.search_bar_2.setVisible)
        # self.search_btn_2.toggled.connect(self.search_bar_2.setHidden)
        self.search_btn_playlist.toggled.connect(self.search_area_playlist.setVisible)
        # self.search_btn_playlist.toggled.connect(self.search_area_playlist.setHidden)
        self.expand_button.clicked.connect(self.icon_name_widget.hide)
        self.expand_button.clicked.connect(self.icon_get_only_widget.show)
        
        self.search_btn_2.setDefault(False)

        
        #self.selected_frame = None  # Track the currently selected frame
        #playlists store playlist 
        #playlists = [playlist, playlist]
        #playlist -> (name, image, desc)
        
        #self.add_placeholder_to_main_content()
        QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.more_btn.setText("")
        self.button_home.setText("")
        self.searchBtn.setText("")
        self.searchPlaceHolder.setText("")
        self.searchPlaceHolder.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  What do you want to play?", None))
        self.hide_window_btn.setText("")
        self.maximize_btn.setText("")
        self.close_btn.setText("")
        self.expand_btn.setText("")

        self.expand_button.setText("")
        self.create_playlist.setText("")
        self.listButton.setText("")
        self.search_btn_2.setText("")
        self.search_bar_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search in Library", None))
        
        self.image_label.setText("")
        self.public_playlist.setText(QCoreApplication.translate("MainWindow", u"Public Playlist", None))
        self.name_playlist_label.setText(QCoreApplication.translate("MainWindow", u"Library", None))
        self.time_total.setText(QCoreApplication.translate("MainWindow", u"Time durations total", None))
        self.play_btn_in_playlist.setText("")
        self.remove_playlist_from_library.setText("")
        self.moreoptions.setText("")
        self.search_area_playlist.setText("")
        self.search_area_playlist.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  search song in playlist", None))
        self.search_btn_playlist.setText("")
        self.sort_btn_playlist.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"#", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Album", None))
        self.pushButton_3.setText("")
      
    # retranslateUi
    
    # Usage example:
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

