import requests

def scan(url):
    paths = ["/admin", "/login", "/uploads", "/config", "/.git"]
    found = []
    for path in paths:
        try:
            r = requests.get(url + path)
            if r.status_code == 200:
                found.append(f"[!] Found path: {url + path}")
        except:
            pass
    return "\n".join(found) if found else "[✓] No directories found."
