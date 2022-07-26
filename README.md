# Text Based Browser

## Description

Text Based Browser is a simple, command-line driven Python application designed for scraping and reading web content. It enables users to navigate through web pages, saving the text content (paragraphs and headers) into files within a specified directory for offline reading. Additionally, it provides a functionality to backtrack through previously visited pages. With the use of `BeautifulSoup` for parsing web content and `colorama` for distinguishing links within the terminal, it provides a user-friendly way to consume web content.

## Features

- Website content scraping and saving for offline reading.
- Navigation command supports for moving back to previously visited content.
- Use of BeautifulSoup for HTML content parsing.
- Color-coded display of web links using Colorama.
- Simple command-line interface for easy navigation and operation.

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/text-based-browser.git
```

2. Navigate to the cloned repository:

```
cd text-based-browser
```

3. Create and activate a virtual environment:

```
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

4. Install the required dependencies using pip and the requirements.txt file:

```
pip install -r requirements.txt
```

## Usage

To use the Text Based Browser, navigate to the directory containing the script and execute it with Python, passing the directory name where you would like to save the scraped web pages as an argument. For example:

```
python main.py saved_articles
```

Once the script is running, you can start entering commands:
- Simply type a URL (with or without the `https://` prefix) to fetch and view its content.
- Type the filename of a previously saved article to read it again.
- Type `back` to go back to the content of the last visited page.
- Type `exit` to stop the script and exit.

## Limitations

- The script currently processes and saves only textual content (paragraphs, headings, and links). Images and other media types are ignored.
- Only simple error handling is implemented for incorrect URLs or connection issues.

## License

This project is licensed under the [MIT License](LICENSE.txt).

## Acknowledgements

- Thanks to the creators of [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Colorama](https://pypi.org/project/colorama/) for providing such powerful tools.

## Note

- This project was created for educational purposes and is not intended for use in production environments.
