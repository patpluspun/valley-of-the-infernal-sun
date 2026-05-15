import argparse
from bs4 import BeautifulSoup

def strip_div_titles(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            # Using 'html.parser' or 'lxml' if installed
            soup = BeautifulSoup(f, 'html.parser')

        # Find every <div> that HAS a title attribute
        target_divs = soup.find_all('span', attrs={"title": True})
        
        count = 0
        for div in target_divs:
            del div['title']
            count += 1

        # Write the result back to a file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(str(soup)) # Use str(soup) to keep it closer to original formatting

        print(f"Success! Found and removed 'title' from {count} <span> tags.")
        print(f"File saved to: {output_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args()

    strip_div_titles(args.input, args.output)
