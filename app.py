import streamlit as st

st.set_page_config(page_title="Auto Market", layout="wide")

# භාෂාව
lang = st.sidebar.selectbox("භාෂාව / Language", ["සිංහල", "English"])

# ඩොලර් අගය (දැනට රු. 300 ලෙස)
usd_to_lkr = 300.0 

if lang == "සිංහල":
    t_label = "වාහනයේ නම ටයිප් කරන්න (උදා: Suzuki Alto):"
    t_price_lkr = "දළ මිල (රුපියල්):"
    t_note = "සටහන: පින්තූරය වැරදි නම් නම අගට car ලෙස ටයිප් කරන්න."
else:
    t_label = "Enter car name (e.g., Suzuki Alto):"
    t_price_lkr = "Estimated Price (LKR):"
    t_note = "Note: If the image is wrong, add 'car' at the end of the name."

st.title("🚗 Global Auto Finder")
search_query = st.text_input(t_label).strip()

if search_query:
    st.markdown("---")
    
    # මෙතනදී අපි 'car' කියන වචනය query එකට බලෙන්ම එකතු කරනවා
    # එතකොට අනිවාර්යයෙන්ම වාහනයක්මයි එන්නේ
    refined_query = f"{search_query} car"
    img_url = f"https://loremflickr.com/800/500/{refined_query.replace(' ', ',')}/all"
    
    st.image(img_url, caption=f"Showing result for: {search_query}")

    # මිල ගණන් (දළ වශයෙන් ලෝක වෙළඳපොළ මිල පෙන්වීම)
    # අපි උපකල්පනය කරමු සාමාන්‍ය වාහනයක මිල $15,000 කින් පටන් ගන්නවා කියලා
    base_usd = 15000 
    
    # Alto වගේ කුඩා වාහන වලට මිල අඩු කිරීම
    if "alto" in search_query.lower() or "vitz" in search_query.lower():
        base_usd = 8000
    elif "prado" in search_query.lower() or "v8" in search_query.lower():
        base_usd = 65000

    lkr_price = base_usd * usd_to_lkr
    
    st.subheader(f"💰 {t_price_lkr} රු. {lkr_price:,.0f}")
    st.info(f"රුපියල් ලක්ෂ: {lkr_price/100000:.1f}")
    
    # ගූගල් සර්ච් ලින්ක් එක
    google_link = f"https://www.google.com/search?q={search_query.replace(' ', '+')}+price+in+usd"
    st.write(f"🔗 [ලෝක වෙළඳපොළේ සැබෑ මිල මෙතැනින් බලන්න]({google_link})")

st.markdown("---")
st.warning(t_note)
