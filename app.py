import streamlit as st

# ඇප් එකේ නම සහ සැකසුම්
st.set_page_config(page_title="වාහන වල මිල ගණන්", layout="wide")

# ඩොලර් අගය
usd_rate = 300.0 

# වාහන දත්ත ගබඩාව (අලුත්ම මොඩල් සහ විස්තර)
# මෙතනට මම 2024/2025 අලුත්ම තොරතුරු ඇතුළත් කළා
car_database = {
    "alto": {"name": "Suzuki Alto 2024/25", "cc": "800cc / 1000cc", "fuel": "Petrol", "price_usd": 9500},
    "vitz": {"name": "Toyota Vitz (Safety Edition)", "cc": "1000cc", "fuel": "Petrol/Hybrid", "price_usd": 18500},
    "prado": {"name": "Toyota Prado 2024 (LC250)", "cc": "2700cc / 2800cc Turbo", "fuel": "Diesel/Petrol", "price_usd": 75000},
    "land cruiser": {"name": "Toyota Land Cruiser 300 (2025)", "cc": "3300cc / 3500cc Twin-Turbo", "fuel": "Diesel/Petrol", "price_usd": 105000},
    "defender": {"name": "Land Rover Defender 2024", "cc": "2000cc / 3000cc", "fuel": "Diesel/Hybrid", "price_usd": 90000},
    "v8": {"name": "Toyota Land Cruiser V8 2022", "cc": "4500cc", "fuel": "Diesel", "price_usd": 95000},
    "civic": {"name": "Honda Civic FE 2024", "cc": "1500cc VTEC Turbo", "fuel": "Petrol", "price_usd": 32000}
}

st.title("🔍 වාහන වල මිල ගණන් (2025 Update)")

# සර්ච් බාර් එක
query = st.text_input("වාහනයේ නම සහ වර්ෂය ටයිප් කරන්න (උදා: Alto 2025, Prado 2024):").lower().strip()

if query:
    st.markdown("---")
    
    # 1. පින්තූරය ගේන ක්‍රමය (අලුත්ම මොඩල් එක එන විදිහට)
    # අපි query එක අගට 'car high resolution 2025' කියලා එකතු කරනවා
    img_url = f"https://loremflickr.com/1200/600/{query.replace(' ', ',')},car,2025,exterior/all"
    st.image(img_url, caption=f"අලුත්ම මොඩල් එක: {query.upper()}", use_column_width=True)

    # 2. දත්ත සෙවීම
    res = {"name": query.upper(), "cc": "1000cc - 2500cc", "fuel": "Petrol/Hybrid", "price_usd": 25000}
    for key in car_database:
        if key in query:
            res = car_database[key]
            break

    # 3. මිල ගණනය කිරීම (ලක්ෂ ගණන සහ රුපියල් මුදල)
    lkr_price = res["price_usd"] * usd_rate
    lakhs = lkr_price / 100000

    # 4. විස්තර පෙන්වීම (විශාලව සහ පැහැදිලිව)
    st.subheader(f"📊 {res['name']} තොරතුරු")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("එන්ජින් ධාරිතාව (CC)", res["cc"])
    with col2:
        st.metric("ඉන්ධන වර්ගය", res["fuel"])
    with col3:
        st.metric("ලෝක වෙළඳපොළ මිල", f"${res['price_usd']:,}")

    # මිල ලොකුවට පෙන්වීම
    st.markdown(f"""
    <div style="background-color:#f0f2f6; padding:20px; border-radius:10px; border-left: 8px solid #ff4b4b;">
        <h2 style="margin:0; color:#31333f;">ශ්‍රී ලංකාවේ ඇස්තමේන්තුගත මිල:</h2>
        <h1 style="margin:0; color:#ff4b4b;">රුපියල් {lkr_price:,.0f}</h1>
        <h3 style="margin:0; color:#1c83e1;">(ලක්ෂ {lakhs:,.1f} පමණ වේ)</h3>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.info("සටහන: මෙහි දැක්වෙන්නේ ආනයනය කිරීමේදී වැයවන දළ CIF මිල වේ. රජයේ බදු මත මිල වෙනස් විය හැක.")
