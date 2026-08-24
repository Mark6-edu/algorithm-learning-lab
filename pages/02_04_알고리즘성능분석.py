import streamlit as st

from utils.ui import (
    load_css,
    render_html,
)


# =========================================================
# 페이지 설정
# =========================================================
st.set_page_config(
    page_title="2-4 알고리즘 성능 분석",
    page_icon="📊",
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

if "lesson_2_4_score" not in st.session_state:
    st.session_state.lesson_2_4_score = None


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

    if st.button(
        "2-3  알고리즘 설계",
        use_container_width=True,
    ):
        st.switch_page(
            "pages/02_03_알고리즘설계.py"
        )

    st.button(
        "2-4  알고리즘 성능 분석",
        type="primary",
        use_container_width=True,
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
        2-4 알고리즘 성능 분석
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
                UNIT Ⅱ · LESSON 04
            </div>

            <h2>
                알고리즘 성능 분석
            </h2>

            <p>
                같은 문제를 해결하는 알고리즘이라도
                처리 방법에 따라 필요한 작업의 양은 달라집니다.
                입력 데이터의 크기가 증가할 때
                알고리즘의 수행 횟수가 어떻게 변하는지 분석하고,
                더 효율적인 알고리즘을 판단하는 방법을 알아봅시다.
            </p>

        </div>

        <div class="hero-visual">

            <div class="code-window">

                <div class="code-window-header">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>

                <pre>입력 크기 n
    ↓
수행되는 연산 횟수
    ↓
증가하는 정도 분석
    ↓
시간 복잡도
    ↓
알고리즘 비교</pre>

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
                입력 크기와 수행 횟수의 관계를 이해하고,
                시간 복잡도를 이용하여 알고리즘의 효율성을 비교합니다.
            </p>

        </div>

    </div>
    """
)


goal_cols = st.columns(3)

goal_data = [
    (
        "01",
        "📥",
        "입력 크기",
        """
        알고리즘 성능을 분석할 때
        입력 데이터의 크기가 중요한 이유를 설명합니다.
        """,
    ),
    (
        "02",
        "🔢",
        "수행 횟수",
        """
        입력 크기가 증가할 때
        알고리즘의 연산 횟수가 어떻게 변하는지 분석합니다.
        """,
    ),
    (
        "03",
        "⚡",
        "효율성 비교",
        """
        여러 알고리즘의 시간 복잡도를 비교하여
        더 효율적인 방법을 판단합니다.
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
                알고리즘의 효율성을 비교해 봅시다
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
        "🧠 성능 비교 활동",
        "🐍 Python 연결",
        "📝 형성평가",
    ]
)


