# Data-Mining-Project-Diabetes-Detection

## Introduction
This is my course project for CPS844 (Data Mining) at TMU, when I took the course during the Winter 2025 term. In this project, we chose a dataset and predict the correct class. We were required to perform the following tasks:
- Perform exploratory data analysis and decide whether to do any pre-processing.
- Try at least 5 different data mining algorithms to see which performs the best.
- Try at least 1 feature selection algorithm and report on which attributes are most important for the prediction.
- Compare the accuracy of all the algorithms with or without feature selection and report on whether feature selection helps.
- Report on anything else you think you can do.

For the project, I chose diabetes detection as my topic. The dataset comes from a telephone survey conducted by the CDC. The Behavioural Risk Factor Surveillance System (BRFSS) is an annual survey that collects responses from over 400,000 Americans. The data collected includes information on health-related risk behaviours (like drinking and smoking), chronic health conditions, use of health care services, and demographic information.

## Data Exploration and Preprocessing

The dataset can be found on [Kaggle](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset). There are 3 versions of the dataset:
- Diabetes_012 (0 = no diabeters, 1 = prediabetes, 2 = diabetes)
- Diabetes_binary (0 = no diabetes, 1 = prediabetes/diabetes)
- Diabetes_binary_5050 (same as Diabetes_binary, but there is a 50/50 split for no diabetes and diabetes) (This one was used to avoid any problems that could arise from a class imbalance)

The dataset consists of 21 features that can be used. Most attributes are binary, with some ordinal data (coded as integers), and BMI as an integer. Before any analysis and modelling, the data was examined for inconsistencies (removed duplicates, empty values and errors). The data was then checked for outliers using boxplots. From the boxplots, outliers were observed in the "BMI", "MentHlth", and "PhysHlth" columns. The "BMI" column was standardized using sklearn's StandardScaler function. The "MentHlth" and "PhysHlth" columns were integers that represent the number of days out of the last 30 where the participant had bad mental/physical health days. These were discretized into 2 equal interval bins, representing whether the participant had more bad health days than good.

## Testing and Models

For analysis, the following algorithms will be tested and evaluated:
- **Decision trees**: data is split into branches based on the feature attributes to make predictions.
- **Logistic regression**: model that uses a linear regression model and transforms it into a probability for binary classification.
- **Support vector machines**: an algorithm that uses linear models to implement nonlinear class boundaries
- **K nearest neighbours**: an instance-based learning algorithm that makes predictions for a point based on its closest neighbouring points.
- **Random forests**: a  group of deecision trees.

For each model, ten-fold cross validation will be used to evaluate each model except for the support vector machine, as it has the longest computation time compared to the other models. The average accuracy, precision, recall, and f1-score from the cross validations will be examined.

In addition, sklearn's feature selection will be used, and cross validation will also be performed on the resulting feature selection set to see if the models benefit from it vs. using all the feature attributes. In sklearn, the SelectKBest function has an argument score_func, which determines what test is done to find the best features to use. For classification, the recommended values are chi2, f_classif, and mutual_info_classif. Mutual_info_classif was chosen for the score function, as it automatically deals with both continuous and discrete features, whereas the former work better for one type. The default number of features to select is 10; therefore only the 10 best features will be included in the feature selection set. From the feature selection algorithm, the following columns were returned: HighBP, HighChol, CholCheck, BMI, HeartDiseaseorAttack, PhysActivity, GenHlth, DiffWalk, Age, and Imcome.

## Notes on each model
### Decision Tree
The decision tree was tested first with default arguments, and then with values for max depth that gave the highest accuracy (8 for full dataset, 9 for the feature selection set).

### Logistic Regression
Given the default number of max iterations (100), logistic regression fails to reach the minimum default tolerance (0.0001), so the number of max iterations was increased to 200.

### Support Vector Machine
The default kernel function for the support vector machine was the radial basis function. SVM was also tested with the linear and polynomial kernel functions were used. There are other kernel functions, but they weren't tested due to time constraints.

### K Nearest Neighbours
K nearest neighbours was initially tested with 5 neighbours, the default number. Other choices for number of neighbours were used: 11, 21, 31, 51, and 75. Odd numbers were used to avoid possible ties.

### Random Forest
There are two arguments for maximum depth and number of trees in the forest. First, a max depth of 8 and 100 trees were used (depth of 8 came from the decision tree model). The model was tested again with 50 trees, and then with 100 trees with max depths of 12 (for the full dataset) and 9 (for the feature selection set).


## Results 

### Decision Tree
**Before Feature Selection**
|Model|Accuracy|Precision|Recall|F1 Score|
|:-------------------|:------:|:------:|:------:|:------:|
|Default depth|0.6500|0.6598|0.6430|0.6512|
|Depth=8|0.7372|0.7252|0.7780|0.7505|

**After Feature Selection**
|Model|Accuracy|Precision|Recall|F1 Score|
|:-------------------|:------:|:------:|:------:|:------:|
|Default depth|0.6666|0.6880|0.6430|0.6574|
|Depth=9|0.7373|0.7243|0.7800|0.7510|

