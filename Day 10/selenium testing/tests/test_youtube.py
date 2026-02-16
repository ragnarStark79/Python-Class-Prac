from __future__ import annotations

import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
    # Disable autoplay policy for YouTube
    opts.add_argument("--autoplay-policy=no-user-gesture-required")

    service = Service(ChromeDriverManager().install())
    d = webdriver.Chrome(service=service, options=opts)
    d.implicitly_wait(2)

    try:
        yield d
    finally:
        d.quit()


def test_youtube_search_and_play(driver):
    """Test YouTube search for 'python one shot' and play second video (skip ads if present)"""
    base = "https://www.youtube.com"
    
    print("\n🌐 Opening YouTube...")
    driver.get(base)
    time.sleep(3)
    
    # Handle potential cookie consent popup
    try:
        print("✓ Checking for cookie consent...")
        reject_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Reject all']"))
        )
        reject_btn.click()
        time.sleep(1.5)
        print("✓ Cookie consent handled")
    except Exception:
        print("✓ No cookie consent popup (or already accepted)")
        pass
    
    print("🔍 Looking for search box...")
    time.sleep(2)
    
    # Find and click search box
    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "search_query"))
        )
        print("📝 Typing search query: 'python one shot'...")
        search_box.click()
        time.sleep(1)
        
        search_box.send_keys("python one shot")
        time.sleep(2)
        
        print("🔘 Submitting search...")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        
    except Exception as e:
        print(f"❌ Could not find search box: {e}")
        # Try alternative method
        search_icon = driver.find_element(By.ID, "search-icon-legacy")
        search_icon.click()
        time.sleep(1)
        search_box = driver.find_element(By.NAME, "search_query")
        search_box.send_keys("python one shot")
        time.sleep(2)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
    
    print("✓ Waiting for search results...")
    time.sleep(3)
    
    print("🎬 Finding second video (skipping first to avoid ads)...")
    # Find the second video link (skip first which might be an ad)
    try:
        # Wait for video results
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "video-title"))
        )
        time.sleep(2)
        
        # Get all video title links and click the second one
        video_links = driver.find_elements(By.ID, "video-title")
        
        # Filter out empty links and get valid videos
        valid_videos = []
        for link in video_links:
            href = link.get_attribute("href")
            if href and "/watch?v=" in href:
                valid_videos.append(link)
        
        if len(valid_videos) < 2:
            print("⚠️ Less than 2 videos found, playing the first available video...")
            target_video = valid_videos[0]
        else:
            print(f"✓ Found {len(valid_videos)} videos, selecting the 2nd one...")
            target_video = valid_videos[1]  # Select second video
        
        print(f"✓ Target video: {target_video.get_attribute('title')}")
        time.sleep(1.5)
        
        print("🔘 Clicking second video...")
        target_video.click()
        time.sleep(4)
        
        print("▶️ Video page loaded, checking for ads...")
        time.sleep(3)
        
        # Wait for video player to load
        print("✓ Waiting for video player...")
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "video.video-stream"))
        )
        time.sleep(2)
        
        # Handle ad skipping - wait up to 30 seconds for skip button
        print("🔍 Checking for ads...")
        ad_skipped = False
        skip_wait_time = 0
        max_skip_wait = 30  # Maximum 30 seconds to wait for skip button
        
        while skip_wait_time < max_skip_wait:
            try:
                # Look for various skip button selectors YouTube uses
                skip_selectors = [
                    "button.ytp-ad-skip-button",
                    "button.ytp-ad-skip-button-modern",
                    ".ytp-ad-skip-button",
                    ".ytp-ad-skip-button-modern",
                    "button[class*='skip']",
                ]
                
                skip_button = None
                for selector in skip_selectors:
                    try:
                        skip_button = driver.find_element(By.CSS_SELECTOR, selector)
                        if skip_button.is_displayed():
                            break
                    except:
                        continue
                
                if skip_button and skip_button.is_displayed():
                    print("📢 Ad detected! Skip button found.")
                    time.sleep(1)
                    print("🔘 Clicking 'Skip Ad' button...")
                    skip_button.click()
                    time.sleep(2)
                    ad_skipped = True
                    print("✅ Ad skipped successfully!")
                    break
                else:
                    # Check if ad is still playing by looking for ad indicators
                    ad_indicators = driver.find_elements(By.CSS_SELECTOR, ".ytp-ad-text, .ytp-ad-player-overlay")
                    if ad_indicators and any(elem.is_displayed() for elem in ad_indicators):
                        print(f"⏳ Ad is playing... waiting for skip button ({skip_wait_time}s elapsed)...")
                        time.sleep(2)
                        skip_wait_time += 2
                    else:
                        print("✓ No ads detected, video should be playing!")
                        break
                        
            except Exception as e:
                # No skip button found, check if ad is over or never existed
                try:
                    # Check if the actual video is playing (not an ad)
                    video_element = driver.find_element(By.CSS_SELECTOR, "video.video-stream")
                    current_time = driver.execute_script("return arguments[0].currentTime;", video_element)
                    if current_time > 0:
                        print("✓ Video is playing (no ad or ad finished)")
                        break
                except:
                    pass
                
                time.sleep(1)
                skip_wait_time += 1
                
                if skip_wait_time >= max_skip_wait:
                    print("⚠️ Timeout waiting for ad to finish, continuing anyway...")
                    break
        
        # Additional wait to ensure we're past any ads
        time.sleep(3)
        
        print("⏯️ Main video is now playing... waiting 20 seconds of playback...")
        # Let video play for 20 seconds
        for i in range(20, 0, -1):
            print(f"   ⏱️ {i} seconds remaining...")
            time.sleep(1)
        
        print("⏸️ Pausing video...")
        # Find and click the video player to pause
        video_element = driver.find_element(By.CSS_SELECTOR, "video.video-stream")
        
        # Pause using JavaScript (more reliable than clicking)
        driver.execute_script("arguments[0].pause();", video_element)
        time.sleep(2)
        
        # Verify video is paused
        is_paused = driver.execute_script("return arguments[0].paused;", video_element)
        
        if is_paused:
            print("✅ Video successfully paused!")
        else:
            print("⚠️ Video may still be playing")
        
        time.sleep(2)
        
        if ad_skipped:
            print("✅ YouTube test completed successfully! (Ad was skipped)")
        else:
            print("✅ YouTube test completed successfully! (No ads encountered)")
        
    except Exception as e:
        print(f"❌ Error during video playback: {e}")
        # Take a screenshot for debugging
        screenshot_path = "youtube_test_error.png"
        driver.save_screenshot(screenshot_path)
        print(f"📸 Screenshot saved to: {screenshot_path}")
        raise
