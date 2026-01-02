import streamlit as st
import os

# ඇප් එකේ මූලික සැකසුම්
st.set_page_config(page_title="වාහන වල මිල ගණන්", layout="wide")

# භාෂාව තෝරාගැනීම (Sidebar)
lang = st.sidebar.radio("Language / භාෂාව", ["සිංහල", "English"])

usd_rate = 300.0 
base_path = os.path.dirname(__file__)

# වාහන දත්ත ගබඩාව (භාෂා දෙකෙන්ම සහ නිවැරදි විස්තර)
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
    "axio": {
        "name_en": "Toyota Axio Hybrid", "name_si": "ටොයෝටා ඇක්සියෝ හයිබ්‍රිඩ්",
        "cc_en": "1500cc", "cc_si": "සීසී 1500",
        "fuel_en": "Hybrid", "fuel_si": "හයිබ්‍රිඩ්",
        "hp_en": "100 hp", "hp_si": "අශ්ව බල 100",
        "price": 28000, "img": "axio.jpg"
    }
}

# භාෂාව අනුව සියලුම වචන සැකසීම (සිංහල/English 100% වෙන් කර ඇත)
if lang == "සිංහල":
    title = "🚗 වාහන තොරතුරු මධ්‍යස්ථානය"
    label = "වාහනයේ නම ඇතුළත් කරන්න (vitz, prado, axio):"
    specs_h = "⚙️ තාක්ෂණික විස්තර"
    price_h = "💰 වෙළඳපොළ මිල තොරතුරු"
    cc_l, fuel_l, hp_l = "එන්ජින් ධාරිතාව", "ඉන්ධන වර්ගය", "අශ්ව බලය"
    lkr_text, lakhs_text = "මුළු මිල (රුපියල්)", "ලක්ෂ"
    install_btn = "මෙම ඇප් එක ඔබගේ දුරකථනයට ස්ථාපනය (Install) කර ගැනීමට මෙතැන ක්ලික් කරන්න"
    install_msg = "ස්ථාපනය කිරීමට: බ්‍රවුසරයේ ⋮ ලකුණ ඔබා 'Add to Home screen' යන්න තෝරන්න."
else:
    title = "🚗 Vehicle Information Center"
    label = "Type vehicle name (vitz, prado, axio):"
    specs_h = "⚙️ Technical Specifications"
    price_h = "💰 Market Price Info"
    cc_l, fuel_l, hp_l = "Engine Capacity", "Fuel Type", "Horsepower"
    lkr_text, lakhs_text = "Total Price (LKR)", "Lakhs"
    install_btn = "Click here to install this app on your phone"
    install_msg = "To Install: Tap ⋮ in your browser and select 'Add to Home screen'."

st.title(title)

# --- අලුතින් එකතු කළ Install Button එක ---
if st.button(install_btn):
    st.info(install_msg)
# ----------------------------------------

query = st.text_input(label).lower().strip()

if query:
    st.markdown("---")
    if query in car_db:
        car = car_db[query]
        
        # 1. පින්තූරය (ඔයාගේ GitHub එකෙන්)
        img_path = os.path.join(base_path, car["img"])
        if os.path.exists(img_path):
            st.image(img_path, caption=car["name_si"] if lang == "සිංහල" else car["name_en"], use_column_width=True)

        # 2. මිල පෙන්වීම (පැහැදිලිව)
        lkr_val = car["price"] * usd_rate
        lakhs = lkr_val / 100000
        st.subheader(price_h)
        st.markdown(f"""
        <div style="background-color:#111; padding:25px; border-radius:15px; border: 2px solid #ff4b4b; text-align:center;">
            <h1 style="color:white; margin:0;">{lkr_text}: {lkr_val:,.0f}</h1>
            <h2 style="color:#ff4b4b; margin:0;">({lakhs:,.1f} {lakhs_text})</h2>
            <p style="color:#888;">USD: ${car['price']:,}</p>
        </div>
        """, unsafe_allow_html=True)

        # 3. තාක්ෂණික විස්තර (වචන කැපෙන්නේ නැති වෙන්න st.success පාවිච්චි කර ඇත)
        st.subheader(specs_h)
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"**{cc_l}**")
            st.success(car["cc_si"] if lang == "සිංහල" else car["cc_en"])
        with c2:
            st.markdown(f"**{fuel_l}**")
            st.success(car["fuel_si"] if lang == "සිංහල" else car["fuel_si"])
        with c3:
            st.markdown(f"**{hp_l}**")
            st.success(car["hp_si"] if lang == "සිංහල" else car["hp_en"])