# =========================================================
# ① 개념 학습
# =========================================================
with concept_tab:

    st.markdown("## 1. 알고리즘의 성능이란?")

    st.write(
        """
        하나의 문제를 해결하는 방법은 여러 가지가 있을 수 있습니다.

        결과가 정확하더라도 지나치게 많은 시간이 걸리거나
        많은 자원을 사용한다면 좋은 알고리즘이라고 보기 어렵습니다.

        따라서 알고리즘을 설계한 뒤에는
        **얼마나 효율적으로 문제를 해결하는지** 분석할 필요가 있습니다.
        """
    )

    st.success(
        "💡 핵심 질문: **입력 데이터가 많아져도 이 알고리즘은 효율적으로 동작할까?**"
    )

    st.markdown("---")
    st.markdown("## 2. 입력 크기")

    st.write(
        """
        알고리즘이 처리해야 하는 데이터의 양을
        **입력 크기(Input Size)**라고 합니다.

        일반적으로 입력 크기는 `n`으로 표현합니다.
        """
    )

    st.dataframe(
        {
            "문제": [
                "학생 점수에서 최댓값 찾기",
                "전화번호 목록에서 이름 찾기",
                "숫자 목록 정렬하기",
            ],
            "입력 크기 n": [
                "학생 수",
                "전화번호 개수",
                "숫자의 개수",
            ],
        },
        hide_index=True,
        width="stretch",
    )

    st.info(
        """
        예를 들어 학생 10명의 점수를 처리한다면 `n = 10`,
        학생 1,000명의 점수를 처리한다면 `n = 1000`이라고
        생각할 수 있습니다.
        """
    )

    st.markdown("---")
    st.markdown("## 3. 수행 횟수")

    st.write(
        """
        알고리즘의 성능을 비교할 때는
        실제 실행 시간만 측정하기보다,
        입력 크기에 따라 **핵심 연산이 몇 번 수행되는지**
        살펴보는 것이 중요합니다.
        """
    )

    st.markdown("### 예시: 목록에서 숫자 찾기")

    st.code(
        """
numbers = [3, 8, 1, 7, 5]

for number in numbers:
    if number == 7:
        print("찾았습니다.")
        """.strip(),
        language="python",
    )

    st.write(
        """
        최악의 경우 찾으려는 숫자가 목록의 마지막에 있다면
        모든 데이터를 한 번씩 확인해야 합니다.

        데이터가 `n`개라면
        최대 약 `n`번 확인하게 됩니다.
        """
    )

    st.markdown("---")
    st.markdown("## 4. 시간 복잡도")

    st.write(
        """
        **시간 복잡도(Time Complexity)**는
        입력 크기가 증가할 때 알고리즘의 수행 시간이
        어느 정도의 비율로 증가하는지를 나타냅니다.

        보통 **Big-O 표기법**을 사용합니다.
        """
    )

    complexity_cols = st.columns(3)

    with complexity_cols[0]:

        render_html(
            """
            <div class="unit-card active">

                <div class="unit-number">
                    O(1)
                </div>

                <h3>
                    상수 시간
                </h3>

                <p>
                    입력 크기와 관계없이
                    연산 횟수가 거의 일정합니다.
                </p>

            </div>
            """
        )

    with complexity_cols[1]:

        render_html(
            """
            <div class="unit-card active">

                <div class="unit-number">
                    O(n)
                </div>

                <h3>
                    선형 시간
                </h3>

                <p>
                    입력 데이터가 증가하면
                    수행 횟수도 비슷한 비율로 증가합니다.
                </p>

            </div>
            """
        )

    with complexity_cols[2]:

        render_html(
            """
            <div class="unit-card active">

                <div class="unit-number">
                    O(n²)
                </div>

                <h3>
                    제곱 시간
                </h3>

                <p>
                    입력 크기가 증가할수록
                    수행 횟수가 매우 빠르게 증가합니다.
                </p>

            </div>
            """
        )

    st.markdown("### 입력 크기에 따른 수행 횟수 예")

    st.dataframe(
        {
            "입력 크기 n": [
                10,
                100,
                1000,
            ],
            "O(1)": [
                1,
                1,
                1,
            ],
            "O(n)": [
                10,
                100,
                1000,
            ],
            "O(n²)": [
                100,
                10000,
                1000000,
            ],
        },
        hide_index=True,
        width="stretch",
    )

    st.warning(
        """
        ⚠️ Big-O는 실제 실행 시간을 초 단위로 나타내는 것이 아니라,
        **입력 크기가 커질 때 연산량이 증가하는 경향**을 나타냅니다.
        """
    )


