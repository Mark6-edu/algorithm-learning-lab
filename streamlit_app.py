import streamlit as st

from utils.ui import (
    load_css,
    render_html,
)


# =========================================================
# 페이지 기본 설정
# =========================================================
st.set_page_config(
    page_title="Algorithm Design Learning Lab",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# CSS 불러오기
# =========================================================
load_css("assets/style.css")


# =========================================================
# 임시 사용자 정보
# 추후 Google 로그인과 연동 예정
# =========================================================
if "user_role" not in st.session_state:
    st.session_state.user_role = None

if "user_name" not in st.session_state:
    st.session_state.user_name = None

if "progress" not in st.session_state:
    st.session_state.progress = 0


# =========================================================
# 사이드바
# =========================================================
with st.sidebar:

    render_html(
        """
        <div class="sidebar-logo">

            <div class="sidebar-logo-icon">
                🧠
            </div>

            <div>
                <div class="sidebar-logo-title">
                    Algorithm Design
                </div>

                <div class="sidebar-logo-subtitle">
                    Learning Lab
                </div>
            </div>

        </div>
        """
    )

    st.markdown("---")

    st.markdown("### 📚 학습 메뉴")

    if st.button(
        "🏠 홈",
        use_container_width=True,
        type="primary",
    ):
        st.switch_page(
            "streamlit_app.py"
        )

    render_html(
        """
        <div class="sidebar-unit disabled">

            <span>
                Ⅰ
            </span>

            <div>
                <strong>
                    알고리즘과 문제 해결
                </strong>

                <small>
                    준비 중
                </small>
            </div>

        </div>
        """
    )

    if st.button(
        "Ⅱ  추상화와 모델링",
        use_container_width=True,
    ):
        st.switch_page(
            "pages/02_2단원.py"
        )

    render_html(
        """
        <div class="sidebar-unit disabled">

            <span>
                Ⅲ
            </span>

            <div>
                <strong>
                    알고리즘 설계 전략
                </strong>

                <small>
                    준비 중
                </small>
            </div>

        </div>

        <div class="sidebar-unit disabled">

            <span>
                Ⅳ
            </span>

            <div>
                <strong>
                    알고리즘 구현
                </strong>

                <small>
                    준비 중
                </small>
            </div>

        </div>

        <div class="sidebar-unit disabled">

            <span>
                Ⅴ
            </span>

            <div>
                <strong>
                    알고리즘 응용
                </strong>

                <small>
                    준비 중
                </small>
            </div>

        </div>
        """
    )

    st.markdown("---")

    st.markdown("### 📊 학습 관리")

    st.button(
        "📈 학습 대시보드",
        disabled=True,
        use_container_width=True,
    )

    st.button(
        "👨‍🏫 교사 대시보드",
        disabled=True,
        use_container_width=True,
    )

    st.markdown("---")

    st.caption(
        "고등학교 알고리즘 설계\n\n"
        "Python 기반 학습 플랫폼"
    )


# =========================================================
# 상단 헤더
# =========================================================
header_left, header_right = st.columns(
    [7, 3],
    vertical_alignment="center",
)


with header_left:

    render_html(
        """
        <div class="main-title-area">

            <div class="main-title-eyebrow">
                ALGORITHM DESIGN
            </div>

            <h1>
                Algorithm Design Learning Lab
            </h1>

            <p>
                알고리즘 설계 · Python 기반 학습 플랫폼
            </p>

        </div>
        """
    )


with header_right:

    render_html(
        """
        <div class="login-card">

            <div class="login-icon">
                👤
            </div>

            <div class="login-content">

                <strong>
                    로그인이 필요합니다
                </strong>

                <span>
                    Google 계정 로그인 기능은<br>
                    추후 연결 예정입니다.
                </span>

            </div>

        </div>
        """
    )


# =========================================================
# Hero 영역
# =========================================================
render_html(
    """
    <div class="hero-section">

        <div class="hero-content">

            <div class="hero-tag">
                🐍 Python Algorithm Learning
            </div>

            <h2>
                문제를 이해하고,<br>
                알고리즘으로 설계하고,<br>
                Python으로 구현합니다.
            </h2>

            <p>
                교과서 개념 학습부터 알고리즘 설계,
                Python 실습과 형성평가까지
                하나의 웹 앱에서 단계적으로 학습합니다.
            </p>

        </div>

        <div class="hero-visual">

            <div class="code-window">

                <div class="code-window-header">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>

                <pre><span class="code-comment"># 최댓값 찾기</span>

numbers = [3, 7, 2, 9, 5]

max_value = numbers[0]

<span class="code-keyword">for</span> number <span class="code-keyword">in</span> numbers:
    <span class="code-keyword">if</span> number &gt; max_value:
        max_value = number

<span class="code-function">print</span>(max_value)</pre>

            </div>

        </div>

    </div>
    """
)


# =========================================================
# 진행률
# =========================================================
render_html(
    """
    <div class="section-header">

        <div>

            <div class="section-label">
                MY LEARNING
            </div>

            <h3>
                나의 학습 현황
            </h3>

        </div>

    </div>
    """
)


progress_col1, progress_col2 = st.columns(
    [3, 1],
    vertical_alignment="center",
)


with progress_col1:

    render_html(
        """
        <div class="progress-wrapper">

            <div class="progress-header">

                <span>
                    전체 학습 진행률
                </span>

                <strong>
                    0%
                </strong>

            </div>

            <div class="progress-track">

                <div
                    class="progress-bar"
                    style="width:0%;">
                </div>

            </div>

            <div class="progress-description">
                아직 학습을 시작하지 않았습니다.
            </div>

        </div>
        """
    )


with progress_col2:

    render_html(
        """
        <div class="progress-summary">

            <div>

                <strong>
                    0
                </strong>

                <span>
                    완료 학습
                </span>

            </div>

            <div>

                <strong>
                    5
                </strong>

                <span>
                    전체 단원
                </span>

            </div>

        </div>
        """
    )


# =========================================================
# 단원별 학습
# =========================================================
render_html(
    """
    <div class="section-header section-space">

        <div>

            <div class="section-label">
                CURRICULUM
            </div>

            <h3>
                단원별 학습
            </h3>

            <p>
                각 단원을 순서대로 학습하며
                알고리즘 설계 능력을 키워봅시다.
            </p>

        </div>

    </div>
    """
)


# =========================================================
# 단원 카드 함수
# =========================================================
def unit_card(
    number,
    title,
    description,
    status,
    enabled=False,
):

    status_class = (
        "active"
        if enabled
        else "ready"
    )

    render_html(
        f"""
        <div class="unit-card {status_class}">

            <div class="unit-card-top">

                <div class="unit-number">
                    {number}
                </div>

                <div class="unit-status">
                    {status}
                </div>

            </div>

            <h3>
                {title}
            </h3>

            <p>
                {description}
            </p>

        </div>
        """
    )

    if enabled:

        if st.button(
            "학습 시작하기  →",
            key=f"unit_{number}",
            use_container_width=True,
            type="primary",
        ):
            st.switch_page(
                "pages/02_2단원.py"
            )

    else:

        st.button(
            "준비 중",
            key=f"unit_{number}",
            disabled=True,
            use_container_width=True,
        )


# =========================================================
# 1 ~ 3단원
# =========================================================
unit_cols = st.columns(3)


with unit_cols[0]:

    unit_card(
        "Ⅰ",
        "알고리즘과 문제 해결",
        """
        알고리즘의 개념과
        문제 해결 과정을 이해합니다.
        """,
        "준비 중",
    )


with unit_cols[1]:

    unit_card(
        "Ⅱ",
        "추상화와 모델링",
        """
        복잡한 문제를 분석하고
        해결 가능한 형태로
        모델링합니다.
        """,
        "학습 가능",
        True,
    )


with unit_cols[2]:

    unit_card(
        "Ⅲ",
        "알고리즘 설계 전략",
        """
        다양한 알고리즘
        설계 전략과 문제 해결
        방법을 학습합니다.
        """,
        "준비 중",
    )


# =========================================================
# 4 ~ 5단원
# =========================================================
unit_cols2 = st.columns(2)


with unit_cols2[0]:

    unit_card(
        "Ⅳ",
        "알고리즘 구현",
        """
        설계한 알고리즘을
        Python 프로그램으로
        구현합니다.
        """,
        "준비 중",
    )


with unit_cols2[1]:

    unit_card(
        "Ⅴ",
        "알고리즘 응용",
        """
        학습한 알고리즘을
        다양한 실제 문제에
        적용합니다.
        """,
        "준비 중",
    )


# =========================================================
# 학습 방식 안내
# =========================================================
render_html(
    """
    <div class="section-header section-space">

        <div>

            <div class="section-label">
                LEARNING FLOW
            </div>

            <h3>
                이렇게 학습합니다
            </h3>

        </div>

    </div>
    """
)


flow_cols = st.columns(5)

learning_flow = [
    (
        "01",
        "📘",
        "개념 학습",
        "교과서 핵심 개념을 이해합니다.",
    ),
    (
        "02",
        "🧠",
        "문제 분석",
        "입력·출력과 해결 조건을 분석합니다.",
    ),
    (
        "03",
        "🧩",
        "알고리즘 설계",
        "해결 절차를 단계적으로 설계합니다.",
    ),
    (
        "04",
        "🐍",
        "Python 실습",
        "알고리즘을 코드로 구현합니다.",
    ),
    (
        "05",
        "📝",
        "형성평가",
        "학습 내용을 스스로 점검합니다.",
    ),
]


for col, (
    step,
    icon,
    title,
    description,
) in zip(
    flow_cols,
    learning_flow,
):

    with col:

        render_html(
            f"""
            <div class="learning-flow-card">

                <div class="flow-step">
                    STEP {step}
                </div>

                <div class="flow-icon">
                    {icon}
                </div>

                <h4>
                    {title}
                </h4>

                <p>
                    {description}
                </p>

            </div>
            """
        )


# =========================================================
# Colab 안내
# =========================================================
render_html(
    """
    <div class="colab-banner">

        <div>

            <div class="section-label">
                PYTHON PRACTICE
            </div>

            <h3>
                웹 앱에서 배우고,
                Google Colab에서 직접 코딩합니다.
            </h3>

            <p>
                각 학습 활동에서 Python 코드를 확인하고
                Colab 실습 노트북으로 연결하여
                직접 알고리즘을 구현할 수 있도록 구성할 예정입니다.
            </p>

        </div>

        <div class="colab-logo">
            ☁️
        </div>

    </div>
    """
)


# =========================================================
# Footer
# =========================================================
render_html(
    """
    <div class="app-footer">

        <strong>
            Algorithm Design Learning Lab
        </strong>

        <span>
            고등학교 알고리즘 설계 · Python Learning Platform
        </span>

    </div>
    """
)