import streamlit as st
import os

# ඇප් එකේ මූලික සැකසුම්
st.set_page_config(page_title="වාහන වල මිල ගණන්", layout="wide")

# භාෂාව තෝරාගැනීම (Sidebar)
lang = st.sidebar.radio("Language / භාෂාව", ["English", "සිංහල"])

# ඩොලර් අගය
usd_rate = 300.0 
base_path = os.path.dirname(__file__)

# වාහන දත්ත ගබඩාව (ඔයාගේ පින්තූර වල නම් වලට අනුව)
car_db = {
    "vitz": {
        "en": "Toyota Vitz 2024", "si": "ටොයෝටා විට්ස් 2024", 
        "cc": "1000cc", "fuel_en": "Petrol/Hybrid", "fuel_si": "පෙට්‍රල්/හයිබ්‍රිඩ්", 
        "hp": "68 hp", "price": 18500, "img": "vitz.jpg"
    },
    "prado": {
        "en": "Toyota Prado 2025", "si": "ටොයෝටා ප්‍රාඩෝ 2025", 
        "cc": "2800cc Turbo", "fuel_en": "Diesel", "fuel_si": "ඩීසල්", 
        "hp": "201 hp", "price": 78000, "img": "prado.jpg"
    },
    "montero": {
        "en": "Mitsubishi Montero Sport", "si": "මිත්සුබිෂි මොන්ටෙරෝ ස්පෝර්ට්", 
        "cc": "2400cc Diesel", "fuel_en": "Diesel", "fuel_si": "ඩීසල්", 
        "hp": "181 hp", "price": 55000, "img": "montero.jpg"
    },
    "landcruiser": {
        "en": "Toyota Land Cruiser 300", "si": "ටොයෝටා ලෑන්ඩ් කෲසර් 300", 
        "cc": "3300cc Diesel", "fuel_en": "Diesel", "fuel_si": "ඩීසල්", 
        "hp": "304 hp", "price": 95000, "img": "landcruiser.jpg"
    },
    "i8": {
        "en": "BMW i8 Hybrid", "si": "බී.එම්.ඩබ්ලිව් i8 හයිබ්‍රිඩ්", 
        "cc": "1500cc Hybrid", "fuel_en": "Petrol/Electric", "fuel_si": "පෙට්‍රල්/විදුලි", 
        "hp": "369 hp", "price": 140000, "img": "i8.jpg"
    },
    "gtr": {
        "en": "Nissan GTR R35", "si": "නිසාන් GTR R35", 
        "cc": "3800cc Twin-Turbo", "fuel_en": "Petrol", "fuel_si": "පෙට්‍රල්", 
        "hp": "565 hp", "price": 120000, "img": "gtr.jpg"
    }
}

# භාෂාව අනුව වචන සැකසීම
if lang == "English":
    title, label = "🚗 Vehicle Price Hub", "Enter vehicle name (vitz, prado, i8, etc):"
    specs_h, price_h = "⚙️ Technical Specifications", "💰 Market Price Info"
    cc_label, fuel_label, hp_label = "Engine Capacity", "Fuel Type", "Horsepower"
    lkr_text, lakhs_text = "Price in LKR", "Lakhs (Approx)"
else:
    title, label = "🚗 වාහන වල මිල ගණන්", "වාහනයේ නම ටයිප් කරන්න (vitz, prado, i8...):"
    specs_h, price_h = "⚙️ තාක්ෂණික විස්තර", "💰 වෙළඳපොළ මිල තොරතුරු"
    cc_label, fuel_label, hp_label = "එන්ජින් ධාරිතාව", "ඉන්ධන වර්ගය", "අශ්ව බලය"
    lkr_text, lakhs_text = "රුපියල් මිල", "ලක්ෂ"

st.title(title)
query = st.text_input(label).lower().strip()

if query:
    st.markdown("---")
    
    if query in car_db:
        car = car_db[query]
        
        # 1. පින්තූරය පෙන්වීම (ඔයාගේ GitHub එකේ ඇති ෆයිල් එක)
        img_path = os.path.join(base_path, car["img"])
        if os.path.exists(img_path):
            st.image(img_path, caption=car["en"] if lang == "English" else car["si"], use_column_width=True)
        else:
            st.error("Image file not found on GitHub!")

        # 2. මිල ගණන් ගණනය කිරීම
        lkr_val = car["price"] * usd_rate
        lakhs = lkr_val / 100000

        # 3. මිල පෙන්වීම (Clean Dark Design)
        st.subheader(price_h)
        st.markdown(f"""
        <div style="background-color:#0e1117; padding:25px; border-radius:12px; border: 1px solid #3d444d; text-align:center;">
            <h1 style="color:#00ff00; margin:0;">{lkr_text}: {lkr_val:,.0f}</h1>
            <h2 style="color:#1c83e1; margin:0;">({lakhs:,.1f} {lakhs_text})</h2>
            <p style="color:#888;">USD: ${car['price']:,}</p>
        </div>
        """, unsafe_allow_html=True)

        # 4. තාක්ෂණික විස්තර
        st.subheader(specs_h)
        col1, col2, col3 = st.columns(3)
        with col1: st.metric(cc_label, car["cc"])
        with col2: st.metric(fuel_label, car["fuel_en"] if lang == "English" else car["fuel_si"])
        with col3: st.metric(hp_label, car["hp"])
