import os
from playwright.sync_api import sync_playwright

def debug_agent_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local HTML file
        page.goto(f"file://{os.path.abspath('LAgent.html')}")

        # Wait a bit to let JS run (if any)
        page.wait_for_timeout(2000)

        # Take a screenshot to see what's happening
        page.screenshot(path="verification/agent_debug.png")
        print("Debug screenshot saved to verification/agent_debug.png")

        # Print console logs to check for JS errors
        page.on("console", lambda msg: print(f"Console: {msg.text}"))

        browser.close()

if __name__ == "__main__":
    debug_agent_ui()
