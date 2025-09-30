#!/usr/bin/env python3
# ============================================
# Mario Party Toolkit - UI Utilities
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 8/16/2025
# License: MIT
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, CheckBox, PushButton, ComboBox
from functions import fetchResource


def create_scroll_area():
    """Create a standardized scroll area with consistent styling"""
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    scroll_area.setStyleSheet("""
        QScrollArea {
            border: none;
            background: transparent;
        }
        QScrollBar:vertical {
            background: rgba(255, 255, 255, 0.1);
            width: 12px;
            border-radius: 6px;
        }
        QScrollBar::handle:vertical {
            background: rgba(255, 255, 255, 0.3);
            border-radius: 6px;
            min-height: 20px;
        }
        QScrollBar::handle:vertical:hover {
            background: rgba(255, 255, 255, 0.5);
        }
        QScrollBar:horizontal {
            background: rgba(255, 255, 255, 0.1);
            height: 12px;
            border-radius: 6px;
        }
        QScrollBar::handle:horizontal {
            background: rgba(255, 255, 255, 0.3);
            border-radius: 6px;
            min-width: 20px;
        }
        QScrollBar::handle:horizontal:hover {
            background: rgba(255, 255, 255, 0.5);
        }
    """)
    return scroll_area


def create_coin_space_entry(parent_layout, icon_path, action_text, default_value, description, checkbox_text, color_type):
    """Create a coin space entry with icon, input, and checkbox"""
    entry_layout = QHBoxLayout()
    
    # Icon
    icon_label = QLabel()
    icon_label.setPixmap(QIcon(fetchResource(icon_path)).pixmap(32, 32))
    entry_layout.addWidget(icon_label)
    
    # Action label
    action_label = QLabel(action_text)
    action_label.setStyleSheet("font-size: 16px; margin: 0 8px;")
    entry_layout.addWidget(action_label)
    
    # Input field
    entry = LineEdit()
    entry.setPlaceholderText(default_value)
    entry.setFixedWidth(60)
    entry_layout.addWidget(entry)
    
    # Description label
    desc_label = QLabel(description)
    desc_label.setStyleSheet("font-size: 16px; margin: 0 8px;")
    entry_layout.addWidget(desc_label)
    
    # Checkbox
    checkbox = CheckBox(checkbox_text)
    entry_layout.addWidget(checkbox)
    entry_layout.addStretch()
    
    # Add the layout to the parent
    parent_layout.addLayout(entry_layout)
    
    # Return the widgets for the caller to store references
    return entry, checkbox


def create_star_cost_entry(parent_layout):
    """Create a star cost entry with icon and input"""
    entry_layout = QHBoxLayout()
    
    # Icon
    icon_label = QLabel()
    icon_label.setPixmap(QIcon(fetchResource("assets/eventTags/starSpace.png")).pixmap(32, 32))
    entry_layout.addWidget(icon_label)
    
    # Action label
    action_label = QLabel("Costs")
    action_label.setStyleSheet("font-size: 16px; margin: 0 8px;")
    entry_layout.addWidget(action_label)
    
    # Input field
    entry = LineEdit()
    entry.setPlaceholderText("20")
    entry.setFixedWidth(60)
    entry_layout.addWidget(entry)
    
    # Description label
    desc_label = QLabel("coins to buy a Star")
    desc_label.setStyleSheet("font-size: 16px; margin: 0 8px;")
    entry_layout.addWidget(desc_label)
    entry_layout.addStretch()
    
    parent_layout.addLayout(entry_layout)
    return entry


def create_block_weight_entry(parent_layout, icon_path, weight_attr):
    """Create a block weight entry with icon and input"""
    entry_layout = QHBoxLayout()
    
    # Icon
    icon_label = QLabel()
    icon_label.setPixmap(QIcon(fetchResource(icon_path)).pixmap(32, 32))
    entry_layout.addWidget(icon_label)
    
    # Weight label
    weight_label = QLabel("Weight:")
    weight_label.setStyleSheet("font-size: 16px; margin: 0 8px;")
    entry_layout.addWidget(weight_label)
    
    # Input field
    entry = LineEdit()
    entry.setPlaceholderText("0")
    entry.setFixedWidth(60)
    entry_layout.addWidget(entry)
    entry_layout.addStretch()
    
    parent_layout.addLayout(entry_layout)
    return entry


def create_player_handicap_entry(parent_layout, player_name):
    """Create a player handicap entry with star icon and input"""
    entry_layout = QHBoxLayout()
    
    # Star icon
    icon_label = QLabel()
    icon_label.setPixmap(QIcon(fetchResource("assets/eventTags/starSpace.png")).pixmap(32, 32))
    entry_layout.addWidget(icon_label)
    
    # Player label
    player_label = QLabel(f"{player_name} starts with:")
    player_label.setStyleSheet("font-size: 16px; margin: 0 8px;")
    entry_layout.addWidget(player_label)
    
    # Input field
    star_input = LineEdit()
    star_input.setPlaceholderText("0")
    star_input.setFixedWidth(60)
    entry_layout.addWidget(star_input)
    
    # Stars label
    stars_label = QLabel("stars")
    stars_label.setStyleSheet("font-size: 16px; margin: 0 8px;")
    entry_layout.addWidget(stars_label)
    entry_layout.addStretch()
    
    parent_layout.addLayout(entry_layout)
    return star_input


def create_generate_button(text, callback):
    """Create a standardized generate button"""
    button = PushButton(text)
    button.setStyleSheet("""
        QPushButton {
            background: palette(button);
            color: palette(text);
            border: 1px solid palette(mid);
            border-radius: 8px;
            padding: 12px 24px;
            font-size: 14px;
            font-weight: 600;
            margin: 24px 0;
            min-height: 40px;
        }
        QPushButton:hover {
            background: palette(light);
        }
    """)
    button.clicked.connect(callback)
    return button


def create_section_title(text):
    """Create a standardized section title"""
    title = SubtitleLabel(text)
    title.setStyleSheet("font-size: 20px; font-weight: bold; margin: 16px 0;")
    return title
