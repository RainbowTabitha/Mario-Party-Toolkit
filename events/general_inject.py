# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/4/2024
# License: MIT
# ============================================

from functions import *
from codes.marioParty1 import *

import pyperclip
import shutil

def general_injection(file_label, cheatCodeEntry):
    if not cheatCodeEntry.get("1.0", "end"):
        createDialog("Error", "error", "No information provided.", None)
        return
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
    with open("tmp/codes.txt", 'w') as file:
        file.write("$MPToolkit\n" + cheatCodeEntry.get("1.0", "end"))
    iso_path = file_label.cget("text")
    gameName = os.path.basename(iso_path)
    _, gameExt = os.path.splitext(gameName)
    if gameExt == ".iso" and is_file_greater_than_4gb(iso_path) or gameExt == ".wbfs":
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
        file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".wbfs", initialfile=gameName[:-4] + " (Modded).wbfs", filetypes=[("WBFS Files", "*.wbfs")])
        shutil.move("tmp/game.iso", file_path)
        shutil.rmtree("tmp/") 
    elif is_file_less_than_100mb(iso_path): # assuming N64 Rom
        if sys.platform == "win32":
            subprocess.run([fetchResource("dependencies/win32/GSInject.exe"), "tmp/codes.txt", iso_path, "tmp/game.z64"], check=True)
        else:
            subprocess.run([fetchResource("dependencies/darwin/GSInject"), "tmp/codes.txt", iso_path, "tmp/tmp.z64"], check=True)
        file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".z64", initialfile=gameName[:-4] + " (Modded).z64", filetypes=[("Z64 Files", "*.z64")])
        shutil.move("tmp/game.z64", file_path)
        shutil.rmtree("tmp/")
    else:
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
        file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".iso", initialfile=gameName[:-4] + " (Modded).iso", filetypes=[("ISO Files", "*.iso")])
        shutil.move("tmp/game.iso", file_path)
        shutil.rmtree("tmp/")
