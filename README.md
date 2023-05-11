# Iowa Housing Market

---

## Introduction

This is my 5th and last Portfolio Project developed as part of my Full Stack Software Developer and Predictive Analytics studies with Code Institute.

This is a Data Analytics and Machine Learning project to clean and engineer data for an ML Model that predicts the value of a house in Ames, Iowa and to help visualize the most important features considered when predicting that value.

The project is deployed [here](https://www.kaggle.com/codeinstitute/housing-prices-data).

I will develop the steps taken to accomplish this proyect using an approach to **CRISP-DM** metodology.

---

# Bussiness Understanding

## Business Requirements

This project is an example of how using public datasets, we can develop Machine Learning tools for analysing the market in order to take accurate decisions.

For any project, we must focus it's approach to be useful in a bussines perspective. In this example, We took a ficticious caracther named Beberly Crusher, she's a Doctor living in Montreal. She received an inheritance from a deceased great-grandfather located in Ames, Iowa.

As a good friend, she requested us to help in maximising the sales price for the inherited properties.

Although Dr. Crusher has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

## Hypothesis and how to validate?

After reviewing the dataset I have formulated two hypotheses. These hypotheses will guide the data analysis.

1 - We can predict the sales price for any house in Ames iowa.

Reasoning: By analysing the database records of the transactions made in Ames, state of Iowa, we can predict a sales price for a particular house.

2 - Some house attributes will affect the price more than others.

Reasoning: Size of the ground floor living area, the basement and the garage affect and help determine prices, by analysing this historic information from the dataset we will find a guide to fit a price range for our customers properties.

## User Stories

* As a client, i can navigate the dashboard pages easily so that i can get insights from the data analysis.
* As a client, i can study which are the most important features so that i can understand wich factors modify the prices.
* As a client, i can input information on the features wit high correlation to the sales price so that i can predict the value of any other house in Ames, Iowa.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

**Problem Statement 1:** The heiress is interested in discovering how house attributes correlate with sale prices. Therefore, she expects data visualizations of the correlated variables against the sale price.

* As a client I want to inspect the data related to the house records, so that i can discover how the house attributes correlate with the sales price.
* As a client I want to conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to Sale Price, so that I can discover how the house attributes correlate with the sale price.
* As a client I want to plot the main variables against Sale Price to visualize insights, so that ican discover how the house attributes correlate with the sale price.

**Problem Statement 2:** The heiress is also interested in predicting the house sale prices for her 4 inherited houses, and any other house in Ames, Iowa.

* As a client I want to predict the sale price for a given house. We want to build a ML model, so that the client can predict the house sale price from her inherited houses, and any other house in Ames, Iowa.

In order to do so, we may deliver an ML system that is capable of reliably predicting the summed sales price of the 4 inherited houses.

Either by using conventional ML or Neural Networks to map the relationships between the features and the target.

We agreed with the client an R2 score of at least **0.75** on the train set as well as on the test set.

The data will be explaines and visualized using a dashboard. No API needed for this project.

## ML Business Case

We can use conventional data analysis to investigate how house attributes are correlated with the sale prices.

---

# Data Understanding

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data).

* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.

Once the data is loaded we will review it and save a copy in our repository, under the input folder.

---

# Data Preparation

* We'll study the data types and distribution by running a ProfileReport.

* We will run correlation studies and PPS method and plot the results in order to find the variables with the most correlation to SalePrice.

* In order to improve the dataset performance, we will engineer features from the data that have missing
information and/or non relevant information.  

* We look for missing data, run Heatmaps to define feature relevance and check it's distribution.

* We define a cleaning approach for the different variables.

  * GarageYrBlt | ArbitraryNumberImputer
  * GarageFinish | CategoricalImputer
  * BsmtFinType1 | CategoricalImputer
  * BedroomAbvGr	|ArbitraryNumberImputer
  * 2ndFlrSF | ArbitraryNumberImputer
  * LotFrontage | MeanMedianImputer
  * MasVnrArea | MeanMedianImputer
  * Enclosed Porch | Drop
  * WoodDeckSF	| Drop

* We turn datatype float to Integer.

* We split de dataset into Train and Test set.

## Feature Engineering

* We run the custom function from the **Feature-engine lesson** looking for an approach to handle the tasks to implement the feature engineering process.

* We apply **Categorical Encoding, Numerical Transformation and Smart Correlation Selection** transformers.

---

# Modeling

## Regression Model

We will develop ML models that can predict Sale Price based on the input features.The data suggests a regressor (MLM Linear Regresion) where the target is the sale price.

The inputs are house attribute information and the output is the predicted sale price.

Model Evaluation: We will evaluate the ML models using metrics such as mean squared error, accuracy, and precision/recall to ensure they are accurate and effective.

## Hyperparameter Optimisation

* Use default hyperparameters to find most suitable algorithm.

* Run extensive search on most suitable model to find best hyperparameter configuration.

---

# Evaluation

