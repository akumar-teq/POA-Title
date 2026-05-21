from playwright.sync_api import sync_playwright

def test_scraper():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://bexar.tx.publicsearch.us/")

        print(page.title())

        browser.close()
