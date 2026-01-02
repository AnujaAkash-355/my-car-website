import streamlit as st

st.set_page_config(page_title="Auto Price Converter", layout="wide")

# භාෂාව තෝරාගැනීම
lang = st.sidebar.selectbox("භාෂාව තෝරන්න / Select Language", ["සිංහල", "English"])

# අද දවසේ ඩොලර් එකේ රුපියල් අගය (මෙහි ඔයාට කැමති අගයක් දිය හැක)
usd_to_lkr = 300.0 

# වාහන සහ ඒවායේ දළ ඩොලර් මිල ගණන් (Global Prices)
# මම මෙතනට ලෝකයේ ජනප්‍රිය වාහන කිහිපයක් දැම්මා
car_db = {
    "toyota corolla": 22000,
    "toyota camry": 26000,
    "honda civic": 25000,
    "tesla model 3": 39000,
    "bmw i8": 147000,
    "nissan gtr": 115000,
    "mercedes benz s-class": 114000,
    "suzuki alto": 8000, # Global equivalent
    "toyota prado": 60000,
    "land cruiser v8": 85000
}

# භාෂා සැකසුම්
if lang == "සිංහල":
    t_title = "🚗 රුපියල් මිල ගණක යන්ත්‍රය (Live USD to LKR)"
    t_desc = f"අද ඩොලර් එකක අගය: රු. {usd_to_lkr}"
    t_label = "වාහනයේ නම ඇතුළත් කරන්න (උදා: tesla model 3):"
    t_price_usd = "ලෝක වෙළඳපොළ මිල (USD):"
    t_price_lkr = "ශ්‍රී ලංකා රුපියල් වලින් (LKR):"
else:
    t_title = "🚗 Currency Converter (USD to LKR)"
    t_desc = f"Today's Exchange Rate: 1 USD = {usd_to_lkr} LKR"
    t_label = "Enter car name (e.g., tesla model 3):"
    t_price_usd = "Global Market Price (USD):"
    t_price_lkr = "Price in Sri Lankan Rupees (LKR):"

st.title(t_title)
st.write(t_desc)

search_query = st.text_input(t_label).lower().strip()

if search_query:
    st.markdown("---")
    
    # පින්තූරය ගේන කොටස
    img_url = f"https://loremflickr.com/800/500/{search_query.replace(' ', ',')},car"
    st.image(img_url, caption=f"Visual of {search_query}")

    # මිල ගණනය කිරීම
    found = False
    for car_name, usd_price in car_db.items():
        if search_query in car_name:
            lkr_price = usd_price * usd_to_lkr
            
            # ලක්ෂ ගණනින් පෙන්වීම (Millions/Lakhs)
            lakhs = lkr_price / 100000
            
            st.subheader(f"💰 {t_price_usd} ${usd_price:,}")
            st.header(f"➡️ {t_price_lkr} රු. {lkr_price:,.2f}")
            st.success(f"දළ වශයෙන් රුපියල් ලක්ෂ: {lakhs:,.1f}")
            
            found = True
            break
            
    if not found:
        st.warning("මෙම වාහනයේ මිල දත්ත අප සතුව නැත. පින්තූරය පමණක් පහතින් පෙන්වයි.")
        st.info("වැඩිදුර මිල ගණන් සඳහා Google Search කරන්න.")

st.markdown("---")
st.write("⚠️ සටහන: මෙහි පෙන්වන්නේ බදු රහිත (Tax-free) ලෝක වෙළඳපොළ මිල රුපියල් වලට හැරවූ අගයයි. ලංකාවේ ආනයනික බදු නිසා මෙම මිල 200% - 300% කින් වැඩි විය හැක.")
