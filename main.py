import streamlit as st
from large_cap import *
from mid_cap import *
from small_cap import *
from flexi_cap import *
from elss import *

# Main function for the app
def main():
    st.set_page_config(initial_sidebar_state="expanded",layout="wide")
    st.header("Mutual Funds App")

    # Create navigation sidebar
    page = st.sidebar.radio("Select a page", ["Home", "Large Cap Funds","Flexi Cap Funds","ELSS Tax Saving Funds", "Mid Cap Funds", "Small Cap Funds"])

    # Routing logic
    if page == "Home":
        # st.header("Welcome to Mutual Fund Returns App")
        st.write("Please select a page from the sidebar to view returns of different types of mutual funds.")
        # Add image to the home page
        st.image("comp.png")

        

    elif page == "Large Cap Funds":
        large_cap_returns()
    elif page == "Flexi Cap Funds":
        flexi_cap_returns()
    elif page == "ELSS Tax Saving Funds":
        elss_returns()
    elif page == "Mid Cap Funds":
        mid_cap_returns()
    elif page == "Small Cap Funds":
        small_cap_returns()


    st.caption(f'Data Updated till {date.today()}')
    st.caption('Developed with :heart: by [Compounding Fish](https://twitter.com/compoundingFish) in India :flag-in:')

if __name__ == "__main__":
    main()