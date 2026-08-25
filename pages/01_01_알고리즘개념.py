import streamlit as st

from utils.ui import (
    load_css,
    render_html,
)


# =========================================================
# 페이지 설정
# =========================================================
st.set_page_config(
    page_title="1-1 알고리즘 개념",
    page_icon="🧠",
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

if "lesson_1_1_score" not in st.session_state:
    st.session_state.lesson_1_1_score = None


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

    st.button(
        "1-1  알고리즘 개념",
        type="primary",
        use_container_width=True,
        disabled=True,
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
        Ⅰ. 알고리즘 개요 &nbsp;›&nbsp;
        1-1 알고리즘 개념
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
                UNIT Ⅰ · LESSON 01
            </div>

            <h2>
                알고리즘 개념
            </h2>

            <p>
                우리는 일상생활에서도 여러 문제를
                일정한 순서와 방법에 따라 해결합니다.
                <br><br>
                컴퓨터가 문제를 해결할 때에도
                명확한 해결 절차가 필요합니다.
                그것이 바로 <strong>알고리즘</strong>입니다.
            </p>

        </div>

        <div class="hero-visual">

            <div class="code-window">

                <div class="code-window-header">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>

                <pre>문제 발생
   ↓
해결 방법 생각하기
   ↓
해결 순서 정하기
   ↓
알고리즘 실행
   ↓
문제 해결</pre>

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
                알고리즘의 의미와 필요성을 이해하고
                좋은 알고리즘의 기본적인 특징을 설명합니다.
            </p>

        </div>

    </div>
    """
)


goal_cols = st.columns(3)

goal_data = [
    (
        "01",
        "🧠",
        "개념 이해",
        "알고리즘이 무엇인지 설명할 수 있습니다.",
    ),
    (
        "02",
        "💡",
        "필요성 이해",
        "문제 해결에서 알고리즘이 필요한 이유를 설명할 수 있습니다.",
    ),
    (
        "03",
        "✅",
        "특징 이해",
        "좋은 알고리즘이 갖추어야 할 특징을 이해합니다.",
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
                알고리즘의 기본 개념을 알아봅시다
            </h3>

            <p>
                알고리즘의 의미를 이해하고
                일상생활 속 문제 해결 과정과 연결해 봅니다.
            </p>

        </div>

    </div>
    """
)


(
    concept_tab,
    example_tab,
    activity_tab,
    quiz_tab,
) = st.tabs(
    [
        "📘 개념 학습",
        "💡 생활 속 알고리즘",
        "🧠 직접 만들어 보기",
        "📝 형성평가",
    ]
)


# =========================================================
# ① 개념 학습
# =========================================================
with concept_tab:

    st.markdown("## 1. 알고리즘이란?")

    st.markdown(
        """
**알고리즘(Algorithm)**은 어떤 문제를 해결하기 위해
정해진 순서에 따라 수행하는 **명확한 절차**입니다.

쉽게 표현하면 알고리즘은

> **문제를 해결하기 위한 방법과 순서**

라고 할 수 있습니다.
"""
    )

    st.info(
        """
        💡 알고리즘은 컴퓨터 프로그램에서만 사용하는 개념이 아닙니다.

        요리하기, 길 찾기, 자판기 이용하기처럼
        우리가 일상생활에서 수행하는 많은 활동에도
        알고리즘이 존재합니다.
        """
    )

    st.markdown("---")

    st.markdown("## 2. 알고리즘은 왜 필요할까요?")

    st.markdown(
        """
문제를 해결할 때 아무런 계획 없이 행동하면
작업을 빠뜨리거나 잘못된 결과가 나타날 수 있습니다.

알고리즘을 사용하면 문제 해결 과정을
**체계적이고 명확하게 정리**할 수 있습니다.
"""
    )

    need_cols = st.columns(3)

    need_data = [
        (
            "🎯",
            "정확한 문제 해결",
            "필요한 작업과 순서를 명확하게 정할 수 있습니다.",
        ),
        (
            "⚡",
            "효율적인 해결",
            "불필요한 작업을 줄이고 더 효율적으로 문제를 해결할 수 있습니다.",
        ),
        (
            "🔄",
            "반복과 재사용",
            "같은 절차를 활용하여 비슷한 문제를 다시 해결할 수 있습니다.",
        ),
    ]

    for col, (
        icon,
        title,
        description,
    ) in zip(
        need_cols,
        need_data,
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

    st.markdown("---")

    st.markdown("## 3. 좋은 알고리즘의 특징")

    st.markdown(
        """
알고리즘은 문제를 해결할 수 있어야 할 뿐 아니라,
각 단계가 명확하고 실제로 수행 가능해야 합니다.
"""
    )

    feature_cols = st.columns(2)

    with feature_cols[0]:

        st.success(
            """
**① 명확성**

각 단계에서 무엇을 해야 하는지
명확하게 표현되어야 합니다.
"""
        )

        st.success(
            """
**② 유한성**

알고리즘은 일정한 단계를 수행한 뒤
반드시 종료되어야 합니다.
"""
        )

    with feature_cols[1]:

        st.success(
            """
**③ 실행 가능성**

알고리즘의 각 단계는
실제로 수행 가능한 작업이어야 합니다.
"""
        )

        st.success(
            """
**④ 효율성**

같은 문제를 해결한다면
가능한 한 적은 시간과 자원을 사용하는 것이 좋습니다.
"""
        )

    st.markdown("---")

    st.success(
        """
✅ **핵심 정리**

알고리즘은 문제를 해결하기 위한
**명확하고 유한한 해결 절차**입니다.
"""
    )


# =========================================================
# ② 생활 속 알고리즘
# =========================================================
with example_tab:

    st.markdown("## 🍜 생활 속에서도 알고리즘을 찾을 수 있습니다")

    st.markdown(
        """
알고리즘은 특별한 컴퓨터 기술이 아니라
우리 주변에서 쉽게 발견할 수 있습니다.

예를 들어 **라면 끓이기**를 생각해 봅시다.
"""
    )

    render_html(
        """
        <div class="info-card">

            <div class="info-card-icon">
                🍜
            </div>

            <div class="info-card-content">

                <strong>
                    라면 끓이기 알고리즘
                </strong>

                <p>
                    ① 냄비에 물을 넣는다.<br>
                    ② 물을 끓인다.<br>
                    ③ 면과 스프를 넣는다.<br>
                    ④ 일정 시간 끓인다.<br>
                    ⑤ 그릇에 담는다.
                </p>

            </div>

        </div>
        """
    )

    st.markdown(
        """
각 작업은 일정한 **순서**에 따라 이루어집니다.

예를 들어 물을 끓이지 않고 면을 먼저 넣는다면
원하는 결과를 얻기 어려울 수 있습니다.

따라서 알고리즘에서는
**작업의 내용뿐 아니라 작업의 순서도 중요합니다.**
"""
    )

    st.markdown("---")

    st.markdown("## 🚦 조건에 따라 달라지는 알고리즘")

    st.markdown(
        """
횡단보도를 건너는 과정도 하나의 알고리즘으로 생각할 수 있습니다.

1. 횡단보도 앞에서 멈춘다.
2. 보행자 신호를 확인한다.
3. 초록불이면 건넌다.
4. 빨간불이면 기다린다.
"""
    )

    st.info(
        """
        💡 여기에서는 신호의 상태에 따라
        해야 할 행동이 달라집니다.

        이후 단원에서는 이러한 구조를
        **선택 구조**라고 배우게 됩니다.
        """
    )

    st.markdown("---")

    st.markdown("## 🧭 또 다른 예: 길 찾기")

    st.markdown(
        """
목적지까지 이동할 때에도 여러 해결 방법이 존재할 수 있습니다.

예를 들어 학교에서 지하철역까지 이동할 때

- 가장 짧은 길
- 신호등이 적은 길
- 사람이 적은 길

등 여러 방법을 선택할 수 있습니다.

즉, 같은 문제라도 **서로 다른 알고리즘**이 존재할 수 있습니다.
"""
    )

    st.success(
        """
        ✅ 같은 문제를 해결하는 알고리즘이 여러 개라면,
        그중 더 빠르거나 효율적인 방법을 선택할 수 있습니다.
        """
    )


# =========================================================
# ③ 직접 만들어 보기
# =========================================================
with activity_tab:

    st.markdown("## 🧠 나만의 생활 알고리즘 만들기")

    st.markdown(
        """
일상생활에서 일정한 순서에 따라 수행하는 활동 하나를 선택하여
알고리즘으로 표현해 봅시다.
"""
    )

    render_html(
        """
        <div class="info-card">

            <div class="info-card-icon">
                💡
            </div>

            <div class="info-card-content">

                <strong>
                    활동 예시
                </strong>

                <p>
                    학교 갈 준비하기 · 컴퓨터 켜기 ·
                    자판기에서 음료 구매하기 ·
                    친구에게 메시지 보내기 ·
                    컵라면 만들기
                </p>

            </div>

        </div>
        """
    )

    activity_name = st.text_input(
        "① 어떤 활동을 선택했나요?",
        placeholder="예: 학교 갈 준비하기",
        key="lesson_1_1_activity_name",
    )

    activity_steps = st.text_area(
        "② 해결 절차를 순서대로 작성해 보세요.",
        placeholder=(
            "1. 알람을 끈다.\n"
            "2. 세수를 한다.\n"
            "3. 교복을 입는다.\n"
            "4. 가방을 챙긴다.\n"
            "5. 집을 나선다."
        ),
        height=200,
        key="lesson_1_1_activity_steps",
    )

    if st.button(
        "작성 내용 확인하기",
        key="lesson_1_1_activity_check",
        type="primary",
        use_container_width=True,
    ):

        if (
            activity_name.strip()
            and activity_steps.strip()
        ):

            st.success(
                """
잘했습니다! ✅

일상생활의 활동도 일정한 순서와 절차로 표현하면
하나의 알고리즘으로 생각할 수 있습니다.
"""
            )

        else:

            st.warning(
                "활동과 해결 절차를 모두 작성해 주세요."
            )

    with st.expander(
        "💡 예시 답안 보기"
    ):

        st.markdown(
            """
### 활동

컴퓨터 켜기

### 알고리즘

1. 컴퓨터의 전원 버튼을 누른다.
2. 운영체제가 실행될 때까지 기다린다.
3. 로그인 화면이 나타나면 비밀번호를 입력한다.
4. 바탕 화면이 나타나는지 확인한다.
5. 사용할 프로그램을 실행한다.
"""
        )


# =========================================================
# ④ 형성평가
# =========================================================
with quiz_tab:

    st.markdown("## 📝 1-1 형성평가")

    st.caption(
        """
알고리즘의 개념과 필요성,
좋은 알고리즘의 특징을 이해했는지 확인해 봅시다.
"""
    )

    q1 = st.radio(
        "1. 알고리즘에 대한 설명으로 가장 적절한 것은 무엇인가요?",
        [
            "문제를 해결하기 위한 명확한 절차",
            "컴퓨터를 구성하는 부품",
            "인터넷에 접속하는 기술",
            "데이터를 저장하는 장치",
        ],
        index=None,
        key="quiz_1_1_q1",
    )

    q2 = st.radio(
        "2. 다음 중 알고리즘의 예로 가장 적절한 것은 무엇인가요?",
        [
            "라면을 끓이는 순서",
            "모니터의 크기",
            "키보드의 색상",
            "책상의 높이",
        ],
        index=None,
        key="quiz_1_1_q2",
    )

    q3 = st.radio(
        "3. 좋은 알고리즘의 특징으로 적절하지 않은 것은 무엇인가요?",
        [
            "명확성",
            "유한성",
            "실행 가능성",
            "무한 반복",
        ],
        index=None,
        key="quiz_1_1_q3",
    )

    q4 = st.radio(
        "4. 알고리즘의 유한성이 의미하는 것은 무엇인가요?",
        [
            "일정한 단계 후에 반드시 종료되어야 한다.",
            "항상 한 단계만 실행해야 한다.",
            "같은 작업을 영원히 반복해야 한다.",
            "반드시 컴퓨터에서만 실행해야 한다.",
        ],
        index=None,
        key="quiz_1_1_q4",
    )

    q5 = st.radio(
        "5. 알고리즘을 사용하는 이유로 가장 적절한 것은 무엇인가요?",
        [
            "문제를 체계적이고 명확하게 해결하기 위해서",
            "컴퓨터의 색상을 바꾸기 위해서",
            "파일 이름을 만들기 위해서",
            "인터넷 속도를 높이기 위해서",
        ],
        index=None,
        key="quiz_1_1_q5",
    )

    if st.button(
        "형성평가 제출",
        key="submit_quiz_1_1",
        type="primary",
        use_container_width=True,
    ):

        answers = [
            q1,
            q2,
            q3,
            q4,
            q5,
        ]

        if any(
            answer is None
            for answer in answers
        ):

            st.warning(
                "⚠️ 모든 문항에 답한 후 제출해 주세요."
            )

        else:

            correct_answers = [
                "문제를 해결하기 위한 명확한 절차",
                "라면을 끓이는 순서",
                "무한 반복",
                "일정한 단계 후에 반드시 종료되어야 한다.",
                "문제를 체계적이고 명확하게 해결하기 위해서",
            ]

            score = sum(
                answer == correct
                for answer, correct in zip(
                    answers,
                    correct_answers,
                )
            )

            st.session_state.lesson_1_1_score = score

            if score == 5:

                st.success(
                    "🎉 완벽합니다! **5 / 5점**"
                )

            elif score >= 4:

                st.success(
                    f"👏 잘했습니다! **{score} / 5점**입니다."
                )

            elif score >= 3:

                st.warning(
                    f"📚 **{score} / 5점**입니다. "
                    "틀린 내용을 한 번 더 확인해 봅시다."
                )

            else:

                st.error(
                    f"🔄 **{score} / 5점**입니다. "
                    "개념 학습 내용을 다시 살펴보세요."
                )

            if score >= 4:

                st.session_state.unit1_progress[
                    "1-1"
                ] = True

                st.success(
                    "✅ 1-1 알고리즘 개념 학습을 완료했습니다."
                )


# =========================================================
# 학습 상태
# =========================================================
render_html(
    """
    <div class="section-header section-space">

        <div>

            <div class="section-label">
                LESSON STATUS
            </div>

            <h3>
                학습 상태
            </h3>

        </div>

    </div>
    """
)


is_completed = (
    st.session_state.unit1_progress.get(
        "1-1",
        False,
    )
)


if is_completed:

    st.success(
        "🎉 **1-1 알고리즘 개념** 학습을 완료했습니다."
    )

    if (
        st.session_state.lesson_1_1_score
        is not None
    ):

        st.markdown(
            "형성평가 점수: "
            f"**{st.session_state.lesson_1_1_score} / 5점**"
        )

else:

    st.info(
        """
형성평가에서 4점 이상을 받으면
1-1 학습이 완료됩니다.
"""
    )


# =========================================================
# 핵심 정리
# =========================================================
with st.expander(
    "📚 1-1 핵심 내용 다시 보기",
    expanded=False,
):

    st.markdown(
        """
### 알고리즘

문제를 해결하기 위해 정해진 순서에 따라 수행하는
**명확한 해결 절차**입니다.

### 알고리즘이 필요한 이유

- 문제 해결 과정을 체계적으로 정리할 수 있습니다.
- 불필요한 작업을 줄일 수 있습니다.
- 같은 해결 절차를 다시 사용할 수 있습니다.

### 좋은 알고리즘의 특징

- **명확성**
- **유한성**
- **실행 가능성**
- **효율성**

### 핵심 문장

> **알고리즘은 문제 해결을 위한 명확하고 유한한 절차이다.**
"""
    )


# =========================================================
# 페이지 이동
# =========================================================
render_html("<br>")

nav_left, nav_right = st.columns(2)


with nav_left:

    if st.button(
        "← 1단원 개요",
        use_container_width=True,
    ):

        st.switch_page(
            "pages/01_1단원.py"
        )


with nav_right:

    if st.button(
        "1-2 알고리즘 표현 방법 →",
        use_container_width=True,
        type="primary",
    ):

        st.switch_page(
            "pages/01_02_알고리즘표현방법.py"
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
            Ⅰ. 알고리즘 개요 · 1-1 알고리즘 개념
        </span>

    </div>
    """
)