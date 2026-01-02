import streamlit as st

st.set_page_config(page_title="Mega Motors SL", layout="wide")

st.title("🚗 ශ්‍රී ලංකා වාහන සහ බයික් තොරතුරු")
st.write("පහත ඕනෑම වාහනයක නම ටයිප් කර තොරතුරු සහ පින්තූර බලන්න.")

# ඔයා අප්ලෝඩ් කළ පින්තූර වල නම් මෙතන හරියටම තියෙනවා
data_store = {
    "vitz": {"name": "Toyota Vitz", "price": "රු. ලක්ෂ 35 - 65", "url": "vitz.jpg"},
    "prado": {"name": "Toyota Prado", "price": "රු. ලක්ෂ 120 - 450", "url": "prado.jpg"},
    "montero": {"name": "Mitsubishi Montero Sport", "price": "රු. ලක්ෂ 250 - 450", "url": "montero.jpg"},
    "landcruiser": {"name": "Toyota Land Cruiser", "price": "රු. ලක්ෂ 650 - 850", "url": "landcruiser.jpg"},
    "i8": {"name": "BMW i8 Hybrid", "price": "රු. ලක්ෂ 550 - 650", "url": "i8.jpg"},
    "gtr": {"name": "Nissan GTR R35", "price": "රු. ලක්ෂ 300 - 550", "url": "gtr.jpg"},
    "defender": {"name": "Land Rover Defender", "price": "රු. ලක්ෂ 500 - 900", "url": "defender.jpg"},
    "benz": {"name": "Mercedes-Benz S-Class", "price": "රු. ලක්ෂ 250 - 800", "url": "benz.jpg"},
    "axio": {"name": "Toyota Axio", "price": "රු. ලක්ෂ 75 - 95", "url": "axio.jpg"},
    "allion": {"name": "Toyota Allion", "price": "රු. ලක්ෂ 65 - 85", "url": "allion.jpg"}
}

search_query = st.text_input("වාහනයේ නම ටයිප් කරන්න (උදා: gtr, prado, vitz):").lower().strip()

if search_query:
    if search_query in data_store:
        v = data_store[search_query]
        st.subheader(v["name"])
        st.write(f"**මිල:** {v['price']}")
        # කළු පාට message එක එන්නේ මේ පල්ලෙහා පේළිය නිසයි. මම ඒක දැන් නිවැරදි කළා.
        st.image(v["url"], use_column_width=True)
    else:
        st.warning("කණගාටුයි, එම වාහනයේ තොරතුරු අප සතුව නැත.")

st.markdown("---")
st.subheader("ප්‍රදර්ශනාගාරය (Showroom)")
cols = st.columns(3)
for i, (key, val) in enumerate(list(data_store.items())[:6]):
    with cols[i % 3]:
        st.image(val["url"], caption=val["name"], use_column_width=True)
