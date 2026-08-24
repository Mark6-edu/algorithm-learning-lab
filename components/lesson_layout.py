import streamlit as st


# =========================================================
# 사이드바
# =========================================================
def render_lesson_sidebar(
    unit_title: str,
    current_lesson: str,
    lessons: list,
    unit_page: str,
):
    """
    소단원 학습 페이지에서 사용하는 공통 사이드바

    lessons 예시:
    [
        {
            "id": "2-1",
            "title": "문제 이해와 분석",
            "page": "pages/02_01_문제이해와분석.py",
            "enabled": True,
        },
        ...
    ]
    """

    with st.sidebar:

        # -------------------------------------------------
        # 로고
        # -------------------------------------------------
        st.markdown(
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
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")

        # -------------------------------------------------
        # 단원
        # -------------------------------------------------
        st.markdown(
            f"### {unit_title}"
        )

        if st.button(
            "← 단원 목록으로",
            key="sidebar_unit_back",
            use_container_width=True,
        ):
            st.switch_page(unit_page)

        st.markdown("---")

        # -------------------------------------------------
        # 소단원 목록
        # -------------------------------------------------
        for lesson in lessons:

            lesson_id = lesson["id"]
            title = lesson["title"]

            page = lesson.get(
                "page"
            )

            enabled = lesson.get(
                "enabled",
                True,
            )

            button_label = (
                f"{lesson_id}  {title}"
            )

            # 현재 페이지
            if lesson_id == current_lesson:

                st.button(
                    button_label,
                    key=f"sidebar_{lesson_id}",
                    type="primary",
                    use_container_width=True,
                )

            # 활성 페이지
            elif enabled and page:

                if st.button(
                    button_label,
                    key=f"sidebar_{lesson_id}",
                    use_container_width=True,
                ):
                    st.switch_page(page)

            # 비활성 페이지
            else:

                st.button(
                    button_label,
                    key=f"sidebar_{lesson_id}",
                    disabled=True,
                    use_container_width=True,
                )

        st.markdown("---")

        # -------------------------------------------------
        # 홈
        # -------------------------------------------------
        if st.button(
            "🏠 메인 화면",
            key="sidebar_home",
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
def render_breadcrumb(
    unit_title: str,
    lesson_title: str,
):
    st.markdown(
        f"""
        <div style="
            color:#64748b;
            font-size:13px;
            margin-bottom:18px;
        ">
            홈
            &nbsp;›&nbsp;
            {unit_title}
            &nbsp;›&nbsp;
            {lesson_title}
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# 학습 Hero
# =========================================================
def render_lesson_hero(
    unit_number: str,
    lesson_number: str,
    title: str,
    description: str,
    flow_text: str,
    icon: str = "🧠",
):
    st.markdown(
        f"""
        <div class="hero-section">

            <div class="hero-content">

                <div class="hero-tag">
                    UNIT {unit_number}
                    ·
                    LESSON {lesson_number}
                </div>

                <h2>
                    {title}
                </h2>

                <p>
                    {description}
                </p>

            </div>

            <div class="hero-visual">

                <div class="code-window">

                    <div class="code-window-header">
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>

                    <pre>{flow_text}</pre>

                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# 섹션 제목
# =========================================================
def render_section_header(
    label: str,
    title: str,
    description: str = "",
    space: bool = False,
):
    section_class = (
        "section-header section-space"
        if space
        else "section-header"
    )

    description_html = ""

    if description:

        description_html = (
            f"<p>{description}</p>"
        )

    st.markdown(
        f"""
        <div class="{section_class}">

            <div>

                <div class="section-label">
                    {label}
                </div>

                <h3>
                    {title}
                </h3>

                {description_html}

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# 학습 목표 카드
# =========================================================
def render_learning_goals(
    goals: list,
):
    """
    goals 예시:

    [
        {
            "icon": "📍",
            "title": "현재 상태",
            "description": "현재 상황을 설명할 수 있습니다."
        },
        ...
    ]
    """

    columns = st.columns(
        len(goals)
    )

    for index, (
        col,
        goal,
    ) in enumerate(
        zip(
            columns,
            goals,
        ),
        start=1,
    ):

        with col:

            st.markdown(
                f"""
                <div class="learning-flow-card">

                    <div class="flow-step">
                        GOAL {index:02d}
                    </div>

                    <div class="flow-icon">
                        {goal["icon"]}
                    </div>

                    <h4>
                        {goal["title"]}
                    </h4>

                    <p>
                        {goal["description"]}
                    </p>

                </div>
                """,
                unsafe_allow_html=True,
            )


# =========================================================
# 개념 카드
# =========================================================
def render_concept_cards(
    concepts: list,
):
    """
    concepts 예시:

    [
        {
            "number": "01",
            "title": "현재 상태",
            "description": "현재 문제 상황입니다."
        },
        ...
    ]
    """

    columns = st.columns(
        len(concepts)
    )

    for col, concept in zip(
        columns,
        concepts,
    ):

        with col:

            st.markdown(
                f"""
                <div class="unit-card active">

                    <div class="unit-number">
                        {concept["number"]}
                    </div>

                    <h3>
                        {concept["title"]}
                    </h3>

                    <p>
                        {concept["description"]}
                    </p>

                </div>
                """,
                unsafe_allow_html=True,
            )


# =========================================================
# 학습 상태
# =========================================================
def render_lesson_status(
    lesson_id: str,
    lesson_title: str,
    score_key: str,
    pass_score: int = 4,
    total_score: int = 5,
):
    """
    st.session_state.unit2_progress 같은
    progress dictionary를 사용하는 구조
    """

    render_section_header(
        label="LESSON STATUS",
        title="학습 상태",
        space=True,
    )

    progress = st.session_state.get(
        "unit2_progress",
        {},
    )

    completed = progress.get(
        lesson_id,
        False,
    )

    score = st.session_state.get(
        score_key,
    )

    if completed:

        st.success(
            f"🎉 **{lesson_id} {lesson_title}** 학습을 완료했습니다."
        )

        if score is not None:

            st.write(
                f"형성평가 점수: "
                f"**{score} / {total_score}점**"
            )

    else:

        st.info(
            f"형성평가에서 "
            f"{pass_score}점 이상을 받으면 "
            f"{lesson_id} 학습이 완료됩니다."
        )


# =========================================================
# 핵심 정리
# =========================================================
def render_summary(
    title: str,
    content: str,
):
    with st.expander(
        f"📚 {title}",
        expanded=False,
    ):

        st.markdown(
            content
        )


# =========================================================
# 이전 / 다음 페이지 이동
# =========================================================
def render_navigation(
    previous_label: str = None,
    previous_page: str = None,
    next_label: str = None,
    next_page: str = None,
    next_enabled: bool = True,
):
    st.markdown(
        "<br>",
        unsafe_allow_html=True,
    )

    nav_left, nav_right = st.columns(
        2
    )

    # -----------------------------------------------------
    # 이전
    # -----------------------------------------------------
    with nav_left:

        if (
            previous_label
            and previous_page
        ):

            if st.button(
                f"← {previous_label}",
                key="lesson_previous",
                use_container_width=True,
            ):

                st.switch_page(
                    previous_page
                )

    # -----------------------------------------------------
    # 다음
    # -----------------------------------------------------
    with nav_right:

        if (
            next_label
            and next_page
            and next_enabled
        ):

            if st.button(
                f"{next_label} →",
                key="lesson_next",
                type="primary",
                use_container_width=True,
            ):

                st.switch_page(
                    next_page
                )

        elif next_label:

            st.button(
                f"{next_label} →",
                key="lesson_next_disabled",
                disabled=True,
                use_container_width=True,
            )


# =========================================================
# Footer
# =========================================================
def render_footer(
    subtitle: str,
):
    st.markdown(
        f"""
        <div class="app-footer">

            <strong>
                Algorithm Design Learning Lab
            </strong>

            <span>
                {subtitle}
            </span>

        </div>
        """,
        unsafe_allow_html=True,
    )