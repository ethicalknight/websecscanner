import requests

def scan(url):
    payloads = ["'", "' OR '1'='1", "';--", '" OR ""="']
    for p in payloads:
        try:
            r = requests.get(url, params={"id": p})
            if "mysql" in r.text.lower() or "syntax error" in r.text.lower():
                return f"[!] Possible SQL Injection: Payload = {p}"
        except:
            pass
    return "[✓] No SQL Injection found."
