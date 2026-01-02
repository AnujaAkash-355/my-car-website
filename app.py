import streamlit as st
import os

# ඇප් එකේ මූලික සැකසුම්
st.set_page_config(page_title="වාහන වල මිල ගණන්", layout="wide")

# භාෂාව තෝරාගැනීම (Sidebar)
lang = st.sidebar.radio("භාෂාව තෝරන්න / Select Language", ["සිංහල", "English"])

usd_rate = 300.0 
base_path = os.path.dirname(__file__)

# වාහන දත්ත ගබඩාව (භාෂා දෙකෙන්ම විස්තර ඇතුළත් කර ඇත)
car_db = {
    "vitz": {
        "name_en": "Toyota Vitz 2024", "name_si": "ටොයෝටා විට්ස් 2024",
        "cc_en": "1000cc", "cc_si": "සීසී 1000",
        "fuel_en": "Petrol/Hybrid", "fuel_si": "පෙට්‍රල්/හයිබ්‍රිඩ්",
        "hp_en": "68 hp", "hp_si": "අශ්ව බල 68",
        "price": 18500, "img": "vitz.jpg"
    },
    "prado": {
        "name_en": "Toyota Prado 2025", "name_si": "ටොයෝටා ප්‍රාඩෝ 2025",
        "cc_en": "2800cc Turbo Diesel", "cc_si": "සීසී 2800 ටර්බෝ ඩීසල්",
        "fuel_en": "Diesel", "fuel_si": "ඩීසල්",
        "hp_en": "201 hp", "hp_si": "අශ්ව බල 201",
        "price": 78000, "img": "prado.jpg"
    },
    "montero": {
        "name_en": "Mitsubishi Montero Sport", "name_si": "මිත්සුබිෂි මොන්ටෙරෝ ස්පෝර්ට්",
        "cc_en": "2400cc Diesel", "cc_si": "සීසී 2400 ඩීසල්",
        "fuel_en": "Diesel", "fuel_si": "ඩීසල්",
        "hp_en": "181 hp", "hp_si": "අශ්ව බල 181",
        "price": 55000, "img": "montero.jpg"
    },
    "landcruiser": {
        "name_en": "Toyota Land Cruiser 300", "name_si": "ටොයෝටා ලෑන්ඩ් කෲසර් 300",
        "cc_en": "3300cc Twin-Turbo", "cc_si": "සීසී 3300 ට්වින්-ටර්බෝ",
        "fuel_en": "Diesel", "fuel_si": "ඩීසල්",
        "hp_en": "304 hp", "hp_si": "අශ්ව බල 304",
        "price": 95000, "img": "landcruiser.jpg"
    }
}

# භාෂාව අනුව වචන සම්පූර්ණයෙන්ම වෙන් කිරීම
if lang == "සිංහල":
    title = "🚗 වාහන තොරතුරු මධ්‍යස්ථානය"
    label = "වාහනයේ නම ඇතුළත් කරන්න (උදා: vitz, prado):"
    specs_h = "⚙️ තාක්ෂණික විස්තර"
    price_h = "💰 වෙළඳපොළ මිල තොරතුරු"
    cc_l, fuel_l, hp_l = "එන්ජින් ධාරිතාව", "ඉන්ධන වර්ගය", "අශ්ව බලය"
    lkr_text, lakhs_text = "මුළු මිල (රුපියල්)", "ලක්ෂ"
    err_msg = "තොරතුරු සොයාගත නොහැක! කරුණාකර vitz, prado, montero හෝ landcruiser ලෙස ටයිප් කරන්න."
else:
    title = "🚗 Vehicle Information Center"
    label = "Type vehicle name (e.g., vitz, prado):"
    specs_h = "⚙️ Technical Specifications"
    price_h = "💰 Market Price Info"
    cc_l, fuel_l, hp_l = "Engine Capacity", "Fuel Type", "Horsepower"
    lkr_text, lakhs_text = "Total Price (LKR)", "Lakhs"
    err_msg = "Data not found! Please try: vitz, prado, montero, or landcruiser."

st.title(title)
query = st.text_input(label).lower().strip()

if query:
    st.markdown("---")
    if query in car_db:
        car = car_db[query]
        
        # 1. පින්තූරය (ඔයාගේ GitHub එකෙන්)
        img_path = os.path.join(base_path, car["img"])
        if os.path.exists(img_path):
            st.image(img_path, caption=car["name_si"] if lang == "සිංහල" else car["name_en"], use_column_width=True)

        # 2. මිල ගණනය
        lkr_val = car["price"] * usd_rate
        lakhs = lkr_val / 100000

        # 3. මිල පෙන්වීම (පැහැදිලිව)
        st.subheader(price_h)
        st.markdown(f"""
        <div style="background-color:#111; padding:25px; border-radius:15px; border: 2px solid #ff4b4b; text-align:center;">
            <h1 style="color:white; margin:0;">{lkr_text}: {lkr_val:,.0f}</h1>
            <h2 style="color:#ff4b4b; margin:0;">({lakhs:,.1f} {lakhs_text})</h2>
            <p style="color:#888;">USD: ${car['price']:,}</p>
        </div>
        """, unsafe_allow_html=True)

        # 4. තාක්ෂණික විස්තර (වචන කැපෙන්නේ නැති වෙන්න)
        st.subheader(specs_h)
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"**{cc_l}**")
            st.success(car["cc_si"] if lang == "සිංහල" else car["cc_en"])
        with c2:
            st.markdown(f"**{fuel_l}**")
            st.success(car["fuel_si"] if lang == "සිංහල" else car["fuel_en"])
        with col3 if 'col3' in locals() else c3:
            st.markdown(f"**{hp_l}**")
            st.success(car["hp_si"] if lang == "සිංහල" else car["hp_en"])
    else:
        st.error(err_msg)

st.markdown("---")
