# Day 10 — Selenium Testing Suite

This folder contains Selenium UI tests for three different sites:
1. **Local Flask site** (`simple_site`) - login/dashboard/logout flow
2. **Quotes.toscrape.com** - external demo site login
3. **YouTube** - search and video playback automation with ad skipping

## Requirements
- Use the **root** virtual environment: `/.venv`
- Google Chrome installed

## Quick Start (Easy Method)

From `Day 10/selenium testing/` directory:

### Test local Flask site
```bash
python main.py user
```

### Test quotes.toscrape.com
```bash
python main.py quotes
```

### Test YouTube (NEW!)
```bash
python main.py youtube
```
This will:
- Open YouTube
- Search for "python one shot"
- Click the **second video** (to avoid potential ads on first result)
- **Automatically detect and skip ads** (waits up to 30 seconds for skip button)
- Let the main video play for **20 seconds**
- Pause the video

All tests include:
- Human-like delays (sleep between actions)
- Step-by-step progress in terminal
- Timestamped reports saved in respective log folders

## Watch Browser (Non-Headless)

**Highly Recommended for YouTube test** to see the ad skipping and video playing:
```bash
env HEADLESS=0 python main.py youtube
env HEADLESS=0 python main.py user
env HEADLESS=0 python main.py quotes
```

## Manual Method (Direct pytest)

From the repository root:

### Test local Flask site
```bash
./.venv/bin/python -m pytest "Day 10/selenium testing/tests/test_ui_login.py" -v -s
```

### Test quotes.toscrape.com
```bash
./.venv/bin/python -m pytest "Day 10/selenium testing/tests/test_quotes_site.py" -v -s
```

### Test YouTube
```bash
./.venv/bin/python -m pytest "Day 10/selenium testing/tests/test_youtube.py" -v -s
```

### Run all tests
```bash
./.venv/bin/python -m pytest "Day 10/selenium testing/tests" -v -s
```

*Note: Add `-s` flag to see print output during test execution*

## Login Credentials

### Local Flask site (`user`)
- Username: `student`
- Password: `password123`

### Quotes.toscrape.com (`quotes`)
- Username: `admin`
- Password: `admin`

### YouTube (`youtube`)
- No login required
- Search query: `python one shot`
- Plays **second video** (skips first to avoid ads)
- **Automatically skips ads** if present (waits for skip button up to 30 seconds)
- Plays main video for 20 seconds then pauses

## Test Reports

Reports are automatically generated in separate folders:
- **User tests:** `tests/testlogs/userlogs/`
  - `test-run-user-{timestamp}.txt` - Human-readable log
  - `test-report-user.xml` - JUnit XML for CI/CD
- **Quotes tests:** `tests/testlogs/quotelogs/`
  - `test-run-quotes-{timestamp}.txt` - Human-readable log
  - `test-report-quotes.xml` - JUnit XML for CI/CD
- **YouTube tests:** `tests/testlogs/youtubelogs/`
  - `test-run-youtube-{timestamp}.txt` - Human-readable log
  - `test-report-youtube.xml` - JUnit XML for CI/CD

## Human-Like Testing

Tests include realistic delays between actions:
- **User/Quotes tests:**
  - 2 seconds after opening a page
  - 1.5 seconds between form field entries
  - 2.5 seconds after clicking submit buttons
- **YouTube test:**
  - 3 seconds after opening YouTube
  - 2 seconds between typing and searching
  - 3 seconds waiting for search results
  - Selects second video (skips first to avoid ads)
  - **Smart ad detection:**
    - Monitors for ad indicators
    - Waits for skip button to appear
    - Clicks skip button automatically
    - Continues if no ads present
  - 20 seconds of main video playback before pausing
- Step-by-step console output showing what's happening

This makes the tests easier to follow and more realistic.

## YouTube Ad Handling

The YouTube test includes intelligent ad skipping:
1. **Detects if an ad is playing** by looking for ad indicators
2. **Waits for skip button** to appear (up to 30 seconds)
3. **Automatically clicks skip button** when available
4. **Handles no-ad scenarios** gracefully
5. **Reports ad status** in terminal output

Example output:
```
🔍 Checking for ads...
📢 Ad detected! Skip button found.
🔘 Clicking 'Skip Ad' button...
✅ Ad skipped successfully!
⏯️ Main video is now playing...
```

## Project Structure
```
selenium testing/
├── main.py              # CLI entry point
├── simple_site/         # Local Flask app
│   ├── app.py
│   └── templates/
└── tests/               # Selenium tests
    ├── conftest.py      # Pytest fixtures
    ├── test_ui_login.py # Local site tests
    ├── test_quotes_site.py # External site tests
    ├── test_youtube.py  # YouTube automation tests (with ad skipping)
    └── testlogs/        # Test reports saved here
        ├── userlogs/    # User (local Flask) test logs
        │   ├── test-run-user-*.txt
        │   └── test-report-user.xml
        ├── quotelogs/   # Quotes site test logs
        │   ├── test-run-quotes-*.txt
        │   └── test-report-quotes.xml
        └── youtubelogs/ # YouTube test logs
            ├── test-run-youtube-*.txt
            └── test-report-youtube.xml
```

## Examples

### Watch YouTube test with ad skipping in action
```bash
cd "Day 10/selenium testing"
env HEADLESS=0 python main.py youtube
```

You'll see:
1. Browser opens YouTube
2. Searches for "python one shot"
3. Clicks **second video** (to avoid ads)
4. **Detects if ad is playing**
5. **Waits for skip button** (if ad present)
6. **Automatically clicks skip** when available
7. Main video plays for 20 seconds (with countdown)
8. Video pauses automatically
9. Test report saved with ad status

### Run all three tests
```bash
python main.py user
python main.py quotes
python main.py youtube
```
