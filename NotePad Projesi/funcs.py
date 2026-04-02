import os

def isTitleEmpty(title):
    if title == "":
        return True
    else:
        return False

def untiled_generator():
    files = os.listdir("Notes/")
    count = 0
    for i in files:
        if i.startswith("Untiled"):
            count += 1
    for i in range(count,1001):
        if i == 0:
            yield "Untiled"
        else:
            yield "Untiled"+str(i)


def search_note(title):
    files_list = ""
    _title = title.lower()
    files = os.listdir("Notes/")
    _files = list()
    for i in files:
        name = i.lower()
        if name.startswith(_title) or title == "all":
            _files.append(i)
    _files = enumerate(_files)
    for i,j in _files:
        files_list += str(i+1)+"-) "+j.removesuffix(".txt")+"\n"

    return files_list

def import_file(file_path):
    with open(file_path[0], "r", encoding="utf-8") as rfile:
        file_content = rfile.read()

    path = file_path[0].split("/")
    files_list = search_note(path[-1])

    if not files_list:
        with open("Notes/{}".format(path[-1]),"w", encoding="utf-8") as wfile:
            wfile.write(file_content)
            return path[-1].removesuffix(".txt")
    else:
        return False

def export_file(title,file_path):
    files_list = search_note(title)

    if files_list:
        return False

    with open("Notes/{}.txt".format(title),"r", encoding="utf-8") as rfile:
        file_content = rfile.read()

    with open(file_path[0],"w", encoding="utf-8") as wfile:
        wfile.write(file_content)

class Notes:
    def __init__(self, note_title:str = "Untiled", note_content:str = "", state:str ="Closed"):
        self.note_title = note_title
        self.note_content = note_content
        self.state = state


    def save_note(self,new_title,new_content):
        if self.state == "Closed":
            self.note_title = new_title
            self.note_content = new_content

            with open("Notes/{}.txt".format(self.note_title),"w", encoding="utf-8") as file:
                file.write(self.note_content)
            self.state = "Open"

            return

        if self.state == "Open" and self.note_title.startswith("Untiled"):
            self.note_title = new_title
            self.note_content = new_content

            with open("Notes/{}.txt".format(self.note_title),"w", encoding="utf-8") as file:
                file.write(self.note_content)
            self.state = "Open"

            return

        if self.state == "Open" and self.note_title != new_title:
            old_title = self.note_title
            self.note_title = new_title
            self.rename_note(old_title)

        if self.state == "Open" and self.note_content != new_content:
            self.note_content = new_content
            self.change_note_content()


    def show_note(self,note_title):
        self.note_title = note_title
        self.state = "Open"

        try:
            with open("Notes/{}.txt".format(self.note_title),"r", encoding="utf-8") as file:
                file = file.read()
                self.note_content = file
        except FileNotFoundError:
            self.note_title = "Untiled"
            self.note_content = ""
            self.state = "Closed"
            return "Dosya Bulunamadı"


    def close_note(self):
        self.state = "Closed"
        self.note_title = "Untiled"
        self.note_content = ""


    def delete_note(self,title):
        note_path = "Notes/{}.txt".format(title)
        try:
            os.remove(note_path)
        except FileNotFoundError:
            return "Dosya Bulunamadı"

        self.note_title= "Untiled"
        self.note_content = ""
        self.state = "Closed"


    def rename_note(self,old_title):
        note_path = "Notes/{}.txt".format(old_title)
        new_title = "Notes/{}.txt".format(self.note_title)
        os.rename(note_path,new_title)


    def change_note_content(self):
        with open("Notes/{}.txt".format(self.note_title),"w", encoding="utf-8") as file:
            file.write(self.note_content)

note = Notes()

