![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Gitpod Template Instructions

Welcome,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Gitpod Template Instructions section of this README.md file,  and modify the remaining paragraphs for your own project. Please do read the Gitpod Template Instructions at least once, though! It contains some important information about Gitpod and the extensions we use.

## Gitpod Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with *Regenerate API Key*.

# Iowa Housing Market

## Introduction

This is my 5th and last Portfolio Project developed as part of my Full Stack Software Developer and Predictive Analytics studies with Code Institute.

This is a Machine Learning project, It is based on a dataset of Housing market history in Ames, Iowa.

The Project is both a data analysis and a machine learning application.

The data analysis helps users understand what factors affect the use of bike insted of other transport services such as bus or subway, the duration of travel, departure and arrival position.

The machine learning application allows users to input temperature, humidity, wind speed,...etc information and get predictions of bike rental usage.

The project is deployed here

## Business Requirements

This is an example of how using public datasets, we can develop Machine Learning tools for analysing the market in order to take accurate decisions.

For this example, We took a ficticious caracther named Beberly, she's a Doctor living in Montreal. She received an inheritance from a deceased great-grandfather located in Ames, Iowa.

As a good friend, she requested us to help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

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

As a user, i can select house features that will modify the house price.

## Hypothesis and how to validate?

* List here your project hypothesis(es) and how you envision validating it (them).

After reviewing the dataset I have formulated several hypotheses. These hypotheses will guide the data analysis.

* Some house attributes will affect the price more than others.

Reasoning: Size, construction year and habitable surface affect the prices in different manners, by analysing this historic information from the dataset we will find a guide to fit a price range for our customers properties.

* We can predict the sales price for any house in Ames iowa.

Reasoning: By applying the house information and comparing to the database, we can predict a sales price for a particular house.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

* List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.

**Problem Statement 1:** The heiress is interested in discovering how house attributes correlate with sale prices. Therefore, she expects data visualizations of the correlated variables against the sale price.

**Problem Statement 2:** The heiress is also interested in predicting the house sale prices for her 4 inherited houses, and any other house in Ames, Iowa.

In order to do so, we may deliver an ML system that is capable of reliably predicting the summed sales price of the 4 inherited houses.

Either by using conventional ML or Neural Networks to map the relationships between the features and the target.

We agreed with the client an R2 score of at least 0.75 on the train set as well as on the test set.

The data will be explaines and visualized using a dashboard. NO api needed for this project.

## ML Business Case

* In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.

We can use conventional data analysis to investigate how house attributes are correlated with the sale prices.

The data suggests a regressor (MLM Linear Regresion) where the target is the sale price.

The inputs are house attribute information and the output is the predicted sale price.

Regression Model
We want an ML model to predict tenure levels, in months, for a prospect expected to churn. A target variable is a discrete number. We consider a regression model, which is supervised and uni-dimensional.
Our ideal outcome is to provide our sales team with reliable insight into onboarding customers with a higher sense of loyalty.
The model success metrics are
At least 0.7 for R2 score, on train and test set
The ML model is considered a failure if:
after 12 months of usage, the model's predictions are 50% off more than 30% of the time. Say, a prediction is >50% off if predicted 10 months and the actual value was 2 months.
The output is defined as a continuous value for tenure in months. It is assumed that this model will predict tenure if the Predict Churn Classifier predicts 1 (yes for churn). If the prospect is online, the prospect will have already provided the input data via a form. If the prospect talks to a salesperson, the salesperson will interview to gather the input data and feed it into the App. The prediction is made on the fly (not in batches).
Heuristics: Currently, there is no approach to predict the tenure levels for a prospect.
The training data to fit the model comes from the Telco Customer. This dataset contains about 7 thousand customer records.
Train data - filter data where Churn == 1, then drop the Churn variable. Target: tenure; features: all other variables, but total charges and customerID

Data Collection: We will collect data on temperature, weather conditions, bike availability, and user rental history.

Data Preprocessing: We will preprocess the data by cleaning and transforming it into a format that can be used for modeling.

Feature Engineering: We will engineer features from the data, such as weather conditions, time of day, location, and day type (holiday, working day, weekend), to optimize bike availability, pricing, and promotions.

Model Development: We will develop ML models that can predict rental usage based on the input features. We will use regression and classification models for this purpose.

Model Evaluation: We will evaluate the ML models using metrics such as mean squared error, accuracy, and precision/recall to ensure they are accurate and effective.

Deployment: Once the ML models are trained and evaluated, we will deploy them into the bike rental system to optimize rental usage based on the input features.

Maintenance and Monitoring: We will continuously monitor the ML models' performance and update them as needed to ensure they are effective and accurate over time.

Business Outcomes: By utilizing ML to optimize sales price suggestions,The client will maximize the sales price for the inherited properties. Additionally, the Model can be used with other datasets to be trained in different cities.

1. Information gathering and data collection.

2. Data visualization, cleaning, and preparation.

3. Model training, optimization and validation.

4. Dashboard planning, designing, and development.

5. Dashboard deployment and release.

## Dashboard Design (Streamlit App User Interface)

* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items that your dashboard library supports.

### Page 1: Quick project summary

A project summary page, showing the project dataset summary and the client's requirements.

Describe Project Dataset

State Business Requirements

### Page 2: Price correlation Vs. features

A page listing your findings related to which features have the strongest correlation to the house sale price.

### Page 3: Price Vs. features graphics

A page displaying the 4 houses' attributes and their respective predicted sale price. It should display a message informing the summed predicted price for all 4 inherited houses. You should add interactive input widgets that allow a user to provide real-time house data to predict the sale price.

### Page 4: Project Hypothesis and Validation

A page indicating your project hypothesis(es) and how you validated it across the project.

### Page 5: Model Performance

A technical page displaying your model performance. If you deployed an ML pipeline, you have to display your pipeline steps.

Considerations and conclusions after the pipeline is trained
Present ML pipeline steps
Feature importance
Pipeline performance

* Eventually, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)

THERE SHOOULD BE A PAGE FOR EACH MACHINE LEARNING PROJECT.

## Unfixed Bugs

* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not valid reason to leave bugs unfixed.

Bug1 - This error message suggests that there might be an issue with the installation of the NumPy package, specifically with the build dependencies required to install the package. The error message states that the process failed while preparing metadata (pyproject.toml), which indicates that there might be an issue with the package's setup file.

One possible solution to this issue is to try installing the package again after making sure that all the required dependencies are installed. You could also try upgrading pip and setuptools to the latest version by running the following command:

ERROR: Cannot install -r /workspace/PP5-iowa-housing-market/requirements.txt (line 2) and numpy==1.18.5 because these package versions have conflicting dependencies.

The conflict is caused by:
    The user requested numpy==1.18.5
    pandas 1.4.3 depends on numpy>=1.21.0; python_version >= "3.10"

## Deployment

### Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.

## Credits  

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

* The text for the Home page was taken from Wikipedia Article A
* Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

* The photos used on the home and sign-up page are from This Open Source site
* The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)

* In case you would like to thank the people that provided support through this project.
