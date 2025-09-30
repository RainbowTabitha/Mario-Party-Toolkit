# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, PushButton, TextEdit, CardWidget, ScrollArea, MessageBox
from functions import createDialog, fetchResource
import os
import sys
import subprocess
import shutil


class InjectionWorker(QThread):
    """Worker thread for code injection to prevent UI freezing"""
    finished = pyqtSignal(bool, str)
    save_file_requested = pyqtSignal(str, str, str)  # extension, initial_name, file_types
    
    def __init__(self, file_path, codes_text, parent_widget):
        super().__init__()
        self.file_path = file_path
        self.codes_text = codes_text
        self.parent_widget = parent_widget
        self.save_file_path = None
    
    def run(self):
        try:
            # Create temporary directory
            if not os.path.exists("tmp"):
                os.mkdir("tmp")
            else:
                try:
                    shutil.rmtree("tmp")
                except:
                    pass
                try:
                    os.mkdir("tmp")
                except:
                    pass
            
            # Write codes to file
            with open("tmp/codes.txt", 'w') as file:
                file.write("$MPToolkit\n" + self.codes_text)
            
            iso_path = self.file_path
            gameName = os.path.basename(iso_path)
            _, gameExt = os.path.splitext(gameName)
            
            # Handle different file types
            if gameExt == ".iso" and self.is_file_greater_than_4gb(iso_path) or gameExt == ".wbfs":
                self.handle_wbfs_iso(iso_path, gameName)
            elif self.is_file_less_than_100mb(iso_path):  # N64 ROM
                self.handle_n64_rom(iso_path, gameName)
            else:  # Regular ISO
                self.handle_regular_iso(iso_path, gameName)
            
            # Clean up
            shutil.rmtree("tmp/")
            self.finished.emit(True, "Code injection completed successfully!")
            
        except Exception as e:
            self.finished.emit(False, f"Error during injection: {str(e)}")
    
    def is_file_greater_than_4gb(self, file_path):
        file_size_bytes = os.path.getsize(file_path)
        file_size_gb = file_size_bytes / (1024**3)
        return file_size_gb > 4
    
    def is_file_less_than_100mb(self, file_path):
        file_size_bytes = os.path.getsize(file_path)
        file_size_mb = file_size_bytes / (1024**2)
        return file_size_mb < 100
    
    def handle_wbfs_iso(self, iso_path, gameName):
        if sys.platform == "win32":
            subprocess.run([fetchResource("dependencies/win32/wit.exe"), "extract", iso_path, "tmp/tmpROM/"], check=True)
        else:
            subprocess.run([fetchResource("dependencies/darwin/wit"), "extract", iso_path, "tmp/tmpROM/"], check=True)
        
        tmpromContents = os.listdir("tmp/tmpROM")
        folders = [item for item in tmpromContents if os.path.isdir(os.path.join("tmp/tmpROM", item))]
        folder_name = folders[0]
        folder_path = os.path.join("tmp/tmpROM", folder_name + "/sys/main.dol")
        folder_path_raw = os.path.join("tmp/tmpROM", folder_name)
        
        if sys.platform == "win32":
            subprocess.run([fetchResource("dependencies/win32/GeckoLoader.exe"), "--hooktype=GX", "--optimize", folder_path, "tmp/codes.txt", "--dest=tmp/tmpDOL"], check=True)
        else:
            subprocess.run([fetchResource("dependencies/darwin/GeckoLoader"), "--hooktype=GX", "--optimize", folder_path, "tmp/codes.txt", "--dest=tmp/tmpDOL"], check=True)
        
        os.remove(folder_path)
        shutil.move("tmp/tmpDOL/main.dol", folder_path)
        
        if sys.platform == "win32":
            subprocess.run([fetchResource("dependencies/win32/wit.exe"), "copy", folder_path_raw, "--dest=tmp/game.wbfs"], check=True)
        else:
            subprocess.run([fetchResource("dependencies/darwin/wit"), "copy", folder_path_raw, "--dest=tmp/game.wbfs"], check=True)
        
        # Request save file dialog from main thread
        self.save_file_requested.emit(".wbfs", gameName[:-4] + " (Modded).wbfs", "WBFS Files (*.wbfs)")
        # Wait for the result
        while self.save_file_path is None:
            self.msleep(100)
        
        if self.save_file_path:
            shutil.move("tmp/game.wbfs", self.save_file_path)
    
    def handle_n64_rom(self, iso_path, gameName):
        if sys.platform == "win32":
            subprocess.run([fetchResource("dependencies/win32/GSInject.exe"), "tmp/codes.txt", iso_path, "tmp/game.z64"], check=True)
        else:
            subprocess.run([fetchResource("dependencies/darwin/GSInject"), "tmp/codes.txt", iso_path, "tmp/tmp.z64"], check=True)
        
        # Request save file dialog from main thread
        self.save_file_requested.emit(".z64", gameName[:-4] + " (Modded).z64", "Z64 Files (*.z64)")
        # Wait for the result
        while self.save_file_path is None:
            self.msleep(100)
        
        if self.save_file_path:
            shutil.move("tmp/game.z64", self.save_file_path)
    
    def handle_regular_iso(self, iso_path, gameName):
        if sys.platform == "win32":
            subprocess.run([fetchResource("dependencies/win32/pyisotools.exe"), iso_path, "E", "--dest=tmp/tmpROM/"], check=True)
        else:
            subprocess.run([fetchResource("dependencies/darwin/pyisotools"), iso_path, "E", "--dest=tmp/tmpROM/"], check=True)
        
        tmpromContents = os.listdir("tmp/tmpROM")
        folders = [item for item in tmpromContents if os.path.isdir(os.path.join("tmp/tmpROM", item))]
        folder_name = folders[0]
        folder_path = os.path.join("tmp/tmpROM", folder_name + "/sys/main.dol")
        folder_path_raw = os.path.join("tmp/tmpROM", folder_name)
        
        if sys.platform == "win32":
            subprocess.run([fetchResource("dependencies/win32/GeckoLoader.exe"), "--hooktype=GX", folder_path, "tmp/codes.txt", "--dest=tmp/tmpDOL"], check=True)
        else:
            subprocess.run([fetchResource("dependencies/darwin/GeckoLoader"), "--hooktype=GX", folder_path, "tmp/codes.txt", "--dest=tmp/tmpDOL"], check=True)
        
        os.remove(folder_path)
        shutil.move("tmp/tmpDOL/main.dol", folder_path)
        
        if sys.platform == "win32":
            subprocess.run([fetchResource("dependencies/win32/pyisotools.exe"), folder_path_raw, "B", "--dest=../../game.iso"], check=True)
        else:
            subprocess.run([fetchResource("dependencies/darwin/pyisotools"), folder_path_raw, "B", "--dest=../../game.iso"], check=True)
        
        # Request save file dialog from main thread
        self.save_file_requested.emit(".iso", gameName[:-4] + " (Modded).iso", "ISO Files (*.iso)")
        # Wait for the result
        while self.save_file_path is None:
            self.msleep(100)
        
        if self.save_file_path:
            shutil.move("tmp/game.iso", self.save_file_path)


class InjectorPage(QWidget):
    def __init__(self):
        super().__init__()
        self.selected_file_path = ""
        self.setup_ui()

    def setup_ui(self):
        """Set up the injector page UI"""
        self.setObjectName("injectorPage")
        
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(16)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        title = SubtitleLabel("Code Injector")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)
        
        # Description
        desc = BodyLabel("Inject generated codes into your Mario Party games")
        desc.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(desc)
        
        # File selection card
        file_card = CardWidget()
        file_layout = QVBoxLayout(file_card)
        file_layout.setSpacing(12)
        
        file_title = BodyLabel("Select ROM/ISO File")
        file_layout.addWidget(file_title)
        
        # File selection row
        file_row = QHBoxLayout()
        self.file_path_edit = LineEdit()
        self.file_path_edit.setPlaceholderText("No file selected")
        self.file_path_edit.setReadOnly(True)
        file_row.addWidget(self.file_path_edit)
        
        self.select_file_btn = PushButton("Browse")
        self.select_file_btn.clicked.connect(self.select_file)
        file_row.addWidget(self.select_file_btn)
        
        file_layout.addLayout(file_row)
        main_layout.addWidget(file_card)
        
        # Codes input card
        codes_card = CardWidget()
        codes_layout = QVBoxLayout(codes_card)
        codes_layout.setSpacing(12)
        
        codes_title = BodyLabel("Enter Codes")
        codes_layout.addWidget(codes_title)
        
        codes_desc = BodyLabel("Paste your generated codes here (one per line)")
        codes_layout.addWidget(codes_desc)
        
        self.codes_text_edit = TextEdit()
        self.codes_text_edit.setPlaceholderText("Paste your codes here...")
        self.codes_text_edit.setMaximumHeight(200)
        self.codes_text_edit.setStyleSheet("TextEdit { color: palette(text); }")
        self.codes_text_edit.textChanged.connect(self.on_codes_changed)
        codes_layout.addWidget(self.codes_text_edit)
        
        main_layout.addWidget(codes_card)
        
        # Inject button
        self.inject_btn = PushButton("Inject Codes")
        self.inject_btn.clicked.connect(self.inject_codes)
        self.inject_btn.setEnabled(False)
        main_layout.addWidget(self.inject_btn)
        
        # Add stretch to push everything to the top
        main_layout.addStretch()
    
    def select_file(self):
        """Open file dialog to select ROM/ISO file"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select ROM/ISO File",
            "",
            "Game Files (*.z64 *.iso *.wbfs);;Z64 Files (*.z64);;ISO Files (*.iso);;WBFS Files (*.wbfs);;All Files (*.*)"
        )
        
        if file_path:
            self.selected_file_path = file_path
            self.file_path_edit.setText(file_path)
            self.update_inject_button_state()
    
    def on_codes_changed(self):
        """Handle text changes in codes text edit"""
        self.update_inject_button_state()
    
    def update_inject_button_state(self):
        """Update the inject button enabled state based on file selection and codes"""
        has_file = bool(self.selected_file_path)
        has_codes = bool(self.codes_text_edit.toPlainText().strip())
        self.inject_btn.setEnabled(has_file and has_codes)
    
    def inject_codes(self):
        """Start the code injection process"""
        if not self.selected_file_path:
            createDialog("Error", "error", "Please select a ROM/ISO file first.", None)
            return
        
        codes_text = self.codes_text_edit.toPlainText().strip()
        if not codes_text:
            createDialog("Error", "error", "Please enter codes to inject.", None)
            return
        
        if not os.path.exists(self.selected_file_path):
            createDialog("Error", "error", "Selected file does not exist.", None)
            return
        
        # Disable button during injection
        self.inject_btn.setEnabled(False)
        self.inject_btn.setText("Injecting...")
        
        # Start injection worker thread
        self.injection_worker = InjectionWorker(self.selected_file_path, codes_text, self)
        self.injection_worker.finished.connect(self.on_injection_finished)
        self.injection_worker.save_file_requested.connect(self.handle_save_file_request)
        self.injection_worker.start()
    
    def handle_save_file_request(self, extension, initial_name, file_types):
        """Handle save file request from worker thread"""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Modified Game File",
            initial_name,
            f"{file_types};;All Files (*.*)"
        )
        
        # Set the result back to the worker thread
        if file_path:
            self.injection_worker.save_file_path = file_path
        else:
            self.injection_worker.save_file_path = ""  # User cancelled
    
    def on_injection_finished(self, success, message):
        """Handle injection completion"""
        # Re-enable button
        self.inject_btn.setEnabled(True)
        self.inject_btn.setText("Inject Codes")
        
        if success:
            createDialog("Success", "success", message, None)
        else:
            createDialog("Error", "error", message, None)
