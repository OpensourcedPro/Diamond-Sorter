import os
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFileDialog, QMessageBox, QPushButton, QCheckBox

class LoadTextFileDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Load Text File or Set Directory Path")
        self.layout = QVBoxLayout()

        self.label = QLabel("Choose an option:")
        self.layout.addWidget(self.label)

        self.button_load_file = QPushButton("Load Text File")
        self.button_load_file.clicked.connect(self.load_text_file)
        self.layout.addWidget(self.button_load_file)

        self.button_set_directory = QPushButton("Set Directory Path")
        self.button_set_directory.clicked.connect(self.set_directory_path)
        self.layout.addWidget(self.button_set_directory)

        self.setLayout(self.layout)

    def load_text_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Text File", "", "Text Files (*.txt)")
        if file_path:
            msg_box = QMessageBox.question(self, "Confirm", "Are you sure you want to load the text file?\nThis will process and copy the domains.", QMessageBox.Yes | QMessageBox.No)
            if msg_box == QMessageBox.Yes:
                domains = self.get_selected_domains()
                if domains:
                    self.process_and_copy(file_path, domains)
                else:
                    QMessageBox.warning(self, "No Domains Selected", "Please select at least one domain.")
        else:
            QMessageBox.warning(self, "Invalid File", "Please select a valid text file.")

    def set_directory_path(self):
        directory_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory_path:
            msg_box = QMessageBox.question(self, "Confirm", "Are you sure you want to set the directory path?\nThis will process and copy the domains.", QMessageBox.Yes | QMessageBox.No)
            if msg_box == QMessageBox.Yes:
                domains = self.get_selected_domains()
                if domains:
                    self.process_and_copy(directory_path, domains)
                else:
                    QMessageBox.warning(self, "No Domains Selected", "Please select at least one domain.")
        else:
            QMessageBox.warning(self, "Invalid Directory", "Please select a valid directory.")

    def get_selected_domains(self):
        domains = []
        for checkbox in self.checkboxes:
            if checkbox.isChecked():
                domains.append(checkbox.text())
        return domains

    def process_and_copy(self, path, domains):
        if os.path.isfile(path):
            with open(path, "r") as file:
                lines = file.readlines()

            output_directory = os.path.join(os.path.dirname(path), "Diamond Sorter Domains - Sorted")
            os.makedirs(output_directory, exist_ok=True)

            for line in lines:
                extension = line.strip()
                if extension in domains:
                    output_filename = os.path.join(output_directory, f"{extension}.txt")
                    with open(output_filename, "w") as output_file:
                        output_file.write(extension)

        elif os.path.isdir(path):
            output_directory = os.path.join(path, "Diamond Sorter Domains - Sorted")
            os.makedirs(output_directory, exist_ok=True)

app = QApplication([])
dialog = LoadTextFileDialog()

# Add checkboxes for the specified domains
domains = [
    "126.com", "163.com", "icloud", "pe", "gr", "al", "il", "an", "at", "ad", "af", "ag", "ai", "am", "ao", "aq", "as", "aw", "ax", "az",
    "ba", "bb", "bd", "bf", "bh", "bi", "bj", "bm", "bn", "bo", "bs", "bt", "bv", "bw", "bz", "cc", "cd", "cf", "cg", "ci", "ck", "cm",
    "co", "cr", "cu", "cv", "cx", "cy", "dj", "do", "ec", "ee", "eg", "er", "et", "eu", "fi", "fj", "fk", "fm", "fo", "ga", "gb",
    "gd", "ge", "gf", "gg", "gh", "gi", "gl", "gm", "gn", "gp", "gq", "gs", "gt", "gu", "gw", "gy",
    "hm", "hn", "hr", "ht", "ie", "im", "io", "iq", "ir", "je", "jm", "jo", "ke", "kg", "kh", "ki", "km", "kn", "kp", "kd", "kw",
    "ky", "kz", "la", "lb", "lc", "li", "lk", "lr", "ls", "lt", "ly", "ma", "mc", "md", "me", "mg", "mh", "mk", "ml", "mm", "mn",
    "mo", "mp", "mq", "mr", "ms", "mt", "mu", "mv", "mw", "mz", "na", "nc", "ne", "nf", "ng", "ni", "np", "nr", "nu", "nz", "om",
    "pa", "pf", "pg", "pk", "pm", "pn", "pr", "ps", "pw", "py", "qa", "re", "rs", "rw", "sa", "sb", "sc", "sd", "sh", "si", "sj",
    "sl", "sm", "sn", "so", "sr", "st", "su", "sv", "sy", "sz", "tc", "td", "tf", "tg", "th", "tj", "tk", "tl", "tm", "tn", "to",
    "tp", "tt", "tv", "tz", "ug", "uy", "uz", "va", "vc", "vg", "vi", "vu", "wf", "ws", "xk", "ye", "yt", "yu", "zm", "zw", "it",
    "za", "id", "tx", "uk", "kr", "dk", "ca", "yw", "aol.com", "au", "be", "bg", "br", "ch", "cn", "cz", "dm", "dz", "edu", "es",
    "fr", "hk", "hu", "le", "in", "is", "jp", "lu", "lv", "ru", "mx", "my", "nl", "no", "ph", "pl", "pt", "ro", "se", "sg", "sk",
    "tw", "us", "ve", "de", "vn", "tr", "ar", "ac", "ae", "ua", "by", "yahoo.com", "hotmail.com", "gmail.com", "gmx.net", "att.net",
    "academy", "accountant", "accountants", "active", "actor", "adult", "agency", "airforce", "apartments", "app", "archi", "army",
    "associates", "asia", "attorney", "auction", "audio", "autos", "coop", "dance", "eus", "family", "fun", "info", "int", "jobs",
    "mil", "mobi", "museum", "name", "one", "ong", "onl", "online", "ooo", "org", "organic", "partners", "parts", "party", "pharmacy",
    "photo", "photography", "photos", "physio", "pics", "pictures", "feedback", "pink", "pizza", "place", "pe", "plumbing", "plus",
    "poker", "porn", "post", "press", "pro", "productions", "prof", "properties", "property", "qpon", "racing", "recipes", "red",
    "rehab", "ren", "rent", "rentals", "repair", "report", "republican", "rest", "review", "reviews", "rich", "site",
    "tel", "trade", "travel", "xxx", "xyz", "yoga", "zone", "ninja", "art", "moe", "dev"
]

# Create checkboxes for the specified domains
checkboxes = []
select_all_checkbox = QCheckBox("Select All")
checkboxes.append(select_all_checkbox)
for domain in domains:
    checkbox = QCheckBox(domain)
    checkboxes.append(checkbox)

dialog.checkboxes = checkboxes

# Add checkboxes to the layout
for checkbox in checkboxes:
    dialog.layout.addWidget(checkbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = LoadTextFileDialog()
    dialog.show()
    window = DiamondSorter()
    window.show()
    sys.exit(app.exec_())