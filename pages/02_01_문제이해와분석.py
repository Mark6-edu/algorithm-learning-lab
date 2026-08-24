import streamlit as st

from utils.ui import (
    load_css,
    render_html,
)


# =========================================================
# 페이지 설정
# =========================================================
st.set_page_config(
    page_title="2-1 문제 이해와 분석",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_css("assets/style.css")

# 2-1
COLAB_URL = (
    "https://colab.research.google.com/github/"
    "Mark6-edu/"
    "algorithm-learning-lab/"
    "blob/main/"
    "notebooks/unit2/lesson_2_1.ipynb"
)

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

    st.markdown("### Ⅱ. 추상화와 모델링")

    if st.button(
        "← 2단원으로 돌아가기",
        use_container_width=True,
    ):
        st.switch_page(
            "pages/02_2단원.py"
        )

    st.markdown("---")

    st.button(
        "2-1  문제 이해와 분석",
        type="primary",
        use_container_width=True,
    )

    if st.button(
        "2-2  문제 분해와 모델링",
        use_container_width=True,
    ):
        st.switch_page(
            "pages/02_02_문제분해와모델링.py"
        )

    if st.button(
        "2-3  알고리즘 설계",
        use_container_width=True,
    ):
        st.switch_page(
            "pages/02_03_알고리즘설계.py"
        )

    if st.button(
        "2-4  알고리즘 성능 분석",
        use_container_width=True,
    ):
        st.switch_page(
            "pages/02_04_알고리즘성능분석.py"
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
        Ⅱ. 추상화와 모델링 &nbsp;›&nbsp;
        2-1 문제 이해와 분석
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
                UNIT Ⅱ · LESSON 01
            </div>

            <h2>
                문제 이해와 분석
            </h2>

            <p>
                알고리즘을 설계하기 전에 가장 먼저 해야 할 일은
                해결하려는 문제가 무엇인지 정확하게 이해하는 것입니다.
                현재 상태와 목표 상태를 구분하고,
                목표 상태에 도달하기 위해 필요한 작업을 분석해 봅시다.
            </p>

        </div>

        <div class="hero-visual">

            <div class="code-window">

                <div class="code-window-header">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>

                <pre>현재 상태
    ↓
문제 분석
    ↓
필요한 작업
    ↓
목표 상태</pre>

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
                현재 상태와 목표 상태를 구분하고
                문제 해결에 필요한 작업을 분석합니다.
            </p>

        </div>

    </div>
    """
)


goal_cols = st.columns(3)

goal_data = [
    (
        "📍",
        "현재 상태",
        "문제 해결을 시작하기 전의 상황을 설명할 수 있습니다.",
    ),
    (
        "🎯",
        "목표 상태",
        "문제를 해결한 뒤 도달해야 하는 상태를 설명할 수 있습니다.",
    ),
    (
        "⚙️",
        "필요한 작업",
        "현재 상태에서 목표 상태로 이동하기 위한 작업을 분석할 수 있습니다.",
    ),
]

for col, (
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
# 학습 탭
# =========================================================
render_html(
    """
    <div class="section-header section-space">

        <div>

            <div class="section-label">
                LEARNING
            </div>

            <h3>
                문제 해결 과정을 알아봅시다
            </h3>

        </div>

    </div>
    """
)


(
    concept_tab,
    example_tab,
    activity_tab,
    python_tab,
    quiz_tab,
) = st.tabs(
    [
        "📘 개념 학습",
        "💡 예제 분석",
        "🧠 문제 분석 활동",
        "🐍 Python 연결",
        "📝 형성평가",
    ]
)


# =========================================================
# 1. 개념 학습
# =========================================================
with concept_tab:

    st.markdown("## 1. 문제란 무엇일까요?")

    st.write(
        """
        우리가 원하는 결과와 현재 상황이 서로 다를 때
        해결해야 할 **문제**가 발생합니다.

        알고리즘을 설계하려면 먼저 문제 상황을 정확하게 이해해야 합니다.
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
                    문제 분석의 첫 번째 질문
                </strong>

                <p>
                    지금 어떤 상황인가?
                </p>

            </div>

        </div>
        """
    )

    st.markdown("---")

    st.markdown("## 2. 현재 상태")

    st.markdown(
        """
        **현재 상태(Current State)**는 문제 해결을 시작하기 전의 상황을 의미합니다.

        현재 상태를 정확하게 파악해야 어떤 작업이 필요한지 결정할 수 있습니다.
        """
    )

    st.markdown("### 예시")

    st.info(
        """
        학교 도서관에서 원하는 책을 찾으려고 합니다.

        현재 상태:
        책의 제목은 알고 있지만,
        책이 어느 위치에 있는지는 모릅니다.
        """
    )

    st.markdown("---")

    st.markdown("## 3. 목표 상태")

    st.write(
        """
        **목표 상태(Goal State)**는
        문제를 해결한 뒤 도달하고자 하는 상태입니다.

        어떤 상태가 되면 문제가 해결된 것인지
        분명하게 정해야 합니다.
        """
    )

    st.success(
        """
        목표 상태:
        원하는 책의 위치를 알아내고
        실제로 해당 책을 찾습니다.
        """
    )

    st.markdown("---")

    st.markdown("## 4. 수행해야 할 작업")

    st.write(
        """
        현재 상태에서 목표 상태에 도달하려면
        하나 이상의 작업을 수행해야 합니다.

        이러한 작업을 찾아내는 과정이
        알고리즘 설계의 출발점입니다.
        """
    )

    st.markdown(
        """
        **도서관 예시**

        1. 책의 제목을 확인한다.
        2. 도서 검색 시스템에서 제목을 검색한다.
        3. 책의 위치를 확인한다.
        4. 해당 책장으로 이동한다.
        5. 책을 찾는다.
        """
    )

    st.warning(
        """
        이 단계에서는 Python 코드를 먼저 작성하기보다
        문제 상황과 해결 목표를 정확히 이해하는 것이 중요합니다.
        """
    )


# =========================================================
# 2. 예제 분석
# =========================================================
with example_tab:

    st.markdown(
        "## 예제: 학생 중 가장 높은 점수 찾기"
    )

    st.write(
        """
        학생 5명의 시험 점수 중
        가장 높은 점수를 찾으려고 합니다.
        """
    )

    st.code(
        "78, 92, 85, 67, 95",
        language="text",
    )

    st.markdown("### ① 현재 상태")

    st.info(
        """
        학생들의 점수는 알고 있지만
        가장 높은 점수가 무엇인지는 아직 모르는 상태입니다.
        """
    )

    st.markdown("### ② 목표 상태")

    st.success(
        """
        학생들의 점수 중
        가장 높은 점수인 95를 찾아낸 상태입니다.
        """
    )

    st.markdown("### ③ 필요한 작업")

    st.markdown(
        """
        1. 학생들의 점수를 확인한다.
        2. 하나의 점수를 기준값으로 정한다.
        3. 다른 점수와 기준값을 비교한다.
        4. 더 큰 점수가 있으면 기준값을 변경한다.
        5. 모든 점수를 확인할 때까지 반복한다.
        6. 가장 큰 값을 출력한다.
        """
    )

    st.markdown("### 문제 분석 표")

    st.dataframe(
        {
            "구분": [
                "현재 상태",
                "목표 상태",
                "수행해야 할 작업",
            ],
            "분석": [
                "여러 점수가 있지만 가장 높은 점수를 모른다.",
                "가장 높은 점수를 찾아낸다.",
                "점수를 하나씩 비교하여 가장 큰 값을 찾는다.",
            ],
        },
        hide_index=True,
        width="stretch",
    )


# =========================================================
# 3. 문제 분석 활동
# =========================================================
with activity_tab:

    st.markdown(
        "## 🧠 직접 문제를 분석해 봅시다"
    )

    st.write(
        """
        다음 문제에서 현재 상태, 목표 상태,
        수행해야 할 작업을 직접 분석해 보세요.
        """
    )

    render_html(
        """
        <div class="info-card">

            <div class="info-card-icon">
                🌡️
            </div>

            <div class="info-card-content">

                <strong>
                    문제 상황
                </strong>

                <p>
                    학교 교실의 온도가 너무 높습니다.
                    온도 센서로 현재 온도를 측정하고,
                    일정 온도 이상이면 선풍기를 작동시키려고 합니다.
                </p>

            </div>

        </div>
        """
    )

    current_state = st.text_area(
        "① 현재 상태는 무엇인가요?",
        placeholder=(
            "예: 교실의 온도가 높지만 "
            "현재 온도를 정확히 모른다."
        ),
        key="activity_2_1_current",
    )

    goal_state = st.text_area(
        "② 목표 상태는 무엇인가요?",
        placeholder=(
            "예: 온도를 확인하고 "
            "필요한 경우 선풍기를 작동한다."
        ),
        key="activity_2_1_goal",
    )

    tasks = st.text_area(
        "③ 어떤 작업이 필요할까요?",
        placeholder=(
            "1. 현재 온도를 측정한다.\n"
            "2. 기준 온도와 비교한다.\n"
            "3. 기준 이상이면 선풍기를 켠다."
        ),
        height=150,
        key="activity_2_1_tasks",
    )

    if st.button(
        "분석 내용 확인하기",
        key="check_activity_2_1",
        type="primary",
    ):

        if (
            current_state.strip()
            and goal_state.strip()
            and tasks.strip()
        ):

            st.success(
                """
                좋습니다! 현재 상태 → 목표 상태 →
                필요한 작업의 순서로 문제를 분석했습니다. ✅
                """
            )

        else:

            st.warning(
                "세 항목을 모두 작성해 주세요."
            )

    with st.expander(
        "💡 예시 답안 보기"
    ):

        st.markdown(
            """
            **현재 상태**

            교실의 온도가 높지만
            정확한 현재 온도를 확인해야 한다.

            **목표 상태**

            현재 온도를 확인하고,
            기준 온도 이상이면 선풍기를 작동한다.

            **필요한 작업**

            1. 온도를 측정한다.
            2. 기준 온도와 비교한다.
            3. 기준 이상이면 선풍기를 켠다.
            4. 기준 미만이면 선풍기를 끈다.
            """
        )


# =========================================================
# ④ Python 연결 + Colab 실습
# =========================================================
with python_tab:

    st.markdown(
        "## 🐍 문제 분석을 Python으로 연결해 봅시다"
    )

    st.markdown(
        """
앞에서 학습한 **현재 상태, 목표 상태, 필요한 작업**이
Python 문제 해결 과정에서는 어떻게 연결되는지 살펴봅시다.

예제를 확인한 뒤에는 Google Colab에서
직접 값을 바꾸고 코드를 실행해 봅니다.
"""
    )

    st.markdown("### 1. 문제 상황")

    st.code(
        """
scores = [78, 92, 85, 67, 95]

print(scores)
        """.strip(),
        language="python",
    )

    st.info(
        """
        💡 현재 상태:
        여러 점수가 있지만 아직 가장 높은 점수를 모릅니다.
        """
    )

    st.markdown("---")

    st.markdown("### 2. 필요한 작업")

    st.code(
        """
scores = [78, 92, 85, 67, 95]

max_score = scores[0]

for score in scores:
    if score > max_score:
        max_score = score

print(max_score)
        """.strip(),
        language="python",
    )

    st.success(
        """
        🎯 목표 상태:
        모든 점수를 비교하여 가장 높은 점수인 95를 찾았습니다.
        """
    )

    st.markdown("#### 출력 결과를 예상해 봅시다")

    answer = st.radio(
        "위 코드의 출력 결과는 무엇일까요?",
        [
            "78",
            "85",
            "92",
            "95",
        ],
        index=None,
        key="python_2_1_answer",
    )

    if answer == "95":
        st.success("정답입니다! ✅")

    elif answer is not None:
        st.error(
            "max_score가 어떤 경우에 변경되는지 다시 확인해 보세요."
        )

    st.markdown("---")

    render_html(
        """
        <div class="colab-banner">

            <div>

                <div class="section-label">
                    PROBLEM ANALYSIS LAB
                </div>

                <h3>
                    직접 문제를 분석하고 실행해 봅시다
                </h3>

                <p>
                    Google Colab에서 현재 상태와 목표 상태를 확인하고,
                    필요한 작업을 Python 코드로 직접 구현해 봅니다.
                </p>

            </div>

            <div class="colab-logo">
                🔎
            </div>

        </div>
        """
    )

    st.markdown("### 🚀 Colab 실습 내용")

    practice_cols = st.columns(4)

    practice_data = [
        (
            "01",
            "📍",
            "현재 상태",
            "주어진 데이터와 문제 상황을 확인합니다.",
        ),
        (
            "02",
            "⚙️",
            "필요한 작업",
            "최댓값을 찾는 비교 과정을 구현합니다.",
        ),
        (
            "03",
            "🎯",
            "목표 상태",
            "입력·처리·출력의 관계를 확인합니다.",
        ),
        (
            "04",
            "🏆",
            "도전 문제",
            "세 수 중 가장 큰 값을 찾아봅니다.",
        ),
    ]

    for col, (
        step,
        icon,
        title,
        description,
    ) in zip(
        practice_cols,
        practice_data,
    ):

        with col:

            render_html(
                f"""
                <div class="learning-flow-card">

                    <div class="flow-step">
                        PRACTICE {step}
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

    st.markdown("---")

    st.link_button(
        "🚀 Google Colab에서 문제 분석 실습하기",
        COLAB_URL,
        use_container_width=True,
        type="primary",
    )

    st.caption(
        """
        Colab에서 각 코드 셀을 실행한 뒤
        데이터 값을 직접 수정하면서 결과 변화를 확인해 보세요.
        """
    )

# =========================================================
# 5. 형성평가
# =========================================================
with quiz_tab:

    st.markdown("## 📝 2-1 형성평가")

    st.caption(
        "현재 상태, 목표 상태, 수행해야 할 작업에 대한 내용을 확인합니다."
    )

    # -----------------------------------------------------
    # 1번
    # -----------------------------------------------------
    q1 = st.radio(
        "1. 문제 해결을 시작하기 전의 상황을 무엇이라고 하나요?",
        [
            "현재 상태",
            "목표 상태",
            "반복 상태",
            "종료 상태",
        ],
        index=None,
        key="quiz_2_1_q1",
    )

    # -----------------------------------------------------
    # 2번
    # -----------------------------------------------------
    q2 = st.radio(
        "2. 문제 해결 후 도달하고자 하는 상태는 무엇인가요?",
        [
            "현재 상태",
            "입력 상태",
            "목표 상태",
            "초기 상태",
        ],
        index=None,
        key="quiz_2_1_q2",
    )

    # -----------------------------------------------------
    # 3번
    # -----------------------------------------------------
    q3 = st.radio(
        "3. 현재 상태를 파악한 다음 가장 적절한 과정은?",
        [
            "무조건 Python 코드를 작성한다.",
            "목표 상태를 확인한다.",
            "프로그램을 종료한다.",
            "모든 데이터를 삭제한다.",
        ],
        index=None,
        key="quiz_2_1_q3",
    )

    # -----------------------------------------------------
    # 4번
    # -----------------------------------------------------
    q4 = st.radio(
        "4. 모든 점수를 차례대로 비교하는 것은 문제 분석의 어느 요소에 해당하나요?",
        [
            "현재 상태",
            "목표 상태",
            "수행해야 할 작업",
            "문제의 이름",
        ],
        index=None,
        key="quiz_2_1_q4",
    )

    # -----------------------------------------------------
    # 5번
    # -----------------------------------------------------
    q5 = st.radio(
        "5. 문제 해결을 위해 가장 먼저 해야 할 일은?",
        [
            "코드를 길게 작성한다.",
            "문제 상황과 목표를 이해한다.",
            "무조건 반복문을 사용한다.",
            "실행 시간을 측정한다.",
        ],
        index=None,
        key="quiz_2_1_q5",
    )

    # -----------------------------------------------------
    # 제출
    # -----------------------------------------------------
    if st.button(
        "형성평가 제출",
        key="submit_quiz_2_1",
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

        # 하나라도 선택하지 않은 문항이 있으면 제출하지 않음
        if any(answer is None for answer in answers):

            st.warning(
                "⚠️ 모든 문항에 답한 후 제출해 주세요."
            )

        else:

            correct_answers = [
                "현재 상태",
                "목표 상태",
                "목표 상태를 확인한다.",
                "수행해야 할 작업",
                "문제 상황과 목표를 이해한다.",
            ]

            score = sum(
                answer == correct
                for answer, correct in zip(
                    answers,
                    correct_answers,
                )
            )

            st.session_state.lesson_2_1_score = score

            # -------------------------------------------------
            # 결과
            # -------------------------------------------------
            if score == 5:

                st.success(
                    "🎉 모두 정답입니다! **5 / 5점**"
                )

            elif score >= 4:

                st.success(
                    f"👏 잘했습니다! **{score} / 5점**입니다."
                )

            elif score >= 3:

                st.warning(
                    f"📚 **{score} / 5점**입니다. "
                    "틀린 내용을 다시 확인해 보세요."
                )

            else:

                st.error(
                    f"🔄 **{score} / 5점**입니다. "
                    "개념 학습을 다시 살펴보세요."
                )

            # -------------------------------------------------
            # 4점 이상이면 학습 완료
            # -------------------------------------------------
            if score >= 4:

                st.session_state.unit2_progress[
                    "2-1"
                ] = True

                st.success(
                    "✅ 2-1 문제 이해와 분석 학습을 완료했습니다."
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


is_completed = st.session_state.unit2_progress.get(
    "2-1",
    False,
)

if is_completed:

    st.success(
        "🎉 **2-1 문제 이해와 분석**을 완료했습니다."
    )

    if (
        st.session_state.lesson_2_1_score
        is not None
    ):

        st.write(
            f"형성평가 점수: "
            f"**{st.session_state.lesson_2_1_score} / 5점**"
        )

else:

    st.info(
        """
        형성평가에서 4점 이상을 받으면
        2-1 학습이 완료됩니다.
        """
    )


# =========================================================
# 핵심 정리
# =========================================================
with st.expander(
    "📚 2-1 핵심 내용 다시 보기",
    expanded=False,
):

    st.markdown(
        """
        ### 현재 상태
        문제 해결을 시작하기 전의 상황

        ### 목표 상태
        문제 해결 후 도달하고자 하는 상황

        ### 수행해야 할 작업
        현재 상태에서 목표 상태로 이동하기 위해 필요한 과정

        ### 기본 흐름

        **현재 상태 → 필요한 작업 분석 → 목표 상태**
        """
    )


# =========================================================
# 페이지 이동
# =========================================================
render_html(
    "<br>"
)

nav_left, nav_right = st.columns(2)

with nav_left:

    if st.button(
        "← 2단원 목록으로",
        use_container_width=True,
    ):
        st.switch_page(
            "pages/02_2단원.py"
        )

with nav_right:

    if st.button(
        "2-2 문제 분해와 모델링 →",
        use_container_width=True,
        type="primary",
    ):
        st.switch_page(
            "pages/02_02_문제분해와모델링.py"
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
            Ⅱ. 추상화와 모델링 · 2-1 문제 이해와 분석
        </span>

    </div>
    """
)