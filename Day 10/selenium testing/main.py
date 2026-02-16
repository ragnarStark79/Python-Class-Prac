#!/usr/bin/env python3
"""Main entry point for Selenium tests.

Usage:
    python main.py user     # Test local Flask site (simple_site)
    python main.py quotes   # Test quotes.toscrape.com
    python main.py youtube  # Test YouTube search and video play
"""
from __future__ import annotations

import sys
import subprocess
from pathlib import Path
from datetime import datetime


def run_tests(target: str) -> int:
    """Run pytest for the specified target and generate a report."""
    repo_root = Path(__file__).resolve().parents[2]
    venv_python = repo_root / ".venv" / "bin" / "python"
    tests_dir = Path(__file__).parent / "tests"
    
    # Determine which test file to run
    if target == "user":
        test_file = tests_dir / "test_ui_login.py"
        site_name = "Local Flask Site (simple_site)"
        log_subdir = "userlogs"
    elif target == "quotes":
        test_file = tests_dir / "test_quotes_site.py"
        site_name = "Quotes.toscrape.com"
        log_subdir = "quotelogs"
    elif target == "youtube":
        test_file = tests_dir / "test_youtube.py"
        site_name = "YouTube (python one shot search)"
        log_subdir = "youtubelogs"
    else:
        print(f"❌ Unknown target: {target}")
        print("Usage: python main.py [user|quotes|youtube]")
        return 1
    
    if not test_file.exists():
        print(f"❌ Test file not found: {test_file}")
        return 1
    
    # Generate timestamped report filename in tests/testlogs/{userlogs|quotelogs|youtubelogs}/
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    report_dir = tests_dir / "testlogs" / log_subdir
    report_dir.mkdir(parents=True, exist_ok=True)
    
    txt_report = report_dir / f"test-run-{target}-{timestamp}.txt"
    xml_report = report_dir / f"test-report-{target}.xml"
    
    print(f"\n{'='*60}")
    print(f"🚀 Running Selenium tests for: {site_name}")
    print(f"{'='*60}\n")
    
    # Run pytest with verbose output
    cmd = [
        str(venv_python),
        "-m",
        "pytest",
        str(test_file),
        "-vv",
        "--tb=short",
        "-s",  # Show print output for YouTube test
        f"--junitxml={xml_report}",
    ]
    
    try:
        # Run and capture output
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(repo_root),
        )
        
        # Combine stdout and stderr
        output = result.stdout + result.stderr
        
        # Print to console
        print(output)
        
        # Save to text file
        with open(txt_report, "w") as f:
            f.write(f"Selenium Test Report\n")
            f.write(f"Target: {site_name}\n")
            f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"{'='*60}\n\n")
            f.write(output)
        
        # Print summary
        print(f"\n{'='*60}")
        if result.returncode == 0:
            print(f"✅ All tests PASSED for {site_name}")
        else:
            print(f"❌ Some tests FAILED for {site_name}")
        print(f"{'='*60}")
        print(f"📄 Text report saved: {txt_report}")
        print(f"📄 XML report saved:  {xml_report}")
        print(f"{'='*60}\n")
        
        return result.returncode
        
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return 1


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python main.py [user|quotes|youtube]")
        print("\nOptions:")
        print("  user    - Test local Flask site (simple_site)")
        print("  quotes  - Test quotes.toscrape.com")
        print("  youtube - Test YouTube search and video play")
        return 1
    
    target = sys.argv[1].lower()
    return run_tests(target)


if __name__ == "__main__":
    sys.exit(main())
