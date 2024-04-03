import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from modules.read_csv import read_csv_line_by_line
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the URL from the environment variable
url = os.getenv('site_url')

# Path to the CSV file
csv_file_path = './_acceptance_criteria/acc.csv'

# Initialize the WebDriver (ensure the driver is in your PATH)
driver = webdriver.Chrome()

# Navigate to the URL
driver.get(url)

# Example of reading CSV as list and comparing DOM elements, skipping the first row
print("Comparing DOM elements against CSV values:")
first_row = True  # Flag to skip the first row

for row in read_csv_line_by_line(csv_file_path):
    if first_row:  # Check if it's the first row
        first_row = False  # Update the flag so the next rows are processed
        continue  # Skip the rest of the loop for the first row

    # Assuming the CSV format is: Selector,Attribute,ExpectedValue
    breakpoint, selector, attribute, expected_value = row

    # Find the element
    element = driver.find_element(By.CSS_SELECTOR, '.'+selector)

    # Adjust to handle 'text' separately; otherwise, use `value_of_css_property` for CSS attributes
    if attribute.lower() == 'text':
        actual_value = element.text
    else:
        actual_value = element.value_of_css_property(attribute)

    # Compare the actual value with the expected value
    print(f"Testing {selector} [{attribute}]: ", end='')
    if actual_value == expected_value:
        print("PASS")
    else:
        print(f"FAIL (Expected: '{expected_value}', Actual: '{actual_value}')")

# Close the browser after the tests
driver.quit()
