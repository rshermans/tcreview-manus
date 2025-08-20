import re
from playwright.sync_api import sync_playwright, Page, expect

def run_verification(page: Page):
    """
    Verifies the TrueCheck application flow.
    """
    # 1. Navigate to the app
    page.goto("http://localhost:5173")

    # DEBUG: Take a screenshot immediately to see what the page looks like on load
    page.screenshot(path="jules-scratch/verification/debug_initial_load.png")

    # 2. Select input type and fill content
    page.get_by_role("button", name="Texto").click()

    # Fill the textarea
    page.get_by_placeholder("Cole ou digite o texto aqui...").fill("Esta é uma notícia de teste para verificar o fluxo da aplicação.")

    # 3. Click the submit button
    page.get_by_role("button", name="Verificar agora").click()

    # 4. Wait for the results page to load
    results_heading = page.get_by_role("heading", name="Resultados da Verificação Preliminar")
    expect(results_heading).to_be_visible(timeout=15000)

    # 5. Take a screenshot
    page.screenshot(path="jules-scratch/verification/verification.png")

# --- Boilerplate to run the script ---
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        run_verification(page)
        browser.close()

if __name__ == "__main__":
    main()
