import streamlit as st

from utils.ui import (
    load_css,
    render_html,
)


# =========================================================
# 페이지 설정
# =========================================================
st.set_page_config(
    page_title="1-2 알고리즘 표현 방법",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_css("assets/style.css")


# =========================================================
# 세션 상태 초기화
# =========================================================
if "unit1_progress" not in st.session_state:
    st.session_state.unit1_progress = {
        "1-1": False,
        "1-2": False,
        "1-3": False,
    }

if "lesson_1_2_score" not in st.session_state:
    st.session_state.lesson_1_2_score = None


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

    st.markdown("### Ⅰ. 알고리즘 개요")

    if st.button(
        "← 1단원으로 돌아가기",
        use_container_width=True,
    ):
        st.switch_page(
            "pages/01_1단원.py"
        )

    st.markdown("---")

    if st.button(
        "1-1  알고리즘 개념",
        use_container_width=True,
    ):
        st.switch_page(
            "pages/01_01_알고리즘개념.py"
        )

    st.button(
        "1-2  알고리즘 표현 방법",
        type="primary",
        use_container_width=True,
        disabled=True,
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
        Ⅰ. 알고리즘 개요 &nbsp;›&nbsp;
        1-2 알고리즘 표현 방법
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
                UNIT Ⅰ · LESSON 02
            </div>

            <h2>
                알고리즘 표현 방법
            </h2>

            <p>
                알고리즘은 머릿속에만 존재하는 것이 아니라
                다른 사람이 이해할 수 있도록
                명확하게 표현해야 합니다.
                <br><br>
                이번 시간에는 알고리즘을
                <strong>자연어, 의사코드, 순서도</strong>로
                표현하는 방법을 알아봅니다.
            </p>

        </div>

        <div class="hero-visual">

            <div class="code-window">

                <div class="code-window-header">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>

                <pre>알고리즘
   ↓
┌───────────┐
│ 자연어     │
│ 의사코드   │
│ 순서도     │
└───────────┘</pre>

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
                오늘의 학습 목표
            </h3>

            <p>
                알고리즘을 여러 방법으로 표현하고
                각 표현 방법의 특징을 설명합니다.
            </p>

        </div>

    </div>
    """
)


goal_cols = st.columns(3)

goal_data = [
    (
        "01",
        "💬",
        "자연어",
        "일상적인 문장을 이용하여 해결 절차를 표현합니다.",
    ),
    (
        "02",
        "🧾",
        "의사코드",
        "프로그래밍 구조와 비슷한 형태로 해결 절차를 표현합니다.",
    ),
    (
        "03",
        "🔷",
        "순서도",
        "기호와 화살표를 이용하여 알고리즘의 흐름을 표현합니다.",
    ),
]

for col, (
    step,
    icon,
    title,
    description,
) in zip(
    goal_cols,
    goal_data,
):

    with col:

        render_html(
            f"""
            <div class="learning-flow-card">

                <div class="flow-step">
                    GOAL {step}
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
# 학습 영역
# =========================================================
render_html(
    """
    <div class="section-header section-space">

        <div>

            <div class="section-label">
                LEARNING
            </div>

            <h3>
                같은 알고리즘을 여러 방법으로 표현해 봅시다
            </h3>

            <p>
                표현 방법은 서로 다르지만
                문제를 해결하는 기본적인 절차는 같습니다.
            </p>

        </div>

    </div>
    """
)


(
    concept_tab,
    compare_tab,
    activity_tab,
    quiz_tab,
) = st.tabs(
    [
        "📘 표현 방법",
        "🔄 비교해 보기",
        "🧠 직접 표현하기",
        "📝 형성평가",
    ]
)


# =========================================================
# ① 표현 방법
# =========================================================
with concept_tab:

    # -----------------------------------------------------
    # 자연어
    # -----------------------------------------------------
    st.markdown("## 1. 자연어")

    st.markdown(
        """
**자연어**는 우리가 일상생활에서 사용하는
말이나 글을 이용하여 알고리즘을 표현하는 방법입니다.

누구나 쉽게 이해할 수 있다는 장점이 있지만,
표현하는 사람에 따라 문장이 달라지거나
의미가 모호해질 수 있습니다.
"""
    )

    st.code(
        """
1. 두 수를 입력받는다.
2. 두 수를 더한다.
3. 계산한 결과를 출력한다.
        """.strip(),
        language="text",
    )

    st.info(
        """
        💡 자연어는 이해하기 쉽지만
        복잡한 알고리즘을 표현하면 내용이 길어질 수 있습니다.
        """
    )

    st.markdown("---")

    # -----------------------------------------------------
    # 의사코드
    # -----------------------------------------------------
    st.markdown("## 2. 의사코드")

    st.markdown(
        """
**의사코드(Pseudocode)**는 실제 프로그래밍 언어는 아니지만,
프로그래밍 코드와 비슷한 형태로 알고리즘을 표현하는 방법입니다.

자연어보다 구조가 분명하고,
실제 프로그램으로 구현하기 전에
알고리즘의 흐름을 정리하기에 좋습니다.
"""
    )

    st.code(
        """
두 수 A, B를 입력한다.

SUM ← A + B

SUM을 출력한다.
        """.strip(),
        language="text",
    )

    st.success(
        """
        ✅ 의사코드는 특정 프로그래밍 언어의
        정확한 문법을 따를 필요가 없습니다.
        """
    )

    st.markdown("---")

    # -----------------------------------------------------
    # 순서도
    # -----------------------------------------------------
    st.markdown("## 3. 순서도")

    st.markdown(
        """
**순서도(Flowchart)**는 약속된 기호와 화살표를 사용하여
알고리즘의 처리 흐름을 그림으로 표현하는 방법입니다.

작업의 순서와 흐름을 시각적으로 볼 수 있어
알고리즘의 전체 구조를 이해하기 쉽습니다.
"""
    )

    symbol_cols = st.columns(4)

    symbol_data = [
        (
            "⬭",
            "시작 / 종료",
            "알고리즘의 시작과 끝을 나타냅니다.",
        ),
        (
            "▱",
            "입력 / 출력",
            "데이터를 입력하거나 결과를 출력합니다.",
        ),
        (
            "▭",
            "처리",
            "계산이나 값을 변경하는 작업을 나타냅니다.",
        ),
        (
            "◇",
            "판단",
            "조건을 확인하고 흐름을 선택합니다.",
        ),
    ]

    for col, (
        icon,
        title,
        description,
    ) in zip(
        symbol_cols,
        symbol_data,
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

    st.info(
        """
        💡 순서도에서는 화살표를 사용하여
        알고리즘이 진행되는 방향을 나타냅니다.
        """
    )

    st.markdown("---")

    st.success(
        """
        ✅ **핵심 정리**

        알고리즘은 자연어, 의사코드, 순서도 등
        여러 가지 방법으로 표현할 수 있습니다.
        """
    )


# =========================================================
# ② 비교해 보기
# =========================================================
with compare_tab:

    st.markdown("## 🍜 같은 알고리즘을 세 가지 방법으로 표현하기")

    st.markdown(
        """
이번에는 **컵라면 만들기**라는 같은 알고리즘을
자연어, 의사코드, 순서도 방식으로 각각 표현해 봅시다.
"""
    )

    st.markdown("### 💬 자연어")

    st.code(
        """
1. 컵라면의 뚜껑을 연다.
2. 스프를 넣는다.
3. 뜨거운 물을 붓는다.
4. 뚜껑을 닫는다.
5. 3분 동안 기다린다.
6. 컵라면을 먹는다.
        """.strip(),
        language="text",
    )

    st.markdown("### 🧾 의사코드")

    st.code(
        """
컵라면 준비

뚜껑 열기
스프 넣기
뜨거운 물 넣기
뚜껑 닫기

3분 기다리기

컵라면 먹기
        """.strip(),
        language="text",
    )

    st.markdown("### 🔷 순서도 형태")

    render_html(
        """
        <div style="
            max-width: 430px;
            margin: 20px auto;
            text-align: center;
        ">

            <div class="learning-flow-card">
                🟢 시작
            </div>

            <div style="font-size: 28px; margin: 6px 0;">
                ↓
            </div>

            <div class="learning-flow-card">
                컵라면 준비
            </div>

            <div style="font-size: 28px; margin: 6px 0;">
                ↓
            </div>

            <div class="learning-flow-card">
                뜨거운 물 붓기
            </div>

            <div style="font-size: 28px; margin: 6px 0;">
                ↓
            </div>

            <div class="learning-flow-card">
                3분 기다리기
            </div>

            <div style="font-size: 28px; margin: 6px 0;">
                ↓
            </div>

            <div class="learning-flow-card">
                컵라면 먹기
            </div>

            <div style="font-size: 28px; margin: 6px 0;">
                ↓
            </div>

            <div class="learning-flow-card">
                🔴 종료
            </div>

        </div>
        """
    )

    st.success(
        """
        ✅ 표현 방법은 달라도
        **해결하려는 문제와 알고리즘의 기본적인 절차는 같습니다.**
        """
    )

    st.markdown("---")

    st.markdown("## 📊 세 가지 표현 방법 비교")

    compare_cols = st.columns(3)

    comparison_data = [
        (
            "💬",
            "자연어",
            "쉽게 작성하고 이해할 수 있음",
            "복잡해지면 길거나 모호해질 수 있음",
        ),
        (
            "🧾",
            "의사코드",
            "알고리즘의 논리 구조를 명확하게 표현",
            "정해진 하나의 표준 문법은 없음",
        ),
        (
            "🔷",
            "순서도",
            "전체 흐름을 시각적으로 파악하기 쉬움",
            "복잡한 알고리즘은 그림이 커질 수 있음",
        ),
    ]

    for col, (
        icon,
        title,
        advantage,
        disadvantage,
    ) in zip(
        compare_cols,
        comparison_data,
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
                        <strong>장점</strong><br>
                        {advantage}
                    </p>

                    <p>
                        <strong>특징</strong><br>
                        {disadvantage}
                    </p>

                </div>
                """
            )


# =========================================================
# ③ 직접 표현하기
# =========================================================
with activity_tab:

    st.markdown("## 🧠 하나의 알고리즘을 여러 방법으로 표현해 봅시다")

    render_html(
        """
        <div class="info-card">

            <div class="info-card-icon">
                🥤
            </div>

            <div class="info-card-content">

                <strong>
                    문제 상황
                </strong>

                <p>
                    자판기에서 원하는 음료수를 구매하는 과정을
                    자연어, 의사코드, 순서도의 흐름으로
                    표현해 봅시다.
                </p>

            </div>

        </div>
        """
    )

    natural_language = st.text_area(
        "① 자연어로 표현하세요.",
        placeholder=(
            "1. 자판기에 돈을 넣는다.\n"
            "2. 원하는 음료를 선택한다.\n"
            "3. ..."
        ),
        height=170,
        key="lesson_1_2_natural",
    )

    pseudocode = st.text_area(
        "② 의사코드 형태로 표현하세요.",
        placeholder=(
            "돈 입력\n"
            "음료 선택\n"
            "가격 확인\n"
            "..."
        ),
        height=170,
        key="lesson_1_2_pseudocode",
    )

    flowchart_text = st.text_area(
        "③ 순서도의 흐름을 글로 표현하세요.",
        placeholder=(
            "시작 → 돈 입력 → 음료 선택 → "
            "가격 확인 → 음료 출력 → 종료"
        ),
        height=130,
        key="lesson_1_2_flowchart",
    )

    if st.button(
        "작성 내용 확인하기",
        key="lesson_1_2_activity_check",
        type="primary",
        use_container_width=True,
    ):

        if (
            natural_language.strip()
            and pseudocode.strip()
            and flowchart_text.strip()
        ):

            st.success(
                """
                잘했습니다! ✅

                같은 문제 해결 절차를
                세 가지 방법으로 표현했습니다.
                """
            )

        else:

            st.warning(
                "세 가지 표현 방법을 모두 작성해 주세요."
            )

    with st.expander(
        "💡 예시 답안 보기"
    ):

        st.markdown(
            """
            ### 자연어

            1. 자판기에 돈을 넣는다.
            2. 원하는 음료를 선택한다.
            3. 넣은 금액이 충분한지 확인한다.
            4. 금액이 충분하면 음료를 받는다.
            5. 잔돈이 있으면 잔돈을 받는다.
            """
        )

        st.markdown("### 의사코드")

        st.code(
            """
            돈 입력
            음료 선택
            음료 가격 확인

            만약 입력한 돈이 음료 가격 이상이면
            음료 출력
            잔돈 계산
            잔돈 출력
            """.strip(),
            language="text",
        )

        st.markdown("### 순서도의 흐름")

        st.markdown(
            """
            **시작 → 돈 입력 → 음료 선택 → 금액 확인 → 음료 출력 → 잔돈 출력 → 종료**
            """
        )