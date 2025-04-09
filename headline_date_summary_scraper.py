from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

# List of URLs
urls = {
    'Argentina': 'https://www.capitaleconomics.com/search?s=Argentina&f%5B0%5D=region%3A119',
    'Australia': 'https://www.capitaleconomics.com/search?s=&f%5B0%5D=product%3A1798&f%5B1%5D=region%3A17',
    'Austria': 'https://www.capitaleconomics.com/search?s=Austria',
    'Belgium': 'https://www.capitaleconomics.com/search?s=Belgium',
    'Brazil': 'https://www.capitaleconomics.com/search?f%5B0%5D=product%3A1806&f%5B1%5D=region%3A121',
    'Canada': 'https://www.capitaleconomics.com/search?f%5B0%5D=product%3A1799&f%5B1%5D=region%3A57',
    'Chile': 'https://www.capitaleconomics.com/search?s=Chile&f%5B0%5D=region%3A122',
    'China': 'https://www.capitaleconomics.com/search?f%5B0%5D=product%3A1800&f%5B1%5D=region%3A11',
    'Colombia': 'https://www.capitaleconomics.com/search?s=Columbia',
    'Costa Rica': 'https://www.capitaleconomics.com/search?s=%22Costa+Rica%22',
    'Czech Republic': 'https://www.capitaleconomics.com/search?s=Czech',
    'Finland': 'https://www.capitaleconomics.com/search?s=Finland',
    'France': 'https://www.capitaleconomics.com/search?s=France&f%5B0%5D=region%3A82',
    'Germany': 'https://www.capitaleconomics.com/search?s=Germany&f%5B0%5D=region%3A6&f%5B1%5D=region%3A75&f%5B2%5D=region%3A79',
    'Greece': 'https://www.capitaleconomics.com/search?s=Greece&f%5B0%5D=region%3A76',
    'Guatemala': 'https://www.capitaleconomics.com/search?s=Guatemala',
    'Hong Kong': 'https://www.capitaleconomics.com/search?s=Hong%20Kong',
    'Hungary': 'https://www.capitaleconomics.com/search?s=Hungary',
    'India': 'https://www.capitaleconomics.com/search?f%5B0%5D=product%3A1804&f%5B1%5D=region%3A87',
    'Ireland': 'https://www.capitaleconomics.com/search?s=Ireland',
    'Italy': 'https://www.capitaleconomics.com/search?s=Italy',
    'Japan': 'https://www.capitaleconomics.com/search?s=&f%5B0%5D=product%3A1805&f%5B1%5D=region%3A10',
    'Mexico': 'https://www.capitaleconomics.com/search?s=Mexico&f%5B0%5D=region%3A126',
    'Netherlands': 'https://www.capitaleconomics.com/search?s=Netherlands',
    'Norway': 'https://www.capitaleconomics.com/search?s=Norway',
    'Panama': 'https://www.capitaleconomics.com/search?s=Panama',
    'Peru': 'https://www.capitaleconomics.com/search?s=Peru',
    'Poland': 'https://www.capitaleconomics.com/search?s=Poland',
    'Portugal': 'https://www.capitaleconomics.com/search?s=portugal&f%5B0%5D=region%3A110',
    'Romania': 'https://www.capitaleconomics.com/search?s=Romania',
    'Singapore': 'https://www.capitaleconomics.com/search?s=Singapore',
    'Slovakia': 'https://www.capitaleconomics.com/search?s=Slovakia',
    'Spain': 'https://www.capitaleconomics.com/search?s=Spain',
    'Sweden': 'https://www.capitaleconomics.com/search?s=Sweden',
    'Switzerland': 'https://www.capitaleconomics.com/search?s=Switzerland',
    'Taiwan': 'https://www.capitaleconomics.com/search?s=Taiwan',
    'Turkey': 'https://www.capitaleconomics.com/search?s=Turkey',
    'UAE': 'https://www.capitaleconomics.com/search?s=UAE',
    'UK': 'https://www.capitaleconomics.com/search?f%5B0%5D=region%3A8',
    'USA': 'https://www.capitaleconomics.com/search?f%5B0%5D=product%3A1811&f%5B1%5D=region%3A118'

}

results_dict = {}


### Scraper FOR loop
for country, url in urls.items():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    results = soup.find_all('li', class_='py-4 white-box hover:bg-gray-50', limit=15)

    entries = []
    for result in results:
        title_elem = result.find('h5')
        summary_elem = result.find('p', class_='text-sm text-gray-500')
        title = title_elem.get_text(strip=True) if title_elem else ''
        summary = summary_elem.get_text(strip=True) if summary_elem else ''
        date_elem = result.find('time')
        date = date_elem.get_text(strip=True) if date_elem else ''
        combined = f"{title} --- {date} --- {summary}"
        entries.append(combined)

    results_dict[country] = entries

# Combine into rows side by side 
rows = list(zip(*results_dict.values()))


# Generate filename with timestamp
timestamp = datetime.now().strftime('%Y-%m-%d_%H%M')
filename = f"MEOS_secondary_{timestamp}.csv"

# Specified final file location
file_path = fr"C:\SPECIFY THE LOCATION\{filename}"

# Create the csv
with open(file_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(results_dict.keys())  # Header row
    writer.writerows(rows)

# Show completion
print(f" CSV file saved to: {file_path}")
