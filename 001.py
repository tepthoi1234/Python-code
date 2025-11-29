import streamlit as st
import feedparser
from sklearn.linear_model import LinearRegression

# --- NEW: page config + custom styles ---
st.set_page_config(page_title="Photify", layout="wide", initial_sidebar_state="expanded")

st.markdown(
    """
    <style>
    /* background + main font */
    .stApp { background-color: #0f1724; color: #e6eef8; font-family: "Inter", sans-serif; }
    /* center and style title */
    .photify-title { font-size:48px; font-weight:700; color:#ffffff; margin-bottom:0; }
    .photify-sub { color:#9fb3d6; margin-top:4px; margin-bottom:18px; }
    /* sidebar style */
    .css-1d391kg { background-color:#0b1220; } /* may vary by Streamlit version */
    /* card */
    .card {
        background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));
        border-radius:12px;
        padding:12px;
        margin-bottom:12px;
        box-shadow: 0 4px 18px rgba(2,6,23,0.6);
    }
    .card h4 { margin:0; color:#fff; }
    .muted { color:#9fb3d6; font-size:13px; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.image("https://i.imgur.com/2QGQ9bL.png", use_column_width=True)  # optional logo URL
st.sidebar.markdown("### Photify\nTrải nghiệm âm nhạc trực tuyến — đơn giản & gọn nhẹ")

selected_artist = st.sidebar.selectbox("Chọn nghệ sĩ", ["Ngọt", "Hotel ugly", "Kendrick lamar"])
videos = {
    "Ngọt": [
        ("Top 1", "https://www.youtube.com/watch?v=LvNEPB5x7T8&list=RDLvNEPB5x7T8&start_radio=1"),
        ("top 2", "https://www.youtube.com/watch?v=ECZVU4x6Xq0&list=RDLvNEPB5x7T8&index=3"),
        ("top 3", "https://www.youtube.com/watch?v=9mA7h1jfxc8&list=RDLvNEPB5x7T8&index=6"),
        ("Special", "https://www.youtube.com/watch?v=kSjj0LlsqnI&list=RDLvNEPB5x7T8&index=10")
    ],
    "Hotel ugly": [
        ("top 1", "https://www.youtube.com/watch?v=a24EUd0zeqI&list=RDEMlgk1vDuNv1WHg0h3jtoeFg&start_radio=1"),
        ("top 2", "https://www.youtube.com/watch?v=4d-cYDVZj5s&list=RDEMlgk1vDuNv1WHg0h3jtoeFg&index=2"),
        ("top 3", "https://www.youtube.com/watch?v=8r77kgMe3-g"),
        ("special", "https://www.youtube.com/watch?v=HB9bGQxOQSQ")
    ],
    "Kendrick lamar": [
        ("top 1", "https://www.youtube.com/watch?v=phLb_SoPBlA&list=RDEMiH8aXmL0GBif6quidMdHew&start_radio=1"),
        ("top2", "https://www.youtube.com/watch?v=IHGAX4IYREw&list=RDEMiH8aXmL0GBif6quidMdHew&index=2"),
        ("top 3", "https://www.youtube.com/watch?v=fuV4yQWdn_4"),
        ("special", "https://www.youtube.com/watch?v=sNY_2TEmzho")
    ]
}

st.markdown('<div class="photify-title">Photify - Ứng dụng nghe nhạc trực tuyến</div>', unsafe_allow_html=True)
st.markdown('<div class="photify-sub">Nghe, khám phá và thư giãn với danh sách nhạc được tuyển chọn</div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab10, tab4, tab6, tab7, tab8, tab9, tab5, tab11 = st.tabs([
    "Trang chủ",
    "Giới thiệu",
    "Dự đoán giờ đi ngủ",
    "Số bước chân cần đi trong một ngày",
    "Liên hệ",
    "Tin tức",
    "Giá vàng",
    "Kiểm tra chỉ số BMI",
    "Lượng nước cần uống trong một ngày",
    "Shop",
    "nen ngu bao nhieu 1 ngay"
])

with tab1:
    st.header(f"Bài hát của {selected_artist}")
    # show videos in two-column cards for nicer layout
    cols = st.columns(2)
    idx = 0
    for title, url in videos[selected_artist]:
        col = cols[idx % 2]
        with col:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown(f"<h4>{title}</h4>", unsafe_allow_html=True)
            st.markdown(f'<div class="muted">Nghệ sĩ: {selected_artist}</div>', unsafe_allow_html=True)
            st.video(url)
            st.markdown('</div>', unsafe_allow_html=True)
        idx += 1
with tab2:
    st.header("Giới thiệu về Photify")
    st.write("""
    Photify là một ứng dụng nghe nhạc trực tuyến miễn phí, cho phép người dùng lựa chọn nghệ sĩ yêu thích và thưởng thức các bài hát của họ thông qua các video nhạc được nhúng từ YouTube.

    Trong thời đại công nghệ số phát triển mạnh mẽ , việc tiếp cận âm nhạc trở nên dễ dàng hơn bao giờ hết. Tuy nhiên, giữa vô vàn các nền tảng nghe nhạc hiện nay, Photify nổi bật lên như một lựa chọn thân thiện, đơn giản và hiệu quả dành cho mọi đối tượng người dùng. Ứng dụng này được xây dựng dựa trên nền tảng Streamlit, một framework mạnh mẽ giúp tạo ra các ứng dụng web tương tác một cách dễ dàng và nhanh chóng. Nhờ đó, Photify không chỉ mang đến trải nghiệm nghe nhạc mượt mà mà còn giúp người dùng tương tác trực tiếp với giao diện, lựa chọn nghệ sĩ và bài hát yêu thích chỉ với vài thao tác đơn giản.

    Photify hướng tới mục tiêu trở thành cầu nối giữa người yêu nhạc và các nghệ sĩ nổi tiếng trên toàn thế giới. Ứng dụng cung cấp danh sách các nghệ sĩ đa dạng, từ những ban nhạc trẻ trung như Ngọt, những nghệ sĩ indie quốc tế như Hotel Ugly, cho đến các rapper đình đám như Kendrick Lamar. Mỗi nghệ sĩ đều có bộ sưu tập các video nhạc nổi bật, giúp người dùng dễ dàng khám phá và thưởng thức những ca khúc hay nhất của họ.

    Một trong những điểm mạnh của Photify là khả năng tích hợp trực tiếp các video nhạc từ YouTube. Điều này không chỉ giúp người dùng tiết kiệm thời gian tìm kiếm mà còn đảm bảo chất lượng âm thanh và hình ảnh luôn ở mức tốt nhất. Ngoài ra, việc sử dụng nguồn video chính thống từ YouTube cũng giúp bảo vệ quyền lợi của các nghệ sĩ, đảm bảo các sản phẩm âm nhạc được lan tỏa một cách hợp pháp và minh bạch.

    Photify còn chú trọng đến trải nghiệm người dùng thông qua giao diện trực quan, dễ sử dụng. Thanh sidebar cho phép lựa chọn nghệ sĩ nhanh chóng, các tab phân chia rõ ràng giữa trang chủ và phần giới thiệu, giúp người dùng dễ dàng chuyển đổi giữa các chức năng mà không gặp bất kỳ khó khăn nào. Đặc biệt, với thiết kế responsive, Photify có thể hoạt động tốt trên nhiều thiết bị khác nhau, từ máy tính cá nhân đến điện thoại di động, mang lại sự tiện lợi tối đa cho người dùng.

    Không chỉ dừng lại ở việc nghe nhạc, Photify còn hướng tới xây dựng một cộng đồng yêu âm nhạc sôi động. Trong tương lai, ứng dụng sẽ bổ sung các tính năng như bình luận, chia sẻ playlist, đánh giá bài hát và nghệ sĩ, giúp người dùng kết nối và trao đổi cảm nhận về âm nhạc một cách dễ dàng. Bên cạnh đó, Photify cũng sẽ mở rộng danh sách nghệ sĩ và bài hát, cập nhật liên tục các xu hướng âm nhạc mới nhất trên thế giới, đáp ứng nhu cầu thưởng thức đa dạng của người dùng.

    Photify cam kết mang đến cho người dùng những trải nghiệm âm nhạc tuyệt vời nhất. Đội ngũ phát triển luôn lắng nghe ý kiến đóng góp từ cộng đồng để cải thiện và nâng cấp ứng dụng từng ngày. Chúng tôi tin rằng âm nhạc là ngôn ngữ chung của nhân loại, là cầu nối giữa các nền văn hóa, là nguồn cảm hứng bất tận cho cuộc sống. Với Photify, bạn không chỉ được nghe nhạc mà còn được sống trong không gian âm nhạc đầy màu sắc, nơi mọi cảm xúc đều được thăng hoa.

    Hãy cùng Photify khám phá thế giới âm nhạc đa dạng, thưởng thức những ca khúc bất hủ và kết nối với cộng đồng yêu nhạc trên toàn cầu. Dù bạn là người yêu thích những giai điệu nhẹ nhàng, những bản rap sôi động hay những ca khúc indie độc đáo, Photify đều có thể đáp ứng mọi nhu cầu của bạn. Chúng tôi hy vọng Photify sẽ trở thành người bạn đồng hành thân thiết trên hành trình âm nhạc của bạn, mang lại những phút giây thư giãn, cảm xúc và sáng tạo không giới hạn.

    Để sử dụng Photify, bạn chỉ cần truy cập vào ứng dụng, lựa chọn nghệ sĩ yêu thích từ danh sách bên trái, và thưởng thức các video nhạc được hiển thị trên trang chủ. Mỗi nghệ sĩ đều có các bài hát nổi bật, được chọn lọc kỹ lưỡng để đảm bảo chất lượng và phù hợp với thị hiếu của người nghe. Ngoài ra, phần giới thiệu sẽ cung cấp cho bạn những thông tin hữu ích về ứng dụng, các tính năng mới, cũng như các hướng dẫn sử dụng chi tiết.

    Photify không ngừng đổi mới để đáp ứng nhu cầu ngày càng cao của người dùng. Chúng tôi luôn cập nhật các công nghệ mới nhất, tối ưu hóa hiệu suất và bảo mật, đảm bảo mọi dữ liệu cá nhân của người dùng đều được bảo vệ an toàn tuyệt đối. Đội ngũ hỗ trợ khách hàng của Photify luôn sẵn sàng giải đáp mọi thắc mắc, hỗ trợ bạn trong quá trình sử dụng ứng dụng.

    Trong tương lai, Photify sẽ mở rộng hợp tác với các nghệ sĩ, nhà sản xuất âm nhạc và các nền tảng truyền thông để mang đến nhiều nội dung phong phú hơn nữa. Chúng tôi cũng sẽ phát triển các tính năng thông minh như đề xuất bài hát dựa trên sở thích cá nhân, tạo playlist tự động, và tích hợp các công cụ chia sẻ lên mạng xã hội, giúp bạn dễ dàng lan tỏa niềm đam mê âm nhạc đến bạn bè và người thân.

    Âm nhạc là ngôn ngữ chung của nhân loại, là cầu nối giữa các nền văn hóa, là nguồn cảm hứng bất tận cho cuộc sống. Với Photify, bạn không chỉ được nghe nhạc mà còn được sống trong không gian âm nhạc đầy màu sắc, nơi mọi cảm xúc đều được thăng hoa.

    Cảm ơn bạn đã lựa chọn Photify. Chúng tôi hy vọng bạn sẽ có những trải nghiệm âm nhạc tuyệt vời, những phút giây thư giãn và những kỷ niệm đáng nhớ cùng ứng dụng của chúng tôi. Nếu có bất kỳ ý kiến đóng góp hoặc thắc mắc nào, đừng ngần ngại liên hệ với chúng tôi. Photify luôn sẵn sàng lắng nghe và phục vụ bạn!

    Chúc bạn có những trải nghiệm âm nhạc tuyệt vời với Photify!
    """)
with tab3:
    st.header("Dự đoán giờ đi ngủ")
    x = [
        [10, 1, 8],
        [20, 5, 6],
        [25, 8, 3],
        [30, 6, 5],
        [35, 2, 9],
        [40, 4, 3]
    ]
    y = [10, 8, 6, 7, 9.5, 9]
    model = LinearRegression()
    model.fit(x, y)
    st.write("Nhập các thông tin sau:")
    age = st.number_input("Tuổi", min_value=1, max_value=100, value=20, key="age_tab3")
    activity_level = st.slider("Mức độ hoạt động (giờ/ngày)", min_value=0, max_value=10, value=5, key="activity_tab3")
    screen_time = st.slider("Thời gian sử dụng thiết bị điện tử (giờ/ngày)", min_value=0, max_value=24, value=5, key="screen_time_tab3")

    if st.button("Dự đoán", key="predict_sleep"):
        input_data = [[age, activity_level, screen_time]]
        result = model.predict(input_data)
        st.success(f"Dự đoán giờ đi ngủ: {result[0]:.1f} giờ tối")
        if result[0] < 6.5:
            st.warning("Bạn nên đi ngủ sớm hơn để đảm bảo sức khỏe!")
        elif result[0] > 9:
            st.info("Bạn nên điều chỉnh lại thói quen sinh hoạt để có giấc ngủ tốt hơn!")
        else:
            st.success("Giờ đi ngủ của bạn khá hợp lý, hãy duy trì thói quen này!")

with tab10:
    st.header("Số bước chân cần đi trong một ngày")
    st.write("Nhập thông tin của bạn để tính số bước chân cần đi hàng ngày:")
    age_s = st.number_input("Tuổi", min_value=1, max_value=100, value=20, key="age_steps_tab")
    weight_s = st.number_input("Cân nặng (kg)", min_value=1.0, max_value=300.0, value=70.0, key="weight_steps_tab")
    activity_level_s = st.slider("Mức độ hoạt động (giờ/ngày)", min_value=0, max_value=10, value=5, key="activity_steps_tab")

    if st.button("Tính số bước chân", key="calc_steps"):
        base_steps = 5000  # base steps
        age_factor = max(0, (50 - age_s) * 50)  # decrease steps with age
        weight_factor = max(0, (100 - weight_s) * 20)  # decrease steps with weight
        activity_factor = activity_level_s * 1000  # increase steps with activity level
        total_steps = base_steps + age_factor + weight_factor + activity_factor
        st.success(f"Số bước chân bạn cần đi mỗi ngày là: {total_steps:.0f} bước")
        st.info("Hãy duy trì thói quen đi bộ để có sức khỏe tốt!")
with tab4:
    st.header("Liên hệ")
    st.write("Nếu bạn có bất kỳ câu hỏi hoặc góp ý nào, vui lòng liên hệ với chúng tôi qua email: nguyen3112012@gmail.com")
    st.write("Chúng tôi rất mong nhận được phản hồi từ bạn để cải thiện và phát triển ứng dụng ngày càng tốt hơn!")
    st.write("Cảm ơn bạn đã sử dụng Photify!")
    st.write("© 2024 Photify. All rights reserved.")
with tab6:
    st.header("Tin tức âm nhạc")
    tabA, tabB = st.tabs(["Tin tức âm nhạc", "Sport"])

    with tabA:
        feed = feedparser.parse("https://rss.app/feeds/InmZrDEBSInIRlqd.xml")
        if getattr(feed, "bozo", False):
            st.warning("Không thể tải feed âm nhạc. Kiểm tra kết nối hoặc thử lại.")
        elif not feed.entries:
            st.info("Feed âm nhạc rỗng. Thử nguồn thay thế:")
            alt = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/Arts.xml")
            if alt.entries:
                for entry in alt.entries[:5]:
                    st.subheader(entry.title)
                    if hasattr(entry, "published"):
                        st.write(entry.published)
                    st.write(entry.link)
            else:
                st.write("Không tìm thấy tin tức âm nhạc.")
        else:
            for entry in feed.entries[:5]:
                st.subheader(entry.title)
                if hasattr(entry, "published"):
                    st.write(entry.published)
                st.write(entry.link)

    with tabB:
        st.header("Sport")
        feed = feedparser.parse("https://www.espn.com/espn/rss/news")
        if getattr(feed, "bozo", False):
            st.warning("Không thể tải feed thể thao. Kiểm tra kết nối hoặc thử lại.")
        elif not feed.entries:
            st.write("Không tìm thấy tin tức thể thao trong feed này.")
        else:
            for entry in feed.entries[:5]:
                st.subheader(entry.title)
                if hasattr(entry, "published"):
                    st.write(entry.published)
                st.write(entry.link)
with tab7:
    st.header("Giá vàng hôm nay")
    
    feeds = feedparser.parse("https://vietnamnet.vn/rss/kinh-doanh.rss")
    gold_news = [entry for entry in feeds.entries if "vàng" in entry.title.lower() or "giá vàng" in entry.title.lower()]

    if gold_news:
        for entry in gold_news[:5]:
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)
    else:
        st.write("Không tìm thấy tin tức về giá vàng hôm nay.")
        st.write("Cảm ơn bạn đã quan tâm đến tin tức giá vàng trên Photify!")
with tab8:
    st.header("Kiểm tra chỉ số BMI")
    st.write("Nhập thông tin của bạn để tính chỉ số BMI:")
    weight = st.number_input("Cân nặng (kg)", min_value=1.0, max_value=300.0, value=70.0, key="weight_bmi_tab")
    height = st.number_input("Chiều cao (cm)", min_value=50.0, max_value=250.0, value=170.0, key="height_bmi_tab")
    bmi_min = 18.5
    bmi_max = 24.9
    weight_min = bmi_min * ((height / 100)**2)
    weight_max = bmi_max * ((height / 100)**2)
    if st.button("Tính BMI", key="calc_bmi"):
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        st.success(f"Chỉ số BMI của bạn là: {bmi:.2f}")
        if bmi < 18.5:
            st.warning("Bạn đang thiếu cân.")
            Tang_can = weight_min - weight
            st.write(f"Bạn nên tăng khoảng {Tang_can:.2f} kg để đạt cân nặng bình thường.")
        elif 18.5 <= bmi < 24.9:
            st.success("Bạn có cân nặng bình thường.")
        elif 25 <= bmi < 29.9:
            st.warning("Bạn đang thừa cân.")
            Giam_can = weight - weight_max
            st.write(f"Bạn nên giảm khoảng {Giam_can:.2f} kg để đạt cân nặng bình thường.")
        else:
            st.error("Bạn bị béo phì.")
            Giam_can = weight - weight_max
            st.write(f"Bạn nên giảm khoảng {Giam_can:.2f} kg để đạt cân nặng bình thường.")
with tab9:
    st.header("Lượng nước cần uống trong một ngày")
    st.write("Nhập thông tin của bạn để tính lượng nước cần uống hàng ngày:")
    weight_n = st.number_input(
        "Cân nặng (kg)",
        min_value=1.0,
        max_value=300.0,
        value=70.0,
        key="weight_water_tab"
    )
    activity_level_n = st.slider("Mức độ hoạt động (giờ/ngày)", min_value=0, max_value=10, value=5, key="activity_tab9")

    if st.button("Tính lượng nước", key="calc_water"):
        base_water = weight_n * 35  # ml
        additional_water = activity_level_n * 500  # ml
        total_water = (base_water + additional_water) / 1000  # liters
        st.success(f"Lượng nước bạn cần uống mỗi ngày là: {total_water:.2f} lít")
        st.info("Hãy nhớ uống đủ nước để duy trì sức khỏe tốt!")
with tab5:
    st.header("Shop")
    st.write("Chào mừng bạn đến với cửa hàng của chúng tôi!")
    st.write("Hiện tại, cửa hàng đang trong quá trình xây dựng. Vui lòng quay lại sau để khám phá các sản phẩm hấp dẫn và ưu đãi đặc biệt từ Photify.")
    st.write("Cảm ơn bạn đã quan tâm và ủng hộ chúng tôi!")
with tab11:
    st.title("Thời gian cần ngủ 1 ngày")
    tabA, tabB = st.tabs(["Trẻ con", "người lớn"])
    with tabA:
        thang = st.number_input("Nhập số tháng tuổi của bé:", min_value=0, max_value=24, value=12, key="months_tabA")
        if st.button('Tính thời gian đi ngủ theo tháng '):
            if thang < 4:
                st.info("Nên ngủ từ 14 đến 17 giờ mỗi ngày.")
            else:
                st.info("Nên ngủ từ 12 đến 15 giờ mỗi ngày.")
    with tabB:
        tuoi = st.number_input("Nhập tuổi của bạn:", min_value=1, max_value=100, value=25, key="age_tabB")
        if st.button('Tính thời gian cần ngủ'):
            if tuoi < 3:
                st.info("Nên ngủ từ 14 đến 17 giờ mỗi ngày.")
            elif tuoi < 6:
                st.info("Nên ngủ từ 10 đến 14 giờ mỗi ngày.")
            elif tuoi < 14:
                st.info("Nên ngủ từ 9 đến 11 giờ mỗi ngày.")
            elif tuoi < 18:
                st.info("Nên ngủ từ 8 đến 10 giờ mỗi ngày.")
            elif tuoi < 65:
                st.info("Nên ngủ từ 7 đến 9 giờ mỗi ngày.")
            else:
                st.info("Nên ngủ từ 7 đến 8 giờ mỗi ngày.")
