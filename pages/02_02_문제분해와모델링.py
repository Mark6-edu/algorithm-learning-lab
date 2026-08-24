import streamlit as st

from utils.ui import (
    load_css,
    render_html,
)


# =========================================================
# 페이지 설정
# =========================================================
st.set_page_config(
    page_title="2-2 문제 분해와 모델링",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_css("assets/style.css")

# 2-2
COLAB_URL = (
    "https://colab.research.google.com/github/"
    "Mark6-edu/"
    "algorithm-learning-lab/"
    "blob/main/"
    "notebooks/unit2/lesson_2_2.ipynb"
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

if "lesson_2_2_score" not in st.session_state:
    st.session_state.lesson_2_2_score = None


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

    if st.button(
        "2-1  문제 이해와 분석",
        use_container_width=True,
    ):
        st.switch_page(
            "pages/02_01_문제이해와분석.py"
        )

    st.button(
        "2-2  문제 분해와 모델링",
        type="primary",
        use_container_width=True,
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
        2-2 문제 분해와 모델링
    </div>
    """
)


# =========================================================
# 학습 Hero
# =========================================================
render_html(
    """
    <div class="hero-section">

        <div class="hero-content">

            <div class="hero-tag">
                UNIT Ⅱ · LESSON 02
            </div>

            <h2>
                문제 분해와 모델링
            </h2>

            <p>
                복잡한 문제를 한 번에 해결하려고 하면
                해결 과정이 어렵고 복잡해질 수 있습니다.
                문제를 작은 문제로 나누고,
                필요한 요소만 추출하여 단순한 형태로 표현하는
                방법을 학습합니다.
            </p>

        </div>

        <div class="hero-visual">

            <div class="code-window">

                <div class="code-window-header">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>

                <pre>복잡한 문제
     ↓
문제 분해
     ↓
작은 문제들
     ↓
핵심 요소 추출
     ↓
추상화
     ↓
모델링</pre>

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
                복잡한 문제를 작은 문제로 나누고,
                핵심 요소를 추출하여 해결 가능한 형태로 모델링합니다.
            </p>

        </div>

    </div>
    """
)


goal_cols = st.columns(3)

goal_data = [
    (
        "01",
        "🧩",
        "문제 분해",
        """
        복잡한 문제를 해결 가능한
        작은 문제로 나눌 수 있습니다.
        """,
    ),
    (
        "02",
        "🔍",
        "추상화",
        """
        문제 해결에 필요한 핵심 요소와
        불필요한 요소를 구분할 수 있습니다.
        """,
    ),
    (
        "03",
        "🗺️",
        "모델링",
        """
        실제 문제를 단순한 구조나
        데이터 형태로 표현할 수 있습니다.
        """,
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
                문제를 단순하게 만들어봅시다
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
        "🧠 모델링 활동",
        "🐍 Python 연결",
        "📝 형성평가",
    ]
)


# =========================================================
# ① 개념 학습
# =========================================================
with concept_tab:

    st.markdown("## 1. 문제 분해란?")

    st.write(
        """
        **문제 분해(Decomposition)**는
        복잡한 문제를 여러 개의 작은 문제로 나누는 과정입니다.

        큰 문제를 한 번에 해결하기보다
        작은 문제를 하나씩 해결하면
        전체 문제를 더 쉽게 이해하고 해결할 수 있습니다.
        """
    )

    st.success(
        "💡 핵심 질문: **이 문제를 더 작은 문제로 나눌 수 있을까?**"
    )

    st.markdown("### 예시: 학교 급식 주문 시스템")

    st.markdown(
        """
        '급식 주문 시스템을 만든다'라는 큰 문제는
        다음과 같이 작은 문제로 나눌 수 있습니다.

        1. 학생 정보를 확인한다.
        2. 메뉴를 보여준다.
        3. 학생이 메뉴를 선택한다.
        4. 선택 결과를 저장한다.
        5. 주문 결과를 확인한다.
        """
    )

    st.markdown("---")

    st.markdown("## 2. 추상화란?")

    st.write(
        """
        **추상화(Abstraction)**는
        문제를 해결하는 데 필요한 핵심 요소만 남기고
        불필요한 세부 요소를 제거하는 과정입니다.

        현실의 모든 정보를 컴퓨터에 그대로 표현할 필요는 없습니다.
        문제 해결에 필요한 정보만 선택하면 됩니다.
        """
    )

    st.success(
        "💡 핵심 질문: **이 문제를 해결하는 데 꼭 필요한 정보는 무엇일까?**"
    )

    st.markdown("### 학생 정보 예시")

    st.dataframe(
        {
            "정보": [
                "학생 이름",
                "학번",
                "급식 메뉴 선택",
                "신발 색상",
                "좋아하는 음악",
            ],
            "급식 주문에 필요한가?": [
                "필요",
                "필요",
                "필요",
                "불필요",
                "불필요",
            ],
        },
        hide_index=True,
        width="stretch",
    )

    st.markdown("---")

    st.markdown("## 3. 모델링이란?")

    st.write(
        """
        **모델링(Modeling)**은
        실제 문제의 중요한 요소와 관계를
        컴퓨터가 처리하기 쉬운 형태로 표현하는 것입니다.

        모델은 현실 세계 전체를 그대로 복제하는 것이 아니라,
        문제 해결에 필요한 부분만 단순화하여 표현합니다.
        """
    )

    st.markdown("### 급식 주문 문제 모델")

    st.code(
        """
학생
 ├─ 학번
 ├─ 이름
 └─ 선택한 메뉴

메뉴
 ├─ 메뉴 번호
 └─ 메뉴 이름
        """.strip(),
        language="text",
    )

    st.info(
        """
        문제 분해 → 추상화 → 모델링 과정을 거치면
        복잡한 현실 문제를 컴퓨터가 처리할 수 있는 형태로
        바꿀 수 있습니다.
        """
    )


# =========================================================
# ② 예제 분석
# =========================================================
with example_tab:

    st.markdown(
        "## 예제: 스마트 교실 온도 관리"
    )

    st.write(
        """
        교실의 온도를 자동으로 확인하여
        일정 온도 이상이면 선풍기를 켜는 시스템을
        만들려고 합니다.
        """
    )

    st.markdown("### ① 문제 분해")

    st.markdown(
        """
        큰 문제를 다음과 같이 나눌 수 있습니다.

        1. 현재 온도를 측정한다.
        2. 기준 온도를 설정한다.
        3. 현재 온도와 기준 온도를 비교한다.
        4. 기준 이상이면 선풍기를 켠다.
        5. 기준 미만이면 선풍기를 끈다.
        """
    )

    st.markdown("### ② 추상화")

    st.dataframe(
        {
            "정보": [
                "현재 온도",
                "기준 온도",
                "선풍기 상태",
                "교실 벽 색상",
                "학생의 이름",
            ],
            "필요 여부": [
                "필요",
                "필요",
                "필요",
                "불필요",
                "불필요",
            ],
        },
        hide_index=True,
        width="stretch",
    )

    st.markdown("### ③ 모델링")

    st.code(
        """
입력
 └─ 현재 온도

조건
 └─ 현재 온도 >= 기준 온도

출력
 └─ 선풍기 ON / OFF
        """.strip(),
        language="text",
    )

    st.markdown("### 전체 흐름")

    st.code(
        """
온도 측정
    ↓
기준 온도와 비교
    ↓
┌──────────────┐
│ 기준 이상인가? │
└──────┬───────┘
       │
   ┌───┴───┐
  YES      NO
   ↓        ↓
선풍기 ON  선풍기 OFF
        """.strip(),
        language="text",
    )


# =========================================================
# ③ 모델링 활동
# =========================================================
with activity_tab:

    st.markdown(
        "## 🧠 직접 문제를 분해해 봅시다"
    )

    st.write(
        """
        다음 문제를 작은 문제로 나누고,
        필요한 정보만 골라 모델링해 봅시다.
        """
    )

    render_html(
        """
        <div class="info-card">

            <div class="info-card-icon">
                📚
            </div>

            <div class="info-card-content">

                <strong>
                    문제 상황
                </strong>

                <p>
                    학교 도서관에서 학생이 원하는 책의 제목을 입력하면
                    책의 대출 가능 여부를 알려주는 프로그램을
                    만들려고 합니다.
                </p>

            </div>

        </div>
        """
    )

    decomposition = st.text_area(
        "① 이 문제를 작은 작업들로 나누어 보세요.",
        placeholder=(
            "예:\n"
            "1. 책 제목을 입력받는다.\n"
            "2. 도서 목록에서 책을 찾는다.\n"
            "3. 대출 여부를 확인한다."
        ),
        height=150,
        key="activity_2_2_decomposition",
    )

    important_info = st.multiselect(
        "② 문제 해결에 필요한 정보를 선택하세요.",
        [
            "책 제목",
            "대출 가능 여부",
            "책의 위치",
            "도서관 벽 색상",
            "학생의 좋아하는 음식",
            "도서 번호",
        ],
        key="activity_2_2_info",
    )

    model = st.text_area(
        "③ 입력, 처리, 출력 구조로 모델링해 보세요.",
        placeholder=(
            "입력: 책 제목\n"
            "처리: 도서 목록 검색 및 대출 상태 확인\n"
            "출력: 대출 가능 / 대출 불가"
        ),
        height=130,
        key="activity_2_2_model",
    )

    if st.button(
        "모델링 내용 확인하기",
        key="check_activity_2_2",
        type="primary",
    ):

        if (
            decomposition.strip()
            and important_info
            and model.strip()
        ):

            st.success(
                """
                좋습니다! 문제 분해 → 핵심 정보 선택 →
                모델링의 과정을 수행했습니다. ✅
                """
            )

        else:

            st.warning(
                "모든 활동을 완료한 후 확인해 주세요."
            )

    with st.expander(
        "💡 예시 답안 보기"
    ):

        st.markdown(
            """
            **문제 분해**

            1. 책 제목을 입력받는다.
            2. 도서 목록에서 책을 검색한다.
            3. 해당 책의 대출 상태를 확인한다.
            4. 결과를 사용자에게 보여준다.

            **필요한 정보**

            - 책 제목
            - 도서 번호
            - 대출 가능 여부

            **모델링**

            - 입력: 책 제목
            - 처리: 도서 검색 → 대출 상태 확인
            - 출력: 대출 가능 여부
            """
        )


# =========================================================
# ④ Python 연결 + Colab 실습
# =========================================================
with python_tab:

    st.markdown(
        "## 🐍 모델을 Python으로 표현해 봅시다"
    )

    st.markdown(
        """
앞에서 학습한 **문제 분해 → 추상화 → 모델링** 과정이
Python 코드에서는 어떻게 표현되는지 확인해 봅시다.

이후 Google Colab에서 직접 값을 변경하고
간단한 문제 모델을 만들어 봅니다.
"""
    )

    st.markdown("### 1. 문제 분해")

    st.markdown(
        """
스마트 교실의 온도를 관리하는 문제를
다음과 같은 작은 작업으로 나눌 수 있습니다.

1. 현재 온도를 확인한다.
2. 기준 온도를 설정한다.
3. 두 값을 비교한다.
4. 선풍기 상태를 결정한다.
"""
    )

    st.code(
        """
current_temp = 29
standard_temp = 28
        """.strip(),
        language="python",
    )

    st.markdown("---")

    st.markdown("### 2. 추상화와 모델링")

    st.code(
        """
current_temp = 29
standard_temp = 28

if current_temp >= standard_temp:
    fan = "ON"
else:
    fan = "OFF"

print(fan)
        """.strip(),
        language="python",
    )

    st.info(
        """
        💡 문제 해결에 필요한 핵심 요소만 남겼습니다.

        - 현재 온도
        - 기준 온도
        - 선풍기 상태
        """
    )

    st.markdown("#### 출력 결과를 예상해 봅시다")

    answer = st.radio(
        "`current_temp = 29`, `standard_temp = 28`일 때 결과는 무엇일까요?",
        [
            "ON",
            "OFF",
            "29",
            "28",
        ],
        index=None,
        key="python_2_2_answer",
    )

    if answer == "ON":

        st.success(
            """
            정답입니다! ✅
            현재 온도가 기준 온도 이상이므로 선풍기는 ON 상태가 됩니다.
            """
        )

    elif answer is not None:

        st.error(
            "`current_temp >= standard_temp` 조건을 다시 확인해 보세요."
        )

    st.markdown("---")

    st.markdown("### 3. 데이터를 모델로 표현하기")

    st.code(
        """
book = {
    "title": "알고리즘 설계",
    "available": True,
    "location": "A-03"
}

print(book["title"])
print(book["available"])
        """.strip(),
        language="python",
    )

    st.info(
        """
        💡 현실의 책 전체를 표현하는 것이 아니라,
        문제 해결에 필요한 정보만 선택하여 모델링한 것입니다.
        """
    )

    st.markdown("---")

    render_html(
        """
        <div class="colab-banner">

            <div>

                <div class="section-label">
                    MODELING LAB
                </div>

                <h3>
                    문제를 나누고 모델로 표현해 봅시다
                </h3>

                <p>
                    Google Colab에서 문제를 작은 작업으로 나누고,
                    필요한 정보만 추출하여 Python 데이터와 코드로
                    표현해 봅니다.
                </p>

            </div>

            <div class="colab-logo">
                🧩
            </div>

        </div>
        """
    )

    st.markdown("### 🚀 Colab 실습 내용")

    practice_cols = st.columns(4)

    practice_data = [
        (
            "01",
            "🧩",
            "문제 분해",
            "온도 관리 문제를 작은 작업으로 나눕니다.",
        ),
        (
            "02",
            "🔍",
            "추상화",
            "문제 해결에 필요한 정보만 선택합니다.",
        ),
        (
            "03",
            "🗺️",
            "모델링",
            "핵심 요소를 Python 데이터로 표현합니다.",
        ),
        (
            "04",
            "📚",
            "도전 문제",
            "도서 대출 가능 여부 프로그램을 구현합니다.",
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
        "🚀 Google Colab에서 모델링 실습하기",
        COLAB_URL,
        use_container_width=True,
        type="primary",
    )

    st.caption(
        """
        Colab에서 각 코드 셀을 실행하고
        온도 값, 도서 정보 등을 직접 수정해 보세요.
        """
    )

# =========================================================
# ⑤ 형성평가
# =========================================================
with quiz_tab:

    st.markdown("## 📝 2-2 형성평가")

    st.caption(
        "문제 분해, 추상화, 모델링의 개념을 확인합니다."
    )

    q1 = st.radio(
        "1. 복잡한 문제를 여러 개의 작은 문제로 나누는 것을 무엇이라고 하나요?",
        [
            "문제 분해",
            "반복",
            "정렬",
            "디버깅",
        ],
        index=None,
        key="quiz_2_2_q1",
    )

    q2 = st.radio(
        "2. 문제 해결에 필요한 핵심 요소만 남기는 과정은 무엇인가요?",
        [
            "컴파일",
            "추상화",
            "출력",
            "반복",
        ],
        index=None,
        key="quiz_2_2_q2",
    )

    q3 = st.radio(
        "3. 실제 문제를 컴퓨터가 처리하기 쉬운 형태로 표현하는 과정은 무엇인가요?",
        [
            "모델링",
            "삭제",
            "입력",
            "실행",
        ],
        index=None,
        key="quiz_2_2_q3",
    )

    q4 = st.radio(
        "4. 교실 온도 관리 문제에서 문제 해결에 가장 필요하지 않은 정보는 무엇인가요?",
        [
            "현재 온도",
            "기준 온도",
            "선풍기 상태",
            "교실 벽 색상",
        ],
        index=None,
        key="quiz_2_2_q4",
    )

    q5 = st.radio(
        "5. 문제 해결 과정을 가장 적절한 순서로 나타낸 것은 무엇인가요?",
        [
            "코딩 → 모델링 → 문제 분해",
            "문제 분해 → 추상화 → 모델링",
            "모델링 → 삭제 → 출력",
            "추상화 → 실행 → 문제 분해",
        ],
        index=None,
        key="quiz_2_2_q5",
    )

    if st.button(
        "형성평가 제출",
        key="submit_quiz_2_2",
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

        if any(answer is None for answer in answers):

            st.warning(
                "⚠️ 모든 문항에 답한 후 제출해 주세요."
            )

        else:

            correct_answers = [
                "문제 분해",
                "추상화",
                "모델링",
                "교실 벽 색상",
                "문제 분해 → 추상화 → 모델링",
            ]

            score = sum(
                answer == correct
                for answer, correct in zip(
                    answers,
                    correct_answers,
                )
            )

            st.session_state.lesson_2_2_score = score

            if score == 5:

                st.success(
                    "🎉 5문항 모두 정답입니다! **5 / 5점**"
                )

            elif score >= 4:

                st.success(
                    f"👏 잘했습니다! **{score} / 5점**입니다."
                )

            elif score >= 3:

                st.warning(
                    f"📚 **{score} / 5점**입니다. "
                    "틀린 내용을 다시 확인해 봅시다."
                )

            else:

                st.error(
                    f"🔄 **{score} / 5점**입니다. "
                    "개념 학습을 다시 살펴보세요."
                )

            if score >= 4:

                st.session_state.unit2_progress[
                    "2-2"
                ] = True

                st.success(
                    "✅ 2-2 문제 분해와 모델링 학습을 완료했습니다."
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
    "2-2",
    False,
)

if is_completed:

    st.success(
        "🎉 **2-2 문제 분해와 모델링**을 완료했습니다."
    )

    if (
        st.session_state.lesson_2_2_score
        is not None
    ):

        st.write(
            "형성평가 점수: "
            f"**{st.session_state.lesson_2_2_score} / 5점**"
        )

else:

    st.info(
        """
        형성평가에서 4점 이상을 받으면
        2-2 학습이 완료됩니다.
        """
    )


# =========================================================
# 핵심 정리
# =========================================================
with st.expander(
    "📚 2-2 핵심 내용 다시 보기",
    expanded=False,
):

    st.markdown(
        """
        ### 1. 문제 분해
        복잡한 문제를 작은 문제로 나누는 과정

        ### 2. 추상화
        문제 해결에 필요한 핵심 요소만 남기는 과정

        ### 3. 모델링
        현실 문제를 컴퓨터가 처리하기 쉬운 형태로 표현하는 과정

        ### 기본 흐름

        **복잡한 문제 → 문제 분해 → 추상화 → 모델링**

        좋은 알고리즘을 설계하기 위해서는
        문제를 적절하게 단순화하고 구조화하는 과정이 중요합니다.
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
        "← 2-1 문제 이해와 분석",
        use_container_width=True,
    ):
        st.switch_page(
            "pages/02_01_문제이해와분석.py"
        )

with nav_right:

    if st.button(
        "2-3 알고리즘 설계 →",
        use_container_width=True,
        type="primary",
    ):
        st.switch_page(
            "pages/02_03_알고리즘설계.py"
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
            Ⅱ. 추상화와 모델링 · 2-2 문제 분해와 모델링
        </span>

    </div>
    """
)