# =========================================================
# ② 예제 분석
# =========================================================
with example_tab:

    st.markdown(
        "## 예제: 특정 학생의 점수 찾기"
    )

    st.write(
        """
        학생 번호와 점수가 저장되어 있다고 가정해 봅시다.
        특정 학생 번호의 점수를 찾으려고 합니다.
        """
    )

    st.code(
        """
students = [
    [1, 85],
    [2, 92],
    [3, 78],
    [4, 95],
    [5, 88]
]
        """.strip(),
        language="python",
    )

    st.markdown(
        "### 방법 A: 처음부터 하나씩 찾기"
    )

    st.code(
        """
target = 4

for student in students:
    if student[0] == target:
        print(student[1])
        break
        """.strip(),
        language="python",
    )

    st.write(
        """
        학생이 `n`명일 때 최악의 경우
        모든 학생을 확인해야 합니다.

        따라서 수행 횟수는 입력 크기에 비례하여 증가합니다.

        **시간 복잡도: O(n)**
        """
    )

    st.markdown("---")

    st.markdown(
        "### 방법 B: 학생 번호를 키로 저장하기"
    )

    st.code(
        """
students = {
    1: 85,
    2: 92,
    3: 78,
    4: 95,
    5: 88
}

print(students[4])
        """.strip(),
        language="python",
    )

    st.write(
        """
        딕셔너리에서 키를 이용해 값을 찾는 경우
        일반적으로 원하는 데이터에 빠르게 접근할 수 있습니다.

        같은 문제라도
        데이터를 어떤 구조로 저장하고
        어떤 알고리즘을 사용하는지에 따라
        성능이 달라질 수 있습니다.
        """
    )

    st.info(
        """
        💡 알고리즘의 효율성은
        **문제 해결 방법뿐 아니라 데이터 표현 방법**과도 관련이 있습니다.
        """
    )


# =========================================================
# ③ 성능 비교 활동
# =========================================================
with activity_tab:

    st.markdown(
        "## 🧠 입력 크기에 따른 작업량을 비교해 봅시다"
    )

    st.write(
        """
        입력 데이터의 크기 `n`을 바꾸면서
        각 시간 복잡도의 예상 작업량을 비교해 보세요.
        """
    )

    n = st.slider(
        "입력 데이터의 개수 n을 선택하세요.",
        min_value=1,
        max_value=100,
        value=10,
        step=1,
        key="complexity_n",
    )

    constant_ops = 1
    linear_ops = n
    quadratic_ops = n ** 2

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "O(1)",
            f"{constant_ops:,}회",
            help="입력 크기에 관계없이 일정한 작업량",
        )

    with col2:

        st.metric(
            "O(n)",
            f"{linear_ops:,}회",
            help="입력 크기에 비례하는 작업량",
        )

    with col3:

        st.metric(
            "O(n²)",
            f"{quadratic_ops:,}회",
            help="입력 크기의 제곱에 비례하는 작업량",
        )

    st.markdown("### 비교 표")

    st.dataframe(
        {
            "복잡도": [
                "O(1)",
                "O(n)",
                "O(n²)",
            ],
            "예상 수행 횟수": [
                constant_ops,
                linear_ops,
                quadratic_ops,
            ],
        },
        hide_index=True,
        width="stretch",
    )

    if n >= 50:

        st.warning(
            f"""
            `n = {n}`일 때 O(n²)은 약
            **{quadratic_ops:,}번**의 작업이 필요합니다.

            입력 데이터가 커질수록
            알고리즘 선택이 중요해집니다.
            """
        )

    else:

        st.info(
            """
            슬라이더를 움직여 입력 데이터가 증가할 때
            각 알고리즘의 작업량이 어떻게 달라지는지 확인해 보세요.
            """
        )

    st.markdown("---")

    st.markdown(
        "### 어떤 알고리즘을 선택할까요?"
    )

    choice = st.radio(
        """
        데이터가 10만 개 이상이고
        같은 문제를 해결할 수 있다는 조건이라면
        일반적으로 어느 알고리즘이 더 유리할까요?
        """,
        [
            "아직 선택하지 않음",
            "O(1)",
            "O(n)",
            "O(n²)",
        ],
        key="activity_2_4_choice",
    )

    if choice == "O(1)":

        st.success(
            """
            정답입니다! ✅
            동일한 문제를 해결할 수 있다는 조건이라면
            입력 크기의 영향을 가장 적게 받는 O(1)이 유리합니다.
            """
        )

    elif choice != "아직 선택하지 않음":

        st.warning(
            """
            입력 크기가 매우 커질 때
            각 복잡도의 수행 횟수를 다시 비교해 보세요.
            """
        )


