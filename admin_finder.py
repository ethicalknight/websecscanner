import requests

def scan(url):
    paths = ["/admin", "/administrator", "/adminpanel", "/cms"]
    found = []
    for path in paths:
        try:
            r = requests.get(url + path)
            if r.status_code == 200:
                found.append(f"[!] Possible Admin Panel: {url + path}")
        except:
            pass
    return "\n".join(found) if found else "[✓] No admin panels found."
