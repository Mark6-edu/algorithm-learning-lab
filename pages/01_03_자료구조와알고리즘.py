import streamlit as st

from utils.ui import (
    load_css,
    render_html,
)


# =========================================================
# 페이지 설정
# =========================================================
st.set_page_config(
    page_title="1-3 자료 구조와 알고리즘",
    page_icon="🗂️",
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

if "lesson_1_3_score" not in st.session_state:
    st.session_state.lesson_1_3_score = None


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

    if st.button(
        "1-2  알고리즘 표현 방법",
        use_container_width=True,
    ):
        st.switch_page(
            "pages/01_02_알고리즘표현방법.py"
        )

    st.button(
        "1-3  자료 구조와 알고리즘",
        type="primary",
        use_container_width=True,
        disabled=True,
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
        1-3 자료 구조와 알고리즘
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
                UNIT Ⅰ · LESSON 03
            </div>

            <h2>
                자료 구조와 알고리즘
            </h2>

            <p>
                컴퓨터가 문제를 해결하려면
                데이터를 적절한 형태로 저장하고 관리해야 합니다.
                <br><br>
                <strong>자료 구조</strong>는 데이터를 정리하는 방법이고,
                <strong>알고리즘</strong>은 그 데이터를 이용하여
                문제를 해결하는 방법입니다.
            </p>

        </div>

        <div class="hero-visual">

            <div class="code-window">

                <div class="code-window-header">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>

                <pre>데이터
   ↓
자료 구조
   ↓
알고리즘
   ↓
처리 결과</pre>

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
                자료 구조의 의미를 이해하고,
                자료 구조와 알고리즘의 관계를 설명합니다.
            </p>

        </div>

    </div>
    """
)


goal_cols = st.columns(3)

goal_data = [
    (
        "01",
        "🗂️",
        "자료 구조 이해",
        "데이터를 저장하고 관리하는 방법을 이해합니다.",
    ),
    (
        "02",
        "⚙️",
        "알고리즘 연결",
        "자료 구조에 저장된 데이터를 알고리즘이 어떻게 처리하는지 이해합니다.",
    ),
    (
        "03",
        "🔍",
        "간단한 탐색",
        "데이터에서 원하는 값을 찾는 과정을 살펴봅니다.",
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
                데이터와 알고리즘의 관계를 알아봅시다
            </h3>

            <p>
                데이터를 어떻게 정리하느냐에 따라
                문제 해결 방법과 효율이 달라질 수 있습니다.
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
        "🔍 예제로 이해하기",
        "🧠 직접 찾아보기",
        "📝 형성평가",
    ]
)


# =========================================================
# ① 개념 학습
# =========================================================
with concept_tab:

    st.markdown("## 1. 자료 구조란?")

    st.markdown(
        """
**자료 구조(Data Structure)**는
여러 데이터를 컴퓨터에서 효율적으로
저장하고 관리하기 위한 방법입니다.

예를 들어 학생들의 점수를 저장한다고 생각해 봅시다.
"""
    )

    st.code(
        """
85, 92, 78, 95, 88
        """.strip(),
        language="text",
    )

    st.markdown(
        """
여러 데이터를 일정한 구조로 정리해 두면
필요한 데이터를 찾거나 수정하고,
계산하는 작업을 더 쉽게 수행할 수 있습니다.
"""
    )

    st.info(
        """
        💡 자료 구조는 쉽게 말하면
        **데이터를 정리하여 저장하는 방법**입니다.
        """
    )

    st.markdown("---")

    st.markdown("## 2. 자료 구조와 알고리즘")

    st.markdown(
        """
자료 구조와 알고리즘은 서로 밀접한 관계가 있습니다.

- **자료 구조** → 데이터를 어떻게 저장할 것인가?
- **알고리즘** → 저장된 데이터를 어떻게 처리할 것인가?

같은 데이터라도 어떤 방식으로 저장하고 정리하느냐에 따라
문제를 해결하는 방법과 효율이 달라질 수 있습니다.
"""
    )

    relation_cols = st.columns(3)

    relation_data = [
        (
            "📦",
            "데이터",
            "문제를 해결하기 위해 필요한 정보를 준비합니다.",
        ),
        (
            "🗂️",
            "자료 구조",
            "데이터를 일정한 방식으로 저장하고 정리합니다.",
        ),
        (
            "⚙️",
            "알고리즘",
            "저장된 데이터를 이용하여 문제를 해결합니다.",
        ),
    ]

    for col, (
        icon,
        title,
        description,
    ) in zip(
        relation_cols,
        relation_data,
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

    st.markdown("## 3. 대표적인 자료 구조")

    st.markdown(
        """
자료 구조에는 여러 종류가 있습니다.

이번 시간에는 대표적인 예만 간단하게 살펴봅니다.
"""
    )

    structure_cols = st.columns(3)

    structure_data = [
        (
            "📋",
            "리스트",
            "여러 데이터를 순서대로 저장하는 구조",
            "[80, 90, 70, 100]",
        ),
        (
            "🥞",
            "스택",
            "나중에 들어온 데이터를 먼저 꺼내는 구조",
            "접시 쌓기",
        ),
        (
            "🚶",
            "큐",
            "먼저 들어온 데이터를 먼저 처리하는 구조",
            "줄 서기",
        ),
    ]

    for col, (
        icon,
        title,
        description,
        example,
    ) in zip(
        structure_cols,
        structure_data,
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

                    <small>
                        예: {example}
                    </small>

                </div>
                """
            )

    st.info(
        """
        💡 지금은 각각의 자료 구조를 깊게 학습하기보다

        **데이터를 어떤 방식으로 저장하느냐가
        알고리즘에 영향을 줄 수 있다**

        는 점을 이해하면 됩니다.
        """
    )

    st.markdown("---")

    st.success(
        """
        ✅ **핵심 정리**

        자료 구조는 데이터를 저장하고 관리하는 방법이며,
        알고리즘은 저장된 데이터를 이용하여
        문제를 해결하는 절차입니다.
        """
    )


# =========================================================
# ② 예제로 이해하기
# =========================================================
with example_tab:

    st.markdown("## 🔍 학생 점수에서 가장 높은 점수 찾기")

    st.markdown(
        """
다음과 같은 학생들의 점수가 있다고 생각해 봅시다.
"""
    )

    st.code(
        """
[78, 92, 85, 67, 95]
        """.strip(),
        language="text",
    )

    st.markdown(
        """
이 점수들은 하나의 **리스트 형태의 자료 구조**로 생각할 수 있습니다.

이제 목록의 값을 차례대로 확인하면서
가장 높은 점수를 찾는 알고리즘을 생각해 봅시다.
"""
    )

    render_html(
        """
        <div class="info-card">

            <div class="info-card-icon">
                🔍
            </div>

            <div class="info-card-content">

                <strong>
                    최댓값 찾기 알고리즘
                </strong>

                <p>
                    ① 첫 번째 값을 현재 최댓값으로 정한다.<br>
                    ② 다음 값을 현재 최댓값과 비교한다.<br>
                    ③ 더 큰 값이 있으면 최댓값을 변경한다.<br>
                    ④ 모든 값을 확인할 때까지 반복한다.<br>
                    ⑤ 최댓값을 출력한다.
                </p>

            </div>

        </div>
        """
    )

    st.success(
        """
        ✅ 이 문제에서

        **자료 구조**는 점수를 저장한 목록이고,

        **알고리즘**은 목록을 하나씩 확인하여
        가장 큰 값을 찾는 과정입니다.
        """
    )

    st.markdown("---")

    st.markdown("## 📚 도서관에서도 같은 원리를 찾을 수 있습니다")

    st.markdown(
        """
도서관의 책이 아무런 기준 없이 놓여 있다면
원하는 책을 찾기 어렵습니다.

하지만 책을

**분야별 → 분류 번호별 → 제목별**

등의 기준으로 정리하면
원하는 책을 더 쉽게 찾을 수 있습니다.

컴퓨터에서도 데이터를 적절하게 정리하면
필요한 데이터를 더 효율적으로 처리할 수 있습니다.
"""
    )

    st.info(
        """
        💡 자료 구조와 알고리즘은 서로 따로 떨어진 개념이 아니라
        함께 문제 해결의 효율을 결정합니다.
        """
    )


# =========================================================
# ③ 직접 찾아보기
# =========================================================
with activity_tab:

    st.markdown("## 🧠 데이터에서 원하는 값을 찾아봅시다")

    st.markdown(
        """
다음과 같은 데이터가 저장되어 있습니다.
"""
    )

    numbers = [
        15,
        32,
        8,
        41,
        27,
        50,
        19,
    ]

    st.code(
        str(numbers),
        language="text",
    )

    target = st.selectbox(
        "찾고 싶은 값을 선택하세요.",
        numbers,
        index=None,
        placeholder="값을 선택하세요.",
        key="lesson_1_3_target",
    )

    if st.button(
        "값 찾아보기",
        key="lesson_1_3_find",
        type="primary",
        use_container_width=True,
    ):

        if target is None:

            st.warning(
                "찾을 값을 먼저 선택해 주세요."
            )

        else:

            position = (
                numbers.index(target) + 1
            )

            st.success(
                f"✅ **{target}**은(는) "
                f"왼쪽에서 **{position}번째** 위치에 있습니다."
            )

            st.info(
                """
                컴퓨터도 이와 비슷하게
                데이터를 앞에서부터 하나씩 확인하면서
                원하는 값을 찾을 수 있습니다.
                """
            )

    st.markdown("---")

    st.markdown("### 🔎 직접 탐색 과정을 생각해 봅시다")

    search_answer = st.radio(
        "목록 `[15, 32, 8, 41, 27]`에서 41을 앞에서부터 찾는다면 몇 번째에 발견할까요?",
        [
            "1번째",
            "2번째",
            "3번째",
            "4번째",
        ],
        index=None,
        key="lesson_1_3_search_answer",
    )

    if search_answer == "4번째":

        st.success(
            "정답입니다! ✅ 앞에서부터 확인하면 41은 4번째에 있습니다."
        )

    elif search_answer is not None:

        st.error(
            "목록을 왼쪽부터 하나씩 확인해 보세요."
        )

    st.markdown("---")

    st.markdown("### 💭 생각해 보기")

    student_answer = st.text_area(
        "데이터를 일정한 기준으로 정리해 두면 어떤 점이 좋을까요?",
        placeholder=(
            "예: 필요한 데이터를 더 쉽게 찾을 수 있다."
        ),
        height=130,
        key="lesson_1_3_activity",
    )

    if st.button(
        "생각 확인하기",
        key="lesson_1_3_activity_check",
    ):

        if student_answer.strip():

            st.success(
                """
                좋아요! ✅

                데이터를 적절한 구조로 정리해 두면
                검색, 비교, 수정과 같은 작업을
                더 쉽게 수행할 수 있습니다.
                """
            )

        else:

            st.warning(
                "생각한 내용을 작성해 주세요."
            )


# =========================================================
# ④ 형성평가
# =========================================================
with quiz_tab:

    st.markdown("## 📝 1-3 형성평가")

    st.caption(
        """
자료 구조의 의미와
자료 구조와 알고리즘의 관계를 이해했는지 확인해 봅시다.
"""
    )

    q1 = st.radio(
        "1. 자료 구조에 대한 설명으로 가장 적절한 것은 무엇인가요?",
        [
            "데이터를 저장하고 관리하는 방법",
            "컴퓨터의 전원을 켜는 방법",
            "인터넷에 연결하는 방법",
            "프로그램을 삭제하는 방법",
        ],
        index=None,
        key="quiz_1_3_q1",
    )

    q2 = st.radio(
        "2. 자료 구조에 저장된 데이터를 이용하여 문제를 해결하는 절차는 무엇인가요?",
        [
            "알고리즘",
            "모니터",
            "운영체제",
            "네트워크",
        ],
        index=None,
        key="quiz_1_3_q2",
    )

    q3 = st.radio(
        "3. 여러 데이터를 순서대로 저장하는 대표적인 자료 구조는 무엇인가요?",
        [
            "리스트",
            "모니터",
            "CPU",
            "키보드",
        ],
        index=None,
        key="quiz_1_3_q3",
    )

    q4 = st.radio(
        "4. 자료 구조와 알고리즘의 관계에 대한 설명으로 가장 적절한 것은 무엇인가요?",
        [
            "자료 구조는 데이터를 저장하고 알고리즘은 데이터를 처리한다.",
            "자료 구조와 알고리즘은 서로 관계가 없다.",
            "자료 구조는 컴퓨터를 종료하는 방법이다.",
            "알고리즘은 데이터를 저장하기만 한다.",
        ],
        index=None,
        key="quiz_1_3_q4",
    )

    q5 = st.radio(
        "5. 데이터를 적절한 구조로 정리하는 이유로 가장 적절한 것은 무엇인가요?",
        [
            "필요한 데이터를 효율적으로 처리하기 위해서",
            "컴퓨터의 크기를 줄이기 위해서",
            "키보드 색상을 바꾸기 위해서",
            "인터넷 속도를 항상 두 배로 만들기 위해서",
        ],
        index=None,
        key="quiz_1_3_q5",
    )

    if st.button(
        "형성평가 제출",
        key="submit_quiz_1_3",
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
                "데이터를 저장하고 관리하는 방법",
                "알고리즘",
                "리스트",
                "자료 구조는 데이터를 저장하고 알고리즘은 데이터를 처리한다.",
                "필요한 데이터를 효율적으로 처리하기 위해서",
            ]

            score = sum(
                answer == correct
                for answer, correct in zip(
                    answers,
                    correct_answers,
                )
            )

            st.session_state.lesson_1_3_score = score

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
                    "자료 구조와 알고리즘의 관계를 다시 확인해 봅시다."
                )

            else:

                st.error(
                    f"🔄 **{score} / 5점**입니다. "
                    "개념 학습 내용을 다시 살펴보세요."
                )

            if score >= 4:

                st.session_state.unit1_progress[
                    "1-3"
                ] = True

                st.success(
                    "✅ 1-3 자료 구조와 알고리즘 학습을 완료했습니다."
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
        "1-3",
        False,
    )
)


