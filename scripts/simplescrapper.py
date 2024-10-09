
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_categories(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all category elements (adjust based on the website structure)
        categories = []
        for category in soup.find_all('a', class_='category-link'):  # Adjust class or tag based on the website structure
            category_name = category.text.strip()
            category_url = category['href']
            categories.append({'Category': category_name, 'URL': category_url})

        return categories
    except Exception as e:
        print(f"An error occurred while scraping categories: {e}")
        return []

def scrape_products(category_url):
    try:
        # Send a GET request to the category URL
        response = requests.get(category_url)
        response.raise_for_status()  # Check for request errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all product elements (adjust based on the website structure)
        products = []
        for product in soup.find_all('div', class_='product-item'):  # Adjust class or tag based on the website structure
            product_name = product.find('h2', class_='product-name').text.strip()  # Adjust based on the website structure
            product_price = product.find('span', class_='product-price').text.strip()  # Adjust based on the website structure
            product_url = product.find('a', class_='product-link')['href']  # Adjust based on the website structure
            products.append({'Product Name': product_name, 'Price': product_price, 'URL': product_url})

        return products
    except Exception as e:
        print(f"An error occurred while scraping products: {e}")
        return []

def save_to_excel(categories, output_file):
    try:
        # Create a DataFrame from the categories list
        df = pd.DataFrame(categories)

        # Save the DataFrame to an Excel file
        df.to_excel(output_file, index=False)
        print(f"Categories and products saved to {output_file}")
    except Exception as e:
        print(f"An error occurred while saving to Excel: {e}")

if __name__ == "__main__":
    # Input: E-commerce website URL
    url = input("Enter the e-commerce website URL: ").strip()

    # Output: Excel file name
    output_file = 'categories_and_products.xlsx'

    # Scrape categories
    categories = scrape_categories(url)

    # Scrape products for each category
    for category in categories:
        category_url = category['URL']
        products = scrape_products(category_url)
        for product in products:
            product['Category'] = category['Category']  # Add category name to each product
            category['Products'] = products

    # Flatten the data for saving to Excel
    all_data = []
    for category in categories:
        for product in category.get('Products', []):
            all_data.append({
                'Category': category['Category'],
                'Product Name': product['Product Name'],
                'Price': product['Price'],
                'Product URL': product['URL'],
                'Category URL': category['URL']
            })

    # Save to Excel
    save_to_excel(all_data, output_file)
