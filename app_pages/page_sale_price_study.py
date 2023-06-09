import streamlit as st

from src.file_management import load_housing_price_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_sale_price_study_body():

    # load data
    df = load_housing_price_data()

    # hard copied from sale price study notebook
    # The 6 variables that correlate to Sale Price
    # These variables will be tested on strength to predicting Sale Price
    corr_var_list = ['1stFlrSF', 'GarageArea', 'GrLivArea',
                     'OverallQual', 'TotalBsmtSF', 'YearBuilt']

    st.write("### House Sale Price Study")
    st.info(
        f"* The client is interested in discovering how the house attributes "
        f"correlate with the sale price.\n"
        f"* Therefore, the client expects data visualizations of the "
        f"correlated variables against the sale price to show that."
    )

    # inspect data
    if st.checkbox("Inspect House Price Data"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"the first 10 rows are displayed below.")

        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* Correlation studies were conducted, using the Pearson and Spearman methods "
        f"to better understand how the variables correlate to sale price.\n"
        f"* The most correlated variable are: \n"
        f"  * **1stFlrSF, GarageArea, GrLivArea, OverallQual, TotalBsmtSF, YearBuilt**"
    )

    # Text based on "sale price study" notebook
    #  "Conclusions and Next steps" section
    st.info(
        f"#### The correlations and plots interpretation converge.\n"
        f"* The following are the variables isolated in the"
        f" correlation study:\n"
        f"* 1stFlrSF: First Floor square feet\n"
        f"* GarageArea: Size of garage in square feet\n"
        f"* GrLivArea: Above grade (ground) living area square feet\n"
        f"* OverallQual: Rates the overall material and finish of the house\n"
        f"* TotalBsmtSF: Total square feet of basement area\n"
        f"* YearBuilt: Original construction date\n\n"
        f"* The correlation analysis shows that the sizes of the "
        f" ground floor living area, Basement area and the garage area,"
        f" play a key role in determining house price\n"
        f" In addition, the year the house was built and the overall "
        f"quality of materials used and the finishes in the house\n\n"
        f" The plots show that the variables, isolated in the correlation ,\n"
        f" study, do indeed have a strong correlation and hence \n"
        f" possibly strong predictive power for Sale Price.\n\n"
        f" PLOT INTERPRETATION\n\n"
        f" Prediction vs Actual values for train and test sets\n\n"
        f" The blue dot indicates the actual value and its predicted value \n"
        f" provided by the ML Pipeline for a given datapoint. \n\n"
        f" The red line indicates where the predicted value in the actual value.\n\n"
        f" Ideally, the blue dots should follow along the red line. \n"
        f" We note there are few datapoints when the actual price is greater tha 500k,\n"
        f" and for these datapoints, the model tends to under estimate the sale price."
    )

    # Code copied from "sale price study" notebook
    # "EDA on the Correlated Variable List" section
    df_eda = df.filter(corr_var_list + ['SalePrice'])

    # Individual plots per variable
    if st.checkbox("Variable correlation to Sale Price"):
        variable_correlation_to_sale_price(df_eda, corr_var_list)


def variable_correlation_to_sale_price(df_eda, corr_var_list):
    # function created using "sale price study" notebook
    # "Visualize variable correlation to Sale Price" section
    target_var = 'SalePrice'
    for col in corr_var_list:
        plot_numerical(df_eda, col, target_var)
        st.write("\n\n")


def plot_numerical(df, col, target_var):
    # function created using "sale price study" notebook
    # "Visualize variable correlation to Sale Price" section

    fig, axes = plt.subplots(figsize=(15, 8))
    sns.regplot(data=df, x=col, y=target_var)
    plt.title(f"{col}", fontsize=20)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()
