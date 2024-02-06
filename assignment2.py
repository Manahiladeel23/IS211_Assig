import argparse
import csv
from datetime import datetime
import logging
import urllib.request

def download_data(url):
    """
    Reads data from a URL and returns the data as a string

    :param url: URL of the CSV file
    :return: the content of the URL
    """
    # read the URL
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    # return the data
    return response

# Rest of your script remains the same...

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Process CSV data from a given URL.')
    parser.add_argument('--url', type=str, help='URL of the CSV file', required=True)
    args = parser.parse_args()

    # Download data from the specified URL
    try:
        csv_data = download_data(args.url)
    except Exception as e:
        print(f"Error downloading data: {e}")
        return

    # Set up the logger
    setupLogger()

    # Process the CSV data
    person_data = processData(csv_data)

    # Ask the user for an ID to lookup
    while True:
        try:
            user_input = int(input("Enter an ID to lookup (enter a negative number or 0 to exit): "))
            if user_input <= 0:
                break
            displayPerson(user_input, person_data)
        except ValueError:
            print("Invalid input. Please enter a valid ID.")

if __name__ == "__main__":
    main()
