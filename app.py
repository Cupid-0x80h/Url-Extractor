import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_links(url):
    try:
        # Send an HTTP GET request to the URL
        print(f"[*] Fetching {url}...")
        response = requests.get(url, timeout=10)
        # Exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        
    except requests.exceptions.RequestException as e:
        # Handle connection errors, timeouts
        print(f"[!] Error: Could not fetch the URL. {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Use a set to store unique links
    links = set()

    # Find all anchor tags <a> which contain the 'href' attribute
    for anchor_tag in soup.find_all('a', href=True):
        href = anchor_tag.get('href')
        
        if href:
            # Convert relative URLs (like '/about') to absolute URLs
            absolute_url = urljoin(url, href)
            links.add(absolute_url)
            
    return links

if __name__ == "__main__":
    target_url = input("Enter the website URL to extract links from: ")

    if not target_url.startswith('http://') and not target_url.startswith('https://'):
        target_url = 'https://' + target_url

    found_links = extract_links(target_url)

    if found_links:
        print(f"\n[+] Found {len(found_links)} unique links:\n")
        for link in sorted(list(found_links)): # Sort them for clean output
            print(link)
    else:
        print("\n[-] No links were found or an error occurred.")