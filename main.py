import streamlit as st

# --- 1. MBTI 유형별 직업 추천 데이터 정의 (이전과 동일) ---
mbti_career_map = {
    "ISTJ": ["행정직", "회계사", "공무원", "데이터 분석가", "경찰관"],
    "ISFJ": ["간호사", "유치원 교사", "사회복지사", "사서", "행정직원"],
    "INFJ": ["상담사", "작가", "심리학자", "예술가", "교사"],
    "INTJ": ["과학자", "연구원", "시스템 분석가", "전략 기획가", "엔지니어"],
    "ISTP": ["엔지니어", "정비사", "스포츠 선수", "기술자", "경찰/소방관"],
    "ISFP": ["예술가", "디자이너", "음악가", "요리사", "수의사"],
    "INFP": ["작가", "예술가", "상담사", "심리학자", "사회 운동가"],
    "INTP": ["과학자", "프로그래머", "교수", "발명가", "철학자"],
    "ESTP": ["영업", "기업가", "응급 구조사", "경찰관", "군인"],
    "ESFP": ["연예인", "활동가", "파티 플래너", "어린이집 교사", "스포츠 코치"],
    "ENFP": ["상담사", "마케터", "배우", "작가", "컨설턴트"],
    "ENTP": ["기업가", "변호사", "컨설턴트", "발명가", "대학교수"],
    "ESTJ": ["경영자", "관리자", "공무원", "영업 관리", "군 장교"],
    "ESFJ": ["교사", "간호사", "사회복지사", "HR 전문가", "종교 지도자"],
    "ENFJ": ["교사", "상담사", "리더", "인사 담당자", "코치"],
    "ENTJ": ["경영 컨설턴트", "기업가", "변호사", "정치가", "CEO"],
}

# MBTI 특징에 대한 간략한 설명 (이전과 동일)
mbti_descriptions = {
    "ISTJ": "논리적이고 현실적이며 책임감이 강하고 신중합니다.",
    "ISFJ": "헌신적이고 따뜻하며 책임감이 강하고 성실합니다.",
    "INFJ": "통찰력이 있고 영감을 주는 이상주의자이며 조용하고 신비로운 면이 있습니다.",
    "INTJ": "독립적이고 전략적이며 분석적인 사고를 하는 비전가입니다.",
    "ISTP": "논리적이고 현실적이며 호기심이 많고 문제 해결에 능합니다.",
    "ISFP": "겸손하고 예술적이며 호기심이 많고 따뜻한 마음을 가졌습니다.",
    "INFP": "이상주의적이고 창의적이며 공감능력이 뛰어나고 진정성을 추구합니다.",
    "INTP": "논리적이고 분석적이며 지적 호기심이 많고 비판적 사고를 합니다.",
    "ESTP": "활동적이고 현실적이며 유연하고 위기 대처에 능합니다.",
    "ESFP": "활동적이고 사교적이며 낙천적이고 즐거움을 추구합니다.",
    "ENFP": "열정적이고 창의적이며 사교적이고 영감이 넘칩니다.",
    "ENTP": "논리적이고 독창적이며 토론을 즐기고 새로운 아이디어에 흥미를 느낍니다.",
    "ESTJ": "실용적이고 현실적이며 체계적이고 리더십이 강합니다.",
    "ESFJ": "사교적이고 친절하며 협조적이고 타인의 필요에 민감합니다.",
    "ENFJ": "열정적이고 카리스마 있으며 타인을 돕고 이끄는 데 능숙합니다.",
    "ENTJ": "결단력 있고 논리적이며 목표 지향적이고 타고난 리더입니다."
}


# --- 2. Streamlit 웹 앱 레이아웃 설정 ---

st.set_page_config(
    page_title="🌈 MBTI 성격 유형별 맞춤 진로 가이드 📚", # 웹 브라우저 탭 제목
    page_icon="✨", # 웹 브라우저 탭 아이콘
    layout="centered" # 페이지 레이아웃을 중앙 정렬
)

# 상단 배너 이미지 (이미지 파일 경로를 여기에 넣어주세요! 예: "images/banner.png")
# 이미지 파일이 현재 스크립트 파일과 같은 폴더에 있다면 파일 이름만 적으셔도 됩니다.
# st.image("banner_image.jpg", use_column_width=True) # 적절한 이미지가 있다면 주석 해제하고 사용하세요.
st.image("https://images.unsplash.com/photo-1543269865-cbf427311029?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", use_column_width=True, caption="나의 재능과 열정을 찾아 떠나는 진로 여행!") # 예시 이미지 URL

st.title("💖 MBTI 성격 유형별 맞춤 진로 가이드 📖")
st.write("나의 MBTI 유형을 선택하고, 숨겨진 나의 잠재력을 발견해봐요! ✨")
st.markdown("---") # 구분선

# MBTI 유형 드롭다운 목록
mbti_types = sorted(list(mbti_career_map.keys())) # MBTI 유형을 알파벳 순으로 정렬

# 사용자에게 MBTI 유형 선택받기
selected_mbti = st.selectbox(
    "🧐 **나의 MBTI 유형은 무엇인가요?**", # Selectbox 제목
    mbti_types,
    index=None, # 초기 선택 없음
    placeholder="👇 여기에 당신의 MBTI를 선택해주세요! 😊" # 힌트 텍스트
)

st.markdown("---") # 구분선

# '직업 추천 받기' 버튼
if st.button("🌟 직업 추천 받기! 나에게 딱 맞는 길은? 🚀", use_container_width=True):
    if selected_mbti:
        recommended_careers = mbti_career_map.get(selected_mbti, ["추천할 직업 정보를 찾을 수 없습니다."])
        
        st.subheader(f"✅ **{selected_mbti}** 유형을 위한 추천 직업들이에요! 🎉")
        
        # MBTI 특징 설명 부분을 expander로 깔끔하게 정리
        with st.expander(f"✨ **{selected_mbti} 유형의 특징 자세히 알아보기**"):
            st.info(mbti_descriptions.get(selected_mbti, "이 유형에 대한 설명은 아직 준비되지 않았습니다."))
        
        st.success("👇 아래 직업들을 살펴보시고, 당신의 꿈을 키워나가세요! 💡")
        
        # 추천 직업 리스트 출력
        for i, career in enumerate(recommended_careers):
            st.write(f"**{i+1}. {career}**")
            
        st.markdown("<br>", unsafe_allow_html=True) # 공백 라인 추가
        st.warning("⚠️ **주의사항**: 이 추천은 일반적인 경향성을 기반으로 합니다. 모든 정보는 참고용이며, 가장 중요한 것은 **당신의 진정한 흥미와 재능**이라는 것을 잊지 마세요! ")
    else:
        st.error("🚨 잠시만요! MBTI 유형을 먼저 선택해주셔야 추천해 드릴 수 있어요. 위에서 MBTI를 골라주세요! 🙏")

st.markdown("---") # 하단 구분선
st.caption("©️ 2025 MBTI 진로 가이드 by 감자") # 저작권 표시 (재미로 추가해봤어요!)
