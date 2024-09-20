import streamlit as st
from PIL import Image
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# Function to take screenshots
def take_screenshot(url, device_name):
    chrome_options = Options()
    
    # Emulate different devices
    if device_name == "Mobile":
        chrome_options.add_argument("--window-size=375,667")
    elif device_name == "Tablet":
        chrome_options.add_argument("--window-size=768,1024")
    elif device_name == "Desktop":
        chrome_options.add_argument("--window-size=1366,768")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    
    # Define the screenshot path
    screenshot_path = f'screenshots/{device_name}_{int(time.time())}.png'
    
    # Save the screenshot
    driver.save_screenshot(screenshot_path)
    driver.quit()
    return screenshot_path

# Create a folder to save screenshots
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# Streamlit app layout
st.title("URL Screenshot App")
st.write("Upload up to 5 URLs, and get screenshots across multiple devices.")

# URL input
urls = st.text_area("Enter up to 5 URLs, each on a new line:", max_chars=500).splitlines()

# Capture screenshots on button press
if st.button("Capture Screenshots"):
    if len(urls) > 5:
        st.error("Please limit to 5 URLs.")
    else:
        for url in urls:
            st.write(f"Taking screenshots for {url}")
            mobile_ss = take_screenshot(url, "Mobile")
            tablet_ss = take_screenshot(url, "Tablet")
            desktop_ss = take_screenshot(url, "Desktop")

            st.image(mobile_ss, caption="Mobile")
            st.image(tablet_ss, caption="Tablet")
            st.image(desktop_ss, caption="Desktop")
