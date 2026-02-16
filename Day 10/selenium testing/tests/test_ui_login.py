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
    # Headless by default in CI; set HEADLESS=0 to watch it.
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


def test_home_page(server_url: str, driver):
    print("\n🌐 Opening home page...")
    driver.get(server_url + "/")
    time.sleep(2)  # Human-like pause
    
    print("✓ Checking page title...")
    assert driver.find_element(By.ID, "title").text == "Simple Testing Website"
    time.sleep(1)
    
    print("✓ Checking login link...")
    assert driver.find_element(By.ID, "login-link").get_attribute("href").endswith("/login")
    time.sleep(1)
    print("✅ Home page test passed!")


def test_invalid_login_shows_error(server_url: str, driver):
    print("\n🌐 Opening login page...")
    driver.get(server_url + "/login")
    time.sleep(2)

    print("📝 Entering username: 'student'...")
    driver.find_element(By.ID, "username").send_keys("student")
    time.sleep(1.5)
    
    print("📝 Entering wrong password: 'wrong'...")
    driver.find_element(By.ID, "password").send_keys("wrong")
    time.sleep(1.5)
    
    print("🔘 Clicking submit button...")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    print("✓ Checking for error message...")
    err = driver.find_element(By.ID, "error")
    assert "Invalid username" in err.text
    time.sleep(1)
    print("✅ Invalid login error test passed!")


def test_valid_login_dashboard_logout(server_url: str, driver):
    print("\n🌐 Opening login page...")
    driver.get(server_url + "/login")
    time.sleep(2)

    print("📝 Entering username: 'student'...")
    driver.find_element(By.ID, "username").send_keys("student")
    time.sleep(1.5)
    
    print("📝 Entering password: 'password123'...")
    driver.find_element(By.ID, "password").send_keys("password123")
    time.sleep(1.5)
    
    print("🔘 Clicking submit button...")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2.5)

    print("✓ Waiting for dashboard to load...")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dashboard-title")))
    time.sleep(2)
    
    print("✓ Verifying user is logged in...")
    assert driver.find_element(By.ID, "user").text == "student"
    time.sleep(1.5)

    print("🔘 Clicking logout button...")
    logout_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout"))
    )
    # Use JavaScript click for reliability
    driver.execute_script("arguments[0].click();", logout_btn)
    time.sleep(3)
    
    print("✓ Waiting for redirect to home page...")
    WebDriverWait(driver, 10).until(EC.url_changes(server_url + "/dashboard"))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title")))
    time.sleep(1.5)
    
    print("✓ Verifying we're back on home page...")
    assert driver.find_element(By.ID, "title").text == "Simple Testing Website"
    time.sleep(1)
    print("✅ Full login/logout flow test passed!")