if is_completed:

    st.success(
        "🎉 **1-3 자료 구조와 알고리즘** 학습을 완료했습니다."
    )

    if (
        st.session_state.lesson_1_3_score
        is not None
    ):

        st.markdown(
            "형성평가 점수: "
            f"**{st.session_state.lesson_1_3_score} / 5점**"
        )

else:

    st.info(
        """
형성평가에서 4점 이상을 받으면
1-3 학습이 완료됩니다.
"""
    )


# =========================================================
# 핵심 정리
# =========================================================
with st.expander(
    "📚 1-3 핵심 내용 다시 보기",
    expanded=False,
):

    st.markdown(
        """
### 자료 구조

데이터를 효율적으로 저장하고 관리하기 위한 방법입니다.

### 알고리즘

자료 구조에 저장된 데이터를 이용하여
문제를 해결하는 절차입니다.

### 대표적인 자료 구조

- **리스트**: 여러 데이터를 순서대로 저장
- **스택**: 나중에 들어온 데이터를 먼저 처리
- **큐**: 먼저 들어온 데이터를 먼저 처리

### 자료 구조와 알고리즘의 관계

**자료 구조 → 데이터를 어떻게 저장할 것인가?**

**알고리즘 → 저장된 데이터를 어떻게 처리할 것인가?**

### 핵심 문장

> **데이터를 적절하게 정리하면 알고리즘을 더 효율적으로 수행할 수 있다.**
"""
    )


# =========================================================
# 페이지 이동
# =========================================================
render_html("<br>")

nav_left, nav_right = st.columns(2)


with nav_left:

    if st.button(
        "← 1-2 알고리즘 표현 방법",
        use_container_width=True,
    ):

        st.switch_page(
            "pages/01_02_알고리즘표현방법.py"
        )


with nav_right:

    if st.button(
        "Ⅱ. 추상화와 모델링 →",
        use_container_width=True,
        type="primary",
    ):

        st.switch_page(
            "pages/02_2단원.py"
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
            Ⅰ. 알고리즘 개요 · 1-3 자료 구조와 알고리즘
        </span>

    </div>
    """
)