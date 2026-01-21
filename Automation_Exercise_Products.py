# --------------------------------------------
# Web Scraping Script: Automation Exercise Products
# Description: Scrapes product details (name, price, brand, category, availability, URLs) 
# from the Automation Exercise website and exports the data to a CSV file.
# Author: Saylee Bandal
# --------------------------------------------

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Base URL of the website
BASE_URL = "https://automationexercise.com"

# -------------------------------
# Step 1: Scrape the main products page
# -------------------------------
main_url = BASE_URL + "/products"
response = requests.get(main_url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all product containers on the main page
products = soup.select("div.col-sm-4")
print(f"Found {len(products)} products on main page")

# Initialize a list to store product data
data = []

# -------------------------------
# Step 2: Loop through each product and extract details
# -------------------------------
for product in products:
    # Product Name
    name_tag = product.select_one("p")  # Product name is inside <p> tag
    product_name = name_tag.text.strip() if name_tag else "N/A"

    # Price
    price_tag = product.select_one("h2")
    price = price_tag.text.replace("Rs.", "").strip() if price_tag else "N/A"

    # Image URL
    img_tag = product.select_one("img")
    image_url = BASE_URL + img_tag["src"] if img_tag else "N/A"

    # Product URL: <a> tag that wraps the image
    product_link_tag = product.select_one("a[href*='/product_details/']")
    product_url = BASE_URL + product_link_tag["href"] if product_link_tag else "N/A"

    # Product ID from "Add to Cart" button
    cart_tag = product.select_one("a.add-to-cart")
    product_id = cart_tag["data-product-id"] if cart_tag else "N/A"

    # -------------------------------
    # Step 3: Scrape product detail page for extra info
    # -------------------------------
    if product_url != "N/A":
        detail_resp = requests.get(product_url)
        detail_soup = BeautifulSoup(detail_resp.text, "html.parser")
        info_div = detail_soup.select_one("div.product-information")

        # Brand
        brand = "N/A"
        if info_div:
            brand_tag = info_div.find("b", string="Brand:")
            brand = brand_tag.next_sibling.strip() if brand_tag else "N/A"

        # Category + Description
        category = "N/A"
        if info_div:
            category_tag = info_div.find("b", string="Category:")
            category_text = category_tag.next_sibling.strip() if category_tag else ""

            description_tag = info_div.select_one("p")
            description_text = description_tag.text.strip() if description_tag else ""

            # Combine category and description (pipe separated)
            category = category_text
            if description_text:
                category += " | " + description_text

        # Availability
        availability = "N/A"
        if info_div:
            avail_tag = info_div.find("b", string="Availability:")
            availability = avail_tag.next_sibling.strip() if avail_tag else "N/A"
    else:
        brand = category = availability = "N/A"

    # -------------------------------
    # Step 4: Append product info to data list
    # -------------------------------
    data.append({
        "product_id": product_id,
        "product_name": product_name,
        "category": category,
        "brand": brand,
        "price": price,
        "availability": availability,
        "product_url": product_url,
        "image_url": image_url
    })

    # Optional polite delay to avoid overloading the server
    time.sleep(0.5)

# -------------------------------
# Step 5: Convert data to DataFrame
# -------------------------------
df = pd.DataFrame(data)

# Reorder columns for readability
df = df[["product_id", "product_name", "category", "brand", "price", 
         "availability", "product_url", "image_url"]]

# -------------------------------
# Step 6: Export to CSV
# -------------------------------
df.to_csv("automationexercise_products.csv", index=False)
print("Data exported to 'automationexercise_products.csv' successfully.")

# Display first 5 rows
print(df.head())
