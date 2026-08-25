import streamlit as st

from utils.ui import (
    load_css,
    render_html,
)


# =========================================================
# 페이지 설정
# =========================================================
st.set_page_config(
    page_title="1단원 알고리즘 개요",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_css("assets/style.css")


# =========================================================
# 세션 상태
# =========================================================
if "unit1_progress" not in st.session_state:
    st.session_state.unit1_progress = {
        "1-1": False,
        "1-2": False,
        "1-3": False,
    }


# =========================================================
# 진행률 계산
# =========================================================
completed_count = sum(
    st.session_state.unit1_progress.values()
)

total_count = len(
    st.session_state.unit1_progress
)

progress = int(
    completed_count / total_count * 100
)


# =========================================================
# Sidebar
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

    st.markdown("### Ⅰ. 알고리즘 개요")

    if st.button(
        "1-1  알고리즘 개념",
        use_container_width=True,
    ):
        st.switch_page(
            "pages/01_01_알고리즘개념.py"
        )

    if st.button(
        "1-2  알고리즘 표현 방법",
        use_container_width=True,
    ):
        st.switch_page(
            "pages/01_02_알고리즘표현방법.py"
        )

    if st.button(
        "1-3  자료 구조와 알고리즘",
        use_container_width=True,
    ):
        st.switch_page(
            "pages/01_03_자료구조와알고리즘.py"
        )

    st.markdown("---")

    if st.button(
        "Ⅱ  추상화와 모델링",
        use_container_width=True,
    ):
        st.switch_page(
            "pages/02_2단원.py"
        )

    st.markdown("---")

    if st.button(
        "🏠 메인 화면",
        use_container_width=True,
    ):
        st.switch_page(
            "streamlit_app.py"
        )

    st.markdown("---")

    st.caption(
        "Algorithm Design Learning Lab\n\n"
        "Python 기반 알고리즘 학습"
    )


# =========================================================
# Breadcrumb
# =========================================================
render_html(
    """
    <div class="app-breadcrumb">
        홈 &nbsp;›&nbsp;
        Ⅰ. 알고리즘 개요
    </div>
    """
)


# =========================================================
# Hero
# =========================================================
render_html(
    """
    <div class="hero-section">

        <div class="hero-content">

            <div class="hero-tag">
                UNIT Ⅰ
            </div>

            <h2>
                알고리즘 개요
            </h2>

            <p>
                알고리즘이 무엇인지 이해하고,
                문제 해결 절차를 다양한 방법으로 표현해 봅니다.
                <br><br>
                또한 자료 구조와 알고리즘이 어떤 관계를 가지는지
                간단한 예제를 통해 살펴봅니다.
            </p>

        </div>

        <div class="hero-visual">

            <div class="code-window">

                <div class="code-window-header">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>

                <pre>문제
 ↓
해결 절차
 ↓
알고리즘
 ↓
표현
 ↓
프로그램</pre>

            </div>

        </div>

    </div>
    """
)


# =========================================================
# 학습 목표
# =========================================================
render_html(
    """
    <div class="section-header">

        <div>

            <div class="section-label">
                LEARNING GOALS
            </div>

            <h3>
                1단원에서 무엇을 배울까요?
            </h3>

            <p>
                알고리즘 학습을 시작하기 위한
                가장 기본적인 개념을 익힙니다.
            </p>

        </div>

    </div>
    """
)


goal_cols = st.columns(3)

goals = [
    (
        "🧠",
        "알고리즘 이해",
        "알고리즘의 의미와 중요성을 설명할 수 있습니다.",
    ),
    (
        "📝",
        "알고리즘 표현",
        "자연어, 의사코드, 순서도를 이해할 수 있습니다.",
    ),
    (
        "🗂️",
        "자료 구조와 연결",
        "자료 구조와 알고리즘의 관계를 이해할 수 있습니다.",
    ),
]

for col, (
    icon,
    title,
    description,
) in zip(
    goal_cols,
    goals,
):

    with col:

        render_html(
            f"""
            <div class="learning-flow-card">

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
# 진행률
# =========================================================
render_html(
    """
    <div class="section-header section-space">

        <div>

            <div class="section-label">
                MY PROGRESS
            </div>

            <h3>
                1단원 학습 진행률
            </h3>

        </div>

    </div>
    """
)


st.progress(
    progress / 100
)

st.caption(
    f"{completed_count} / {total_count} 학습 완료 · {progress}%"
)


# =========================================================
# 소단원
# =========================================================
render_html(
    """
    <div class="section-header section-space">

        <div>

            <div class="section-label">
                LESSONS
            </div>

            <h3>
                학습할 내용을 선택하세요
            </h3>

        </div>

    </div>
    """
)


lesson_cols = st.columns(3)


# ---------------------------------------------------------
# 1-1
# ---------------------------------------------------------
with lesson_cols[0]:

    status_1 = (
        "✅ 학습 완료"
        if st.session_state.unit1_progress["1-1"]
        else "학습 전"
    )

    render_html(
        f"""
        <div class="learning-flow-card">

            <div class="flow-step">
                LESSON 01
            </div>

            <div class="flow-icon">
                🧠
            </div>

            <h4>
                알고리즘 개념
            </h4>

            <p>
                알고리즘의 의미와 특징,
                알고리즘이 중요한 이유를 알아봅니다.
            </p>

            <small>
                {status_1}
            </small>

        </div>
        """
    )

    if st.button(
        "1-1 학습하기 →",
        key="unit1_lesson1",
        use_container_width=True,
        type="primary",
    ):

        st.switch_page(
            "pages/01_01_알고리즘개념.py"
        )


# ---------------------------------------------------------
# 1-2
# ---------------------------------------------------------
with lesson_cols[1]:

    status_2 = (
        "✅ 학습 완료"
        if st.session_state.unit1_progress["1-2"]
        else "학습 전"
    )

    render_html(
        f"""
        <div class="learning-flow-card">

            <div class="flow-step">
                LESSON 02
            </div>

            <div class="flow-icon">
                📝
            </div>

            <h4>
                알고리즘 표현 방법
            </h4>

            <p>
                자연어, 의사코드, 순서도를 이용하여
                문제 해결 절차를 표현합니다.
            </p>

            <small>
                {status_2}
            </small>

        </div>
        """
    )

    if st.button(
        "1-2 학습하기 →",
        key="unit1_lesson2",
        use_container_width=True,
        type="primary",
    ):

        st.switch_page(
            "pages/01_02_알고리즘표현방법.py"
        )


# ---------------------------------------------------------
# 1-3
# ---------------------------------------------------------
with lesson_cols[2]:

    status_3 = (
        "✅ 학습 완료"
        if st.session_state.unit1_progress["1-3"]
        else "학습 전"
    )

    render_html(
        f"""
        <div class="learning-flow-card">

            <div class="flow-step">
                LESSON 03
            </div>

            <div class="flow-icon">
                🗂️
            </div>

            <h4>
                자료 구조와 알고리즘
            </h4>

            <p>
                데이터를 저장하는 방법과
                알고리즘의 관계를 살펴봅니다.
            </p>

            <small>
                {status_3}
            </small>

        </div>
        """
    )

    if st.button(
        "1-3 학습하기 →",
        key="unit1_lesson3",
        use_container_width=True,
        type="primary",
    ):

        st.switch_page(
            "pages/01_03_자료구조와알고리즘.py"
        )


# =========================================================
# 전체 학습 흐름
# =========================================================
render_html(
    """
    <div class="section-header section-space">

        <div>

            <div class="section-label">
                LEARNING FLOW
            </div>

            <h3>
                1단원 학습 흐름
            </h3>

        </div>

    </div>
    """
)


flow_cols = st.columns(4)

flow_data = [
    (
        "01",
        "🧠",
        "개념 이해",
        "알고리즘이 무엇인지 알아봅니다.",
    ),
    (
        "02",
        "📝",
        "표현 방법",
        "해결 절차를 여러 방식으로 표현합니다.",
    ),
    (
        "03",
        "🗂️",
        "자료 구조",
        "데이터와 알고리즘의 관계를 이해합니다.",
    ),
    (
        "04",
        "✅",
        "형성평가",
        "핵심 내용을 간단히 확인합니다.",
    ),
]

for col, (
    step,
    icon,
    title,
    description,
) in zip(
    flow_cols,
    flow_data,
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
# 다음 단원 안내
# =========================================================
st.markdown("---")

if completed_count == total_count:

    st.success(
        """
        🎉 1단원 학습을 모두 완료했습니다!

        이제 **Ⅱ. 추상화와 모델링**으로 이동해
        실제 문제 해결 과정을 학습해 봅시다.
        """
    )

    if st.button(
        "Ⅱ. 추상화와 모델링 시작하기 →",
        use_container_width=True,
        type="primary",
    ):

        st.switch_page(
            "pages/02_2단원.py"
        )

else:

    st.info(
        """
        1-1부터 1-3까지 순서대로 학습해 보세요.
        각 소단원의 형성평가를 완료하면 진행률이 올라갑니다.
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
            Ⅰ. 알고리즘 개요
        </span>

    </div>
    """
)