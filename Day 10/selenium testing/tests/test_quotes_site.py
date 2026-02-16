from __future__ import annotations

import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    opts = Options()
    # Headless by default; set HEADLESS=0 to watch it.
    if os.environ.get("HEADLESS", "1") != "0":
        opts.add_argument("--headless=new")

    opts.add_argument("--window-size=1200,900")

    service = Service(ChromeDriverManager().install())
    d = webdriver.Chrome(service=service, options=opts)
    d.implicitly_wait(2)

    try:
        yield d
    finally:
        d.quit()


def test_quotes_login(driver):
    """Test login flow on quotes.toscrape.com"""
    base = "https://quotes.toscrape.com"
    
    print("\n🌐 Opening quotes.toscrape.com login page...")
    driver.get(base + "/login")
    time.sleep(2)

    print("📝 Entering username: 'admin'...")
    driver.find_element(By.ID, "username").send_keys("admin")
    time.sleep(1.5)
    
    print("📝 Entering password: 'admin'...")
    driver.find_element(By.ID, "password").send_keys("admin")
    time.sleep(1.5)
    
    print("🔘 Clicking submit button...")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    time.sleep(2.5)

    print("✓ Waiting for successful login (checking for Logout link)...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Logout"))
    )
    time.sleep(2)

    print("✓ Verifying we're on the quotes site...")
    assert driver.current_url.startswith(base)
    time.sleep(1)
    print(f"✅ Successfully logged in to {base}")


def test_quotes_logout(driver):
    """Test logout flow on quotes.toscrape.com"""
    base = "https://quotes.toscrape.com"
    
    print("\n🌐 Opening quotes.toscrape.com login page...")
    driver.get(base + "/login")
    time.sleep(2)

    print("📝 Entering username: 'admin'...")
    driver.find_element(By.ID, "username").send_keys("admin")
    time.sleep(1.5)
    
    print("📝 Entering password: 'admin'...")
    driver.find_element(By.ID, "password").send_keys("admin")
    time.sleep(1.5)
    
    print("🔘 Clicking submit button...")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    time.sleep(2.5)

    print("✓ Waiting for successful login...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Logout"))
    )
    time.sleep(2)

    print("🔘 Clicking logout link...")
    driver.find_element(By.LINK_TEXT, "Logout").click()
    time.sleep(2.5)

    print("✓ Waiting for Login link to appear after logout...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Login"))
    )
    time.sleep(1.5)

    print("✓ Verifying Logout link is no longer visible...")
    logout_links = driver.find_elements(By.LINK_TEXT, "Logout")
    assert len(logout_links) == 0, "Logout link should not be visible after logging out"
    time.sleep(1)
    print(f"✅ Successfully logged out from {base}")
