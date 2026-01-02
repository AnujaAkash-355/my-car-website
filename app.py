import streamlit as st

# සයිට් එකේ මූලික සැකසුම්
st.set_page_config(page_title="Global Auto Hub", layout="wide")

# භාෂාව තෝරන කොටස (Language Switcher)
lang = st.sidebar.selectbox("භාෂාව තෝරන්න / Select Language", ["සිංහල", "English"])

# පෙන්විය යුතු අකුරු භාෂාව අනුව වෙනස් කිරීම
if lang == "සිංහල":
    title = "🌍 ලෝක වාහන තොරතුරු මධ්‍යස්ථානය"
    sub_title = "ඕනෑම වාහනයක නමක් ටයිප් කරන්න (උදා: Toyota, Tesla, Honda Civic)"
    search_label = "වාහනයේ නම ඇතුළත් කරන්න:"
    not_found = "කණගාටුයි, එම වාහනයේ විස්තර සොයාගත නොහැක."
    showroom_title = "ප්‍රදර්ශනාගාරය"
else:
    title = "🌍 Global Auto Information Hub"
    sub_title = "Type any car name or brand (e.g., Toyota, Tesla, Honda Civic)"
    search_label = "Enter car or brand name:"
    not_found = "Sorry, details for that vehicle were not found."
    showroom_title = "Showroom"

st.title(title)
st.write(sub_title)

# වාහන දත්ත (ප්‍රධාන සමාගම් කිහිපයක්)
car_data = {
    "toyota": {"si": "ජපානයේ අංක 1 වාහන නිෂ්පාදකයා.", "en": "Japan's No. 1 car manufacturer."},
    "honda": {"si": "විශ්වාසවන්ත එන්ජින් සඳහා ප්‍රසිද්ධයි.", "en": "Famous for reliable engines."},
    "bmw": {"si": "ජර්මානු සුඛෝපභෝගී වාහන.", "en": "German luxury vehicle manufacturer."},
    "tesla": {"si": "විද්‍යුත් වාහන (EV) ලෝකයේ පෙරළිකාරයා.", "en": "Pioneer in electric vehicles (EV)."},
    "mercedes": {"si": "ලොව සුඛෝපභෝගී වාහන වල සංකේතය.", "en": "The symbol of luxury vehicles worldwide."},
    "nissan": {"si": "ජපන් තාක්ෂණය සහ කල්පැවැත්ම.", "en": "Japanese technology and durability."},
    "lamborghini": {"si": "ඉතාලි සුපිරි ක්‍රීඩා වාහන.", "en": "Italian super sports cars."},
    "ferrari": {"si": "වේගය සහ රතු පැහැයට උරුමකම් කියන ඉතාලි සමාගම.", "en": "Italian company famous for speed and red color."}
}

# සර්ච් බාර් එක
search_query = st.text_input(search_label).lower().strip()

if search_query:
    st.markdown("---")
    found = False
    
    # නම ආසන්න වශයෙන් සර්ච් කිරීම
    for brand, info in car_data.items():
        if search_query in brand or brand in search_query:
            st.header(f"🚘 {brand.upper()}")
            # තෝරාගත් භාෂාව අනුව විස්තරය පෙන්වීම
            st.info(info["si"] if lang == "සිංහල" else info["en"])
            
            # අන්තර්ජාලයෙන් පින්තූරය ගේන ලින්ක් එක
            image_url = f"https://source.unsplash.com/featured/?{brand},car"
            st.image(image_url, width=800)
            found = True
            break
    
    # ලැයිස්තුවේ නැතිනම් පොදු පින්තූරයක් පෙන්වීම
    if not found:
        st.header(f"🔍 {search_query.upper()}")
        image_url = f"https://source.unsplash.com/featured/?{search_query},vehicle"
        st.image(image_url, caption=search_query, width=800)

st.markdown("---")
st.subheader(showroom_title)
# පොදු පින්තූර කිහිපයක් පෙන්වීම
cols = st.columns(4)
popular_brands = ["Toyota", "BMW", "Tesla", "Nissan"]
for i, b in enumerate(popular_brands):
    with cols[i]:
        st.image(f"https://source.unsplash.com/featured/?{b},car", caption=b)
