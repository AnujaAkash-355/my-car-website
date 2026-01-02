import streamlit as st

st.set_page_config(page_title="Pro Auto Finder", layout="wide")

# භාෂාව තෝරාගැනීම
lang = st.sidebar.selectbox("භාෂාව / Language", ["සිංහල", "English"])

if lang == "සිංහල":
    t_title = "🔍 වාහන සහ මිල ගණන් සොයන්නා"
    t_label = "වාහනයේ නම ටයිප් කරන්න (උදා: Suzuki Alto, Toyota Prado 2024):"
    t_info = "පල්ලෙහායින් Google වෙතින් සොයාගත් නියම පින්තූර පෙනෙනු ඇත."
else:
    t_title = "🔍 Pro Auto & Price Finder"
    t_label = "Enter car name (e.g., Suzuki Alto, Toyota Prado 2024):"
    t_info = "Official Google images will appear below."

st.title(t_title)

# සර්ච් බාර් එක
query = st.text_input(t_label).strip()

if query:
    st.markdown("---")
    st.info(t_info)
    
    # 1. Google Images වෙත සබැඳියක් සැකසීම
    google_img_url = f"https://www.google.com/search?q={query.replace(' ', '+')}+car+official+photo&tbm=isch"
    
    # 2. වාහනයේ මිල සහ විස්තර බැලීමට බටන් එකක්
    google_price_url = f"https://www.google.com/search?q={query.replace(' ', '+')}+price+in+usd"
    
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("📸 පින්තූර බලන්න (View Google Images)", google_img_url)
    with col2:
        st.link_button("💰 මිල ගණන් බලන්න (View Prices)", google_price_url)

    # 3. Google සර්ච් රිසල්ට් එක ඇප් එක ඇතුළෙම පෙන්වීමට උත්සාහ කිරීම (Iframe)
    # සටහන: සමහර බ්‍රවුසර් වල ආරක්ෂක හේතු මත මෙය පෙන්වීමට අවහිර කළ හැක. 
    # එවැනි වෙලාවක ඉහත බටන් එක එබීමෙන් නියම පින්තූර බලාගත හැක.
    st.markdown(f'<iframe src="{google_img_url}" width="100%" height="600" style="border:none;"></iframe>', unsafe_allow_name=True)

st.markdown("---")
st.write("මචං, දැන් ඕනෑම වාහනයක් ගහලා 'පින්තූර බලන්න' බටන් එක ඔබන්න. එතකොට කෙලින්ම Google එකේ තියෙන ඔරිජිනල් පින්තූර ටික වැටෙයි.")
