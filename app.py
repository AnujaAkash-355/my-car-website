import streamlit as st

# වෙබ් පිටුවේ සැකසුම්
st.set_page_config(page_title="Sri Lanka Vehicle Hub", layout="wide")

st.title("🚗 ශ්‍රී ලංකා වාහන සහ බයික් තොරතුරු")
st.write("ඕනෑම වාහනයක හෝ බයික් එකක නම ටයිප් කර තොරතුරු බලන්න.")

# වාහන සහ බයික් දත්ත ගබඩාව (සජීවී පින්තූර ලින්ක් සමඟ)
data_store = {
    # --- වාහන (Cars) ---
    "land cruiser": {"name": "Toyota Land Cruiser V8", "price": "ලක්ෂ 650 - 850", "url": "https://img.sm360.ca/ir/w1024h768c/images/inventory/st-eustache-toyota/toyota/land-cruiser/2024/25292358/i25292358-1.jpg"},
    "bmw i8": {"name": "BMW i8 Hybrid", "price": "ලක්ෂ 550 - 650", "url": "https://paultan.org/image/2014/06/BMW-i8-1.jpg"},
    "benz": {"name": "Mercedes-Benz S-Class", "price": "ලක්ෂ 250 - 800", "url": "https://www.mercedes-benz.com.sg/en/passengercars/models/saloon/s-class/overview/_jcr_content/root/responsivegrid/tabs/tabitem/hotspot_module/image.component.dam_assets.1691147570417.jpg"},
    "defender": {"name": "Land Rover Defender 110", "price": "ලක්ෂ 500 - 900", "url": "https://media.landrover.com/sites/default/files/styles/full_width_retina/public/2023-04/LRO_Defender_130_Outbound_01_260423.jpg"},
    "alto": {"name": "Suzuki Alto", "price": "ලක්ෂ 25 - 35", "url": "https://stimg.cardekho.com/images/carexteriorimages/930x620/Suzuki/Alto-800/7075/1587377192637/front-left-side-47.jpg"},
    "montero": {"name": "Mitsubishi Montero Sport", "price": "ලක්ෂ 250 - 450", "url": "https://www.mitsubishi-motors.com.ph/content/dam/mitsubishi-motors-ph/images/cars/montero-sport/2024/exterior/montero-sport-exterior-1.jpg"},
    "axio": {"name": "Toyota Axio", "price": "ලක්ෂ 75 - 95", "url": "https://global.toyota/pages/news/images/2015/03/30/1200/001.jpg"},
    "prado": {"name": "Toyota Prado", "price": "ලක්ෂ 120 - 450", "url": "https://images.drive.com.au/driveau/image/upload/c_fill,f_auto,g_auto,h_675,q_auto:eco,w_1200/v1/cms/uploads/v9s1shfivly6fcc788n3"},
    "vitz": {"name": "Toyota Vitz", "price": "ලක්ෂ 35 - 65", "url": "https://images.honestjohn.co.uk/imagecache/file/width/640/upload/siteimages/articles/Toyota/Vitz/Toyota_Vitz_1.jpg"},
    "gtr": {"name": "Nissan GTR R35", "price": "ලක්ෂ 300 - 550", "url": "https://images.barrons.com/im-705353?width=1280&size=1.5"},
    
    # --- බයික් (Bikes) ---
    "hornet": {"name": "Honda Hornet 250", "price": "ලක්ෂ 10 - 15", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Honda_CB250_Hornet.jpg/1200px-Honda_CB250_Hornet.jpg"},
    "jade": {"name": "Honda Jade 250", "price": "ලක්ෂ 8 - 12", "url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Honda_Jade250.jpg"},
    "dio": {"name": "Honda Dio (Japan)", "price": "ලක්ෂ 4 - 6", "url": "https://static.autox.com/uploads/2018/05/honda-dio-colors-1.jpg"},
    "wr": {"name": "Yamaha WR 250", "price": "ලක්ෂ 12 - 18", "url": "https://yamaha.lk/wp-content/uploads/2020/09/WR250R-Blue-Hero-L.jpg"},
    "v-strom": {"name": "Suzuki V-Strom 250", "price": "ලක්ෂ 15 - 20", "url": "https://globalsuzuki.com/motorcycle/products/v-strom250/images/visual.jpg"}
}

# සර්ච් බාර් එක
search_query = st.text_input("වාහනයේ නම ටයිප් කරන්න (උදා: gtr, alto, hornet):").lower().strip()

if search_query in data_store:
    data = data_store[search_query]
    st.divider()
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.image(data['url'], use_container_width=True, caption=data['name'])
    with col2:
        st.subheader(f"✅ {data['name']}")
        st.success(f"💰 ඇස්තමේන්තුගත මිල: රු. {data['price']}")
elif search_query:
    st.warning("කණගාටුයි, එම නම අපගේ ලැයිස්තුවේ නැත.")

# පහළින් Gallery එකක් පෙන්වමු
st.divider()
st.subheader("ප්‍රදර්ශනාගාරය (Showroom)")
cols = st.columns(4)
for i, (key, item) in enumerate(list(data_store.items())[:8]): # මුල් අයිතම 8 පෙන්වයි
    with cols[i % 4]:
        st.image(item['url'], caption=item['name'], use_container_width=True)
