from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging

logging.basicConfig(filename='scraper.log', level=logging.INFO)

def scrape_peptide_articles(url):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        driver.get(url)
        time.sleep(5)  # Wait for dynamic content to load

        # Adjust the selector based on the website's structure
        articles = driver.find_elements_by_css_selector('.peptide-article')
        results = []
        for article in articles:
            title = article.find_element_by_css_selector('h2').text
            link = article.find_element_by_css_selector('a').get_attribute('href')
            results.append((title, link))
    
        logging.info(f"Scraped {len(results)} articles from {url}")
        return results
    except Exception as e:
        logging.error(f"Error scraping {url}: {e}")
    finally:
        driver.quit()

# Example usage
# articles = scrape_peptide_articles("https://example-scientific-site.com/peptides")

