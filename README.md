# Automated News Web Scraper

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Overview

The Automated News Web Scraper is an automated script designed to run daily, collecting and aggregating news articles from tech website. This project provides a convenient way to stay updated with the latest news by scraping relevant information from specified website.

## Features

- **Automated Daily Execution with Selenium**: Schedule the script to run daily and fetch the latest news.
- **Website Aggregation**: Scrape news articles from specified websites using XPath.
- **Data Storage in CSV file**: Store scraped data in a structured format for analysis or future reference.
- **Dependencies**: All necessary dependencies are listed in the `requirements.txt` file for easy installation.

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python Package Installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/babicmila/news-web-scraper.git
   cd news-web-scraper


2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:

   ```bash
   python news-headlines.py

4. Schedule Daily Execution (Optional):

   To run the script daily, set up a scheduled task (Windows) or crontab job (macOS).

   For Windows users:
   1. Search for “Task Scheduler”.
   2. Go to Actions > Create Task, and give a name to the task
   3. Go to Actions > New
   4. In Program/Script, add the path to the Python executable file.
   5. In the "Add arguments (optional)” box, add the name of your Python file (news-headlines.exe).
   6. In the "Start in (optional)" box, add the location of that python file.
   7. Go to “Triggers” > New , and schedule script to run daily and choose time you prefer



   ![Screenshot 2024-01-18 1554444](https://github.com/babicmila/news-web-scraper/assets/57596723/867e1782-b144-45c4-94f0-984070e5fade)
