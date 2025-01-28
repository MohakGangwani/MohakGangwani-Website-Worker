from datetime import datetime
import time
import requests
from bs4 import BeautifulSoup

def scrape_webpage(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the webpage content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the full HTML content
        html_content = soup.prettify()

        return html_content

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":

    while True:
        # Replace with the URL you want to scrape
        url = "https://mohakgangwani-website.onrender.com/"
        print(f"Rendering the website at {datetime.fromtimestamp(time.time())}")
        content = scrape_webpage(url)
        time.sleep(300)