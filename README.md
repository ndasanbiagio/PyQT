# PyQT
PyQT Currency Converter
# Currency Converter

This is a simple currency converter application built using PyQt6 and BeautifulSoup. It allows users to convert currency from one type to another using real-time exchange rates fetched from x-rates.com.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    ```

2. Navigate to the project directory:

    ```bash
    cd tu_repositorio
    ```

3. Install the required dependencies:

    ```bash
    pip install PyQt6 beautifulsoup4 requests
    ```

## Usage

1. Run the application:

    ```bash
    python currency_converter.py
    ```

2. Enter the amount you want to convert in the "Amount" field.

3. Select the currency you want to convert from in the "From" dropdown menu.

4. Select the currency you want to convert to in the "To" dropdown menu.

5. Click the "Convert" button to see the converted amount.

## Features

- Real-time currency conversion using exchange rates from x-rates.com.
- Support for various currencies including USD, EUR, BRL, ARS, and INR.
- User-friendly graphical interface built with PyQt6.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).









This code is a PyQt6 application that implements a currency converter. It allows users to convert currency from one type to another using real-time exchange rates fetched from x-rates.com.

Here's a breakdown of the code:

Import Statements:

PyQt6 modules are imported to create the graphical user interface (GUI).
BeautifulSoup and requests modules are imported to fetch and parse HTML data from the x-rates.com website.
get_currency Function:

This function takes two currency codes (in_currency and out_currency) as input.
It constructs a URL with these currency codes and sends a request to the x-rates.com website.
It extracts the currency conversion rate from the HTML response using BeautifulSoup.
If successful, it returns the conversion rate; otherwise, it prints an error message and returns None.
show_currency Function:

This function is called when the "Convert" button is clicked.
It retrieves the input amount, the "from" currency, and the "to" currency from the GUI elements.
It calls the get_currency function to fetch the conversion rate.
If successful, it calculates the converted amount and updates the output label with the result; otherwise, it displays an error message.
Creating the GUI:

An instance of QApplication is created.
A QWidget (main window) is created with the title "Currency Converter".
QVBoxLayout is used to arrange the widgets vertically.
QHBoxLayout is used to arrange the input fields horizontally.
QLabel, QLineEdit, QComboBox, and QPushButton are used to create input fields and buttons.
Widgets are added to layouts using addWidget.
The "Convert" button is connected to the show_currency function using clicked.connect.
The main window's layout is set, and the window is displayed using show.
Overall, this code creates a simple currency converter application with a user-friendly GUI using PyQt6. Users can input the amount and select the currencies they want to convert from and to, and the application fetches the real-time exchange rates to perform the conversion.