# =========================================================
# ④ Python 연결
# =========================================================
with python_tab:

    st.markdown(
        "## 🐍 Python 코드로 수행 횟수를 확인해 봅시다"
    )

    st.write(
        """
        시간 복잡도는 단순히 코드를 실행해 시간을 재는 것보다
        **핵심 작업이 얼마나 반복되는지**
        살펴보면 이해하기 쉽습니다.
        """
    )

    st.markdown("### O(n) 예제")

    st.code(
        """
numbers = [10, 20, 30, 40, 50]

count = 0

for number in numbers:
    count += 1
    print(number)

print("수행 횟수:", count)
        """.strip(),
        language="python",
    )

    st.write(
        """
        리스트에 데이터가 5개 있으므로
        반복문은 5번 실행됩니다.

        데이터가 `n`개라면 반복 횟수도 `n`번이므로
        **O(n)**으로 생각할 수 있습니다.
        """
    )

    st.markdown("---")

    st.markdown("### O(n²) 예제")

    st.code(
        """
numbers = [1, 2, 3, 4, 5]

count = 0

for i in numbers:
    for j in numbers:
        count += 1

print("수행 횟수:", count)
        """.strip(),
        language="python",
    )

    st.write(
        """
        바깥쪽 반복문이 5번,
        안쪽 반복문도 매번 5번 실행됩니다.

        따라서 총 수행 횟수는

        **5 × 5 = 25번**입니다.

        데이터가 `n`개라면
        약 `n × n`번 실행되므로 **O(n²)**입니다.
        """
    )

    st.markdown(
        "### 직접 예상하기"
    )

    answer = st.radio(
        """
        위의 이중 반복문에서
        `numbers`에 데이터가 10개 있다면
        `count += 1`은 몇 번 수행될까요?
        """,
        [
            "아직 선택하지 않음",
            "10번",
            "20번",
            "50번",
            "100번",
        ],
        key="python_2_4_answer",
    )

    if answer == "100번":

        st.success(
            """
            정답입니다! ✅
            10 × 10 = 100번 수행됩니다.
            """
        )

    elif answer != "아직 선택하지 않음":

        st.error(
            """
            바깥 반복문과 안쪽 반복문의
            실행 횟수를 곱해서 생각해 보세요.
            """
        )

    st.markdown("---")

    st.info(
        """
        🚀 이후 Colab 실습에서는
        실제로 입력 크기를 늘려가며
        Python 코드의 실행 시간을 측정하고 비교할 수 있습니다.
        """
    )


