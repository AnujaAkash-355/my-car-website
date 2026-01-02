import streamlit as st

# ඇප් එකේ නම වෙනස් කිරීම
st.set_page_config(page_title="වාහන වල මිල ගණන්", layout="wide")

# භාෂාව
lang = st.sidebar.selectbox("භාෂාව / Language", ["සිංහල", "English"])
usd_rate = 300.0 

# වාහන දත්ත ගබඩාව (Engine & Tech Specs ඇතුළුව)
car_specs = {
    "alto": {"eng": "800cc", "fuel": "Petrol", "hp": "47 hp", "price_usd": 8500},
    "vitz": {"eng": "1000cc / 1300cc", "fuel": "Petrol/Hybrid", "hp": "68 hp", "price_usd": 17500},
    "prado": {"eng": "2700cc / 2800cc", "fuel": "Petrol/Diesel", "hp": "160-200 hp", "price_usd": 65000},
    "land cruiser": {"eng": "3300cc / 3500cc", "fuel": "Diesel/Petrol", "hp": "300+ hp", "price_usd": 95000},
    "axio": {"eng": "1500cc", "fuel": "Hybrid/Petrol", "hp": "110 hp", "price_usd": 22000},
    "civic": {"eng": "1500cc Turbo", "fuel": "Petrol", "hp": "180 hp", "price_usd": 28000},
    "tesla model 3": {"eng": "Electric Motor", "fuel": "Electric", "hp": "283 hp", "price_usd": 42000},
    "defender": {"eng": "2000cc / 3000cc", "fuel": "Diesel/Petrol", "hp": "250-400 hp", "price_usd": 85000}
}

if lang == "සිංහල":
    t_title = "🔍 වාහන වල මිල ගණන් සහ විස්තර"
    t_input = "වාහනයේ නම ඇතුළත් කරන්න:"
    t_details = "⚙️ තාක්ෂණික විස්තර (Technical Specs)"
    t_price = "💰 වත්මන් වෙළඳපොළ මිල"
else:
    t_title = "🔍 Vehicle Prices & Specifications"
    t_input = "Enter car name:"
    t_details = "⚙️ Technical Specifications"
    t_price = "💰 Current Market Price"

st.title(t_title)
query = st.text_input(t_input).lower().strip()

if query:
    st.markdown("---")
    
    # පින්තූරය පෙන්වීම (පූසෝ එන්නේ නැති වෙන්න car කියන එක අගට දමා ඇත)
    img_url = f"https://loremflickr.com/1000/500/{query.replace(' ', ',')},car/all"
    st.image(img_url, use_column_width=True)

    # දත්ත සෙවීම
    base_usd = 20000
    spec_data = {"eng": "Not Available", "fuel": "Not Available", "hp": "Not Available"}
    
    # දත්ත ගබඩාවෙන් තොරතුරු ලබා ගැනීම
    for car in car_specs:
        if car in query:
            base_usd = car_specs[car]["price_usd"]
            spec_data = car_specs[car]
            break

    lkr_price = base_usd * usd_rate
    
    # මිල ගණන් විශාලව පෙන්වීම (මුළු ඉලක්කමම පෙනෙන පරිදි)
    st.subheader(t_price)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"### USD: **${base_usd:,}**")
    with c2:
        st.markdown(f"### LKR: **රු. {lkr_price:,.2f}**")
    
    st.success(f"දළ වශයෙන් රුපියල් ලක්ෂ: **{(lkr_price/100000):,.1f} Lakhs**")

    # තාක්ෂණික විස්තර පෙන්වීම
    st.subheader(t_details)
    st.table({
        "විස්තරය (Feature)": ["එන්ජින් ධාරිතාව (Engine)", "ඉන්ධන වර්ගය (Fuel)", "අශ්ව බලය (Horsepower)"],
        "තොරතුරු (Value)": [spec_data["eng"], spec_data["fuel"], spec_data["hp"]]
    })

st.markdown("---")
st.warning("මෙම තොරතුරු අන්තර්ජාලය ඇසුරින් ලබාගත් දළ දත්ත වේ.")
