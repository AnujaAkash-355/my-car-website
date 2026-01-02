import streamlit as st

st.set_page_config(page_title="Mega Motors SL", layout="wide")

st.title("🚗 ශ්‍රී ලංකා වාහන සහ බයික් තොරතුරු")
st.write("පහත ඕනෑම වාහනයක නම ටයිප් කර තොරතුරු සහ පින්තූර බලන්න.")

# 100% වැඩ කරන පින්තූර ලින්ක් සහිත දත්ත ගබඩාව
data_store = {
    "land cruiser": {"name": "Toyota Land Cruiser", "price": "රු. ලක්ෂ 650 - 850", "url": "https://images.unsplash.com/photo-1594568284297-7c64464062b1?auto=format&fit=crop&q=80&w=1000"},
    "bmw i8": {"name": "BMW i8 Hybrid", "price": "රු. ලක්ෂ 550 - 650", "url": "https://images.unsplash.com/photo-1556122071-e40497129f21?auto=format&fit=crop&q=80&w=1000"},
    "alto": {"name": "Suzuki Alto", "price": "රු. ලක්ෂ 25 - 35", "url": "https://images.unsplash.com/photo-1620211110058-29472e39906d?auto=format&fit=crop&q=80&w=1000"},
    "hornet": {"name": "Honda Hornet", "price": "රු. ලක්ෂ 12 - 18", "url": "https://images.unsplash.com/photo-1614165933026-0750f6829e79?auto=format&fit=crop&q=80&w=1000"},
    "gtr": {"name": "Nissan GTR R35", "price": "රු. ලක්ෂ 300 - 550", "url": "https://images.unsplash.com/photo-1614200187524-dc4b892acf16?auto=format&fit=crop&q=80&w=1000"},
    "defender": {"name": "Land Rover Defender", "price": "රු. ලක්ෂ 500 - 900", "url": "https://images.unsplash.com/photo-1605333396915-47ed6b68a00e?auto=format&fit=crop&q=80&w=1000"}
}

search_query = st.text_input("වාහනයේ නම ටයිප් කරන්න (gtr, hornet, alto):").lower()

if search_query:
    if search_query in data_store:
        v = data_store[search_query]
        st.subheader(v["name"])
        st.write(f"**මිල:** {v['price']}")
        st.image(v["url"], use_container_width=True)
    else:
        st.warning("කණගාටුයි, එම වාහනය හමුවුනේ නැත.")

st.markdown("---")
st.subheader("ප්‍රදර්ශනාගාරය (Showroom)")
cols = st.columns(3)
for i, (key, val) in enumerate(list(data_store.items())[:6]):
    with cols[i % 3]:
        st.image(val["url"], caption=val["name"], use_container_width=True)
    
