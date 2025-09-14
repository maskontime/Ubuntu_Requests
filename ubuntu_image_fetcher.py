"""
Ubuntu Image Fetcher
---------------------
"I am because we are."

This script fetches an image from a URL and saves it locally in a
Fetched_Images/ folder. It emphasizes Ubuntu principles:
- Community: connecting to the global web
- Respect: handling errors gracefully
- Sharing: organizing fetched images
- Practicality: creating a useful tool
"""

import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Prompt user for image URL
    url = input("Please enter the image URL: ").strip()

    try:
        # Ensure folder exists
        os.makedirs("Fetched_Images", exist_ok=True)

        # Request image from the web
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for HTTP errors

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # Fallback filename if none provided
        if not filename:
            filename = "downloaded_image.jpg"

        filepath = os.path.join("Fetched_Images", filename)

        # Check content type header
        content_type = response.headers.get("Content-Type", "")
        if "image" not in content_type:
            print("✗ The provided URL does not contain an image.")
            return

        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        # Success messages
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")


if __name__ == "__main__":
    main()
