import requests
import time
from bs4 import BeautifulSoup

# Your Render URL
url = "https://mohakgangwani.onrender.com"

# How long to wait between checks (seconds)
check_interval = 5

# Maximum wait time (seconds) before giving up
max_wait_time = 120

def wait_for_site(url):
    print(f"Trying to wake up {url} ...")
    start_time = time.time()

    while True:
        try:
            response = requests.get(url, timeout=10)
            # If the site is actually up and returning OK HTML
            if response.status_code == 200 and "Starting" not in response.text:
                print("✅ Site is awake!")
                return response.text
            else:
                print(f"⏳ Still waking up... (status {response.status_code})")
        except requests.RequestException as e:
            print(f"⚠️ Error: {e}")

        elapsed = time.time() - start_time
        if elapsed > max_wait_time:
            raise TimeoutError("Site did not wake up in time.")

        time.sleep(check_interval)

def main():
    html_content = wait_for_site(url)
    soup = BeautifulSoup(html_content, "html.parser")

    # Print or save all the page content
    print(soup.prettify())

if __name__ == "__main__":
    main()
