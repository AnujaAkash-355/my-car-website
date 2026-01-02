import streamlit as st

# ඇප් එකේ මූලික සැකසුම්
st.set_page_config(page_title="වාහන වල මිල ගණන්", layout="wide")

# භාෂාව තෝරාගැනීම (Sidebar එකේ)
lang = st.sidebar.radio("භාෂාව තෝරන්න / Select Language", ["සිංහල", "English"])

usd_rate = 300.0 

# වාහන දත්ත (2025/26 අලුත්ම දත්ත)
car_db = {
    "alto": {"name": "Suzuki Alto 2025", "cc": "800cc / 1000cc", "fuel": "Petrol", "hp": "60 hp", "price": 9500},
    "prado": {"name": "Toyota Prado 2025 (LC250)", "cc": "2800cc Turbo", "fuel": "Diesel", "hp": "201 hp", "price": 78000},
    "v8": {"name": "Toyota Land Cruiser V8", "cc": "4500cc", "fuel": "Diesel", "hp": "268 hp", "price": 95000},
    "vitz": {"name": "Toyota Vitz 2024", "cc": "1000cc", "fuel": "Petrol/Hybrid", "hp": "68 hp", "price": 18000},
    "defender": {"name": "Land Rover Defender 2024", "cc": "3000cc", "fuel": "Diesel", "hp": "296 hp", "price": 88000},
    "tesla": {"name": "Tesla Model 3 2025", "cc": "Electric", "fuel": "Electric", "hp": "283 hp", "price": 45000}
}

# භාෂාව අනුව වචන වෙනස් කිරීම
if lang == "සිංහල":
    title = "🚗 වාහන වල මිල ගණන් සහ විස්තර (2026)"
    label = "වාහනයේ නම සහ වර්ෂය ටයිප් කරන්න:"
    specs_h = "⚙️ තාක්ෂණික විස්තර"
    price_h = "💰 වත්මන් වෙළඳපොළ මිල"
    cc_label = "එන්ජින් ධාරිතාව"
    fuel_label = "ඉන්ධන වර්ගය"
    hp_label = "අශ්ව බලය (HP)"
else:
    title = "🚗 Vehicle Prices & Specifications (2026)"
    label = "Type car name and year (e.g. Prado 2025):"
    specs_h = "⚙️ Technical Specifications"
    price_h = "💰 Market Price Info"
    cc_label = "Engine Capacity"
    fuel_label = "Fuel Type"
    hp_label = "Horsepower (HP)"

st.title(title)
query = st.text_input(label).lower().strip()

if query:
    st.markdown("---")
    
    # පින්තූරය - පූසෝ එන්නේ නැති වෙන්න Unsplash පාවිච්චි කරනවා
    img_url = f"https://source.unsplash.com/1200x600/?{query.replace(' ', '+')},car,automobile"
    st.image(img_url, use_column_width=True)

    # දත්ත සෙවීම
    res = {"name": query.upper(), "cc": "1000cc - 3000cc", "fuel": "Petrol/Diesel", "hp": "N/A", "price": 25000}
    for key in car_db:
        if key in query:
            res = car_db[key]
            break

    lkr_price = res["price"] * usd_rate
    lakhs = lkr_price / 100000

    # මිල පෙන්වීම (පැහැදිලිව සහ පිළිවෙලට)
    st.subheader(price_h)
    st.markdown(f"""
    <div style="background-color:#1e1e1e; padding:20px; border-radius:15px; text-align:center; border: 2px solid #ff4b4b;">
        <h2 style="color:white; margin:0;">රුපියල් {lkr_price:,.0f}</h2>
        <h3 style="color:#ff4b4b; margin:0;">(ලක්ෂ {lakhs:,.1f} පමණ වේ)</h3>
        <p style="color:#888; margin:5px 0 0 0;">USD Price: ${res['price']:,}</p>
    </div>
    """, unsafe_allow_html=True)

    # තාක්ෂණික විස්තර
    st.subheader(specs_h)
    c1, c2, c3 = st.columns(3)
    with c1: st.metric(cc_label, res["cc"])
    with c2: st.metric(fuel_label, res["fuel"])
    with c3: st.metric(hp_label, res["hp"])

st.markdown("---")
st.caption("All data is updated for the 2026 market. Tax rates may apply.")
