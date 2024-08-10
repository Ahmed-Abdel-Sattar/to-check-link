import requests
from urllib.parse import urlparse, urljoin

def check_url_security(url):
    """Check the security of a URL and identify the original URL if it is malicious."""
    try:
        # Get the final destination URL after redirections
        response = requests.get(url, allow_redirects=True)
        final_url = response.url
        
        # Parse URLs
        parsed_url = urlparse(final_url)
        domain = parsed_url.netloc
        
        # Check for common signs of malicious URLs
        if is_malicious_url(domain):
            print(f"Potentially malicious URL detected: {final_url}")
            original_url = urljoin(url, final_url)  # Original URL if redirection occurs
            print(f"Original URL: {original_url}")
        else:
            print(f"The URL appears to be safe: {final_url}")
    
    except requests.RequestException as e:
        print(f"Error checking URL: {e}")

def is_malicious_url(domain):
    """Simple heuristic to check if a domain is potentially malicious."""
    # For demonstration purposes, we'll use a few common patterns. 
    # In real-world usage, you should use a comprehensive list or service.
    suspicious_patterns = ["malicious", "phishing", "fake", "scam"]
    for pattern in suspicious_patterns:
        if pattern in domain:
            return True
    return False

if __name__ == "__main__":
    url = input("Enter the URL to check (e.g., http://example.com): ")
    check_url_security(url)
