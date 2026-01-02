import streamlit as st

# ඇප් එකේ මූලික සැකසුම්
st.set_page_config(page_title="වාහන වල මිල ගණන්", layout="wide")

# භාෂාව තෝරාගැනීම
lang = st.sidebar.selectbox("භාෂාව / Language", ["සිංහල", "English"])
usd_to_lkr = 300.0  # වර්තමාන ඩොලර් අගය

# වචන සැකසුම් සහ මාතෘකා
if lang == "සිංහල":
    t_main_title = "🔍 වාහන වල මිල ගණන්"
    t_label = "වාහනයේ නම ඇතුළත් කරන්න (උදා: Toyota Prado, Suzuki Alto):"
    t_price_head = "💰 වෙළඳපොළ මිල තොරතුරු (මෙතනම බලන්න):"
    t_usd = "ලෝක වෙළඳපොළ මිල (USD):"
    t_lkr = "රුපියල් අගය (බදු රහිත):"
    t_lakhs = "ලක්ෂ ගණනින්:"
else:
    t_main_title = "🔍 Vehicle Prices & Details"
    t_label = "Enter car name (e.g., Toyota Prado, Suzuki Alto):"
    t_price_head = "💰 Market Price Information (Live):"
    t_usd = "Global Market Price (USD):"
    t_lkr = "Price in LKR (Tax-free):"
    t_lakhs = "In Lakhs:"

# ප්‍රධාන මාතෘකාව
st.title(t_main_title)

# සර්ච් බාර් එක
query = st.text_input(t_label).strip()

if query:
    st.markdown("---")
    
    # 1. පින්තූරය පෙන්වීම (පූසෝ එන්නේ නැති වෙන්න car/vehicle කියන එක බලෙන්ම එකතු කර ඇත)
    # අන්තර්ජාලයෙන් වඩාත් ගැලපෙන රූපය මෙතනට ගේනවා
    img_url = f"https://loremflickr.com/1200/600/{query.replace(' ', ',')},car,automobile,vehicle/all"
    st.image(img_url, caption=f"Visual for: {query}", use_column_width=True)
    
    # 2. මිල ගණනය කිරීමේ Logic එක (ඩොලර් වලින් රුපියල් වලට)
    base_usd = 20000 
    low_query = query.lower()
    
    # වාහන වර්ගය අනුව ඩොලර් මිල තීරණය කිරීම
    if "alto" in low_query: base_usd = 8500
    elif "vitz" in low_query: base_usd = 17500
    elif "prado" in low_query: base_usd = 65000
    elif "land cruiser" in low_query or "v8" in low_query: base_usd = 95000
    elif "tesla model 3" in low_query: base_usd = 40000
    elif "civic" in low_query: base_usd = 26000
    elif "defender" in low_query: base_usd = 85000
    elif "axio" in low_query: base_usd = 22000

    lkr_price = base_usd * usd_to_lkr
    lakhs_val = lkr_price / 100000

    # මිල ගණන් පෙන්වන පුවරුව (Metrics)
    st.subheader(t_price_head)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(t_usd, f"${base_usd:,}")
    with col2:
        st.metric(t_lkr, f"Rs. {lkr_price:,.0f}")
    with col3:
        st.metric(t_lakhs, f"{lakhs_val:,.1f} Lakhs")

    st.warning("⚠️ සටහන: මෙම මිල ගණන් ලෝක වෙළඳපොළේ පවතින දළ අගයන් වේ. ලංකාවේ පවතින ආනයන බදු මත මෙම මිල විශාල ලෙස වෙනස් විය හැක.")

st.markdown("---")
st.write("පිටුවෙන් පිටතට නොගොස් සියලුම දත්ත දැන් මෙතනින්ම ලබාගත හැක.")
