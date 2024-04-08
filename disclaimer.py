from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

class DisclaimerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Disclaimer")
        
        layout = QVBoxLayout()
        
        label = QLabel("Please read and agree to the terms and conditions before proceeding.")
        layout.addWidget(label)
        
        agree_button = QPushButton("I Agree")
        agree_button.clicked.connect(self.accept)  # Close the dialog when "I Agree" button is clicked
        layout.addWidget(agree_button)
        
        self.setLayout(layout)