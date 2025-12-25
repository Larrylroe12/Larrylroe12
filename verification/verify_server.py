from playwright.sync_api import sync_playwright, expect
import sys

def verify_server():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=['--no-sandbox'])
        page = browser.new_page()

        page.on("console", lambda msg: print(f"Console: {msg.text}"))
        page.on("pageerror", lambda exc: print(f"PageError: {exc}"))

        print("Navigating...")
        try:
            page.goto("http://localhost:8000/LAgent.html", timeout=10000)
        except Exception as e:
            print(f"Navigation failed: {e}")
            return

        print("Waiting for UI...")
        try:
            expect(page.locator("text=L-AGENT")).to_be_visible(timeout=15000)
            print("SUCCESS: UI element L-AGENT found.")
        except Exception as e:
            print(f"FAILURE: UI element not found. {e}")

        page.screenshot(path="verification/agent_server.png")
        browser.close()

if __name__ == "__main__":
    verify_server()
