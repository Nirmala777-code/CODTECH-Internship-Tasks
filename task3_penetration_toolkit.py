import socket
import requests

# ---------- Port Scanner ----------
def port_scanner():
    target = input("Enter IP to scan (e.g. 127.0.0.1): ")
    print(f"\n[+] Scanning ports on {target}...\n")
    for port in range(20, 1025):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            print(f"✅ Port {port} is open")
        except:
            pass

# ---------- Brute Forcer ----------
def brute_forcer():
    print("\n[+] Brute Forcing...")
    url = input("Enter login URL (dummy): ")
    username = input("Enter username: ")
    wordlist = ["123456", "password", "admin", "letmein", "root"]

    for pwd in wordlist:
        data = {'username': username, 'password': pwd}
        try:
            response = requests.post(url, data=data)
            if "Invalid" not in response.text:
                print(f"✅ Password found: {pwd}")
                return
            else:
                print(f"❌ Tried: {pwd}")
        except:
            print("Error during request.")

# ---------- Main Menu ----------
def main():
    print("\n=== Penetration Testing Toolkit ===")
    print("1. Port Scanner")
    print("2. Brute Forcer")
    choice = input("Choose (1/2): ")

    if choice == "1":
        port_scanner()
    elif choice == "2":
        brute_forcer()
    else:
        print("❌ Invalid choice.")

main()