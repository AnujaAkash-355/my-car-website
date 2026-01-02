import streamlit as st

st.set_page_config(page_title="Mega Motors SL", layout="wide")

st.title("🚗 ශ්‍රී ලංකා වාහන සහ බයික් තොරතුරු")
st.write("පහත ඕනෑම වාහනයක නම ටයිප් කර තොරතුරු සහ පින්තූර බලන්න.")

# වාහන දත්ත ගබඩාව (Direct links)
data_store = {
    "land cruiser": {"name": "Toyota Land Cruiser V8", "price": "රු. ලක්ෂ 650 - 850", "url": "https://img.sm360.ca/ir/w1024h768c/images/inventory/st-eustache-mitsubishi/mitsubishi/outlander/2022/9431871/2022-mitsubishi-outlander_001.jpg"},
    "bmw i8": {"name": "BMW i8 Hybrid", "price": "රු. ලක්ෂ 550 - 650", "url": "https://paultan.org/image/2014/06/BMW-i8-1.jpg"},
    "alto": {"name": "Suzuki Alto", "price": "රු. ලක්ෂ 25 - 35", "url": "https://stimg.cardekho.com/images/carexteriorimages/930x620/Suzuki/Alto-800/7075/1592144120306/front-left-side-47.jpg"},
    "hornet": {"name": "Honda Hornet 250", "price": "රු. ලක්ෂ 12 - 18", "url": "https://i.ytimg.com/vi/uE6-I6S0Lw0/maxresdefault.jpg"},
    "gtr": {"name": "Nissan GTR R35", "price": "රු. ලක්ෂ 300 - 550", "url": "https://images.barrons.com/im-705353?width=1280&size=1.5"},
    "defender": {"name": "Land Rover Defender 110", "price": "රු. ලක්ෂ 500 - 900", "url": "https://media.landrover.com/sites/default/files/styles/full_width_retina/public/2019-09/L663_101.jpg"}
}

search_query = st.text_input("වාහනයේ නම ටයිප් කරන්න (උදා: gtr, alto, hornet):").lower()

if search_query:
    if search_query in data_store:
        v = data_store[search_query]
        st.subheader(v["name"])
        st.write(f"**මිල:** {v['price']}")
        st.image(v["url"], use_container_width=True)
    else:
        st.warning("කණගාටුයි, එම වාහනයේ තොරතුරු අප සතුව නැත.")

st.markdown("---")
st.subheader("ප්‍රදර්ශනාගාරය (Showroom)")
cols = st.columns(3)
for i, (key, val) in enumerate(list(data_store.items())[:6]):
    with cols[i % 3]:
        st.image(val["url"], caption=val["name"], use_container_width=True)
