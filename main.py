import requests
from bs4 import BeautifulSoup

def scrape_laptops():
    url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"
    

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    
    products = soup.select(".thumbnail")

    print("\n💻 Laptops Found:\n")

    for product in products:
        title = product.select_one(".title").get_text(strip=True)
        price = product.select_one(".price").get_text(strip=True)
        description = product.select_one(".description").get_text(strip=True)
        print(f"Title: {title}\nPrice: {price}\nDescription: {description}\n")

if __name__ == "__main__":
    scrape_laptops()