# =========================================================
# ⑤ 형성평가
# =========================================================
with quiz_tab:

    st.markdown("## 📝 2-4 형성평가")

    st.caption(
        "입력 크기, 수행 횟수, 시간 복잡도에 대한 내용을 확인합니다."
    )

    q1 = st.radio(
        "1. 알고리즘이 처리해야 하는 데이터의 양을 무엇이라고 하나요?",
        [
            "출력 크기",
            "입력 크기",
            "프로그램 크기",
            "저장 크기",
        ],
        index=None,
        key="quiz_2_4_q1",
    )

    q2 = st.radio(
        "2. 입력 크기와 관계없이 수행 횟수가 거의 일정한 시간 복잡도는 무엇인가요?",
        [
            "O(1)",
            "O(n)",
            "O(n²)",
            "O(n³)",
        ],
        index=None,
        key="quiz_2_4_q2",
    )

    q3 = st.radio(
        "3. 데이터가 n개이고 모든 데이터를 한 번씩 확인하는 알고리즘의 시간 복잡도는 무엇인가요?",
        [
            "O(1)",
            "O(n)",
            "O(n²)",
            "O(2ⁿ)",
        ],
        index=None,
        key="quiz_2_4_q3",
    )

    q4 = st.radio(
        "4. 데이터가 n개일 때 두 개의 중첩 반복문이 각각 n번씩 실행된다면 시간 복잡도는 무엇인가요?",
        [
            "O(1)",
            "O(n)",
            "O(n²)",
            "O(n³)",
        ],
        index=None,
        key="quiz_2_4_q4",
    )

    q5 = st.radio(
        "5. 알고리즘의 시간 복잡도를 분석하는 가장 중요한 이유는 무엇인가요?",
        [
            "코드의 글자 수를 확인하기 위해",
            "입력 크기가 증가할 때 알고리즘의 효율성을 비교하기 위해",
            "Python 버전을 확인하기 위해",
            "프로그램의 색상을 변경하기 위해",
        ],
        index=None,
        key="quiz_2_4_q5",
    )

    if st.button(
        "형성평가 제출",
        key="submit_quiz_2_4",
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
                "입력 크기",
                "O(1)",
                "O(n)",
                "O(n²)",
                "입력 크기가 증가할 때 알고리즘의 효율성을 비교하기 위해",
            ]

            score = sum(
                answer == correct
                for answer, correct in zip(
                    answers,
                    correct_answers,
                )
            )

            st.session_state.lesson_2_4_score = score

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
                    "2-4"
                ] = True

                st.success(
                    "✅ 2-4 알고리즘 성능 분석 학습을 완료했습니다."
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
    "2-4",
    False,
)

if is_completed:

    st.success(
        "🎉 **2-4 알고리즘 성능 분석**을 완료했습니다."
    )

    if (
        st.session_state.lesson_2_4_score
        is not None
    ):

        st.write(
            f"형성평가 점수: "
            f"**{st.session_state.lesson_2_4_score} / 5점**"
        )

else:

    st.info(
        """
        형성평가에서 4점 이상을 받으면
        2-4 학습이 완료됩니다.
        """
    )


# =========================================================
# 2단원 전체 완료 여부
# =========================================================
unit2_completed = all(
    st.session_state.unit2_progress.values()
)

if unit2_completed:

    st.markdown("---")

    st.success(
        """
        🎉 **Ⅱ. 추상화와 모델링 단원을 모두 완료했습니다!**

        문제 이해 → 문제 분해 → 추상화와 모델링 →
        알고리즘 설계 → 성능 분석의 전체 흐름을 학습했습니다.
        """
    )


# =========================================================
# 핵심 정리
# =========================================================
with st.expander(
    "📚 2-4 핵심 내용 다시 보기",
    expanded=False,
):

    st.markdown(
        """
        ### 알고리즘 성능 분석

        같은 문제를 해결하는 알고리즘이라도
        필요한 연산 횟수와 처리 시간은 다를 수 있습니다.

        ### 입력 크기

        알고리즘이 처리해야 하는 데이터의 양이며
        일반적으로 **n**으로 표현합니다.

        ### 시간 복잡도

        입력 크기가 증가할 때
        알고리즘의 수행 횟수가 어떻게 증가하는지 나타냅니다.

        - **O(1)** : 입력 크기와 관계없이 거의 일정
        - **O(n)** : 입력 크기에 비례
        - **O(n²)** : 입력 크기의 제곱에 비례

        ### 알고리즘 설계의 전체 흐름

        **문제 이해 → 문제 분해 → 추상화와 모델링 → 알고리즘 설계 → 성능 분석**
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
        "← 2-3 알고리즘 설계",
        use_container_width=True,
    ):
        st.switch_page(
            "pages/02_03_알고리즘설계.py"
        )

with nav_right:

    if st.button(
        "Ⅱ. 추상화와 모델링 완료 →",
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
            Ⅱ. 추상화와 모델링 · 2-4 알고리즘 성능 분석
        </span>

    </div>
    """
)