### Logistic Regression
**Before Feature Selection**
|Model|Accuracy|Precision|Recall|F1 Score|
|:-------------------|:------:|:------:|:------:|:------:|
|tol=0.0001|0.7442|0.7378|0.7706|0.7538|
|tol=0.0005|0.7439|0.7378|0.7698|0.7534|
|tol=0.00001|0.7442|0.7378|0.7705|0.7537|

**After Feature Selection**
|Model|Accuracy|Precision|Recall|F1 Score|
|:-------------------|:------:|:------:|:------:|:------:|
|tol=0.0001|0.7404|0.7347|0.7658|0.7499|
|tol=0.0005|0.7403|0.7347|0.7654|0.7497|
|tol=0.00001|0.7404|0.7347|0.7659|0.7499|

### Support Vector Machine
**Before Feature Selection**
|Model|Accuracy|Precision|Recall|F1 Score|
|:-------------------|:------:|:------:|:------:|:------:|
|Radial basis function, 5 fold CV|0.7481|0.7194|0.8270|0.7694|
|Linear kernel function, 5 fold CV|0.7441|0.7283|0.7922|0.7589|
|Polynomial kernel function, 5 fold CV|0.7485|0.7311|0.7988|0.7635|

**After Feature Selection**
|Model|Accuracy|Precision|Recall|F1 Score|
|:-------------------|:------:|:------:|:------:|:------:|
|Radial basis function, 5 fold CV|0.7428|0.7147|0.8222|0.7647|
|Linear kernel function, 5 fold CV|0.7401|0.7244|0.7885|0.7551|
|Polynomial kernel function, 5 fold CV|0.7413|0.7448|0.7470|0.7458|

### K Nearest Neighbours
**Before Feature Selection**
|Model|Accuracy|Precision|Recall|F1 Score|
|:-------------------|:------:|:------:|:------:|:------:|
|5 neighbours|0.7027|0.7092|0.7035|0.7063|
|11 neighbours|0.7223|0.7188|0.7451|0.7317|
|31 neighbours|0.7354|0.7223|0.7788|0.7494|
|75 neighbours|0.7410|0.7242|0.7920|0.7565|

**After Feature Selection**
|Model|Accuracy|Precision|Recall|F1 Score|
|:-------------------|:------:|:------:|:------:|:------:|
|5 neighbours|0.7031|0.7175|0.6862|0.7014|
|11 neighbours|0.7241|0.7246|0.7375|0.7310|
|31 neighbours|0.7359|0.7247|0.7745|0.7487|
|75 neighbours|0.7398|0.7241|0.7883|0.7548|

### Random Forest
**Before Feature Selection**
|Model|Accuracy|Precision|Recall|F1 Score|
|:-------------------|:------:|:------:|:------:|:------:|
|Default depth, 100 trees|0.7446|0.7278|0.7947|0.7597|
|Default depth, 50 trees|0.7446|0.7283|0.7936|0.7595|
|Depth=12, 100 trees|0.7472|0.7305|0.7965|0.7620|

**After Feature Selection**
|Model|Accuracy|Precision|Recall|F1 Score|
|:-------------------|:------:|:------:|:------:|:------:|
|Default depth, 100 trees|0.7436|0.7271|0.7931|0.7587|
|Default depth, 50 trees|0.7440|0.7272|0.7942|0.7592|
|Depth=9, 100 trees|0.7438|0.7273|0.7934|0.7589|

From the results, when using the full feature set, the support vector machine had the best accuracy, recall, and f1, while logistic regression offered the best precision. Decision trees had the worst accuracy, K nearest neighbours had the lowest precision. When looking at the feature selection set, the random forest had the best accuracy, recall, and f1, while the support vector machine had the highest precision. Although it appears some models performed better than others, all models performed similarly, as the values for each metric were close to each other.

When looking at the impact of feature selection, only the decision tree benefited, but only when the max depth was not specifiied. In all other cases, feature selection either had no impact or performed slightly worse than the full dataset. The slight performance loss could be due to feature selection, and error could be explained by the excluded variables. The number of features to include for the feature selection was kept at 10, the default for the algorithm, so the models could have performed better with more or less arguments. Despite not improving the performances of the models, feature selection showed that the full dataset contained some redundant attributes, as the models performed just as well with all features of the dataset compared to half the features after feature selection.

## Conclusion

The data mining algorithms were all able to correctly diagnose diabetes, with each presenting over 70% accuracy. While the models have shown their effectiveness in this classification problem, there are other data mining algorithms that can be explored that can potentially give better results. The importance of feature selection algorithms was also explored. While the models did not significantly benefit from feature selection, they did demonstrate that some features of the dataset can be removed, and their removal will not have any significant impact on model performance. The models tested have also showed the potential applications for data mining in the health care industry.  Data mining classification tasks are not just limited to diabetes; these models can be valuable in diagnosing other medical conditions as well. Being able to correctly diagnose medical conditions without the need for testing results can help with preventative care and help avoid these conditions from reaching the worst-case scenario.
