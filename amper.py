#!/usr/bin/env python3
import os
import sys
import time
import json
import requests
import subprocess
import random
import threading
from typing import Optional, Dict, Any, List
from enum import Enum
import platform
import argparse
import socket
import webbrowser
from pathlib import Path
from fake_useragent import UserAgent

class Color:
    """Enhanced ANSI color codes with more styles"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'

class Tool(Enum):
    """Extended enumeration of available tools"""
    IP_TRACKER = 1
    GPS_TRACKER = 2
    CAMERA_HACK = 3
    PAYLOAD_GEN = 4
    VIRUS_PRANK = 5
    PHISHING = 6
    PORT_SCAN = 7
    DOS_TOOL = 8
    PHONE_PRANK = 9
    SOCIAL_MEDIA = 10

class DigitalAmperPro:
    """Enhanced Digital Amper Pro toolkit"""
    
    def __init__(self):
        self.version = "2.0.0"
        self.author = "@thedigamber"
        self.instagram_url = "https://www.instagram.com/thedigamber?igsh=MXA5dDV5aHRub3Z3cQ=="
        self.github_url = "https://github.com/thedigamber"
        self.required_packages = [
            'requests', 'colorama', 'fake-useragent', 'pyfiglet'
        ]
        self.tools_dir = Path.home() / ".digital_amper_pro"
        self.config_file = self.tools_dir / "config.json"
        self.ua = UserAgent()
        self._setup_environment()
        
    def _setup_environment(self) -> None:
        """Ensure required directories and files exist"""
        try:
            self.tools_dir.mkdir(exist_ok=True)
            if not self.config_file.exists():
                with open(self.config_file, 'w') as f:
                    json.dump({
                        "first_run": True,
                        "prank_count": 0,
                        "last_used": str(time.time())
                    }, f)
        except Exception as e:
            self.error(f"Failed to setup environment: {e}")
            sys.exit(1)

    def clear_screen(self) -> None:
        """Clear terminal screen with animation"""
        if os.name == 'nt':
            os.system('cls')
        else:
            print("\033c", end="")
            time.sleep(0.1)

    def display_banner(self) -> None:
        """Display animated application banner"""
        self.clear_screen()
        
        # Animated colors
        colors = [Color.RED, Color.GREEN, Color.YELLOW, Color.BLUE, 
                 Color.MAGENTA, Color.CYAN, Color.WHITE]
        current_color = random.choice(colors)
        
        banner = f"""
{current_color}╔═══╗╔╗──╔╗╔═══╗╔═══╗╔══╗╔╗──╔╗╔═══╗╔═══╗╔══╗╔═══╗╔═══╗
{current_color}║╔══╝║║──║║║╔══╝║╔═╗║╚╣─╝║║──║║║╔══╝║╔═╗║╚╣─╝║╔═╗║║╔══╝
{current_color}║╚══╗║║──║║║╚══╗║║─║║─║║─║║──║║║╚══╗║║─║║─║║─║║─║║║╚══╗
{current_color}║╔══╝║║──║║║╔══╝║║─║║─║║─║║─╔╣║║╔══╝║║─║║─║║─║║─║║║╔══╝
{current_color}║║───║╚═╗║╚╣╚══╗║╚═╝║╔╣─╗║╚═╝║╚╣╚══╗║╚═╝║╔╣─╗║╚═╝║║╚══╗
{current_color}╚╝───╚══╝╚═╩═══╝╚═══╝╚══╝╚═══╝─╚═══╝╚═══╝╚══╝╚═══╝╚═══╝
{Color.RESET}
            {Color.BOLD}{Color.BLINK}v{self.version} by {self.author}{Color.RESET}
    {Color.UNDERLINE}Follow me: {self.instagram_url}{Color.RESET}
    {Color.YELLOW}GitHub: {self.github_url}{Color.RESET}
"""
        print(banner)

    def display_menu(self) -> None:
        """Display enhanced main menu with more tools"""
        menu = f"""
{Color.BOLD}{Color.REVERSE}🔥 DIGITAL AMPER PRO - ULTIMATE TOOLKIT 🔥{Color.RESET}

