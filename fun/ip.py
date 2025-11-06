import requests
from colorama import init, Fore, Style

# Initialize colorama for colored terminal output
init(autoreset=True)

def get_public_ip():
    """Fetch your public IP address."""
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=10)
        response.raise_for_status()
        return response.json().get("ip", "")
    except requests.RequestException as e:
        print(Fore.RED + f"[!] Error getting public IP: {e}")
        return ""

def geolocate_ip(ip):
    """Get approximate location information from IP."""
    if not ip:
        return {}
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=10)
        response.raise_for_status()
        data = response.json()
        loc = data.get("loc", ",").split(",")
        return {
            "city": data.get("city", ""),
            "region": data.get("region", ""),
            "country": data.get("country", ""),
            "lat": loc[0] if len(loc) == 2 else "",
            "lon": loc[1] if len(loc) == 2 else ""
        }

    except requests.RequestException as e:
        print(Fore.RED + f"[!] Error geolocating IP: {e}")
        return {}

def fetch_weather_ascii(lat, lon, units="u"):
    """Fetch ASCII weather data from wttr.in."""
    if not lat or not lon:
        return "[!] No coordinates available for weather data."
    try:
        url = f"https://wttr.in/{lat},{lon}?{units}"
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return Fore.RED + f"[!] Error fetching weather: {e}"

def main():
    print(Fore.CYAN + Style.BRIGHT + "Fetching your IP and weather report...\n")

    ip = get_public_ip()
    if not ip:
        return

    print(Fore.YELLOW + f"Public IP: {ip}")

    loc = geolocate_ip(ip)
    if not loc:
        return

    print(Fore.GREEN + f"Location: {loc['city']}, {loc['region']}, {loc['country']}\n")

    weather_report = fetch_weather_ascii(loc["lat"], loc["lon"])
    print(Style.BRIGHT + weather_report)

if __name__ == "__main__":
    main()
