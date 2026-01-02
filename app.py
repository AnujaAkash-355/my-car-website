import streamlit as st
import os

st.set_page_config(page_title="Mega Motors SL", layout="wide")

st.title("🚗 ශ්‍රී ලංකා වාහන සහ බයික් තොරතුරු")
st.write("පහත ඕනෑම වාහනයක නම ටයිප් කර තොරතුරු බලන්න.")

base_path = os.path.dirname(__file__)

data_store = {
    "vitz": {"name": "Toyota Vitz", "price": "රු. ලක්ෂ 35 - 65", "img": "vitz.jpg"},
    "prado": {"name": "Toyota Prado", "price": "රු. ලක්ෂ 120 - 450", "img": "prado.jpg"},
    "montero": {"name": "Mitsubishi Montero Sport", "price": "රු. ලක්ෂ 250 - 450", "img": "montero.jpg"},
    "landcruiser": {"name": "Toyota Land Cruiser", "price": "රු. ලක්ෂ 650 - 850", "img": "landcruiser.jpg"},
    "i8": {"name": "BMW i8 Hybrid", "price": "රු. ලක්ෂ 550 - 650", "img": "i8.jpg"},
    "gtr": {"name": "Nissan GTR R35", "price": "රු. ලක්ෂ 300 - 550", "img": "gtr.jpg"},
    "defender": {"name": "Land Rover Defender", "price": "රු. ලක්ෂ 500 - 900", "img": "defender.jpg"},
    "benz": {"name": "Mercedes-Benz S-Class", "price": "රු. ලක්ෂ 250 - 800", "img": "benz.jpg"},
    "axio": {"name": "Toyota Axio", "price": "රු. ලක්ෂ 75 - 95", "img": "axio.jpg"},
    "allion": {"name": "Toyota Allion", "price": "රු. ලක්ෂ 65 - 85", "img": "allion.jpg"}
}

search_query = st.text_input("වාහනයේ නම ටයිප් කරන්න:").lower().strip()

if search_query:
    if search_query in data_store:
        item = data_store[search_query]
        st.subheader(item["name"])
        st.write(f"**මිල:** {item['price']}")
        img_path = os.path.join(base_path, item["img"])
        if os.path.exists(img_path):
            # මෙතන width=600 දැම්මම පින්තූරය ගොඩක් ඇදෙන්නේ නැතුව පැහැදිලිව පේනවා
            st.image(img_path, width=600)
    else:
        st.warning("තොරතුරු හමුවුනේ නැත.")

st.markdown("---")
st.subheader("ප්‍රදර්ශනාගාරය (Showroom)")
cols = st.columns(3)
items = list(data_store.values())
for i in range(min(6, len(items))):
    with cols[i % 3]:
        img_path = os.path.join(base_path, items[i]["img"])
        if os.path.exists(img_path):
            # Showroom එකේ පින්තූර කුඩාවට පෙන්වීම
            st.image(img_path, caption=items[i]["name"], width=300)
