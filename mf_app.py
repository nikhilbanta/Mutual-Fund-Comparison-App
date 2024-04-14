import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def format_numeric(x):
    try:
        return '{:.2f}'.format(float(x))
    except ValueError:
        return x

def main():
    st.set_page_config(initial_sidebar_state="expanded",layout="wide")
    st.markdown("<h3 style='text-align: center; color: rainbow;'>Mutual Fund Returns Comparison App</h3>", unsafe_allow_html=True)
    # st.write("### Mutual Fund Returns Comparison App",)
    st.markdown(
    """
        <style>
            .appview-container .main .block-container {{
                padding-top: {padding_top}rem;
                padding-bottom: {padding_bottom}rem;
                }}

        </style>""".format(
        padding_top=1.9, padding_bottom=0
    ),
    unsafe_allow_html=True,
)

    # Load the data from the CSV file
    df = pd.read_csv("small_cap/small_cap_yearly_final.csv")

    # Display the DataFrame
    st.write("#### Small Cap Yearly Returns(%)")


    # Apply color gradient to the returns for each column

    cmap = LinearSegmentedColormap.from_list(
        'custom', [(0, 'lightsalmon'), (0.5, 'yellow'), (1, 'limegreen')])
    df_styled = df.style.background_gradient(cmap=cmap, axis=0)

    df_styled = df_styled.format("{:.2f}")

    # Round off returns columns to 2 decimal places
    returns_cols = [col for col in df.columns if col != 'Funds']
    df_styled = df_styled.format({col: "{:.2f}" for col in returns_cols})

    st.dataframe(data=df_styled,hide_index=True,height=800,use_container_width=True)
    st.markdown(
                """
                <style>
                [data-testid="stElementToolbar"] {
                    display: none;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
    disable_df_selection_css = """
    <style>
        div[role="grid"] div {user-select: none;}
    </style>
    """
    st.markdown(disable_df_selection_css, unsafe_allow_html=True)

    hide_github_icon = """
    #GithubIcon {
    visibility: hidden;
    }
    """
    st.markdown(hide_github_icon, unsafe_allow_html=True)

    st.caption('Data Updated till 13-April-2024.')
    st.caption('Developed with love :heart: in India :flag-in:')

if __name__ == "__main__":
    main()
