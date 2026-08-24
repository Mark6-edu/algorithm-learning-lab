import streamlit as st

from utils.ui import (
    load_css,
    render_html,
)


# =========================================================
# 페이지 설정
# =========================================================
st.set_page_config(
    page_title="Ⅱ. 추상화와 모델링",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_css("assets/style.css")


# =========================================================
# 세션 상태 초기화
# =========================================================
if "unit2_progress" not in st.session_state:
    st.session_state.unit2_progress = {
        "2-1": False,
        "2-2": False,
        "2-3": False,
        "2-4": False,
    }

if "lesson_2_1_score" not in st.session_state:
    st.session_state.lesson_2_1_score = None

if "lesson_2_2_score" not in st.session_state:
    st.session_state.lesson_2_2_score = None

if "lesson_2_3_score" not in st.session_state:
    st.session_state.lesson_2_3_score = None

if "lesson_2_4_score" not in st.session_state:
    st.session_state.lesson_2_4_score = None


# =========================================================
# 단원 진행률 계산
# =========================================================
unit2_progress = st.session_state.unit2_progress

completed_count = sum(unit2_progress.values())
total_count = len(unit2_progress)

progress_percent = int(
    completed_count / total_count * 100
)

unit2_completed = all(
    unit2_progress.values()
)


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

    st.button(
        "Ⅱ  추상화와 모델링",
        type="primary",
        use_container_width=True,
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

    st.markdown("### 📊 2단원 진행")

    st.progress(
        progress_percent / 100
    )

    st.caption(
        f"{completed_count} / {total_count} 학습 완료"
    )

    st.markdown("---")

    st.caption(
        "고등학교 알고리즘 설계\n\n"
        "Python 기반 학습 플랫폼"
    )


# =========================================================
# Breadcrumb
# =========================================================
render_html(
    """
    <div class="app-breadcrumb">
        홈 &nbsp;›&nbsp; Ⅱ. 추상화와 모델링
    </div>
    """
)


# =========================================================
# 단원 Hero
# =========================================================
render_html(
    """
    <div class="hero-section">

        <div class="hero-content">

            <div class="hero-tag">
                UNIT Ⅱ
            </div>

            <h2>
                추상화와 모델링
            </h2>

            <p>
                복잡한 문제를 정확하게 이해하고,
                작은 문제로 나눈 뒤 핵심 요소를 추출하여
                해결 가능한 형태로 모델링합니다.
                <br><br>
                이후 해결 절차를 알고리즘으로 설계하고,
                알고리즘의 효율성을 분석하는 과정을 학습합니다.
            </p>

        </div>

        <div class="hero-visual">

            <div class="code-window">

                <div class="code-window-header">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>

                <pre>문제 이해
    ↓
문제 분석
    ↓
문제 분해
    ↓
추상화 · 모델링
    ↓
알고리즘 설계
    ↓
성능 분석</pre>

            </div>

        </div>

    </div>
    """
)


# =========================================================
# 단원 학습 목표
# =========================================================
render_html(
    """
    <div class="section-header">

        <div>

            <div class="section-label">
                LEARNING GOALS
            </div>

            <h3>
                이 단원에서 무엇을 배우나요?
            </h3>

            <p>
                문제를 분석하고 해결 가능한 형태로 바꾸는
                알고리즘 설계의 기본 과정을 학습합니다.
            </p>

        </div>

    </div>
    """
)


goal_cols = st.columns(4)

goal_data = [
    (
        "🔎",
        "문제 분석",
        """
        현재 상태와 목표 상태를 파악하고
        필요한 작업을 분석합니다.
        """,
    ),
    (
        "🧩",
        "문제 분해",
        """
        복잡한 문제를 작은 문제로
        나누어 해결하기 쉽게 만듭니다.
        """,
    ),
    (
        "🗺️",
        "추상화와 모델링",
        """
        문제 해결에 필요한 핵심 요소만
        추출하여 구조화합니다.
        """,
    ),
    (
        "📊",
        "성능 분석",
        """
        입력 크기와 수행 횟수를 통해
        알고리즘의 효율성을 비교합니다.
        """,
    ),
]

for col, data in zip(
    goal_cols,
    goal_data,
):

    icon, title, description = data

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
# 단원 진행률
# =========================================================
render_html(
    """
    <div class="section-header section-space">

        <div>

            <div class="section-label">
                PROGRESS
            </div>

            <h3>
                2단원 학습 진행률
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

    if progress_percent == 0:
        progress_message = (
            "아직 학습을 시작하지 않았습니다."
        )

    elif progress_percent < 100:
        progress_message = (
            "좋습니다! 남은 학습도 계속 진행해 봅시다."
        )

    else:
        progress_message = (
            "2단원의 모든 학습을 완료했습니다."
        )

    render_html(
        f"""
        <div class="progress-wrapper">

            <div class="progress-header">

                <span>
                    단원 학습 진행률
                </span>

                <strong>
                    {progress_percent}%
                </strong>

            </div>

            <div class="progress-track">

                <div
                    class="progress-bar"
                    style="width:{progress_percent}%;">
                </div>

            </div>

            <div class="progress-description">
                {progress_message}
            </div>

        </div>
        """
    )


with progress_col2:

    render_html(
        f"""
        <div class="progress-summary">

            <div>

                <strong>
                    {completed_count}
                </strong>

                <span>
                    완료
                </span>

            </div>

            <div>

                <strong>
                    {total_count}
                </strong>

                <span>
                    전체 학습
                </span>

            </div>

        </div>
        """
    )


# =========================================================
# 전체 완료 안내
# =========================================================
if unit2_completed:

    st.success(
        """
        🎉 **Ⅱ. 추상화와 모델링 단원을 모두 완료했습니다!**

        문제 이해 → 문제 분해 → 추상화와 모델링 →
        알고리즘 설계 → 성능 분석의 전체 흐름을 학습했습니다.
        """
    )


# =========================================================
# 소단원 학습 로드맵
# =========================================================
render_html(
    """
    <div class="section-header section-space">

        <div>

            <div class="section-label">
                UNIT ROADMAP
            </div>

            <h3>
                학습 순서
            </h3>

            <p>
                각 학습을 순서대로 진행하며
                알고리즘 설계의 기본 과정을 익혀봅시다.
            </p>

        </div>

    </div>
    """
)


# =========================================================
# 학습 카드 함수
# =========================================================
def lesson_card(
    lesson_no,
    title,
    description,
    icon,
    page,
    completed=False,
    score=None,
):

    if completed:
        card_class = "active"
        status = "✓ 완료"

    else:
        card_class = "active"
        status = "학습 가능"

    render_html(
        f"""
        <div class="unit-card {card_class}">

            <div class="unit-card-top">

                <div class="unit-number">
                    {lesson_no}
                </div>

                <div class="unit-status">
                    {status}
                </div>

            </div>

            <div style="
                font-size:32px;
                margin-bottom:14px;
            ">
                {icon}
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

    if score is not None:

        st.caption(
            f"📝 최근 형성평가: {score} / 5점"
        )

    button_label = (
        "다시 학습하기  →"
        if completed
        else "학습 시작하기  →"
    )

    if st.button(
        button_label,
        key=f"lesson_{lesson_no}",
        use_container_width=True,
        type="primary",
    ):

        st.switch_page(
            page
        )


# =========================================================
# 2-1 / 2-2
# =========================================================
row1 = st.columns(2)


with row1[0]:

    lesson_card(
        lesson_no="2-1",
        title="문제 이해와 분석",
        description="""
        문제 해결을 시작하기 전에
        현재 상태와 목표 상태를 파악하고,
        목표 상태에 도달하기 위해 필요한
        작업을 분석합니다.
        """,
        icon="🔎",
        page="pages/02_01_문제이해와분석.py",
        completed=unit2_progress["2-1"],
        score=st.session_state.lesson_2_1_score,
    )


with row1[1]:

    lesson_card(
        lesson_no="2-2",
        title="문제 분해와 모델링",
        description="""
        복잡한 문제를 여러 개의 작은 문제로
        나누고, 문제 해결에 필요한 핵심 요소를
        추출하여 컴퓨터가 처리하기 쉬운
        형태로 모델링합니다.
        """,
        icon="🧩",
        page="pages/02_02_문제분해와모델링.py",
        completed=unit2_progress["2-2"],
        score=st.session_state.lesson_2_2_score,
    )


# =========================================================
# 2-3 / 2-4
# =========================================================
row2 = st.columns(2)


with row2[0]:

    lesson_card(
        lesson_no="2-3",
        title="알고리즘 설계",
        description="""
        문제 해결에 필요한 절차를
        순차·선택·반복 구조로 표현하고,
        의사코드와 Python 코드로 연결합니다.
        """,
        icon="⚙️",
        page="pages/02_03_알고리즘설계.py",
        completed=unit2_progress["2-3"],
        score=st.session_state.lesson_2_3_score,
    )


with row2[1]:

    lesson_card(
        lesson_no="2-4",
        title="알고리즘 성능 분석",
        description="""
        입력 데이터의 크기가 증가할 때
        알고리즘의 수행 횟수가 어떻게 달라지는지
        살펴보고 시간 복잡도를 이용해
        알고리즘의 효율성을 비교합니다.
        """,
        icon="📊",
        page="pages/02_04_알고리즘성능분석.py",
        completed=unit2_progress["2-4"],
        score=st.session_state.lesson_2_4_score,
    )


# =========================================================
# 학습 흐름
# =========================================================
render_html(
    """
    <div class="section-header section-space">

        <div>

            <div class="section-label">
                LEARNING PROCESS
            </div>

            <h3>
                각 학습은 이렇게 진행됩니다
            </h3>

            <p>
                단순히 개념을 읽는 것에서 끝나지 않고,
                직접 문제를 분석하고 Python 코드로 연결합니다.
            </p>

        </div>

    </div>
    """
)


flow_cols = st.columns(5)

flow_data = [
    (
        "01",
        "📘",
        "개념 이해",
        "교과서의 핵심 개념을 학습합니다.",
    ),
    (
        "02",
        "💡",
        "예제 분석",
        "실제 문제 상황을 분석합니다.",
    ),
    (
        "03",
        "🧠",
        "문제 해결 활동",
        "학생이 직접 해결 방법을 생각합니다.",
    ),
    (
        "04",
        "🐍",
        "Python 연결",
        "알고리즘을 Python 코드로 표현합니다.",
    ),
    (
        "05",
        "📝",
        "형성평가",
        "학습한 내용을 스스로 확인합니다.",
    ),
]


for col, data in zip(
    flow_cols,
    flow_data,
):

    step, icon, title, description = data

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
# Python / Colab 안내
# =========================================================
render_html(
    """
    <div class="colab-banner">

        <div>

            <div class="section-label">
                PYTHON PRACTICE
            </div>

            <h3>
                알고리즘을 이해하고 Python으로 직접 구현합니다.
            </h3>

            <p>
                각 소단원에서는 알고리즘의 핵심 개념을
                Python 코드와 연결하여 학습합니다.
                <br><br>
                이후 Google Colab 실습 노트북과 연결하여
                학생이 직접 코드를 수정하고 실행할 수 있도록
                확장할 예정입니다.
            </p>

        </div>

        <div class="colab-logo">
            🐍
        </div>

    </div>
    """
)


# =========================================================
# 2단원 핵심 흐름 정리
# =========================================================
render_html(
    """
    <div class="section-header section-space">

        <div>

            <div class="section-label">
                UNIT SUMMARY
            </div>

            <h3>
                2단원의 핵심 흐름
            </h3>

        </div>

    </div>
    """
)


st.code(
    """
문제 상황
   ↓
현재 상태와 목표 상태 파악
   ↓
필요한 작업 분석
   ↓
복잡한 문제 분해
   ↓
핵심 요소 추상화
   ↓
문제 모델링
   ↓
알고리즘 설계
   ↓
Python 구현
   ↓
알고리즘 성능 분석
    """.strip(),
    language="text",
)


# =========================================================
# 페이지 이동
# =========================================================
render_html(
    "<br>"
)

nav_left, nav_right = st.columns(
    [1, 1]
)


with nav_left:

    if st.button(
        "← 메인 화면으로",
        use_container_width=True,
    ):

        st.switch_page(
            "streamlit_app.py"
        )


with nav_right:

    if unit2_completed:

        st.button(
            "✓ 2단원 학습 완료",
            disabled=True,
            use_container_width=True,
        )

    else:

        next_page = None
        next_label = None

        lesson_pages = {
            "2-1": (
                "pages/02_01_문제이해와분석.py",
                "2-1 문제 이해와 분석",
            ),
            "2-2": (
                "pages/02_02_문제분해와모델링.py",
                "2-2 문제 분해와 모델링",
            ),
            "2-3": (
                "pages/02_03_알고리즘설계.py",
                "2-3 알고리즘 설계",
            ),
            "2-4": (
                "pages/02_04_알고리즘성능분석.py",
                "2-4 알고리즘 성능 분석",
            ),
        }

        for lesson_no in [
            "2-1",
            "2-2",
            "2-3",
            "2-4",
        ]:

            if not unit2_progress[lesson_no]:

                next_page, next_label = (
                    lesson_pages[lesson_no]
                )

                break

        if next_page:

            if st.button(
                f"다음 학습: {next_label} →",
                use_container_width=True,
                type="primary",
            ):

                st.switch_page(
                    next_page
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
            Ⅱ. 추상화와 모델링 · Unit Learning Roadmap
        </span>

    </div>
    """
)