* Evaluate Pipeline performance, Applying Regressor with PCA and
Explore potential values for PCA n_components.

* Refit pipeline with best features in order to improve Model performance.

## Business Outcomes

* By utilizing ML to optimize sales price suggestions,The client will maximize the sales price for the inherited properties. Additionally, the Model could be used with other datasets to be trained in different cities.

* By enhace hyperparameters we improve to 0.80, superior to the client business requirement that was an R2 score of at least 0.75.

---

# Deployment

## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick project summary

A project summary page, showing the project dataset summary and the client's requirements.

* Describe Project Dataset
* State Business Requirements
* Dataset Content Guidelines

### Page 2:  House Sale Price Study

* State business requirement 1
  * Checkbox: data inspection on housing sale dataset.
  * Display the number of rows and columns in the data.
  * Display the first ten rows of the data.
  * Display the variables with the strongest correlation to sale price.able

### Page 3: Price estimatior tool

* A page displaying the 4 houses' attributes and their respective predicted sale price.
* Displays a message informing the summed predicted price for all 4 inherited houses.

### Page 4: Project Hypothesis and Validation

Before the analysis, we knew we wanted this page to describe each project hypothesis, the conclusions, and how we validated each.

After the data analysis, we can report that:
1 - An evaluation of sales prices of other houses in the area based on attributes similar to attributes of each of the clients 4 inherited houses should provide a prediction of sales price for each house respectively.
2 - The correlation analysis shows that the sizes of the ground floor living area, the first floor, the basement and the garage, play a key role in determining house price. In addition, the year the house was built and the overall quality of materials used and the finishes in the house also play a significant role in determining house price.

After conducting the analysis we answered our hypothesis.

1 - We can predict the sales price for any house in Ames iowa.

* Correct. Considering the unique features of each house, we can predict a price by merging the information of features that have high correlatio so Sale Price.

2 - Some house attributes will affect the price more than others.

* Correct. Certain features of the house affect either in a positive or negative way, and we can predict a Sale Price considering this features.

### Page 5: Model Performance

* Considerations and conclusions after the pipeline is trained
* Present ML pipeline steps
* Feature importance
* Pipeline performance

## Deploying to Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

---

## Main Data Analysis and Machine Learning Libraries

* Kaggle | Fetch data
* Numpy | Manage data
* Pandas | Profile Report
* Scikit Learn | Create ML Pipelines, Regressor
* Matplot | Plot results from correlation studies
* Seaborn | Plot results from correlation studies
* Scypy | Matemathical operations
* Seaborn | Plot results from correlation studies

## Bugs

**Bug1**

To begin with, i started woking on this project using GitPod. I tried to install requirements.txt and i got the first error.

This error message suggests that there might be an issue with the installation of the NumPy package, specifically with the build dependencies required to install the package. The error message states that the process failed while preparing metadata (pyproject.toml), which indicates that there might be an issue with the package's setup file.

One possible solution to this issue is to try installing the package again after making sure that all the required dependencies are installed. You could also try upgrading pip and setuptools to the latest version by running the following command:

ERROR: Cannot install -r /workspace/PP5-iowa-housing-market/requirements.txt (line 2) and numpy==1.18.5 because these package versions have conflicting dependencies.

The conflict is caused by:
    The user requested numpy==1.18.5
    pandas 1.4.3 depends on numpy>=1.21.0; python_version >= "3.10"

I went thru Slack in order to find guidance; i was told that this project can't be made o Gitpod, because the python version is intended to work on is 3.8.12 and gitpod allows 3.10 and above.

I stop working in Gitpod and change to Code Anywhere to create a new enviroment there.

**Bug2**

Working in Code Anywhere has been a nightmare.

Many times the workspace didn't even start, most of the times it did after no less than 10 minutes.

While creating jupiter notebooks, The kernel didn't start, and if it finally started, it got frozen by running cells.

But the worst issue i encountered was at the moment of commit to Github. While in Code Anywhere appears to be pushing the code it was not making the commits to github.

I did create the workspace many times, i downloaded copies of the .ypbn files and uploaded to the repository manually; for this reason it may show few commit messages.

**Bug3**

Before running the stramlit app i had to install altair==4.1.0 from terminal, wich replaced the 5.0 version pevioulsly installed. I did this because the streamlit app didnt run he first time and throw an error asking to change the version

**Bug4**

In order to deploy to heroku, i had to run heroku CLI command to change the stack to 20.
To acomplish this i followed the stepts indicated in the readme file originaly included in the Code Institute's template.
I also modified the runtime.txt file, changing the python version from 3.8.16 to 3.8.12

**Unfixed Bugs**

At the moment of submitting i found no bugs.

## Credits  

* As suggested in the learning lessons, I followed carefully the Walkthru projects and the Churnometer project, as well as the repository template for this project.
* The data source for this project was extracted from Kaggle.

## Acknowledgements (optional)

* To the Code Anywhere team.

---
