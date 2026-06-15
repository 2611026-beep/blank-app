import streamlit as plt
import streamlit as st

# 1. 데이터 정의
artworks = ["수련", "피리부는 소년", "발레수업", "태양"]
artists = ["클로드 모네", "에두아르 마네", "에드가 드가", "에드바르 뭉크"]
descriptions = [
    "빛과 시간을 담은 작품",
    "전통 원근법에서 벗어나 강조와 실사감을 표현한 작품",
    "무대위 화려함이 아닌 뒷편의 어린 발레리나들을 담아낸 작품",
    "강렬한 색체로 빛을 표현한 작품",
]

# 2. 웹 페이지 제목 및 안내
st.title("🎨 명화 전시관 안내")
st.subheader("전시 작품 목록")

# 사용자가 직관적으로 선택할 수 있도록 작품 이름으로 셀렉트박스 생성
# (기존의 번호 입력 방식보다 웹에서 훨씬 편리합니다!)
selected_artwork = st.selectbox(
    "상세 정보를 보고 싶은 작품을 선택하세요:",
    artworks,
    index=None,
    placeholder="작품을 선택해 주세요...",
)

st.markdown("---")

# 3. 결과 출력 로직
if selected_artwork:
    # 선택한 작품의 인덱스(위치) 찾기
    idx = artworks.index(selected_artwork)

    # 정보 출력
    st.success(f"**🖼️ 작품명:** {artworks[idx]}")
    st.info(f"**👨‍🎨 작가:** {artists[idx]}")

    st.write("**📝 작품 설명:**")
    st.write(descriptions[idx])

else:
    st.warning("작품을 선택하시면 상세 정보가 표시됩니다.")