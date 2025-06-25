import requests

def scan(url):
    try:
        resp = requests.get(url)
        headers = ["X-Frame-Options", "X-XSS-Protection", "Content-Security-Policy"]
        results = ["[*] Security Headers:"]
        for header in headers:
            if header in resp.headers:
                results.append(f"  [+] {header}: {resp.headers[header]}")
            else:
                results.append(f"  [-] {header}: Not Set")
        return "\n".join(results)
    except:
        return "[x] Failed to fetch headers."
