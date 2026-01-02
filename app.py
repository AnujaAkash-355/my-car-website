import streamlit as st
import os

# ඇප් එකේ මූලික සැකසුම්
st.set_page_config(page_title="වාහන වල මිල ගණන්", layout="wide")

# භාෂාව තෝරාගැනීම (Sidebar)
lang = st.sidebar.radio("Language / භාෂාව", ["English", "සිංහල"])

usd_rate = 300.0 
base_path = os.path.dirname(__file__)

# වාහන දත්ත ගබඩාව (ඔයාගේ GitHub පින්තූර සහ නිවැරදි විස්තර)
car_db = {
    "vitz": {
        "en": "Toyota Vitz 2024", "si": "ටොයෝටා විට්ස් 2024", 
        "cc": "1000cc", "fuel_en": "Petrol/Hybrid", "fuel_si": "පෙට්‍රල්/හයිබ්‍රිඩ්", 
        "hp": "68 hp", "price": 18500, "img": "vitz.jpg"
    },
    "prado": {
        "en": "Toyota Prado 2025", "si": "ටොයෝටා ප්‍රාඩෝ 2025", 
        "cc": "2800cc Turbo Diesel", "fuel_en": "Diesel", "fuel_si": "ඩීසල්", 
        "hp": "201 hp", "price": 78000, "img": "prado.jpg"
    },
    "montero": {
        "en": "Mitsubishi Montero Sport", "si": "මිත්සුබිෂි මොන්ටෙරෝ ස්පෝර්ට්", 
        "cc": "2400cc Diesel", "fuel_en": "Diesel", "fuel_si": "ඩීසල්", 
        "hp": "181 hp", "price": 55000, "img": "montero.jpg"
    },
    "landcruiser": {
        "en": "Toyota Land Cruiser 300", "si": "ටොයෝටා ලෑන්ඩ් කෲසර් 300", 
        "cc": "3300cc Twin-Turbo Diesel", "fuel_en": "Diesel", "fuel_si": "ඩීසල්", 
        "hp": "304 hp", "price": 95000, "img": "landcruiser.jpg"
    }
}

# භාෂාව අනුව වචන සැකසීම
if lang == "English":
    title, label = "🚗 Vehicle Information Center", "Type vehicle name (vitz, prado, montero):"
    specs_h, price_h = "⚙️ Technical Specifications", "💰 Market Price Info"
    cc_l, fuel_l, hp_l = "Engine Capacity", "Fuel Type", "Horsepower"
    lkr_text, lakhs_text = "Price in LKR", "Lakhs (Approx)"
else:
    title, label = "🚗 වාහන වල මිල ගණන් සහ විස්තර", "වාහනයේ නම ටයිප් කරන්න (vitz, prado, montero):"
    specs_h, price_h = "⚙️ තාක්ෂණික විස්තර", "💰 වෙළඳපොළ මිල තොරතුරු"
    cc_l, fuel_l, hp_l = "එන්ජින් ධාරිතාව", "ඉන්ධන වර්ගය", "අශ්ව බලය"
    lkr_text, lakhs_text = "රුපියල් මිල", "ලක්ෂ"

st.title(title)
query = st.text_input(label).lower().strip()

if query:
    st.markdown("---")
    
    if query in car_db:
        car = car_db[query]
        
        # 1. පින්තූරය (ඔයාගේ GitHub එකෙන්)
        img_path = os.path.join(base_path, car["img"])
        if os.path.exists(img_path):
            st.image(img_path, use_column_width=True)
        else:
            st.warning("⚠️ Image file not found in your GitHub folder.")

        # 2. මිල ගණනය
        lkr_val = car["price"] * usd_rate
        lakhs = lkr_val / 100000

        # 3. මිල පෙන්වීම (විශාලව සහ පිරිසිදුව)
        st.subheader(price_h)
        st.markdown(f"""
        <div style="background-color:#0e1117; padding:20px; border-radius:15px; border: 1px solid #3d444d; text-align:center; margin-bottom:20px;">
            <h1 style="color:#00ff00; margin:0;">{lkr_text}: {lkr_val:,.0f}</h1>
            <h2 style="color:#1c83e1; margin:0;">({lakhs:,.1f} {lakhs_text})</h2>
            <p style="color:#888;">USD: ${car['price']:,}</p>
        </div>
        """, unsafe_allow_html=True)

        # 4. තාක්ෂණික විස්තර (වචන කැපෙන්නේ නැති වෙන්න හදපු ක්‍රමය)
        st.subheader(specs_h)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"**{cc_l}**")
            st.info(car["cc"])
        with col2:
            st.markdown(f"**{fuel_l}**")
            st.info(car["fuel_en"] if lang == "English" else car["fuel_si"])
        with col3:
            st.markdown(f"**{hp_l}**")
            st.info(car["hp"])
            
    else:
        st.error("No data found! Please search for: vitz, prado, montero, or landcruiser.")

st.markdown("---")
