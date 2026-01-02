import streamlit as st

st.set_page_config(page_title="Auto Hub SL", layout="wide")

# භාෂාව තෝරාගැනීම
lang = st.sidebar.selectbox("භාෂාව / Language", ["සිංහල", "English"])

# ඩොලර් අගය රුපියල් වලට (දැනට පවතින සාමාන්‍ය අගය)
usd_rate = 300.0 

if lang == "සිංහල":
    t_title = "🚗 රිය අනාවරණය (Auto Finder)"
    t_label = "වාහනයේ නම ටයිප් කරන්න (උදා: Alto, Land Cruiser):"
    t_price = "දළ මිල (රුපියල්):"
    t_load = "පින්තූරය පූරණය වෙමින් පවතී..."
else:
    t_title = "🚗 Auto Finder"
    t_label = "Enter car name (e.g., Alto, Land Cruiser):"
    t_price = "Estimated Price (LKR):"
    t_load = "Image loading..."

st.title(t_title)

# සර්ච් බාර් එක
query = st.text_input(t_label).strip()

if query:
    st.markdown("---")
    
    # පින්තූරය ගේන කොටස (මෙතනදී අනිවාර්යයෙන්ම වාහනයක් එන ලෙස සකසා ඇත)
    with st.spinner(t_load):
        # අපි query එක අගට 'car' කියන වචනය බලෙන්ම එකතු කරනවා
        img_search = f"{query} car"
        img_url = f"https://loremflickr.com/800/500/{img_search.replace(' ', ',')}/all"
        st.image(img_url, caption=f"Result for: {query}")

    # මිල ගණන් පෙන්වීම
    base_usd = 15000 
    low_query = query.lower()
    
    # වාහනය අනුව මිල වෙනස් කිරීම (Logic එකක්)
    if "alto" in low_query: base_usd = 8500
    elif "vitz" in low_query: base_usd = 18000
    elif "prado" in low_query: base_usd = 65000
    elif "v8" in low_query or "land cruiser" in low_query: base_usd = 95000
    elif "tesla" in low_query: base_usd = 45000

    lkr_val = base_usd * usd_rate
    
    st.subheader(f"💰 {t_price} රු. {lkr_val:,.0f}")
    st.info(f"දළ වශයෙන් රුපියල් ලක්ෂ: {lkr_val/100000:.1f}")

    # සැබෑ මිල බැලීමට Google සර්ච් ලින්ක් එක
    st.write(f"🔗 [Real-time Market Price (Google)](https://www.google.com/search?q={query.replace(' ', '+')}+car+price+in+usd)")

st.markdown("---")
st.write("පින්තූරය වැරදි නම්, තවත් විස්තරාත්මකව ටයිප් කරන්න (උදා: Suzuki Alto Car 2022).")
