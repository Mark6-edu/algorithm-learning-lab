import streamlit as st


def render_colab_card(
    title: str,
    description: str,
    colab_url: str,
    button_label: str = "🚀 Google Colab에서 실습하기",
    notebook_name: str | None = None,
):
    """
    Google Colab 실습 안내 카드

    Parameters
    ----------
    title : str
        실습 제목

    description : str
        실습 설명

    colab_url : str
        Colab 또는 GitHub 기반 Colab 링크

    button_label : str
        버튼 문구

    notebook_name : str | None
        노트북 파일명 표시용
    """

    notebook_html = ""

    if notebook_name:
        notebook_html = f"""
        <div style="
            margin-top:10px;
            color:#64748b;
            font-size:12px;
        ">
            📓 Notebook: {notebook_name}
        </div>
        """

    st.markdown(
        f"""
        <div class="colab-banner">

            <div>

                <div class="section-label">
                    GOOGLE COLAB
                </div>

                <h3>
                    {title}
                </h3>

                <p>
                    {description}
                </p>

                {notebook_html}

            </div>

            <div class="colab-logo">
                ☁️
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.link_button(
        button_label,
        colab_url,
        use_container_width=True,
    )


def render_colab_practice(
    practice_title: str,
    objectives: list[str],
    colab_url: str,
    notebook_name: str | None = None,
):
    """
    학습 목표가 포함된 Colab 실습 카드
    """

    st.markdown(
        f"### 🐍 {practice_title}"
    )

    st.write(
        "이번 실습에서는 다음 내용을 직접 확인합니다."
    )

    for objective in objectives:
        st.markdown(
            f"- {objective}"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    render_colab_card(
        title=practice_title,
        description=(
            "Google Colab에서 Python 코드를 직접 실행하고 "
            "값을 변경하면서 알고리즘의 동작을 확인해 보세요."
        ),
        colab_url=colab_url,
        notebook_name=notebook_name,
    )


def make_colab_url(
    github_user: str,
    repository: str,
    notebook_path: str,
    branch: str = "main",
):
    """
    GitHub에 저장된 ipynb 파일의 Colab 링크 생성

    예:
    https://colab.research.google.com/github/
    USER/REPO/blob/main/notebooks/unit2/lesson_2_1.ipynb
    """

    notebook_path = notebook_path.lstrip("/")

    return (
        "https://colab.research.google.com/github/"
        f"{github_user}/{repository}/blob/"
        f"{branch}/{notebook_path}"
    )