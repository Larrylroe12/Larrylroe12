import os
from playwright.sync_api import sync_playwright, expect

def test_agent_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local HTML file
        page.goto(f"file://{os.path.abspath('LAgent.html')}")

        # Wait for the app to initialize
        # We expect the "L-AGENT" header to be visible
        expect(page.locator("text=L-AGENT")).to_be_visible()

        # Expect the system initialized message
        expect(page.locator("text=SYSTEM INITIALIZED")).to_be_visible()

        # Check input area exists
        expect(page.get_by_placeholder("Enter command or ask for flights...")).to_be_visible()

        # Take a screenshot
        page.screenshot(path="verification/agent_ui.png")
        print("Screenshot saved to verification/agent_ui.png")

        browser.close()

if __name__ == "__main__":
    test_agent_ui()