{Color.BOLD}Core Tools:{Color.RESET}
{Color.GREEN}[1] IP Tracker 🌍           {Color.YELLOW}[6] Phishing Toolkit 🎣
{Color.GREEN}[2] GPS Tracker 🛰️         {Color.YELLOW}[7] Port Scanner 🔍
{Color.GREEN}[3] Camera Hack 📸         {Color.YELLOW}[8] DoS Tool ⚡
{Color.GREEN}[4] Payload Generator 💣   {Color.YELLOW}[9] Phone Prank 📞
{Color.GREEN}[5] Virus Prank 😈        {Color.YELLOW}[10] Social Media Toolkit 📱

{Color.RED}[0] Exit ❌{Color.RESET}

{Color.CYAN}Follow for more tools: {self.instagram_url}{Color.RESET}
"""
        print(menu)

    def error(self, message: str) -> None:
        """Enhanced error message with timestamp"""
        timestamp = time.strftime("%H:%M:%S")
        print(f"{Color.RED}[{timestamp}] [!] ERROR: {message}{Color.RESET}")

    def success(self, message: str) -> None:
        """Enhanced success message with timestamp"""
        timestamp = time.strftime("%H:%M:%S")
        print(f"{Color.GREEN}[{timestamp}] [+] {message}{Color.RESET}")

    def warning(self, message: str) -> None:
        """Enhanced warning message with timestamp"""
        timestamp = time.strftime("%H:%M:%S")
        print(f"{Color.YELLOW}[{timestamp}] [!] {message}{Color.RESET}")

    def info(self, message: str) -> None:
        """Enhanced informational message"""
        timestamp = time.strftime("%H:%M:%S")
        print(f"{Color.BLUE}[{timestamp}] [*] {message}{Color.RESET}")

    def animate_text(self, text: str, delay: float = 0.05) -> None:
        """Animate text printing"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def check_dependencies(self) -> bool:
        """Check and install dependencies with progress"""
        missing = []
        for pkg in self.required_packages:
            try:
                __import__(pkg)
            except ImportError:
                missing.append(pkg)
        
        if missing:
            self.warning(f"Missing packages: {', '.join(missing)}")
            if self.confirm("Install missing packages automatically?"):
                self.install_packages(missing)
                return True
            return False
        return True

    def install_packages(self, packages: List[str]) -> None:
        """Install packages with progress indicator"""
        try:
            self.info("Installing dependencies...")
            for pkg in packages:
                print(f"{Color.CYAN}Installing {pkg}...{Color.RESET}")
                subprocess.run(
                    [sys.executable, '-m', 'pip', 'install', pkg],
                    check=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
            self.success("All dependencies installed successfully!")
        except subprocess.CalledProcessError as e:
            self.error(f"Failed to install packages: {e}")

    def confirm(self, question: str) -> bool:
        """Enhanced confirmation with colored prompt"""
        response = input(f"{Color.YELLOW}{question} {Color.BOLD}(y/N): {Color.RESET}").strip().lower()
        return response == 'y'

    # [Previous tool methods (track_ip, gps_tracker, etc.) remain the same but enhanced...]

    def virus_prank(self) -> None:
        """Enhanced Virus Prank with multiple options and animations"""
        self.info("🔥 ULTIMATE VIRUS PRANK TOOL 🔥")
        
        prank_options = {
            '1': ("FBI Virus Prank", self._fbi_prank),
            '2': ("System Hacking Simulation", self._system_hack_prank),
            '3': ("Rick Roll Classic", self._rick_roll_prank),
            '4': ("Fake Bitcoin Miner", self._bitcoin_prank),
            '5': ("Matrix Effect", self._matrix_prank)
        }
        
        while True:
            print(f"\n{Color.BOLD}Available Prank Options:{Color.RESET}")
            for key, (name, _) in prank_options.items():
                print(f"{Color.GREEN}[{key}] {name}{Color.RESET}")
            print(f"{Color.RED}[0] Back to main menu{Color.RESET}")
            
            choice = input("\nSelect prank type: ").strip()
            if choice == '0':
                return
            elif choice in prank_options:
                name, func = prank_options[choice]
                if self.confirm(f"Start '{name}' prank?"):
                    func()
                    break
            else:
                self.error("Invalid choice")

    def _fbi_prank(self) -> None:
        """FBI Warning Prank"""
        try:
            self.clear_screen()
            print(f"{Color.RED}{Color.BOLD}")
            self.animate_text("WARNING: UNAUTHORIZED ACCESS DETECTED!", 0.02)
            time.sleep(1)
            
            print(f"{Color.WHITE}")
            self.animate_text("This computer has been locked by the", 0.03)
            self.animate_text("Federal Bureau of Investigation (FBI)", 0.03)
            print(f"{Color.RED}")
            self.animate_text("======================================", 0.01)
            
            time.sleep(1)
            print(f"{Color.WHITE}")
            self.animate_text("Your IP address has been logged", 0.04)
            self.animate_text("for illegal activities:", 0.04)
            print(f"{Color.BLUE}")
            self.animate_text("- Copyright infringement", 0.04)
            self.animate_text("- Hacking attempts", 0.04)
            self.animate_text("- Illegal downloads", 0.04)
            
            time.sleep(2)
            print(f"{Color.RED}")
            self.animate_text("TO UNLOCK YOUR COMPUTER:", 0.03)
            print(f"{Color.YELLOW}")
            self.animate_text("Pay a fine of $500 via Bitcoin", 0.04)
            self.animate_text("or face federal charges!", 0.04)
            
            time.sleep(3)
            print(f"{Color.GREEN}")
            self.animate_text("\nJust kidding! This was a prank! 😜", 0.05)
            print(f"{Color.CYAN}")
            self.animate_text(f"Follow me for more fun: {self.instagram_url}", 0.03)
            
            # Play scary sound if possible
            try:
                if platform.system() == 'Darwin':  # macOS
                    os.system('afplay /System/Library/Sounds/Sosumi.aiff &')
                elif platform.system() == 'Linux':
                    os.system('paplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga &')
            except:
                pass
                
            input("\nPress Enter to continue...")
            
        except Exception as e:
            self.error(f"Prank failed: {e}")

    def _system_hack_prank(self) -> None:
        """Simulate system hacking"""
        try:
            self.clear_screen()
            print(f"{Color.GREEN}{Color.BOLD}")
            self.animate_text("Initializing system scan...", 0.03)
            time.sleep(1)
            
            # Simulate scanning
            for i in range(1, 101):
                print(f"\rScanning system files... {i}%", end='')
                time.sleep(random.uniform(0.02, 0.1))
            print()
            
            print(f"{Color.RED}")
            self.animate_text("\nCRITICAL VULNERABILITIES FOUND!", 0.02)
            time.sleep(1)
            
            # Simulate hacking
            print(f"{Color.YELLOW}")
            hacking_phrases = [
                "Bypassing firewall...",
                "Injecting payload...",
                "Escalating privileges...",
                "Accessing root directory...",
                "Downloading sensitive data..."
            ]
            
            for phrase in hacking_phrases:
                print(phrase)
                time.sleep(random.uniform(0.5, 1.5))
                
            print(f"{Color.MAGENTA}")
            self.animate_text("\nSYSTEM COMPROMISED!", 0.03)
            time.sleep(1)
            print(f"{Color.WHITE}")
            self.animate_text("All your files have been encrypted", 0.04)
            self.animate_text("Send 0.5 BTC to unlock", 0.04)
            
            time.sleep(2)
            print(f"{Color.GREEN}")
            self.animate_text("\nGotcha! This was just a prank! 😂", 0.05)
            print(f"{Color.CYAN}")
            self.animate_text(f"Follow for more: {self.instagram_url}", 0.03)
            
            input("\nPress Enter to continue...")
            
        except Exception as e:
            self.error(f"Prank failed: {e}")

    def _rick_roll_prank(self) -> None:
        """Classic Rick Roll with animation"""
        try:
            self.clear_screen()
            print(f"{Color.CYAN}{Color.BOLD}")
            self.animate_text("PREPARING SYSTEM UPDATE...", 0.03)
            time.sleep(1)
            
            # Countdown with fake progress
            for i in range(5, 0, -1):
                print(f"\rStarting in {i}...", end='')
                time.sleep(1)
            print()
            
            # Open Rick Roll in browser
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            
            # ASCII art
            print(f"""
{Color.RED}⠀⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀
{Color.RED}⠀⠀⠀⣴⠿⠏⠀⠀⠀⠀⠀⠀⢳⡀⠀⡏⠀⠀⠀⠀⢷
{Color.RED}⠀⠀⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀⠀ ⡇
{Color.RED}⠀⠀⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿⠀⣸⠀⠀OK⠀ ⡇
{Color.RED}⠀⠀⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀⣿⠀⢹⠀⠀⠀⠀⠀ ⡇
{Color.RED}⠀⠀⠙⢿⣯⠄⠀⠀⠀⢀⡀⠀⠀⡿⠀⠀⡇⠀⠀⠀⠀⡼
{Color.RED}⠀⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀⠀⠘⠤⣄⣠⠞⠀
{Color.RED}⠀⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Color.RED}⠀⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀
{Color.RED}⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀
{Color.RED}⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀⠀⣄⢸⠀⠀⠀⠀⠀⠀
{Color.RED}⣿⣿⣧⣀⣿.........⣀⣰⣏⣘⣆⣀⠀⠀
""")
            
            print(f"{Color.GREEN}\nYou've been Rick Rolled! 😆{Color.RESET}")
            print(f"{Color.CYAN}Follow me: {self.instagram_url}{Color.RESET}")
            
            # Play sound if possible
            try:
                if platform.system() == 'Darwin':
                    os.system('afplay /System/Library/Sounds/Purr.aiff &')
            except:
                pass
                
            input("\nPress Enter to continue...")
            
        except Exception as e:
            self.error(f"Prank failed: {e}")

    def _bitcoin_prank(self) -> None:
        """Fake Bitcoin miner simulation"""
        try:
            self.clear_screen()
            print(f"{Color.YELLOW}{Color.BOLD}")
            self.animate_text("BITCOIN MINER ACTIVATED", 0.03)
            time.sleep(1)
            
            print(f"{Color.WHITE}")
            self.animate_text("Initializing cryptonight algorithm...", 0.04)
            time.sleep(1.5)
            
            # Simulate mining
            print(f"\n{Color.GREEN}Mining Progress:{Color.RESET}")
            hashes = [
                "7a3b8c...", "f2e4d1...", "9b5a2c...", 
                "4d8e1f...", "c3b7a9...", "e5d2f8..."
            ]
            
            for i in range(1, 101):
                current_hash = random.choice(hashes)
                print(f"\rHash: {current_hash} | Progress: {i}%", end='')
                time.sleep(random.uniform(0.02, 0.1))
            print()
            
            print(f"{Color.YELLOW}")
            self.animate_text("\nWALLET ADDRESS: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", 0.03)
            self.animate_text("BITCOINS MINED: 0.00000001", 0.04)
            
            time.sleep(2)
            print(f"{Color.GREEN}")
            self.animate_text("\nJust kidding! No bitcoins were mined.", 0.05)
            print(f"{Color.CYAN}")
            self.animate_text(f"Follow for more: {self.instagram_url}", 0.03)
            
            input("\nPress Enter to continue...")
            
        except Exception as e:
            self.error(f"Prank failed: {e}")

    def _matrix_prank(self) -> None:
        """Matrix falling code effect"""
        try:
            self.clear_screen()
            print(f"{Color.GREEN}")
            
            chars = "01"
            width = os.get_terminal_size().columns
            lines = []
            
            print("Hacking into the mainframe... (Press Ctrl+C to stop)")
            
            try:
                while True:
                    # Add new random line
                    line = ''.join(random.choice(chars) for _ in range(width))
                    lines.append(line)
                    
                    # Display last 20 lines
                    print('\n'.join(lines[-20:]))
                    
                    # Randomly remove lines to simulate movement
                    if random.random() > 0.7 and len(lines) > 5:
                        lines.pop(0)
                        
                    time.sleep(0.1)
            except KeyboardInterrupt:
                print(f"{Color.RESET}")
                print(f"{Color.GREEN}\nACCESS GRANTED! Just kidding 😜")
                print(f"{Color.CYAN}Follow me: {self.instagram_url}{Color.RESET}")
                
        except Exception as e:
            self.error(f"Prank failed: {e}")

    def phone_prank(self) -> None:
        """Enhanced phone prank tool"""
        self.info("📱 ULTIMATE PHONE PRANK TOOL 📱")
        print(f"{Color.YELLOW}Coming in next version! Stay tuned!{Color.RESET}")
        print(f"{Color.CYAN}Follow {self.instagram_url} for updates{Color.RESET}")
        time.sleep(2)

    def social_media_tool(self) -> None:
        """Social media toolkit"""
        self.info("📱 SOCIAL MEDIA TOOLKIT 📱")
        print(f"{Color.YELLOW}Coming in next version! Stay tuned!{Color.RESET}")
        print(f"{Color.CYAN}Follow {self.instagram_url} for updates{Color.RESET}")
        time.sleep(2)

    def run(self) -> None:
        """Main application loop with enhanced features"""
        try:
            if not self.check_dependencies():
                self.error("Required dependencies are missing")
                if not self.confirm("Continue without all features?"):
                    return
            
            while True:
                self.display_banner()
                self.display_menu()
                
                try:
                    choice = input("\nChoose an option: ").strip()
                    if not choice:
                        continue
                        
                    if choice == '0':
                        self.info("Exiting Digital Amper Pro. Jai Shree Ram! 🙏")
                        print(f"{Color.CYAN}Don't forget to follow: {self.instagram_url}{Color.RESET}")
                        print(f"{Color.MAGENTA}GitHub: {self.github_url}{Color.RESET}")
                        break
                        
                    tool = Tool(int(choice))
                    self.clear_screen()
                    
                    if tool == Tool.IP_TRACKER:
                        self.track_ip()
                    elif tool == Tool.GPS_TRACKER:
                        self.gps_tracker()
                    elif tool == Tool.CAMERA_HACK:
                        self.camera_hack()
                    elif tool == Tool.PAYLOAD_GEN:
                        self.generate_payload()
                    elif tool == Tool.VIRUS_PRANK:
                        self.virus_prank()
                    elif tool == Tool.PHISHING:
                        self.phishing_tool()
                    elif tool == Tool.PORT_SCAN:
                        self.port_scanner()
                    elif tool == Tool.DOS_TOOL:
                        self.dos_tool()
                    elif tool == Tool.PHONE_PRANK:
                        self.phone_prank()
                    elif tool == Tool.SOCIAL_MEDIA:
                        self.social_media_tool()
                    else:
                        self.error("Invalid choice")
                        
                    input("\nPress Enter to return to menu...")
                except ValueError:
                    self.error("Please enter a valid number")
                except KeyboardInterrupt:
                    self.info("\nOperation cancelled by user")
                    time.sleep(1)
                except Exception as e:
                    self.error(f"Unexpected error: {e}")
                    time.sleep(2)
                    
        except KeyboardInterrupt:
            print(f"\n{Color.RED}Shutting down...{Color.RESET}")
        except Exception as e:
            self.error(f"Fatal error: {e}")

def main():
    """Entry point for the application"""
    parser = argparse.ArgumentParser(description="Digital Amper Pro - Ultimate Security Toolkit")
    parser.add_argument('-v', '--version', action='store_true', help="Show version information")
    parser.add_argument('-p', '--prank', action='store_true', help="Go directly to prank tools")
    
    args = parser.parse_args()
    app = DigitalAmperPro()
    
    if args.version:
        print(f"Digital Amper Pro v{app.version}")
        print(f"Follow the developer: {app.instagram_url}")
        print(f"GitHub: {app.github_url}")
        return
        
    try:
        if args.prank:
            app.clear_screen()
            app.virus_prank()
        else:
            app.run()
    except KeyboardInterrupt:
        print(f"\n{Color.RED}Interrupted by user{Color.RESET}")
    except Exception as e:
        print(f"{Color.RED}Fatal error: {e}{Color.RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
