import streamlit as st
import requests

# ScreenshotOne API Key (you can get it by signing up for their service)
API_KEY = "your_screenshotone_api_key_here"

# Function to take screenshots using the ScreenshotOne API
def take_screenshot(url, device_name):
    api_url = f"https://api.screenshotone.com/take?url={url}&device={device_name}&access_key={API_KEY}"
    response = requests.get(api_url)

    if response.status_code == 200:
        file_name = f'screenshots/{device_name}_{url.replace("https://", "").replace("/", "_")}.png'
        with open(file_name, 'wb') as f:
            f.write(response.content)
        return file_name
    else:
        st.error("Failed to capture screenshot")
        return None

# Streamlit app layout
st.title("URL Screenshot App")
st.write("Upload up to 5 URLs, and get screenshots across multiple devices.")

# URL input
urls = st.text_area("Enter up to 5 URLs, each on a new line:", max_chars=500).splitlines()

# Create screenshots directory if it doesn't exist
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# Capture screenshots on button press
if st.button("Capture Screenshots"):
    if len(urls) > 5:
        st.error("Please limit to 5 URLs.")
    else:
        for url in urls:
            st.write(f"Taking screenshots for {url}")
            mobile_ss = take_screenshot(url, "mobile")
            tablet_ss = take_screenshot(url, "tablet")
            desktop_ss = take_screenshot(url, "desktop")

            if mobile_ss:
                st.image(mobile_ss, caption="Mobile")
            if tablet_ss:
                st.image(tablet_ss, caption="Tablet")
            if desktop_ss:
                st.image(desktop_ss, caption="Desktop")
