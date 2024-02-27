from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox, QHBoxLayout
from PyQt6.QtCore import Qt
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    try:
        url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
        content = requests.get(url).text
        soup = BeautifulSoup(content, 'html.parser')
        rate = soup.find("span", class_="ccOutputRslt").get_text()
        rate = float(rate[:-4])
        return rate
    except Exception as e:
        print(f"Error retrieving currency rate: {e}")
        return None
    
def show_currency():
    try:
        input_amount = float(input_text.text())
        in_cur = in_combo.currentText()
        target_cur = target_combo.currentText()
        rate = get_currency(in_cur, target_cur)
        if rate is not None:
            output_amount = round(input_amount * rate, 2)
            message = f'{input_amount} {in_cur} is {output_amount} {target_cur}'
            output_label.setText(message)
        else:
            output_label.setText("Error: Unable to retrieve currency rate")
    except ValueError:
        output_label.setText("Error: Invalid input")

app = QApplication([])
window = QWidget()
window.setWindowTitle('Currency Converter')  

layout = QVBoxLayout()
layout1 = QHBoxLayout()
layout.addLayout(layout1)

output_label = QLabel('')
layout.addWidget(output_label)

layout2 = QVBoxLayout()
layout1.addLayout(layout2)

layout3 = QVBoxLayout()
layout1.addLayout(layout3)


input_label = QLabel('Amount:')
layout.addWidget(input_label)

input_text = QLineEdit()
layout.addWidget(input_text)

in_label = QLabel('From:')
layout.addWidget(in_label)

in_combo = QComboBox()
currencies = ['USD', 'EUR', 'BRL', 'ARS', 'INR']
in_combo.addItems(currencies)
layout2.addWidget(in_combo)

target_combo = QComboBox()
target_combo.addItems(currencies)
layout2.addWidget(target_combo)

btn = QPushButton('Convert')
layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)
btn.clicked.connect(show_currency)

output_label = QLabel('')
layout.addWidget(output_label)

window.setLayout(layout)
window.show()
app.exec()
