# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, 
                             QScrollArea, QTextEdit, QFrame, QSizePolicy, QSpacerItem)
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices
from qfluentwidgets import (SubtitleLabel, BodyLabel, TitleLabel, StrongBodyLabel,
                           CardWidget, ScrollArea, TextEdit, PushButton, FluentIcon)

from version import versionString


class AboutPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        """Set up the modern about page UI"""
        self.setObjectName("aboutPage")
        
        # Set transparent background
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet("QWidget#aboutPage { background: transparent; }")
        
        # Main scroll area for the entire page
        main_scroll = ScrollArea(self)
        main_scroll.setWidgetResizable(True)
        main_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        main_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        main_scroll.setStyleSheet("QScrollArea { background: transparent; border: none; }")
        
        # Container widget for scroll area content
        container = QWidget()
        container.setStyleSheet("QWidget { background: transparent; }")
        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(40, 30, 40, 30)
        main_layout.setSpacing(30)
        
        # Header section
        self.create_header_section(main_layout)
        
        # Create grid layout for main content cards
        content_grid = QGridLayout()
        content_grid.setSpacing(20)
        
        # Features card (left column)
        features_card = self.create_features_card()
        content_grid.addWidget(features_card, 0, 0, 1, 1)
        
        # License card (right column)
        license_card = self.create_license_card()
        content_grid.addWidget(license_card, 0, 1, 1, 1)
        
        # Credits card (spans both columns)
        credits_card = self.create_credits_card()
        content_grid.addWidget(credits_card, 1, 0, 1, 2)
        
        main_layout.addLayout(content_grid)
        
        # Footer section
        self.create_footer_section(main_layout)
        
        # Set the container as the scroll area's widget
        main_scroll.setWidget(container)
        
        # Main page layout
        page_layout = QVBoxLayout(self)
        page_layout.setContentsMargins(0, 0, 0, 0)
        page_layout.addWidget(main_scroll)
        
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def create_header_section(self, layout):
        """Create the header section with title and description"""
        header_layout = QVBoxLayout()
        header_layout.setSpacing(15)
        header_layout.setAlignment(Qt.AlignCenter)
        
        # Main title
        title = TitleLabel("Mario Party Toolkit", self)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("TitleLabel { color: white; }")
        header_layout.addWidget(title)
        
        # Version and description
        version_desc_layout = QVBoxLayout()
        version_desc_layout.setSpacing(8)
        version_desc_layout.setAlignment(Qt.AlignCenter)
        
        version_label = StrongBodyLabel(f"Version {versionString}", self)
        version_label.setAlignment(Qt.AlignCenter)
        version_label.setStyleSheet("StrongBodyLabel { color: white; }")
        version_desc_layout.addWidget(version_label)
        
        description = BodyLabel("A comprehensive desktop application for modifying Mario Party games", self)
        description.setAlignment(Qt.AlignCenter)
        description.setWordWrap(True)
        description.setStyleSheet("BodyLabel { color: white; }")
        version_desc_layout.addWidget(description)
        
        subtitle = BodyLabel("Is it a mario party modding tool? Yes.", self)
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setWordWrap(True)
        subtitle.setStyleSheet("BodyLabel { color: white; }")
        version_desc_layout.addWidget(subtitle)
        
        header_layout.addLayout(version_desc_layout)
        layout.addLayout(header_layout)

    def create_features_card(self):
        """Create the features card"""
        card = CardWidget(self)
        card.setStyleSheet("CardWidget { background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); }")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(25, 20, 25, 20)
        card_layout.setSpacing(15)
        
        # Features title
        features_title = SubtitleLabel("🚀 Features", card)
        card_layout.addWidget(features_title)
        
        # Features list
        features_list = [
            "🎮 Mario Party 1-9 + DS Support",
            "💰 Generic Price Modifications",
            "🏆 Minigame Replacements",
            "🔧 Code Injection Support",
            "🌙 Dark/Light Theme Support",
            "📱 Responsive Modern UI",
            "⚡ Native Integration",
            "🔄 Real-time Code Generation"
        ]
        
        for feature in features_list:
            feature_label = BodyLabel(feature, card)
            feature_label.setWordWrap(True)
            card_layout.addWidget(feature_label)
        
        card_layout.addStretch()
        return card

    def create_license_card(self):
        """Create the license card with scrollable MIT license"""
        card = CardWidget(self)
        card.setStyleSheet("CardWidget { background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); }")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(25, 20, 25, 20)
        card_layout.setSpacing(15)
        
        # License title
        license_title = SubtitleLabel("📄 MIT License", card)
        card_layout.addWidget(license_title)
        
        # License text in scrollable area
        license_text = """MIT License

Copyright (c) 2023 - 2025 Tabitha Hanegan (furtabs)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
        
        license_scroll = TextEdit(card)
        license_scroll.setPlainText(license_text)
        license_scroll.setReadOnly(True)
        license_scroll.setMaximumHeight(300)
        license_scroll.setMinimumHeight(200)
        license_scroll.setStyleSheet("""
            TextEdit { 
                background: rgba(255, 255, 255, 0.05); 
                border: 1px solid rgba(255, 255, 255, 0.1); 
                color: white;
            }
            TextEdit[theme="light"] {
                background: rgba(0, 0, 0, 0.05);
                border: 1px solid rgba(0, 0, 0, 0.1);
                color: black;
            }
        """)
        card_layout.addWidget(license_scroll)
        
        return card

    def create_credits_card(self):
        """Create the credits card"""
        card = CardWidget(self)
        card.setStyleSheet("CardWidget { background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); }")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(25, 20, 25, 20)
        card_layout.setSpacing(15)
        
        # Credits title
        credits_title = SubtitleLabel("👥 Credits & Contributors", card)
        card_layout.addWidget(credits_title)
        
        # Main author
        author_section = QVBoxLayout()
        author_section.setSpacing(8)
        
        author_title = StrongBodyLabel("Main Developer", card)
        author_section.addWidget(author_title)
        
        author_info = BodyLabel("Tabitha Hanegan (tabitha@tabs.gay)", card)
        author_section.addWidget(author_info)
        
        card_layout.addLayout(author_section)
        
        # Key contributors
        contributors_section = QVBoxLayout()
        contributors_section.setSpacing(8)
        
        contributors_title = StrongBodyLabel("Key Contributors", card)
        contributors_section.addWidget(contributors_title)
        
        contributors_list = [
            "🔬 Rainchus - Sustainital resesrach with Mario Party.",
            "🐺 WolfGC64 - Inspiring me to actually learn to write codes",
            "⚙️ Ralf - Posting some codes that I can use as a reference",
            "🔬 Dark - Helping me get off my ass and actually learn to write codes.",
            "🎮 gamemasterplc - Foundational reserach, inspiring me to want to write codes."
        ]
        
        for contributor in contributors_list:
            contributor_label = BodyLabel(contributor, card)
            contributor_label.setWordWrap(True)
            contributors_section.addWidget(contributor_label)
        
        card_layout.addLayout(contributors_section)
        
        # Technical credits
        tech_section = QVBoxLayout()
        tech_section.setSpacing(8)
        
        tech_title = StrongBodyLabel("Technical Stack", card)
        tech_section.addWidget(tech_title)
        
        tech_info = BodyLabel("Built with PyQt5, qfluentwidgets, and Python 3.8+", card)
        tech_section.addWidget(tech_info)
        
        card_layout.addLayout(tech_section)
        card_layout.addStretch()
        
        return card

    def create_footer_section(self, layout):
        """Create the footer section"""
        footer_layout = QVBoxLayout()
        footer_layout.setSpacing(15)
        footer_layout.setAlignment(Qt.AlignCenter)
        
        # Repository info
        repo_info = BodyLabel("🔗 Open Source Project", self)
        repo_info.setAlignment(Qt.AlignCenter)
        repo_info.setStyleSheet("BodyLabel { color: white; }")
        footer_layout.addWidget(repo_info)
        
        # GitHub button
        github_button = PushButton("View on GitHub", self)
        github_button.setIcon(FluentIcon.GITHUB)
        github_button.clicked.connect(self.open_github_repo)
        github_button.setFixedWidth(200)
        github_button.setFixedHeight(40)
        footer_layout.addWidget(github_button, alignment=Qt.AlignCenter)
        
        # Support info
        support_info = BodyLabel("For support and issues, please visit the GitHub repository", self)
        support_info.setAlignment(Qt.AlignCenter)
        support_info.setWordWrap(True)
        support_info.setMaximumWidth(400)
        support_info.setStyleSheet("BodyLabel { color: white; }")
        footer_layout.addWidget(support_info)
        
        layout.addLayout(footer_layout)
    
    def open_github_repo(self):
        """Open the GitHub repository in the default browser"""
        github_url = QUrl("https://github.com/RainbowTabitha/Mario-Party-Toolkit")
        QDesktopServices.openUrl(github_url)
