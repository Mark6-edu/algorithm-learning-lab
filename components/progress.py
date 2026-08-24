# components/progress.py

import streamlit as st


def init_unit_progress(
    progress_key: str,
    lesson_ids: list[str],
):
    """
    단원별 학습 진행 상태 초기화
    """

    if progress_key not in st.session_state:
        st.session_state[progress_key] = {
            lesson_id: False
            for lesson_id in lesson_ids
        }

    else:
        for lesson_id in lesson_ids:
            if lesson_id not in st.session_state[progress_key]:
                st.session_state[progress_key][lesson_id] = False


def init_score(
    score_key: str,
):
    """
    형성평가 점수 초기화
    """

    if score_key not in st.session_state:
        st.session_state[score_key] = None


def mark_lesson_complete(
    progress_key: str,
    lesson_id: str,
):
    """
    특정 학습 완료 처리
    """

    if progress_key not in st.session_state:
        st.session_state[progress_key] = {}

    st.session_state[progress_key][lesson_id] = True


def mark_lesson_incomplete(
    progress_key: str,
    lesson_id: str,
):
    """
    특정 학습 미완료 처리
    """

    if progress_key not in st.session_state:
        st.session_state[progress_key] = {}

    st.session_state[progress_key][lesson_id] = False


def is_lesson_complete(
    progress_key: str,
    lesson_id: str,
) -> bool:
    """
    특정 학습 완료 여부 반환
    """

    progress = st.session_state.get(
        progress_key,
        {},
    )

    return progress.get(
        lesson_id,
        False,
    )


def get_unit_progress(
    progress_key: str,
):
    """
    단원 진행 현황 계산

    return:
    {
        "completed": 2,
        "total": 4,
        "percent": 50,
        "is_completed": False
    }
    """

    progress = st.session_state.get(
        progress_key,
        {},
    )

    total = len(progress)

    completed = sum(
        bool(value)
        for value in progress.values()
    )

    if total == 0:
        percent = 0
    else:
        percent = int(
            completed / total * 100
        )

    return {
        "completed": completed,
        "total": total,
        "percent": percent,
        "is_completed": (
            total > 0
            and completed == total
        ),
    }


def get_next_incomplete_lesson(
    progress_key: str,
    lessons: list[dict],
):
    """
    아직 완료하지 않은 첫 번째 학습 반환

    lessons 예시:
    [
        {
            "id": "2-1",
            "title": "문제 이해와 분석",
            "page": "pages/02_01_문제이해와분석.py",
        },
        ...
    ]
    """

    progress = st.session_state.get(
        progress_key,
        {},
    )

    for lesson in lessons:

        lesson_id = lesson["id"]

        if not progress.get(
            lesson_id,
            False,
        ):
            return lesson

    return None


def save_quiz_score(
    score_key: str,
    score: int,
):
    """
    형성평가 점수 저장
    """

    st.session_state[
        score_key
    ] = score


def get_quiz_score(
    score_key: str,
):
    """
    저장된 형성평가 점수 반환
    """

    return st.session_state.get(
        score_key
    )


def process_quiz_result(
    progress_key: str,
    lesson_id: str,
    score_key: str,
    score: int,
    pass_score: int = 4,
):
    """
    형성평가 결과를 저장하고
    통과 시 학습 완료 처리
    """

    save_quiz_score(
        score_key=score_key,
        score=score,
    )

    passed = (
        score >= pass_score
    )

    if passed:
        mark_lesson_complete(
            progress_key=progress_key,
            lesson_id=lesson_id,
        )

    return passed


def render_unit_progress(
    progress_key: str,
    title: str = "학습 진행률",
):
    """
    단원 진행률 UI
    """

    status = get_unit_progress(
        progress_key
    )

    completed = status["completed"]
    total = status["total"]
    percent = status["percent"]

    st.markdown(
        f"""
        <div class="progress-wrapper">

            <div class="progress-header">

                <span>
                    {title}
                </span>

                <strong>
                    {percent}%
                </strong>

            </div>

            <div class="progress-track">

                <div
                    class="progress-bar"
                    style="width:{percent}%;">
                </div>

            </div>

            <div class="progress-description">
                {completed} / {total} 학습 완료
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    return status