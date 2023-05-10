import streamlit as st


def page_project_hypothesis_body():

    st.success(
        f"### Project Hypothesis and Validation\n\n"
        f"* We can predict the sales price for any house in Ames iowa. "
        f"By analysing the database records of the real state"
        f" transactions made in Ames, state of Iowa, "
        f"we can predict a sales price for a particular house.\n\n"

        f"* Some house attributes will affect the price more than others "
        f"Size of the ground floor, living area, the basement and garage "
        f"affect and help determine prices, by analysing historic\n"
        f" information from the dataset we will find a guide to fit "
        f"a price range for our customer's properties."
    )
