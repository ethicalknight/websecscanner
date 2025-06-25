import requests

def scan(url):
    test_script = "<script>alert('XSS')</script>"
    try:
        resp = requests.get(url, params={"q": test_script}, timeout=3)
        if test_script in resp.text:
            return "[!] XSS vulnerability found!"
        else:
            return "[✓] No XSS found."
    except Exception as e:
        return f"[x] XSS scan failed: {e}"
