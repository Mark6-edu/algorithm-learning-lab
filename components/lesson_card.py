import streamlit as st


def render_unit_card(
    unit_no: str,
    title: str,
    description: str,
    status: str,
    page: str | None = None,
    enabled: bool = False,
    completed: bool = False,
    button_key: str | None = None,
):
    """
    메인 페이지의 대단원 카드

    Parameters
    ----------
    unit_no : str
        단원 번호
        예: "Ⅰ", "Ⅱ"

    title : str
        단원 제목

    description : str
        단원 설명

    status : str
        상태 표시
        예: "준비 중", "학습 가능", "완료"

    page : str | None
        이동할 Streamlit 페이지 경로

    enabled : bool
        학습 가능 여부

    completed : bool
        완료 여부

    button_key : str | None
        Streamlit 버튼 고유 키
    """

    if button_key is None:
        button_key = f"unit_card_{unit_no}"

    if completed:
        card_class = "active"
        status_text = "✓ 완료"

    elif enabled:
        card_class = "active"
        status_text = status

    else:
        card_class = "ready"
        status_text = status

    st.markdown(
        f"""
        <div class="unit-card {card_class}">

            <div class="unit-card-top">

                <div class="unit-number">
                    {unit_no}
                </div>

                <div class="unit-status">
                    {status_text}
                </div>

            </div>

            <h3>
                {title}
            </h3>

            <p>
                {description}
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    if completed and page:

        if st.button(
            "다시 학습하기  →",
            key=button_key,
            type="primary",
            use_container_width=True,
        ):
            st.switch_page(page)

    elif enabled and page:

        if st.button(
            "학습 시작하기  →",
            key=button_key,
            type="primary",
            use_container_width=True,
        ):
            st.switch_page(page)

    else:

        st.button(
            "준비 중",
            key=button_key,
            disabled=True,
            use_container_width=True,
        )


def render_lesson_card(
    lesson_no: str,
    title: str,
    description: str,
    icon: str,
    page: str,
    completed: bool = False,
    score: int | None = None,
    total_score: int = 5,
    button_key: str | None = None,
):
    """
    단원 페이지에서 사용하는 소단원 학습 카드
    """

    if button_key is None:
        button_key = f"lesson_card_{lesson_no}"

    status_text = (
        "✓ 완료"
        if completed
        else "학습 가능"
    )

    st.markdown(
        f"""
        <div class="unit-card active">

            <div class="unit-card-top">

                <div class="unit-number">
                    {lesson_no}
                </div>

                <div class="unit-status">
                    {status_text}
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
        """,
        unsafe_allow_html=True,
    )

    if score is not None:

        st.caption(
            f"📝 최근 형성평가: "
            f"{score} / {total_score}점"
        )

    button_label = (
        "다시 학습하기  →"
        if completed
        else "학습 시작하기  →"
    )

    if st.button(
        button_label,
        key=button_key,
        type="primary",
        use_container_width=True,
    ):
        st.switch_page(page)


def render_locked_lesson_card(
    lesson_no: str,
    title: str,
    description: str,
    icon: str,
    message: str = "이전 학습을 먼저 완료해 주세요.",
    button_key: str | None = None,
):
    """
    순차 학습을 적용할 때 사용하는 잠금 카드
    """

    if button_key is None:
        button_key = f"locked_lesson_{lesson_no}"

    st.markdown(
        f"""
        <div class="unit-card ready">

            <div class="unit-card-top">

                <div class="unit-number">
                    {lesson_no}
                </div>

                <div class="unit-status">
                    🔒 잠김
                </div>

            </div>

            <div style="
                font-size:32px;
                margin-bottom:14px;
                opacity:0.65;
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
        """,
        unsafe_allow_html=True,
    )

    st.caption(
        f"🔒 {message}"
    )

    st.button(
        "학습 잠김",
        key=button_key,
        disabled=True,
        use_container_width=True,
    )


def render_lesson_status_badge(
    completed: bool = False,
    locked: bool = False,
):
    """
    필요할 때 카드 외부에서 상태 문자열을 얻는 함수
    """

    if locked:
        return "🔒 잠김"

    if completed:
        return "✓ 완료"

    return "학습 가능"