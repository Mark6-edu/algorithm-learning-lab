import streamlit as st


# =========================================================
# 형성평가 렌더링
# =========================================================
def render_quiz(
    questions: list,
    quiz_key: str,
    score_key: str,
    progress_key: str,
    lesson_id: str,
    lesson_title: str,
    pass_score: int = 4,
):
    """
    형성평가를 출력하고 채점하는 공통 컴포넌트

    Parameters
    ----------
    questions : list
        문항 목록

        예시:
        [
            {
                "question": "문제 해결 전의 상황은?",
                "options": [
                    "현재 상태",
                    "목표 상태",
                    "종료 상태",
                    "반복 상태",
                ],
                "answer": "현재 상태",
                "explanation": "문제 해결 전의 상황을 현재 상태라고 합니다.",
            }
        ]

    quiz_key : str
        해당 퀴즈의 고유 키
        예: "quiz_2_1"

    score_key : str
        점수를 저장할 session_state 키
        예: "lesson_2_1_score"

    progress_key : str
        진행률 딕셔너리 키
        예: "unit2_progress"

    lesson_id : str
        예: "2-1"

    lesson_title : str
        예: "문제 이해와 분석"

    pass_score : int
        학습 완료 처리 기준 점수
        기본값 4점
    """

    total_questions = len(questions)

    # -----------------------------------------------------
    # 세션 상태 초기화
    # -----------------------------------------------------
    if score_key not in st.session_state:
        st.session_state[score_key] = None

    if progress_key not in st.session_state:
        st.session_state[progress_key] = {}

    if lesson_id not in st.session_state[progress_key]:
        st.session_state[progress_key][lesson_id] = False

    # -----------------------------------------------------
    # 제목
    # -----------------------------------------------------
    st.markdown(
        f"## 📝 {lesson_id} 형성평가"
    )

    st.caption(
        f"총 {total_questions}문항입니다. "
        f"{pass_score}문항 이상 정답이면 학습 완료로 처리됩니다."
    )

    st.markdown("---")

    # -----------------------------------------------------
    # 학생 응답 저장
    # -----------------------------------------------------
    student_answers = []

    for index, item in enumerate(
        questions,
        start=1,
    ):

        question_text = item["question"]
        options = item["options"]

        answer = st.radio(
            f"{index}. {question_text}",
            ["선택하세요."] + options,
            key=f"{quiz_key}_q{index}",
        )

        student_answers.append(
            answer
        )

        st.markdown("<br>", unsafe_allow_html=True)

    # -----------------------------------------------------
    # 제출 버튼
    # -----------------------------------------------------
    if st.button(
        "형성평가 제출",
        key=f"{quiz_key}_submit",
        type="primary",
        use_container_width=True,
    ):

        # 미응답 확인
        if "선택하세요." in student_answers:

            st.warning(
                "모든 문항에 답한 후 제출해 주세요."
            )

            return None

        # -------------------------------------------------
        # 채점
        # -------------------------------------------------
        score = 0
        results = []

        for index, (
            item,
            student_answer,
        ) in enumerate(
            zip(
                questions,
                student_answers,
            ),
            start=1,
        ):

            correct_answer = item["answer"]

            is_correct = (
                student_answer
                == correct_answer
            )

            if is_correct:
                score += 1

            results.append(
                {
                    "number": index,
                    "question": item["question"],
                    "student_answer": student_answer,
                    "correct_answer": correct_answer,
                    "is_correct": is_correct,
                    "explanation": item.get(
                        "explanation",
                        "",
                    ),
                }
            )

        # 점수 저장
        st.session_state[
            score_key
        ] = score

        # -------------------------------------------------
        # 결과 출력
        # -------------------------------------------------
        st.markdown("---")

        st.markdown(
            "### 평가 결과"
        )

        score_percent = int(
            score
            / total_questions
            * 100
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "정답",
                f"{score}문항",
            )

        with col2:
            st.metric(
                "전체",
                f"{total_questions}문항",
            )

        with col3:
            st.metric(
                "정답률",
                f"{score_percent}%",
            )

        # -------------------------------------------------
        # 점수별 메시지
        # -------------------------------------------------
        if score == total_questions:

            st.success(
                f"🎉 모든 문항을 맞혔습니다! "
                f"**{score} / {total_questions}점**"
            )

        elif score >= pass_score:

            st.success(
                f"잘했습니다! "
                f"**{score} / {total_questions}점**입니다."
            )

        elif score >= max(
            1,
            pass_score - 1,
        ):

            st.warning(
                f"**{score} / {total_questions}점**입니다. "
                "틀린 내용을 확인하고 다시 도전해 보세요."
            )

        else:

            st.error(
                f"**{score} / {total_questions}점**입니다. "
                "개념 학습 내용을 다시 살펴보세요."
            )

        # -------------------------------------------------
        # 학습 완료 처리
        # -------------------------------------------------
        if score >= pass_score:

            st.session_state[
                progress_key
            ][lesson_id] = True

            st.success(
                f"✅ **{lesson_id} {lesson_title}** "
                "학습을 완료했습니다."
            )

        # -------------------------------------------------
        # 오답 분석
        # -------------------------------------------------
        wrong_results = [
            result
            for result in results
            if not result["is_correct"]
        ]

        if wrong_results:

            st.markdown("---")

            st.markdown(
                "### 🔍 오답 확인"
            )

            for result in wrong_results:

                with st.expander(
                    f"❌ {result['number']}번 문항"
                ):

                    st.markdown(
                        f"""
                        **문제**

                        {result["question"]}

                        **내 답**

                        {result["student_answer"]}

                        **정답**

                        {result["correct_answer"]}
                        """
                    )

                    if result[
                        "explanation"
                    ]:

                        st.info(
                            "💡 "
                            + result[
                                "explanation"
                            ]
                        )

        else:

            st.balloons()

        # -------------------------------------------------
        # 결과 반환
        # -------------------------------------------------
        return {
            "score": score,
            "total": total_questions,
            "percent": score_percent,
            "passed": score >= pass_score,
            "results": results,
        }

    return None


# =========================================================
# 간단한 단일 문항
# =========================================================
def render_check_question(
    question: str,
    options: list,
    answer: str,
    key: str,
    explanation: str = "",
):
    """
    학습 중간에 사용하는 간단한 확인 문제

    형성평가 점수에는 포함되지 않음
    """

    selected = st.radio(
        question,
        ["아직 선택하지 않음"] + options,
        key=key,
    )

    if selected == "아직 선택하지 않음":
        return None

    if selected == answer:

        st.success(
            "정답입니다! ✅"
        )

        if explanation:
            st.info(
                f"💡 {explanation}"
            )

        return True

    st.error(
        "다시 생각해 봅시다."
    )

    if explanation:

        st.caption(
            "힌트: "
            + explanation
        )

    return False