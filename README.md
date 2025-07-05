Glassdoor Job Scraper
This project is a modular web scraping pipeline for extracting job listings from Glassdoor. It captures individual job cards, parses the relevant data (title, salary, and job link), and stores the results in a structured CSV file.

Built using Python with Selenium, BeautifulSoup, and Pandas, the system runs in a dedicated virtual environment for isolation and reproducibility.

Overview
This scraper is designed for research, analysis, or market exploration purposes. The process is divided into two parts:

main.py: Uses Selenium to dynamically load the Glassdoor job results page and save each job card’s raw HTML.

collect.py: Parses the saved HTML files using BeautifulSoup and extracts the job title, salary estimate, and job link.

The final output is stored in jobs_Data.csv.

Project Structure
graphql
Copy
Edit
.
├── data/              # Saved HTML job card files
├── main.py            # Selenium-based scraper for job cards
├── collect.py         # Parser and CSV writer using BeautifulSoup
├── jobs_Data.csv      # Output file with structured job listings
└── README.md          # Project documentation
Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/glassdoor-job-scraper.git
cd glassdoor-job-scraper
2. Set Up a Virtual Environment
bash
Copy
Edit
python -m venv venv
Activate it:

Windows:

bash
Copy
Edit
venv\Scripts\activate
macOS/Linux:

bash
Copy
Edit
source venv/bin/activate
3. Install Required Libraries
bash
Copy
Edit
pip install selenium beautifulsoup4 pandas
Usage
Step 1: Scrape Job Cards
Run main.py to launch a Chrome browser instance and save the HTML of each job card into the data/ folder.

bash
Copy
Edit
python main.py
Step 2: Parse and Export to CSV
Run collect.py to read the saved files, extract data fields, and save them to jobs_Data.csv.

bash
Copy
Edit
python collect.py
Sample Output
title	salary	link
Data Scientist	$110,000/yr	/partner/jobListing.htm?xyz
ML Engineer	None	/partner/jobListing.htm?abc

Technical Stack
Python 3.x

Selenium (for rendering JavaScript and interacting with dynamic pages)

BeautifulSoup (for HTML parsing and data extraction)

Pandas (for structured data storage and CSV export)

Disclaimer
This project is provided for educational and research purposes only. Please consult and adhere to Glassdoor’s Terms of Service and robots.txt before using any automated tools on their platform.

Contact
Abdullah Muhammad Khalid
contact.abdullahkhalid@gmail.com
