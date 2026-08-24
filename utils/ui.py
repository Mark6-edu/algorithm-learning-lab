from pathlib import Path
from textwrap import dedent

import streamlit as st


# =========================================================
# 프로젝트 루트 경로
# =========================================================
BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================
# CSS 불러오기
# =========================================================
def load_css(
    css_path: str = "assets/style.css",
):
    """
    외부 CSS 파일을 불러와 Streamlit 앱에 적용합니다.

    Parameters
    ----------
    css_path : str
        프로젝트 루트 기준 CSS 파일 경로
        기본값: assets/style.css
    """

    full_path = BASE_DIR / css_path

    if not full_path.exists():
        st.error(
            f"CSS 파일을 찾을 수 없습니다: {full_path}"
        )
        return

    css = full_path.read_text(
        encoding="utf-8"
    )

    # 중요:
    # st.markdown(..., unsafe_allow_html=True) 대신
    # st.html()을 사용합니다.
    st.html(
        f"<style>{css}</style>"
    )


# =========================================================
# HTML 렌더링
# =========================================================
def render_html(
    html: str,
):
    """
    HTML 문자열을 안전하게 렌더링합니다.

    Python 코드에서 보기 좋게 들여쓰기한 HTML 문자열 때문에
    Streamlit Markdown이 코드 블록으로 인식하는 문제를 방지합니다.

    사용 예:
        render_html(
            '''
            <div class="info-card">
                <strong>안녕하세요</strong>
            </div>
            '''
        )
    """

    cleaned_html = dedent(
        html
    ).strip()

    st.html(
        cleaned_html
    )


# =========================================================
# 세로 여백
# =========================================================
def add_space(
    size: int = 1,
):
    """
    세로 여백을 추가합니다.

    size
    ----
    1 : 작은 여백
    2 : 중간 여백
    3 이상 : 큰 여백
    """

    size = max(
        1,
        min(size, 5),
    )

    render_html(
        "<br>" * size
    )


# =========================================================
# 구분선
# =========================================================
def render_divider():
    """
    CSS에서 정의한 공통 구분선을 출력합니다.
    """

    render_html(
        """
        <div class="app-divider"></div>
        """
    )


# =========================================================
# Breadcrumb
# =========================================================
def render_breadcrumb(
    items: list[str],
):
    """
    페이지 경로를 출력합니다.

    예:
        render_breadcrumb(
            [
                "홈",
                "Ⅱ. 추상화와 모델링",
                "2-1 문제 이해와 분석",
            ]
        )
    """

    breadcrumb = (
        "&nbsp;›&nbsp;".join(items)
    )

    render_html(
        f"""
        <div class="app-breadcrumb">
            {breadcrumb}
        </div>
        """
    )


# =========================================================
# 상태 배지
# =========================================================
def render_badge(
    text: str,
    badge_type: str = "default",
):
    """
    작은 상태 배지를 출력합니다.

    badge_type:
        default
        primary
        success
        warning
        locked
    """

    allowed_types = {
        "default",
        "primary",
        "success",
        "warning",
        "locked",
    }

    if badge_type not in allowed_types:
        badge_type = "default"

    render_html(
        f"""
        <span class="app-badge app-badge-{badge_type}">
            {text}
        </span>
        """
    )


# =========================================================
# 정보 카드
# =========================================================
def render_info_card(
    title: str,
    description: str,
    icon: str = "💡",
):
    """
    간단한 정보 안내 카드를 출력합니다.
    """

    render_html(
        f"""
        <div class="info-card">

            <div class="info-card-icon">
                {icon}
            </div>

            <div class="info-card-content">

                <strong>
                    {title}
                </strong>

                <p>
                    {description}
                </p>

            </div>

        </div>
        """
    )


# =========================================================
# 빈 화면 안내
# =========================================================
def render_empty_state(
    title: str,
    description: str,
    icon: str = "📭",
):
    """
    데이터가 없거나 기능 준비 중일 때 사용하는 화면입니다.
    """

    render_html(
        f"""
        <div class="empty-state">

            <div class="empty-state-icon">
                {icon}
            </div>

            <h3>
                {title}
            </h3>

            <p>
                {description}
            </p>

        </div>
        """
    )


# =========================================================
# 일반 페이지 제목
# =========================================================
def render_page_title(
    eyebrow: str,
    title: str,
    description: str = "",
):
    """
    Hero가 필요하지 않은 일반 페이지의 제목 영역입니다.
    """

    description_html = ""

    if description:
        description_html = f"""
        <p>
            {description}
        </p>
        """

    render_html(
        f"""
        <div class="page-title-area">

            <div class="main-title-eyebrow">
                {eyebrow}
            </div>

            <h1>
                {title}
            </h1>

            {description_html}

        </div>
        """
    )


# =========================================================
# Metric 카드
# =========================================================
def render_metric_card(
    label: str,
    value: str,
    description: str = "",
    icon: str = "",
):
    """
    대시보드에서 사용할 수 있는 수치 카드입니다.
    """

    icon_html = ""

    if icon:
        icon_html = f"""
        <div class="metric-card-icon">
            {icon}
        </div>
        """

    description_html = ""

    if description:
        description_html = f"""
        <span>
            {description}
        </span>
        """

    render_html(
        f"""
        <div class="metric-card">

            {icon_html}

            <div class="metric-card-label">
                {label}
            </div>

            <strong>
                {value}
            </strong>

            {description_html}

        </div>
        """
    )


# =========================================================
# 간단한 상태 카드
# =========================================================
def render_status_card(
    title: str,
    description: str,
    status: str,
    icon: str = "📌",
):
    """
    학습 상태, 준비 중 등의 안내에 사용할 수 있는 카드입니다.
    """

    render_html(
        f"""
        <div class="info-card">

            <div class="info-card-icon">
                {icon}
            </div>

            <div class="info-card-content">

                <strong>
                    {title}
                </strong>

                <p>
                    {description}
                </p>

                <div style="
                    margin-top:8px;
                    color:#2563eb;
                    font-size:12px;
                    font-weight:700;
                ">
                    {status}
                </div>

            </div>

        </div>
        """
    )


# =========================================================
# 안전한 rerun
# =========================================================
def rerun():
    """
    현재 Streamlit 페이지를 다시 실행합니다.
    """

    st.rerun()