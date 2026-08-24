import streamlit as st

from utils.ui import (
    load_css,
    render_html,
)


# =========================================================
# 페이지 설정
# =========================================================
st.set_page_config(
    page_title="2-3 알고리즘 설계",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_css("assets/style.css")


# =========================================================
# 이미지 경로
# =========================================================
SEQUENCE_FLOWCHART = (
    "assets/images/unit2/flowchart_sequence.png"
)

SELECTION_FLOWCHART = (
    "assets/images/unit2/flowchart_selection.png"
)

REPETITION_FLOWCHART = (
    "assets/images/unit2/flowchart_repetition.png"
)


# =========================================================
# Google Colab URL
# =========================================================
COLAB_URL = (
    "https://colab.research.google.com/github/"
    "Mark6-edu/"
    "algorithm-learning-lab/"
    "blob/main/"
    "notebooks/unit2/lesson_2_3.ipynb"
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

if "lesson_2_3_score" not in st.session_state:
    st.session_state.lesson_2_3_score = None


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

    if st.button(
        "2-2  문제 분해와 모델링",
        use_container_width=True,
    ):
        st.switch_page(
            "pages/02_02_문제분해와모델링.py"
        )

    st.button(
        "2-3  알고리즘 설계",
        type="primary",
        use_container_width=True,
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
        2-3 알고리즘 설계
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
                UNIT Ⅱ · LESSON 03
            </div>

            <h2>
                알고리즘 설계
            </h2>

            <p>
                문제를 분석하고 모델링한 뒤에는
                실제로 어떤 순서와 조건으로 문제를 해결할지
                구체적인 절차를 설계해야 합니다.
                <br><br>
                순차, 선택, 반복 구조를 이해하고
                순서도와 의사코드, Python 코드로
                알고리즘을 표현해 봅시다.
            </p>

        </div>

        <div class="hero-visual">

            <div class="code-window">

                <div class="code-window-header">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>

                <pre>문제 분석
    ↓
모델링
    ↓
해결 절차 설계
    ↓
순차 · 선택 · 반복
    ↓
순서도 · 의사코드
    ↓
Python 구현</pre>

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
                순차, 선택, 반복 구조를 이해하고
                문제 해결 절차를 알고리즘으로 표현합니다.
            </p>

        </div>

    </div>
    """
)


goal_cols = st.columns(3)

goal_data = [
    (
        "01",
        "➡️",
        "순차 구조",
        "작업이 정해진 순서대로 실행되는 구조를 이해합니다.",
    ),
    (
        "02",
        "🔀",
        "선택 구조",
        "조건에 따라 서로 다른 작업을 선택하는 구조를 이해합니다.",
    ),
    (
        "03",
        "🔁",
        "반복 구조",
        "조건에 따라 같은 작업을 반복하는 구조를 이해합니다.",
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
                해결 절차를 알고리즘으로 표현해 봅시다
            </h3>

            <p>
                개념을 이해한 뒤 교과서의 순서도를 살펴보고,
                이를 Python 코드와 연결해 봅시다.
            </p>

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
        "🧠 알고리즘 설계 활동",
        "🐍 Python 연결",
        "📝 형성평가",
    ]
)


# =========================================================
# ① 개념 학습
# =========================================================
with concept_tab:

    # -----------------------------------------------------
    # 1. 알고리즘
    # -----------------------------------------------------
    st.markdown("## 1. 알고리즘이란?")

    st.markdown(
        """
**알고리즘(Algorithm)**은 문제를 해결하기 위해
정해진 순서에 따라 수행하는 명확한 절차입니다.

문제를 정확하게 이해하고 모델링했다면,
그 다음에는 **어떤 작업을 어떤 순서로 수행할 것인지**
구체적으로 정해야 합니다.
"""
    )

    st.success(
        "💡 핵심 질문: 문제를 해결하기 위해 무엇을 어떤 순서로 해야 할까요?"
    )

    st.info(
        """
        알고리즘은 자연어, 의사코드, 순서도,
        프로그래밍 언어 등 다양한 방법으로 표현할 수 있습니다.
        """
    )

    st.markdown("---")

    # -----------------------------------------------------
    # 2. 순차 구조
    # -----------------------------------------------------
    st.markdown("## 2. 순차 구조")

    st.markdown(
        """
**순차 구조(Sequence)**는 명령이나 작업을
**정해진 순서대로 하나씩 수행하는 구조**입니다.

특별한 조건이나 반복 없이
첫 번째 작업이 끝나면 두 번째 작업을 수행하고,
그 다음 작업으로 계속 진행합니다.
"""
    )

    st.markdown("### 📘 교과서 순서도")

    sequence_left, sequence_center, sequence_right = (
        st.columns([1, 1.2, 1])
    )

    with sequence_center:

        st.image(
            SEQUENCE_FLOWCHART,
            caption="순차 구조의 순서도",
            width=380,
        )

    st.markdown("### 자연어로 표현하면")

    st.code(
        """
1. 두 수를 입력받는다.
2. 두 수를 더한다.
3. 계산한 결과를 출력한다.
        """.strip(),
        language="text",
    )

    st.markdown("### Python으로 표현하면")

    st.code(
        """
num1 = 10
num2 = 20

result = num1 + num2

print(result)
        """.strip(),
        language="python",
    )

    st.info(
        """
        💡 Python 프로그램도 특별한 제어문이 없다면
        기본적으로 위에서 아래 방향으로 순서대로 실행됩니다.
        """
    )

    st.markdown("---")

    # -----------------------------------------------------
    # 3. 선택 구조
    # -----------------------------------------------------
    st.markdown("## 3. 선택 구조")

    st.markdown(
        """
**선택 구조(Selection)**는 주어진 **조건의 결과에 따라
서로 다른 작업 중 하나를 선택하여 수행하는 구조**입니다.

어떤 조건이 참인지 거짓인지 판단한 뒤,
그 결과에 맞는 작업을 수행합니다.
"""
    )

    st.markdown("### 📘 교과서 순서도")

    selection_left, selection_center, selection_right = (
        st.columns([1, 2, 1])
    )

    with selection_center:

        st.image(
            SELECTION_FLOWCHART,
            caption="선택 구조의 순서도",
            use_container_width=True,
        )

    st.markdown("### 자연어로 표현하면")

    st.code(
        """
만약 점수가 60점 이상이면
    "합격"을 출력한다.
그렇지 않으면
    "불합격"을 출력한다.
        """.strip(),
        language="text",
    )

    st.markdown("### Python으로 표현하면")

    st.code(
        """
score = 75

if score >= 60:
    print("합격")
else:
    print("불합격")
        """.strip(),
        language="python",
    )

    st.info(
        """
        💡 Python에서는 `if`, `elif`, `else`를 이용하여
        선택 구조를 표현할 수 있습니다.
        """
    )

    st.markdown("---")

    # -----------------------------------------------------
    # 4. 반복 구조
    # -----------------------------------------------------
    st.markdown("## 4. 반복 구조")

    st.markdown(
        """
**반복 구조(Repetition)**는 특정 조건을 만족하는 동안
**같은 작업을 여러 번 반복하여 수행하는 구조**입니다.

같은 명령을 계속 작성하지 않고
반복 구조를 사용하면 알고리즘을 더 간결하게 표현할 수 있습니다.
"""
    )

    st.markdown("### 📘 교과서 순서도")

    repetition_left, repetition_center, repetition_right = (
        st.columns([1, 2, 1])
    )

    with repetition_center:

        st.image(
            REPETITION_FLOWCHART,
            caption="반복 구조의 순서도",
            use_container_width=True,
        )

    st.markdown("### 자연어로 표현하면")

    st.code(
        """
1부터 5까지의 수를
하나씩 차례대로 출력한다.
        """.strip(),
        language="text",
    )

    st.markdown("### Python으로 표현하면")

    st.code(
        """
for i in range(1, 6):
    print(i)
        """.strip(),
        language="python",
    )

    st.info(
        """
        💡 Python에서는 `for` 또는 `while`을 이용하여
        반복 구조를 표현할 수 있습니다.
        """
    )

    st.markdown("---")

    st.success(
        """
        ✅ 대부분의 알고리즘은
        **순차 구조 · 선택 구조 · 반복 구조**를
        적절하게 조합하여 표현할 수 있습니다.
        """
    )


# =========================================================
# ② 예제 분석
# =========================================================
with example_tab:

    st.markdown(
        "## 예제: 학생 점수에 따라 등급 출력하기"
    )

    st.markdown(
        """
시험 점수를 입력받아 다음 기준에 따라
등급을 출력하는 알고리즘을 생각해 봅시다.

- **90점 이상:** A
- **80점 이상:** B
- **70점 이상:** C
- **70점 미만:** D
"""
    )

    st.markdown("### ① 입력")

    st.info(
        "학생의 시험 점수"
    )

    st.markdown("### ② 처리")

    st.markdown(
        """
조건을 높은 점수부터 차례대로 확인합니다.

1. 90점 이상인지 확인한다.
2. 아니면 80점 이상인지 확인한다.
3. 아니면 70점 이상인지 확인한다.
4. 모든 조건을 만족하지 않으면 D로 처리한다.
"""
    )

    st.markdown("### ③ 출력")

    st.success(
        "A, B, C, D 중 하나의 등급"
    )

    st.markdown("### 의사코드")

    st.code(
        """
점수를 입력받는다.

만약 점수가 90 이상이면
    A를 출력한다.

아니고 점수가 80 이상이면
    B를 출력한다.

아니고 점수가 70 이상이면
    C를 출력한다.

그렇지 않으면
    D를 출력한다.
        """.strip(),
        language="text",
    )

    st.markdown("### Python 코드")

    st.code(
        """
score = 85

if score >= 90:
    grade = "A"

elif score >= 80:
    grade = "B"

elif score >= 70:
    grade = "C"

else:
    grade = "D"

print(grade)
        """.strip(),
        language="python",
    )

    st.info(
        """
        💡 이 알고리즘에서는 조건에 따라
        실행할 내용이 달라지므로 **선택 구조**가 사용됩니다.
        """
    )


# =========================================================
# ③ 알고리즘 설계 활동
# =========================================================
with activity_tab:

    st.markdown(
        "## 🧠 직접 알고리즘을 설계해 봅시다"
    )

    render_html(
        """
        <div class="info-card">

            <div class="info-card-icon">
                🔢
            </div>

            <div class="info-card-content">

                <strong>
                    문제 상황
                </strong>

                <p>
                    정수 하나를 입력받아
                    그 수가 짝수인지 홀수인지 판별하는
                    프로그램을 만들어 봅시다.
                </p>

            </div>

        </div>
        """
    )

    input_data = st.text_input(
        "① 입력은 무엇인가요?",
        placeholder="예: 정수 한 개",
        key="activity_2_3_input",
    )

    process_data = st.text_area(
        "② 어떤 처리가 필요한가요?",
        placeholder=(
            "예:\n"
            "입력한 수를 2로 나눈 나머지를 확인한다.\n"
            "나머지가 0이면 짝수이다."
        ),
        height=120,
        key="activity_2_3_process",
    )

    output_data = st.text_input(
        "③ 출력은 무엇인가요?",
        placeholder="예: 짝수 또는 홀수",
        key="activity_2_3_output",
    )

    pseudocode = st.text_area(
        "④ 의사코드로 표현해 보세요.",
        placeholder=(
            "수를 입력받는다.\n"
            "만약 수를 2로 나눈 나머지가 0이면\n"
            "    짝수를 출력한다.\n"
            "그렇지 않으면\n"
            "    홀수를 출력한다."
        ),
        height=170,
        key="activity_2_3_pseudocode",
    )

    if st.button(
        "알고리즘 설계 내용 확인하기",
        key="check_activity_2_3",
        type="primary",
    ):

        if (
            input_data.strip()
            and process_data.strip()
            and output_data.strip()
            and pseudocode.strip()
        ):

            st.success(
                """
                좋습니다! 입력 → 처리 → 출력의 구조와
                선택 구조를 이용하여 알고리즘을 설계했습니다. ✅
                """
            )

        else:

            st.warning(
                "모든 항목을 작성해 주세요."
            )

    with st.expander(
        "💡 예시 답안 보기"
    ):

        st.markdown(
            """
**입력**

- 정수 한 개

**처리**

- 정수를 2로 나눈 나머지를 구한다.
- 나머지가 0인지 확인한다.

**출력**

- 짝수 또는 홀수

**의사코드**

1. 정수를 입력받는다.
2. 정수를 2로 나눈 나머지를 구한다.
3. 나머지가 0이면 '짝수'를 출력한다.
4. 그렇지 않으면 '홀수'를 출력한다.
"""
        )


# =========================================================
# ④ Python 연결 + Colab 실습
# =========================================================
with python_tab:

    st.markdown(
        "## 🐍 알고리즘을 Python으로 구현해 봅시다"
    )

    st.markdown(
        """
앞에서 학습한 **순차 구조, 선택 구조, 반복 구조**가
Python 코드에서는 어떻게 표현되는지 확인해 봅시다.

예제 코드를 확인한 뒤에는 Google Colab으로 이동하여
직접 코드를 수정하고 실행할 수 있습니다.
"""
    )

    # -----------------------------------------------------
    # 순차 구조
    # -----------------------------------------------------
    st.markdown("### 1. 순차 구조")

    st.code(
        """
num1 = 10
num2 = 20

result = num1 + num2

print(result)
        """.strip(),
        language="python",
    )

    st.info(
        "💡 위에서 아래로 명령이 차례대로 실행됩니다."
    )

    st.markdown("---")

    # -----------------------------------------------------
    # 선택 구조
    # -----------------------------------------------------
    st.markdown("### 2. 선택 구조")

    st.code(
        """
number = 7

if number % 2 == 0:
    print("짝수")
else:
    print("홀수")
        """.strip(),
        language="python",
    )

    st.markdown(
        "#### 출력 결과를 예상해 봅시다"
    )

    answer = st.radio(
        "`number = 7`일 때 출력 결과는 무엇일까요?",
        [
            "짝수",
            "홀수",
            "7",
            "0",
        ],
        index=None,
        key="python_2_3_answer",
    )

    if answer == "홀수":

        st.success(
            """
            정답입니다! ✅
            7을 2로 나눈 나머지는 1이므로 홀수입니다.
            """
        )

    elif answer is not None:

        st.error(
            """
            다시 생각해 봅시다.
            `number % 2 == 0` 조건을 확인해 보세요.
            """
        )

    st.markdown("---")

    # -----------------------------------------------------
    # 반복 구조
    # -----------------------------------------------------
    st.markdown("### 3. 반복 구조")

    st.code(
        """
for number in range(1, 6):
    print(number)
        """.strip(),
        language="python",
    )

    st.info(
        """
        💡 `for`문은 같은 작업을
        여러 데이터에 반복해서 적용할 때 사용합니다.
        """
    )

    st.markdown("---")

    # -----------------------------------------------------
    # Colab 실습 안내
    # -----------------------------------------------------
    render_html(
        """
        <div class="colab-banner">

            <div>

                <div class="section-label">
                    HANDS-ON PRACTICE
                </div>

                <h3>
                    이제 직접 코딩해 봅시다
                </h3>

                <p>
                    예제 코드를 보는 것에서 끝나지 않고
                    Google Colab에서 순차·선택·반복 구조를
                    직접 수정하고 실행해 봅시다.
                </p>

            </div>

            <div class="colab-logo">
                ☁️
            </div>

        </div>
        """
    )

    st.markdown(
        "### 🚀 Colab 실습 내용"
    )

    practice_cols = st.columns(4)

    practice_data = [
        (
            "01",
            "➡️",
            "순차 구조",
            "두 정수를 입력받아 합계를 출력합니다.",
        ),
        (
            "02",
            "🔀",
            "선택 구조",
            "점수에 따라 합격/불합격을 판단합니다.",
        ),
        (
            "03",
            "🔁",
            "반복 구조",
            "1부터 10까지 반복하여 출력합니다.",
        ),
        (
            "04",
            "🏆",
            "도전 문제",
            "1부터 n까지의 합을 계산합니다.",
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
        "🚀 Google Colab에서 직접 실습하기",
        COLAB_URL,
        use_container_width=True,
        type="primary",
    )

    st.caption(
        """
        Colab이 새 탭에서 열리면 ▶ 실행 버튼을 눌러
        각 실습 코드를 직접 수정하고 실행해 보세요.
        """
    )


# =========================================================
# ⑤ 형성평가
# =========================================================
with quiz_tab:

    st.markdown(
        "## 📝 2-3 형성평가"
    )

    st.caption(
        """
        순차, 선택, 반복 구조와
        알고리즘 설계의 기본 개념을 확인합니다.
        """
    )

    q1 = st.radio(
        "1. 명령이 정해진 순서에 따라 차례대로 실행되는 구조는 무엇인가요?",
        [
            "순차 구조",
            "선택 구조",
            "반복 구조",
            "탐색 구조",
        ],
        index=None,
        key="quiz_2_3_q1",
    )

    q2 = st.radio(
        "2. 조건에 따라 서로 다른 작업을 수행하는 구조는 무엇인가요?",
        [
            "순차 구조",
            "선택 구조",
            "반복 구조",
            "입력 구조",
        ],
        index=None,
        key="quiz_2_3_q2",
    )

    q3 = st.radio(
        "3. 같은 작업을 여러 번 수행하는 구조는 무엇인가요?",
        [
            "순차 구조",
            "선택 구조",
            "반복 구조",
            "출력 구조",
        ],
        index=None,
        key="quiz_2_3_q3",
    )

    q4 = st.radio(
        "4. Python에서 조건에 따른 선택 구조를 표현할 때 사용하는 명령어는 무엇인가요?",
        [
            "if",
            "for",
            "print",
            "range",
        ],
        index=None,
        key="quiz_2_3_q4",
    )

    q5 = st.radio(
        "5. 다음 중 알고리즘 설계에 대한 설명으로 가장 적절한 것은 무엇인가요?",
        [
            "문제를 해결하기 위한 절차를 명확하게 정하는 과정",
            "Python 문법만 암기하는 과정",
            "컴퓨터의 전원을 켜는 과정",
            "데이터를 무조건 삭제하는 과정",
        ],
        index=None,
        key="quiz_2_3_q5",
    )

    if st.button(
        "형성평가 제출",
        key="submit_quiz_2_3",
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
                "순차 구조",
                "선택 구조",
                "반복 구조",
                "if",
                "문제를 해결하기 위한 절차를 명확하게 정하는 과정",
            ]

            score = sum(
                answer == correct
                for answer, correct in zip(
                    answers,
                    correct_answers,
                )
            )

            st.session_state.lesson_2_3_score = score

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
                    "2-3"
                ] = True

                st.success(
                    "✅ 2-3 알고리즘 설계 학습을 완료했습니다."
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
    st.session_state.unit2_progress.get(
        "2-3",
        False,
    )
)

if is_completed:

    st.success(
        "🎉 **2-3 알고리즘 설계**를 완료했습니다."
    )

    if (
        st.session_state.lesson_2_3_score
        is not None
    ):

        st.markdown(
            "형성평가 점수: "
            f"**{st.session_state.lesson_2_3_score} / 5점**"
        )

else:

    st.info(
        """
        형성평가에서 4점 이상을 받으면
        2-3 학습이 완료됩니다.
        """
    )


# =========================================================
# 핵심 정리
# =========================================================
with st.expander(
    "📚 2-3 핵심 내용 다시 보기",
    expanded=False,
):

    st.markdown(
        """
### 알고리즘 설계

문제를 해결하기 위한 명확한 절차를 만드는 과정입니다.

### 1. 순차 구조

명령이나 작업을 정해진 순서에 따라 차례대로 수행합니다.

### 2. 선택 구조

조건의 결과에 따라 서로 다른 작업을 선택하여 수행합니다.

### 3. 반복 구조

특정 조건에 따라 같은 작업을 여러 번 수행합니다.

### 알고리즘 표현

알고리즘은 자연어, 의사코드, 순서도,
프로그래밍 언어 등으로 표현할 수 있습니다.

### 전체 흐름

**문제 분석 → 모델링 → 알고리즘 설계 → Python 구현**
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
        "← 2-2 문제 분해와 모델링",
        use_container_width=True,
    ):

        st.switch_page(
            "pages/02_02_문제분해와모델링.py"
        )


with nav_right:

    if st.button(
        "2-4 알고리즘 성능 분석 →",
        use_container_width=True,
        type="primary",
    ):

        st.switch_page(
            "pages/02_04_알고리즘성능분석.py"
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
            Ⅱ. 추상화와 모델링 · 2-3 알고리즘 설계
        </span>

    </div>
    """
)