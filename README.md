# Web Link Extractor

This program extracts all unique links from a given webpage.

## How to Run the Program

1.  **Install Necessary Libraries**\
    If you don't have `requests` and `BeautifulSoup` installed, open
    your terminal or command prompt and run the following command:

    ``` bash
    pip install requests beautifulsoup4
    ```

2.  **Clone the Repository**

    ``` bash
    git clone https://github.com/Cupid-0x80h/Url-Extractor.git
    cd Url-Extractor
    ```

3.  **Execute the Script**\
    Run the file from your terminal:

    ``` bash
    python app.py
    ```

4.  **Enter a URL**\
    The program will prompt you to enter a URL. Type in a full website
    address (e.g., `google.com` or
    `https://en.wikipedia.org/wiki/Python_(programming_language)`) and
    press Enter.

------------------------------------------------------------------------

## How It Works

### Imported Libraries

-   **requests** → Acts like a browser and downloads the source code of
    the webpage.\
-   **BeautifulSoup** → Parses the HTML source code.\
-   **urljoin** → Finds and combines relative and absolute URLs.

### Function: `extract_link(url)`

-   Takes a target URL as an argument.\
-   Uses **try-except** for error handling (invalid URLs, internet
    issues, etc.).\
-   `requests.get(url, timeout=10)` sends a request to the server
    (timeout prevents the script from hanging).\
-   `BeautifulSoup(response.text, 'html.parser')` creates a parsed HTML
    object.\
-   `soup.find_all('a', href=True)` finds all `<a>` tags with an `href`
    attribute.\
-   Extracted links are converted into full URLs using **urljoin**.\
-   Results are stored in a **set** (to ensure uniqueness).

### Main Execution Block (`if __name__ == "__main__":`)

-   Runs when the script is executed directly.\
-   Asks the user for a URL.\
-   Ensures the URL starts with `http://` or `https://` (adds `https://`
    if missing).\
-   Calls `extract_link()` and prints the results in a formatted, sorted
    list.

------------------------------------------------------------------------

## Example Usage

``` bash
Enter a URL: https://www.python.org
Extracted Links:
1. https://www.python.org/about/
2. https://www.python.org/downloads/
3. https://www.python.org/community/
...
```

## License

This project is open-source. Feel free to use and modify it as needed.
