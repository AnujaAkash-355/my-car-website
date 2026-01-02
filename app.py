import streamlit as st
import os

st.set_page_config(page_title="Auto Hub SL", layout="wide")

# භාෂාව තෝරාගැනීම
lang = st.sidebar.selectbox("භාෂාව / Language", ["සිංහල", "English"])
usd_rate = 300.0 
base_path = os.path.dirname(__file__)

# ඔයාගේ දැනට තියෙන වාහන ලැයිස්තුව
local_cars = {
    "vitz": "vitz.jpg", "prado": "prado.jpg", "montero": "montero.jpg",
    "landcruiser": "landcruiser.jpg", "i8": "i8.jpg", "gtr": "gtr.jpg",
    "defender": "defender.jpg", "benz": "benz.jpg", "axio": "axio.jpg", "allion": "allion.jpg"
}

if lang == "සිංහල":
    t_label = "වාහනයේ නම ටයිප් කරන්න (උදා: Alto, Prado, Vitz):"
    t_price = "දළ මිල (රුපියල්):"
else:
    t_label = "Enter car name (e.g., Alto, Prado, Vitz):"
    t_price = "Estimated Price (LKR):"

st.title("🚗 Global Auto Hub")
query = st.text_input(t_label).lower().strip()

if query:
    st.markdown("---")
    
    # 1. මුලින්ම බලනවා GitHub එකේ පින්තූරය තියෙනවාද කියලා
    if query in local_cars:
        img_path = os.path.join(base_path, local_cars[query])
        st.image(img_path, caption=f"Local Image: {query}")
        # දළ මිලක් පෙන්වීම
        price_usd = 25000 if query != "prado" else 65000
    
    # 2. GitHub එකේ නැත්නම් Google/Internet එකෙන් ගන්නවා
    else:
        # පූසෝ එන එක නතර කරන්න 'car' සහ 'automobile' යන වචන එකතු කරනවා
        img_url = f"https://loremflickr.com/800/500/{query.replace(' ', ',')},car,automobile/all"
        st.image(img_url, caption=f"Internet Result: {query}")
        price_usd = 15000 # Default price for unknown cars

    # මිල ගණනය කර පෙන්වීම
    lkr_val = price_usd * usd_rate
    st.subheader(f"💰 {t_price} රු. {lkr_val:,.0f} (ලක්ෂ {lkr_val/100000:.1f})")
    
    # සැබෑ මිලට ලින්ක් එක
    st.write(f"🔗 [Real-time Market Price (Google)](https://www.google.com/search?q={query.replace(' ', '+')}+car+price+in+usd)")

st.markdown("---")
st.info("ඔබට අවශ්‍ය වාහනයක් මෙහි නැත්නම්, එහි පින්තූරයක් GitHub එකට අප්ලෝඩ් කර නම 'වාහනයේ_නම.jpg' ලෙස සකසන්න.")
