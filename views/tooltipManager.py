from PySide6.QtWidgets import QLabel, QGraphicsOpacityEffect
from PySide6.QtCore import Qt, QPoint, QPropertyAnimation, QEasingCurve

class TooltipManager:
    def __init__(self, parent):
        """TooltipManager quản lý tooltip với animation"""
        self.parent = parent
        self.tooltip_label = QLabel(parent)
        self.tooltip_label.setStyleSheet("""
            background-color: #282828;
            font-family: 'Promo';
            font-weight: 600;
            color: #ffffff;
            border: 1px solid #282828;
            border-radius: 5px;
            padding: 5px;
        """)
        self.tooltip_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Hiệu ứng Opacity cho tooltip
        self.opacity_effect = QGraphicsOpacityEffect(self.tooltip_label)
        self.tooltip_label.setGraphicsEffect(self.opacity_effect)
        self.fade_in_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.fade_in_animation.setEasingCurve(QEasingCurve.OutCubic)
        self.fade_in_animation.setDuration(1000)  # Thời gian fade-in (ms)

        self.fade_out_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.fade_out_animation.setEasingCurve(QEasingCurve.OutCubic)
        self.fade_out_animation.setDuration(300)  # Thời gian fade-out (ms)

        self.fade_out_animation.finished.connect(self.tooltip_label.hide)  # Ẩn sau khi fade-out

        self.tooltip_label.hide()  # Ẩn mặc định

    def attach(self, widget, text):
        """Đăng ký tooltip cho một nút"""
        widget.enterEvent = lambda event: self.show_tooltip(widget, text)
        widget.leaveEvent = lambda event: self.hide_tooltip()

    def show_tooltip(self, widget, text):
        """Hiển thị tooltip với hiệu ứng mờ dần (fade-in)"""
        self.fade_out_animation.stop()  # Dừng fade-out nếu đang chạy
        self.tooltip_label.setText(text)
        self.tooltip_label.adjustSize()  # Tự động điều chỉnh kích thước
        
        # Lấy vị trí của nút và cửa sổ chính
        button_pos = widget.mapToGlobal(QPoint(-20, 5))
        parent_rect = self.parent.geometry()
        tooltip_width = self.tooltip_label.width()
        tooltip_height = self.tooltip_label.height()

        # Lấy kích thước của nút
        button_width = widget.width()
        button_height = widget.height()

        # Tính toán vị trí tooltip
        tooltip_x = button_pos.x() + button_width // 2 - tooltip_width // 2
        tooltip_y = button_pos.y() - tooltip_height - 3  # Đặt ở phía trên nút

        # Điều chỉnh nếu tooltip vượt rìa cửa sổ
        if tooltip_x < parent_rect.left():  # Tooltip vượt qua bên trái
            tooltip_x = parent_rect.left() + 5
        elif tooltip_x + tooltip_width > parent_rect.right():  # Tooltip vượt qua bên phải
            tooltip_x = parent_rect.right() - tooltip_width - 5

        if tooltip_y < parent_rect.top():  # Tooltip vượt qua bên trên cửa sổ
            tooltip_y = button_pos.y() + button_height - 50  # Hiển thị bên dưới nút

        # Nếu tooltip vẫn vượt quá dưới cùng cửa sổ, điều chỉnh vị trí
        if tooltip_y + tooltip_height > parent_rect.bottom():
            tooltip_y = parent_rect.bottom() - tooltip_height - 5

        # Đặt lại vị trí tooltip
        self.tooltip_label.move(tooltip_x, tooltip_y)
        self.tooltip_label.show()

        # Thiết lập animation fade-in
        self.opacity_effect.setOpacity(0)  # Đặt opacity về 0 trước khi chạy fade-in
        self.fade_in_animation.setStartValue(0)
        self.fade_in_animation.setEndValue(1)
        self.fade_in_animation.start()

    def hide_tooltip(self):
        """Ẩn tooltip với hiệu ứng mờ dần (fade-out)"""
        self.fade_in_animation.stop()  # Dừng fade-in nếu đang chạy
        # Thiết lập animation fade-out
        self.opacity_effect.setOpacity(1)  # Đặt opacity về 1 trước khi chạy fade-out
        self.fade_out_animation.setStartValue(1)
        self.fade_out_animation.setEndValue(0)
        self.fade_out_animation.start()