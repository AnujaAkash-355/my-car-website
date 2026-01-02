# භාෂාව අනුව Button එකේ වචන වෙනස් කිරීම
if lang == "සිංහල":
    install_btn = "මෙම ඇප් එක ඔබගේ දුරකථනයට ස්ථාපනය (Install) කර ගැනීමට මෙතැන ක්ලික් කරන්න"
    install_msg = """
    **ස්ථාපනය කරන ආකාරය:**
    1. බ්‍රවුසරයේ ඉහළ දකුණු කෙළවරේ ඇති තිත් තුන (⋮) ඔබන්න.
    2. 'Add to Home screen' හෝ 'Install app' යන්න තෝරන්න.
    3. 'Add' බොත්තම එබූ පසු මෙය ඔබගේ ඇප් අතරට එක් වේ.
    """
else:
    install_btn = "Click here to install this app on your phone"
    install_msg = """
    **How to Install:**
    1. Tap the three dots (⋮) on the top right of your browser.
    2. Select 'Add to Home screen' or 'Install app'.
    3. Click 'Add' to see the app on your home screen.
    """

# Button එක පෙන්වීම
if st.button(install_btn):
    st.info(install_msg)
