# A Web Scraping Web interface for deploying into vercel
A Flask-based web scraping application that extracts tables, images, Titles, videos, pdfs, book details, eBay product details and movie details from websites. This project uses BeautifulSoup for static content scraping and Selenium for dynamic content scraping (e.g., IMDb movie details).

## Features
- **Table Scraping**: Extract and display tables from any webpage.
- **Image Scraping**: Fetch images with filtering by format (PNG, JPG) and limit the number of images displayed.
- **Movie Details Scraping**: Retrieve movie information (title, poster, year, rating, plot, genre) from IMDb using Selenium.


## Technologies Used
- **Python**: Core programming language.
- **Flask**: Web framework for the application.
- **BeautifulSoup**: Library for parsing HTML and XML documents.
- **Selenium**: Browser automation for dynamic content scraping.
- **WebDriver Manager**: Automates ChromeDriver installation.
- **Tailwind CSS**: Styling framework via CDN.
- **Jinja2**: Templating engine for HTML rendering.


```markdown
# Project Name

[Add a brief description of your project here]

## Project Structure

```
├── static/              # Static files (CSS, JS, images, etc.)
├── templates/           # HTML templates for Flask
└── venv/                # Virtual environment directory
    ├── Lib/             # Python libraries
    │   └── site-packages/ # Installed Python packages
    └── Scripts/         # Virtual environment scripts
```

## Prerequisites

- Python 3.x (preferably 3.9 or higher)
- Git

## Setup Instructions

Follow these steps to set up the project locally:

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. **Create and Activate Virtual Environment**
- For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
- For MacOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**
The project uses the following main packages (versions may vary):
- Flask==3.1.0
- beautifulsoup4==4.13.3
- requests==2.32.3
- selenium==4.29.0
- python-dotenv==1.0.1
- webdriver-manager==4.0.2

Install them using:
```bash
pip install -r requirements.txt
```
Note: If a `requirements.txt` file isn't present, you can create one by running `pip freeze > requirements.txt` from an environment where the project works.

4. **Environment Variables**
Create a `.env` file in the root directory if required by your application:
```bash
touch .env
```
Add any necessary environment variables (e.g., API keys, database URLs) in this format:
```
KEY_NAME=value
```

5. **Run the Application**
```bash
python app.py
```
Note: Replace `app.py` with your main application file name if different.

## Additional Notes

- The `static/` folder contains static assets
- The `templates/` folder contains Flask HTML templates
- Make sure to have appropriate web drivers installed if using Selenium (e.g., ChromeDriver via webdriver-manager)
- The virtual environment (`venv/`) should not be committed to git (add it to `.gitignore`)

## Troubleshooting

- If you encounter version conflicts, try upgrading pip:
```bash
pip install --upgrade pip
```
- Ensure your Python version matches the one used in development (3.x)

## Contributing

[Add contribution guidelines if applicable]

## License

[Add license information here]
```

### Notes:
1. **Missing Files**: Your structure doesn't show the main Python file (e.g., `app.py`). I assumed it's in the root directory. Adjust the instructions if it's named differently or located elsewhere.
2. **Requirements**: I inferred key dependencies from your `site-packages`. You might want to provide an exact `requirements.txt` file for precision.
3. **Customization**: Replace placeholders (e.g., repo URL, project name, description) with your actual details.
4. **gitignore**: You should add `venv/` and `.env` to your `.gitignore` file to avoid committing them.

Let me know if you need any specific adjustments or additional sections!
