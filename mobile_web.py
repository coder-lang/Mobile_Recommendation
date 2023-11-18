import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Mobile_data_Flipkart.csv', encoding='ISO-8859-1')  # Replace with the actual file path

# Set the theme and style
sns.set_theme(style="whitegrid")
st.set_page_config(
    page_title="Top Mobiles To Buy",
    page_icon="📱",
    layout="wide"
)

# Custom CSS for styling and theme
st.markdown(
    """
    <style>
        body {
            background-color: #f9f9f9;
            color: #333;
            font-family: 'Arial', sans-serif;
        }

        h1 {
            color: #1f4057;
        }

        h2 {
            color: #1f4057;
        }

        h3 {
            color: #1f4057;
        }

        .st-bb {
            background-color: #1f4057;
            color: #ffffff;
        }

        .stButton > button {
            background-color: #1f4057;
            color: #ffffff;
        }

        .stTextInput > div > div > input {
            background-color: #ffffff;
            color: #333;
        }

        .stDataFrame > div > div > div > div.dataframe > table > tbody > tr > th {
            background-color: #1f4057;
            color: #ffffff;
        }

        .stDataFrame > div > div > div > div.dataframe > table > tbody > tr > td {
            background-color: #ffffff;
            color: #333;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Google Search Console verification meta tag
google_verification_meta_tag = '<meta name="google-site-verification" content="LK3AHXVkH7ZU3_N9IvU8mpqWZbNnKr3C9PS2htg2bJA" />'

# Include the meta tag in the HTML head section
st.markdown(google_verification_meta_tag, unsafe_allow_html=True)

# Title of the Streamlit web app
st.title('Mobile Product Information')

# Unique brands in the dataset
brands = data['Brand'].unique()

# Sidebar
selected_brand = st.sidebar.selectbox('Select Brand', ['All Brands'] + list(brands))
st.sidebar.subheader('Top 10 Mobiles Based on Ratings')

# Filter data based on the selected brand
if selected_brand == 'All Brands':
    top_10_mobiles = data.nlargest(10, 'Review')
else:
    top_10_mobiles = data[data['Brand'] == selected_brand].nlargest(10, 'Review')

# Display top 10 mobiles table in the sidebar
st.sidebar.dataframe(top_10_mobiles)

# Bar chart for the top 10 mobiles
plt.figure(figsize=(10, 6))
sns.barplot(x='Product Name', y='Review', data=top_10_mobiles, palette='viridis')
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Mobiles Based on Ratings')
plt.xlabel('Mobiles')
plt.ylabel('Rating')

# Display the plot in the sidebar
st.sidebar.pyplot()

# Main content area
st.subheader('Brand-wise Information')

# Create subpages for each brand
for brand in brands:
    if selected_brand == 'All Brands' or selected_brand == brand:
        st.subheader(brand)

        # Filter data for the selected brand
        brand_data = data[data['Brand'] == brand]

        # Display brand-specific information
        st.subheader(f'{brand} - Top 5 Mobiles Based on Ratings')
        top_5_mobiles = brand_data.nlargest(5, 'Review')
        st.dataframe(top_5_mobiles)

        # Bar chart for the top 3 mobiles of the selected brand
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Product Name', y='Review', data=top_5_mobiles, palette='viridis')
        plt.xticks(rotation=45, ha='right')
        plt.title(f'Top 5 Mobiles of {brand} Based on Ratings')
        plt.xlabel('Mobiles')
        plt.ylabel('Rating')

        # Display the plot
        st.pyplot()
