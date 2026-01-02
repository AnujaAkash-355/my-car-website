import streamlit as st

st.set_page_config(page_title="SL Vehicle Finder", layout="wide")
st.title("🚗 ශ්‍රී ලංකා වාහන තොරතුරු මධ්‍යස්ථානය")

# වාහන දත්ත - ඔයාගේ Colab එකේ තියෙන පින්තූර නම් වලටම මම මේක හැදුවා
vehicle_data = {
    "land cruiser": {"name": "Toyota Land Cruiser", "price": "ලක්ෂ 650 - 850", "url": "https://paultan.org/image/2021/06/2022-Toyota-Land-Cruiser-300-1.jpg"},
    "bmw i8": {"name": "BMW i8", "price": "ලක්ෂ 550 - 650", "url": "https://images.lifestyleasia.com/wp-content/uploads/sites/6/2020/03/12170327/bmw-i8-m-next-concept.jpg"},
    "benz": {"name": "Mercedes-Benz", "price": "ලක්ෂ 250 - 800", "url": "https://www.mercedes-benz.com.sg/en/passengercars/models/saloon/s-class/overview/_jcr_content/root/responsivegrid/tabs/tabitem/hotspot_module/image.component.dam_assets.1691147570417.jpg"},
    "defender": {"name": "Land Rover Defender", "price": "ලක්ෂ 500 - 900", "url": "https://media.landrover.com/sites/default/files/styles/full_width_retina/public/2023-04/LRO_Defender_130_Outbound_01_260423.jpg"},
    "alto": {"name": "Suzuki Alto", "price": "ලක්ෂ 25 - 35", "url": "https://stimg.cardekho.com/images/carexteriorimages/930x620/Suzuki/Alto-800/7075/1587377192637/front-left-side-47.jpg"},
    "montero": {"name": "Mitsubishi Montero", "price": "ලක්ෂ 250 - 450", "url": "https://www.mitsubishi-motors.com.ph/content/dam/mitsubishi-motors-ph/images/cars/montero-sport/2024/exterior/montero-sport-exterior-1.jpg"},
    "axio": {"name": "Toyota Axio", "price": "ලක්ෂ 75 - 95", "url": "https://global.toyota/pages/news/images/2015/03/30/1200/001.jpg"},
    "prado": {"name": "Toyota Prado", "price": "ලක්ෂ 120 - 450", "url": "https://images.drive.com.au/driveau/image/upload/c_fill,f_auto,g_auto,h_675,q_auto:eco,w_1200/v1/cms/uploads/v9s1shfivly6fcc788n3"},
    "vitz": {"name": "Toyota Vitz", "price": "ලක්ෂ 35 - 65", "url": "https://images.honestjohn.co.uk/imagecache/file/width/640/upload/siteimages/articles/Toyota/Vitz/Toyota_Vitz_1.jpg"},
    "gtr": {"name": "Nissan GTR", "price": "ලක්ෂ 300 - 550", "url": "https://images.barrons.com/im-705353?width=1280&size=1.5"}
}

search = st.text_input("වාහනයේ නම ටයිප් කරන්න (උදා: gtr, prado, i8):").lower().strip()

if search in vehicle_data:
    st.subheader(f"✅ {vehicle_data[search]['name']}")
    st.info(f"💰 මිල: රු. {vehicle_data[search]['price']}")
    st.image(vehicle_data[search]['url'], use_container_width=True)
elif search:
    st.error("කණගාටුයි, එම වාහනය අපේ ලැයිස්තුවේ නැහැ.")
