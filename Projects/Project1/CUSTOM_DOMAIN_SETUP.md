# Custom Domain Setup Guide for Portfolio Web App

This guide will help you access your Student Portfolio Web Application using a custom domain name (`portfolio.com`) on your local network.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Step-by-Step Setup](#step-by-step-setup)
4. [Access Methods](#access-methods)
5. [Troubleshooting](#troubleshooting)
6. [Security Notes](#security-notes)

---

## 🎯 Overview

**Goal**: Access your portfolio at `http://portfolio.com` instead of `http://localhost:5001`

**Your Configuration**:
- **IP Address**: `172.28.10.63` (Your MacBook's local network IP)
- **Custom Domain**: `portfolio.com`
- **Application Port**: 80 (standard HTTP) or 5001 (development)

---

## ✅ Prerequisites

Before starting, ensure you have:
- ✓ Python 3 installed
- ✓ Flask installed (`pip3 install flask`)
- ✓ Administrative (sudo) access to your Mac
- ✓ Your MacBook's local IP address (already found: `172.28.10.63`)

---

## 🚀 Step-by-Step Setup

### Step 1: Find Your MacBook's IP Address (Already Done ✓)

You already have this: **172.28.10.63**

To verify or find it again:
```bash
ifconfig | grep "inet " | grep -v 127.0.0.1
```

Look for the IP address under your active network interface (usually `en0` for Wi-Fi).

---

### Step 2: Edit the Hosts File

The hosts file maps domain names to IP addresses locally.

#### 2.1 Open the hosts file with sudo privileges:
```bash
sudo nano /etc/hosts
```

#### 2.2 Add your custom domain mapping:
Add this line at the end of the file:
```
172.28.10.63 portfolio.com
```

**Important**: Use your actual IP address! If your IP is different, replace `172.28.10.63`.

#### 2.3 Save and exit:
- Press `Ctrl + O` (Write Out)
- Press `Enter` (Confirm)
- Press `Ctrl + X` (Exit)

#### 2.4 Verify the changes:
```bash
cat /etc/hosts | grep portfolio
```

You should see your entry: `172.28.10.63 portfolio.com`

---

### Step 3: Flush DNS Cache

After editing `/etc/hosts`, flush the DNS cache:

```bash
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
```

This ensures macOS uses your new hosts entry immediately.

---

### Step 4: Choose Your Running Mode

You have two options:

#### Option A: Development Mode (Port 5001) - No sudo required
```bash
cd "/Users/ragnar/Documents/COD LANG/FTW/Projects/Project1"
./start.sh
```

**Access at**:
- `http://portfolio.com:5001`
- `http://172.28.10.63:5001`
- `http://localhost:5001`

#### Option B: Production Mode (Port 80) - Requires sudo ⭐ RECOMMENDED
```bash
cd "/Users/ragnar/Documents/COD LANG/FTW/Projects/Project1"
./start-production.sh
```

**Access at**:
- `http://portfolio.com` (no port needed!)
- `http://172.28.10.63`
- `http://localhost`

**Note**: Port 80 is the standard HTTP port, so you don't need to specify it in the URL.

---

## 🌐 Access Methods

Once the server is running, you can access your portfolio in multiple ways:

### On Your MacBook (Local Access):

| URL | Mode | Notes |
|-----|------|-------|
| `http://portfolio.com` | Production | Clean URL, port 80 |
| `http://portfolio.com:5001` | Development | Port 5001 |
| `http://localhost` | Production | Standard local access |
| `http://localhost:5001` | Development | Development access |
| `http://127.0.0.1` | Production | Loopback address |
| `http://172.28.10.63` | Production | Your IP address |

### From Other Devices on Your Network:

**Important**: The custom domain `portfolio.com` won't work on other devices unless you edit their hosts files too.

From other devices, use:
- `http://172.28.10.63` (Production mode)
- `http://172.28.10.63:5001` (Development mode)

To use `portfolio.com` on other devices, edit their hosts files:

**Windows**: `C:\Windows\System32\drivers\etc\hosts`
**Mac/Linux**: `/etc/hosts`

Add: `172.28.10.63 portfolio.com`

---

## 🔧 Troubleshooting

### Issue 1: "Address already in use" (Port 80)

**Cause**: Another service is using port 80 (common on macOS with Apache or AirPlay).

**Solution A** - Stop conflicting services:
```bash
# Check what's using port 80
sudo lsof -i :80

# Stop Apache if running
sudo apachectl stop

# Disable AirPlay Receiver (System Settings > General > AirDrop & Handoff)
```

**Solution B** - Use development mode (port 5001):
```bash
./start.sh
```
Access at: `http://portfolio.com:5001`

---

### Issue 2: "Address already in use" (Port 5001)

**Cause**: Flask is already running.

**Solution**:
```bash
# Find the process
lsof -i :5001

# Kill the process (replace PID with actual number)
kill -9 PID

# Or kill all Python processes
killall python3
```

---

### Issue 3: Can't access via `portfolio.com`

**Checklist**:
1. ✓ Check hosts file entry: `cat /etc/hosts | grep portfolio`
2. ✓ Flush DNS cache: `sudo dscacheutil -flushcache`
3. ✓ Verify IP is correct: `ifconfig | grep "inet "`
4. ✓ Ensure server is running: Check terminal output
5. ✓ Try with IP directly: `http://172.28.10.63`

**Test DNS resolution**:
```bash
ping portfolio.com
```
It should show `172.28.10.63`.

---

### Issue 4: Connection refused

**Cause**: Flask not listening on all interfaces.

**Solution**: The app is already configured with `host='0.0.0.0'` - this is correct.

**Verify firewall settings**:
```bash
# Allow incoming connections
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --add python3
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --unblockapp python3
```

---

### Issue 5: Works locally but not from other devices

**Checklist**:
1. ✓ Server must be on `0.0.0.0`, not `127.0.0.1` (already configured ✓)
2. ✓ Check macOS Firewall (System Settings > Network > Firewall)
3. ✓ Ensure both devices are on same network
4. ✓ Use IP address, not `portfolio.com` on other devices (unless hosts file edited)

---

## 🔒 Security Notes

### Important Security Considerations:

1. **Local Development Only**: This setup is for local development/testing
2. **Port 80 Requires Sudo**: Running on port 80 needs administrator privileges
3. **No HTTPS**: This setup uses HTTP (not secure). Don't use for sensitive data
4. **Network Exposure**: `host='0.0.0.0'` makes your app accessible to anyone on your network
5. **Debug Mode**: Don't use debug mode in production environments

### Recommended Practices:

- ✓ Use development mode (port 5001) for daily work
- ✓ Use production mode (port 80) only when testing custom domain
- ✓ Stop the server when not in use
- ✓ Don't expose your development server to the internet
- ✓ Use a proper web server (nginx/Apache) for real production deployment

---

## 📝 Quick Reference Commands

### Start Server (Development - Port 5001):
```bash
cd "/Users/ragnar/Documents/COD LANG/FTW/Projects/Project1"
./start.sh
```

### Start Server (Production - Port 80):
```bash
cd "/Users/ragnar/Documents/COD LANG/FTW/Projects/Project1"
./start-production.sh
```

### Stop Server:
```
Ctrl + C
```

### Check Your IP:
```bash
ifconfig | grep "inet " | grep -v 127.0.0.1
```

### Edit Hosts File:
```bash
sudo nano /etc/hosts
```

### Flush DNS Cache:
```bash
sudo dscacheutil -flushcache && sudo killall -HUP mDNSResponder
```

### Test Domain Resolution:
```bash
ping portfolio.com
```

### Check Port Usage:
```bash
# Check port 80
sudo lsof -i :80

# Check port 5001
lsof -i :5001
```

### View Hosts File:
```bash
cat /etc/hosts
```

---

## 🎯 Complete Setup Example

Here's a complete setup session from scratch:

```bash
# Step 1: Navigate to project
cd "/Users/ragnar/Documents/COD LANG/FTW/Projects/Project1"

# Step 2: Edit hosts file
sudo nano /etc/hosts
# Add: 172.28.10.63 portfolio.com
# Save and exit (Ctrl+O, Enter, Ctrl+X)

# Step 3: Flush DNS
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder

# Step 4: Test DNS resolution
ping -c 3 portfolio.com

# Step 5: Start server (choose one)
./start.sh                  # Development mode (port 5001)
# OR
./start-production.sh       # Production mode (port 80)

# Step 6: Access in browser
# Open: http://portfolio.com (production) or http://portfolio.com:5001 (dev)
```

---

## 🌟 Success Indicators

You'll know everything is working when:

1. ✅ `ping portfolio.com` resolves to `172.28.10.63`
2. ✅ Server starts without errors
3. ✅ You see "Running on http://0.0.0.0:80" or "Running on http://0.0.0.0:5001"
4. ✅ Browser opens `http://portfolio.com` successfully
5. ✅ All three pages load (Home, Previous Semester, Portfolio)
6. ✅ CSS styling and animations work
7. ✅ Can access from other devices using `http://172.28.10.63`

---

## 📱 Accessing from Mobile/Other Devices

### On the same Wi-Fi network:

1. **Find your Mac's IP** (you have: `172.28.10.63`)
2. **Start the server** on your Mac
3. **Open browser** on mobile/other device
4. **Visit**: `http://172.28.10.63` (production) or `http://172.28.10.63:5001` (dev)

### To use `portfolio.com` on mobile:

**iOS/Android** - Can't easily edit hosts file without jailbreak/root

**Alternative**: Use the IP address directly

**Windows/Mac/Linux devices** - Edit hosts file as shown above

---

## 🔄 IP Address Changes

**Important**: Your local IP (`172.28.10.63`) may change if:
- You reconnect to Wi-Fi
- Your router assigns a new IP (DHCP)
- You switch networks

### If your IP changes:

1. Find new IP: `ifconfig | grep "inet " | grep -v 127.0.0.1`
2. Update hosts file: `sudo nano /etc/hosts`
3. Change the line: `NEW_IP portfolio.com`
4. Flush DNS cache
5. Restart the server

### To prevent IP changes:

Configure a **static IP** in your router (DHCP reservation) for your Mac's MAC address.

---

## 🎓 Understanding the Setup

### What is `/etc/hosts`?

The hosts file is a local DNS override. When you type `portfolio.com`:
1. Your OS checks `/etc/hosts` first
2. Finds: `172.28.10.63 portfolio.com`
3. Connects to `172.28.10.63` instead of looking up DNS

### Why port 80?

- Port 80 is the default HTTP port
- URLs like `http://portfolio.com` automatically use port 80
- No need to specify port in URL
- More "production-like" experience

### Why `host='0.0.0.0'`?

- `127.0.0.1` - Only accessible from this Mac
- `0.0.0.0` - Accessible from any network interface
- Allows access from other devices on your network

---

## ✅ Final Checklist

Before you start:

- [ ] Verified your IP address (`172.28.10.63`)
- [ ] Edited `/etc/hosts` with correct mapping
- [ ] Flushed DNS cache
- [ ] Flask is installed
- [ ] Tested `ping portfolio.com`
- [ ] Chose development or production mode
- [ ] Started the server
- [ ] Accessed in browser
- [ ] All pages working
- [ ] Animations and styling visible

---

## 🎉 You're All Set!

Your Student Portfolio is now accessible at:
- **http://portfolio.com** (production mode)
- **http://portfolio.com:5001** (development mode)

Enjoy your custom domain setup! 🚀

---

## 📞 Need Help?

If you encounter issues:
1. Check the troubleshooting section above
2. Verify each step was completed correctly
3. Check terminal output for error messages
4. Ensure firewall isn't blocking connections

---

**Created**: January 22, 2026  
**Project**: Student Portfolio Web Application  
**Location**: `/Users/ragnar/Documents/COD LANG/FTW/Projects/Project1`
