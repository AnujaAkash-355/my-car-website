import streamlit as st

# පේජ් එකේ සෙටින්ග්ස්
st.set_page_config(page_title="Mega Motors SL", layout="wide")

# ප්‍රධාන මාතෘකාව
st.title("🚗 ශ්‍රී ලංකා වාහන සහ බයික් තොරතුරු")
st.write("පහත ඕනෑම වාහනයක නම ටයිප් කර තොරතුරු සහ පින්තූර බලන්න.")

# වාහන සහ බයික් දත්ත ගබඩාව (පින්තූර ඔයාගේ GitHub එකෙන් කෙලින්ම ගනී)
data_store = {
    # --- වාහන (Cars) ---
    "land cruiser": {"name": "Toyota Land Cruiser V8", "price": "රු. ලක්ෂ 650 - 850", "url": "land_cruiser.jpg"},
    "bmw i8": {"name": "BMW i8 Hybrid", "price": "රු. ලක්ෂ 550 - 650", "url": "bmw_i8.jpg"},
    "benz": {"name": "Mercedes-Benz S-Class", "price": "රු. ලක්ෂ 250 - 800", "url": "benz.jpg"},
    "defender": {"name": "Land Rover Defender 110", "price": "රු. ලක්ෂ 500 - 900", "url": "defender.jpg"},
    "alto": {"name": "Suzuki Alto", "price": "රු. ලක්ෂ 25 - 35", "url": "alto.jpg"},
    "montero": {"name": "Mitsubishi Montero Sport", "price": "රු. ලක්ෂ 250 - 450", "url": "montero.jpg"},
    "axio": {"name": "Toyota Axio", "price": "රු. ලක්ෂ 75 - 95", "url": "axio.jpg"},
    "prado": {"name": "Toyota Prado", "price": "රු. ලක්ෂ 120 - 450", "url": "prado.jpg"},
    "vitz": {"name": "Toyota Vitz", "price": "රු. ලක්ෂ 35 - 65", "url": "vitz.jpg"},
    "gtr": {"name": "Nissan GTR R35", "price": "රු. ලක්ෂ 300 - 550", "url": "gtr.jpg"},

    # --- බයික් (Bikes) ---
    "hornet": {"name": "Honda Hornet 250", "price": "රු. ලක්ෂ 12 - 18", "url": "hornet.jpg"},
    "jade": {"name": "Honda Jade 250", "price": "රු. ලක්ෂ 8 - 12", "url": "jade.jpg"},
    "fz": {"name": "Yamaha FZ Version 3", "price": "රු. ලක්ෂ 8 - 10", "url": "fz.jpg"},
    "dio": {"name": "Honda Dio (New)", "price": "රු. ලක්ෂ 5 - 7", "url": "dio.jpg"},
    "pcx": {"name": "Honda PCX 160", "price": "රු. ලක්ෂ 15 - 18", "url": "pcx.jpg"}
}

# සෙවුම් කොටස (Search Bar)
search_query = st.text_input("වාහනයේ නම ටයිප් කරන්න (උදා: gtr, alto, hornet, defender):").lower()

if search_query:
    if search_query in data_store:
        v = data_store[search_query]
        st.subheader(v["name"])
        st.write(f"**මිල:** {v['price']}")
        # GitHub එකේ තියෙන පින්තූරය පෙන්වීම
        st.image(v["url"], use_container_width=True)
    else:
        st.warning("කණගාටුයි, එම වාහනයේ තොරතුරු අප සතුව නැත. කරුණාකර වෙනත් නමක් උත්සාහ කරන්න.")

st.markdown("---")

# ප්‍රදර්ශනාගාරය (Showroom) - වාහන කිහිපයක් එකපාර පෙන්වීමට
st.subheader("ප්‍රදර්ශනාගාරය (Showroom)")
cols = st.columns(3)
for i, (key, val) in enumerate(list(data_store.items())[:6]):
    with cols[i % 3]:
        st.image(val["url"], caption=val["name"], use_container_width=True)
