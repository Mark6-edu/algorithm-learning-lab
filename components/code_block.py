import streamlit as st


def render_python_example(
    title: str,
    code: str,
    description: str = "",
    output: str | None = None,
    language: str = "python",
):
    """
    Python 코드 예제를 공통 형식으로 출력
    """

    st.markdown(f"### 🐍 {title}")

    if description:
        st.write(description)

    st.code(
        code.strip(),
        language=language,
    )

    if output is not None:
        st.markdown("#### 실행 결과")

        st.code(
            output.strip(),
            language="text",
        )


def render_code_explanation(
    rows: list[dict],
):
    """
    코드와 알고리즘 요소를 표 형태로 연결

    예시:
    [
        {
            "concept": "입력 데이터",
            "code": "numbers",
            "description": "숫자 목록을 저장합니다."
        }
    ]
    """

    table_data = {
        "알고리즘 요소": [],
        "Python 코드": [],
        "설명": [],
    }

    for row in rows:
        table_data["알고리즘 요소"].append(
            row.get("concept", "")
        )

        table_data["Python 코드"].append(
            row.get("code", "")
        )

        table_data["설명"].append(
            row.get("description", "")
        )

    st.dataframe(
        table_data,
        hide_index=True,
        width="stretch",
    )


def render_output_prediction(
    question: str,
    options: list[str],
    answer: str,
    key: str,
    explanation: str = "",
):
    """
    코드 실행 결과 예상 문제
    """

    st.markdown("### 🔍 실행 결과를 예상해 봅시다")

    selected = st.radio(
        question,
        ["아직 선택하지 않음"] + options,
        key=key,
    )

    if selected == "아직 선택하지 않음":
        return None

    if selected == answer:
        st.success("정답입니다! ✅")

        if explanation:
            st.info(
                f"💡 {explanation}"
            )

        return True

    st.error("다시 생각해 봅시다.")

    if explanation:
        st.caption(
            f"힌트: {explanation}"
        )

    return False


def render_fill_blank_code(
    title: str,
    code_before: str,
    question: str,
    answer: str,
    key: str,
    hint: str = "",
):
    """
    간단한 빈칸 코딩 활동
    """

    st.markdown(f"### ✏️ {title}")

    st.code(
        code_before.strip(),
        language="python",
    )

    student_answer = st.text_input(
        question,
        key=key,
    )

    if st.button(
        "정답 확인",
        key=f"{key}_check",
    ):

        normalized_student = (
            student_answer
            .strip()
            .replace(" ", "")
        )

        normalized_answer = (
            answer
            .strip()
            .replace(" ", "")
        )

        if normalized_student == normalized_answer:
            st.success(
                "정답입니다! ✅"
            )

            return True

        st.error(
            "정답과 다릅니다. 다시 확인해 보세요."
        )

        if hint:
            st.info(
                f"💡 힌트: {hint}"
            )

    return False


def render_code_trace(
    title: str,
    steps: list[dict],
):
    """
    코드 실행 과정을 단계별로 설명

    예시:
    [
        {
            "step": "1",
            "code": "max_value = numbers[0]",
            "description": "첫 값을 최댓값으로 설정합니다."
        }
    ]
    """

    st.markdown(f"### 🔄 {title}")

    for item in steps:

        step = item.get(
            "step",
            ""
        )

        code = item.get(
            "code",
            ""
        )

        description = item.get(
            "description",
            ""
        )

        st.markdown(
            f"**STEP {step}**"
        )

        if code:
            st.code(
                code,
                language="python",
            )

        if description:
            st.write(
                description
            )


def render_input_process_output(
    input_text: str,
    process_text: str,
    output_text: str,
):
    """
    입력 → 처리 → 출력 구조 표시
    """

    cols = st.columns(3)

    with cols[0]:
        st.markdown(
            f"""
            <div class="learning-flow-card">
                <div class="flow-step">
                    INPUT
                </div>

                <div class="flow-icon">
                    📥
                </div>

                <h4>
                    입력
                </h4>

                <p>
                    {input_text}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with cols[1]:
        st.markdown(
            f"""
            <div class="learning-flow-card">
                <div class="flow-step">
                    PROCESS
                </div>

                <div class="flow-icon">
                    ⚙️
                </div>

                <h4>
                    처리
                </h4>

                <p>
                    {process_text}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with cols[2]:
        st.markdown(
            f"""
            <div class="learning-flow-card">
                <div class="flow-step">
                    OUTPUT
                </div>

                <div class="flow-icon">
                    📤
                </div>

                <h4>
                    출력
                </h4>

                <p>
                    {output_text}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )