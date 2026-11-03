# from playwright.sync_api import sync_playwright, expect

# def test_login() -> None:
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto("https://www.saucedemo.com/")
#         page.locator("[data-test=\"username\"]").fill("standard_user")
#         page.locator("[data-test=\"password\"]").fill("secret_sauce")
#         page.locator("[data-test=\"login-button\"]").click()
#         expect(page).to_have_url("https://www.saucedemo.com/inv")
#         browser.close()


from playwright.sync_api import sync_playwright, expect


from playwright.sync_api import Page, expect


def test_login(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    # expect(page).to_have_url("https://www.saucedemo.com/wrong-url.html")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

#End to end Testing in Playwright Python

#Test data - Use different inputs to test the same workflow 
#API Mocking - Simulate API responses without calling actual 
#backend service

#End to End Workflow 

#Start ->Open LOgin Page -> Enter Username -> Enter Password ->
# Click Login -> Verify Dashboard -> End 