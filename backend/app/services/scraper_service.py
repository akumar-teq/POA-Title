from playwright.sync_api import sync_playwright
import urllib.parse


def search_bexar(search_text):
    results = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Monitor API requests for debugging
        page.on(
            "response",
            lambda response: print("API:", response.url, response.status) if "results?" in response.url else None
        )

        # Open homepage
        page.goto("https://bexar.tx.publicsearch.us/")
        page.wait_for_timeout(3000)
        
        print(f"Searching: {search_text}")

        # Click Advanced Search
        try:
            page.locator('a:has-text("Advanced Search")').first.click(timeout=5000)
            page.wait_for_timeout(2000)
            print("Clicked Advanced Search")
        except Exception as e:
            print("Could not find Advanced Search link or already on it.", e)

        # Fill search box and press Enter to tokenize
        try:
            search_input = page.locator('#partyNames-input')
            search_input.wait_for(state="visible", timeout=5000)
            search_input.fill(search_text)
            page.wait_for_timeout(500)
            page.keyboard.press("Enter")
            print("Filled tokens")
        except Exception as e:
            print("Could not fill #partyNames-input", e)
            browser.close()
            return {"query": search_text, "results": ["Failed to fill search"]}

        page.wait_for_timeout(1000)

        # Click search button
        try:
            page.locator('form button[type="submit"]').first.click()
            print("Clicked explicit submit button")
        except Exception as e:
            print("Could not click submit button", e)

        # Wait for results page network to be idle
        page.wait_for_load_state("networkidle", timeout=15000)
        page.wait_for_timeout(3000)

        print(f"Loaded URL: {page.url}")

        # Extract rows
        rows = page.locator("table tbody tr")
        count = rows.count()
        print(f"Rows found: {count}")

        for i in range(count):
            try:
                row_text = rows.nth(i).inner_text()
                if row_text.strip():
                    results.append(row_text.strip().replace("\n", " | "))
            except:
                pass

        browser.close()

    return {
        "query": search_text,
        "results": results
    }