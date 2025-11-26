### **Chapter 1: Introduction**

**1. Define Data Mining. What are the key characteristics of the extracted patterns?**
*   **Data Mining** is the process of automatically discovering interesting, non-trivial, implicit, previously unknown, and potentially useful patterns or knowledge from large amounts of data.
*   **Key characteristics:** The extracted patterns should be:
    *   **Valid:** Hold true on new data.
    *   **Novel:** Previously unknown.
    *   **Useful:** Actionable and potentially profitable.
    *   **Understandable:** Interpretable by humans.

**2. What is the KDD process? How does it differ from Data Mining?**
*   **KDD (Knowledge Discovery in Databases)** is the overall process of discovering useful knowledge from data. It is a multi-step, iterative process that includes data cleaning, integration, selection, transformation, mining, pattern evaluation, and knowledge presentation.
*   **Difference:** Data Mining is a single, core step within the KDD process, specifically focused on applying algorithms to extract patterns from data.

**3. List the 7 steps of the KDD process in the correct order.**
1.  Data Cleaning
2.  Data Integration
3.  Data Selection
4.  Data Transformation
5.  Data Mining
6.  Pattern Evaluation
7.  Knowledge Presentation

**4. Define the following tasks:**
*   **Classification:** Predicts a categorical (discrete, unordered) class label for a given data instance.
*   **Regression:** Predicts a continuous-valued (ordered) output for a given data instance.
*   **Cluster Analysis:** Groups a set of data objects into clusters (groups) such that objects within a cluster are similar to each other and dissimilar to objects in other clusters. It is an unsupervised learning task.

### **Chapter 2: Data Types & Statistics**

**1. What is the difference between Interval and Ratio attributes? Give examples.**
*   **Interval:** Measurements where the difference between values is meaningful, but there is no true zero point. (e.g., Temperature in Celsius or Fahrenheit, Calendar years).
*   **Ratio:** Measurements where the difference is meaningful *and* there is a true zero point, allowing for statements about ratios. (e.g., Height, Weight, Temperature in Kelvin, Annual income).

**2. What is the "Curse of Dimensionality"?**
It refers to phenomena that arise when analyzing and organizing data in high-dimensional spaces (with many attributes) that do not occur in low-dimensional settings. As dimensions increase, data becomes increasingly sparse, making distance measures less meaningful and algorithms computationally expensive and less effective.

**3. Outlier Detection with Boxplot: Write the formulas for the upper and lower boundaries using IQR.**
*   IQR = Q3 - Q1
*   **Lower Bound** = Q1 - 1.5 * IQR
*   **Upper Bound** = Q3 + 1.5 * IQR
Data points outside these boundaries are considered potential outliers.

**4. Jaccard Coefficient: Write the formula. When is it used (Symmetric or Asymmetric binary)?**
*   **Formula:** \( J = \frac{M_{11}}{M_{01} + M_{10} + M_{11}} \)
    Where \(M_{11}\) = number of attributes where both objects are 1, \(M_{01}\) = number where the first is 0 and second is 1, \(M_{10}\) = number where the first is 1 and second is 0.
*   **Use:** It is used for **Asymmetric binary** attributes, where the presence of an attribute (1) is more important than its absence (0). (e.g., disease diagnosis).

**5. Minkowski Distances: Write the formulas or definitions for:**
*   **Manhattan Distance (h=1):** \( \text{distance} = \sum_{i=1}^{n} |x_i - y_i| \)
*   **Euclidean Distance (h=2):** \( \text{distance} = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2} \)
*   **Supremum Distance (h=∞):** \( \text{distance} = \max_{i} |x_i - y_i| \) (The maximum of the differences along any single dimension).

**6. Cosine Similarity: Write the formula. What type of data is it mostly used for?**
*   **Formula:** \( \text{cos}(x, y) = \frac{x \cdot y}{||x|| \ ||y||} = \frac{\sum_{i=1}^{n} x_i y_i}{\sqrt{\sum_{i=1}^{n} x_i^2} \sqrt{\sum_{i=1}^{n} y_i^2}} \)
*   **Use:** It is mostly used for **high-dimensional sparse data**, such as **text data** represented as word vectors.

### **Chapter 3: Data Preprocessing**

**1. List the four major tasks of Data Preprocessing.**
1.  Data Cleaning
2.  Data Integration
3.  Data Transformation
4.  Data Reduction

**2. Min-Max Normalization: Write the formula to scale data to [new_min, new_max].**
\( v' = \frac{v - \min_A}{\max_A - \min_A} \times (\text{new\_max} - \text{new\_min}) + \text{new\_min} \)

**3. Z-score Normalization: Write the formula. When is it preferred over Min-Max?**
*   **Formula:** \( v' = \frac{v - \mu_A}{\sigma_A} \) where \( \mu_A \) is the mean and \( \sigma_A \) is the standard deviation of attribute A.
*   **Preference:** It is preferred when the actual minimum and maximum values are unknown or when the data contains **outliers**, as it is less sensitive to them.

**4. Discretization: What is the main difference between Entropy-Based and ChiMerge methods?**
*   **Entropy-Based (Top-Down):** A supervised method that uses class information to decide split points, aiming to maximize the purity (minimize entropy) of the resulting intervals.
*   **ChiMerge (Bottom-Up):** A supervised method that starts with each distinct value in its own interval and then merges adjacent intervals based on a chi-square statistical test, stopping when no more similar intervals can be merged.

### **Chapter 4: Association Rule Mining**

**1. Define Support and Confidence formulas.**
For a rule \( X \rightarrow Y \):
*   **Support:** \( \text{supp}(X \rightarrow Y) = P(X \cap Y) = \frac{\text{count}(X \cap Y)}{N} \)
*   **Confidence:** \( \text{conf}(X \rightarrow Y) = P(Y|X) = \frac{\text{count}(X \cap Y)}{\text{count}(X)} \)

**2. Explain the Apriori Principle (Anti-monotone property).**
The Apriori Principle states that "All non-empty subsets of a frequent itemset must also be frequent." Conversely, if an itemset is infrequent, all its supersets will also be infrequent. This **anti-monotone** property (if a set fails a test, all its supersets will also fail it) is used to prune the search space efficiently.

**3. Lift: Write the formula. What do values >1, <1, and =1 mean?**
*   **Formula:** \( \text{Lift}(X \rightarrow Y) = \frac{\text{conf}(X \rightarrow Y)}{\text{supp}(Y)} = \frac{\text{supp}(X \cap Y)}{\text{supp}(X) \times \text{supp}(Y)} \)
*   **Interpretation:**
    *   **Lift > 1:** X and Y are positively correlated. The rule is useful.
    *   **Lift = 1:** X and Y are independent. The rule is not useful.
    *   **Lift < 1:** X and Y are negatively correlated.

**4. What is the difference between Closed and Maximal Itemsets?**
*   **Closed Itemset:** An itemset X is closed if there exists no proper superset of X that has the same support count as X. It is a lossless representation.
*   **Maximal Itemset:** An itemset X is maximal if it is frequent, and no proper superset of X is frequent. It is a lossy representation but very compact.

### **Chapter 4 (Part 2): Data Warehouse**

**1. Compare OLTP and OLAP. (Users, Function, Data type).**
| Feature        | OLTP (Online Transaction Processing)                               | OLAP (Online Analytical Processing)                                |
|----------------|--------------------------------------------------------------------|--------------------------------------------------------------------|
| **Users**      | Clerks, IT professionals                                           | Managers, executives, data analysts                                |
| **Function**   | Day-to-day operations and transactions                             | Long-term decision support, data analysis, complex queries         |
| **Data Type**  | Current, detailed, relational data                                 | Historical, summarized, consolidated, multidimensional data       |

**2. Star Schema vs. Snowflake Schema: Which one is normalized? Which one is faster for queries?**
*   **Normalized:** The **Snowflake Schema** is more normalized because its dimension tables are decomposed into multiple related tables.
*   **Faster for Queries:** The **Star Schema** is generally faster for queries because it has fewer joins due to denormalized dimensions.

**3. List basic OLAP operations (e.g., Slice, Dice...). Describe them briefly.**
*   **Slice:** Selecting data for a single, fixed value of one dimension (e.g., "Sales for the year **2023**").
*   **Dice:** Selecting a subcube by defining a range of values on multiple dimensions (e.g., "Sales for **Q1 and Q2** in **Europe and Asia**").
*   **Roll-up:** Summarizing data to a higher level of abstraction (e.g., from "city" level to "country" level).
*   **Drill-down:** The opposite of roll-up, showing more detailed data (e.g., from "country" level to "city" level).
*   **Pivot (Rotate):** Reorienting the cube to see it from a different perspective (e.g., swapping rows and columns).

### **Chapter 5: Classification**

**1. Decision Trees: Compare the splitting criteria for ID3, C4.5, and CART.**
*   **ID3:** Uses **Information Gain**. Tends to favor attributes with many values.
*   **C4.5:** Uses **Gain Ratio**, which is a normalized version of Information Gain that corrects the bias towards multi-valued attributes.
*   **CART:** Uses **Gini Index** for classification. It measures the impurity of a node.

**2. What is the "Naive" assumption in Naive Bayes?**
The "Naive" assumption is that the values of the attributes (features) are **conditionally independent** given the class label. This simplifies the computation of probabilities significantly.

**3. Zero-Probability Problem: How do we fix it in Bayesian classification?**
We fix it by using **Laplace Estimation** (or Laplace Smoothing), which adds a small constant (usually 1) to every count. This ensures that no conditional probability is ever zero.

**4. Evaluation Metrics: Write the formulas for:**
*   **Precision:** \( \text{Precision} = \frac{TP}{TP + FP} \) (How many of the predicted positives are actual positives?)
*   **Recall:** \( \text{Recall} = \frac{TP}{TP + FN} \) (How many of the actual positives did we correctly predict?)
*   **F-measure:** \( F\text{-}measure = \frac{2 \times \text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} \) (The harmonic mean of Precision and Recall)

**5. Ensemble Methods: What is the main difference between Bagging and Boosting?**
*   **Bagging (Bootstrap Aggregating):** Builds multiple models in **parallel** from bootstrapped samples of the training data and combines them (e.g., by voting). It reduces variance. (e.g., Random Forest).
*   **Boosting:** Builds multiple models in **sequence**, where each new model tries to correct the errors of the previous ones. It gives more weight to misclassified instances. It reduces bias. (e.g., AdaBoost, XGBoost).

### **Chapter 6: Cluster Analysis**

**1. K-Means vs. K-Medoids: How do they differ in choosing the cluster center? Which is more robust to outliers?**
*   **K-Means:** The cluster center is the **mean (centroid)** of all points in the cluster.
*   **K-Medoids:** The cluster center is the most centrally located **actual data point (medoid)** in the cluster.
*   **Robustness:** **K-Medoids (PAM)** is more robust to outliers and noise because using a medoid is less influenced by extreme values than using a mean.

**2. DBSCAN: What are the two main parameters? What shapes can it detect?**
*   **Parameters:** `eps` (epsilon) - the radius of the neighborhood, and `minPts` - the minimum number of points required to form a dense region.
*   **Shapes:** It can detect clusters of **arbitrary shapes**, unlike K-Means which typically finds spherical clusters.

**3. Silhouette Coefficient: What is the range of values? What does a value close to 1 mean?**
*   **Range:** -1 to 1.
*   **Value close to 1:** It means the object is well-matched to its own cluster and poorly-matched to neighboring clusters, indicating good clustering.

### **Chapter 7: Outlier Analysis**

**1. List and define the three types of outliers.**
*   **Global Outliers (Point Anomalies):** A data point that significantly deviates from the entire dataset.
*   **Contextual (Conditional) Outliers:** A data point that is an outlier in a specific context (e.g., a temperature of 35°C is normal in summer but an outlier in winter).
*   **Collective Outliers:** A collection of data points that, as a group, deviate significantly from the entire dataset, even if individual points are not outliers.

**2. Compare Distance-based vs. Density-based (LOF) approaches. Which one handles varying densities better?**
*   **Distance-based:** An object is an outlier if it is far from most of its neighbors. It uses a global threshold. (e.g., k-NN based methods).
*   **Density-based (LOF - Local Outlier Factor):** An object is an outlier if its local density is significantly lower than the density of its neighbors. It uses a local threshold.
*   **Handling Varying Densities:** **Density-based (LOF)** handles varying densities much better because it compares the local density of a point to the local densities of its neighbors, rather than using a single global distance measure.

### **Chapter 8: Regression Analysis**

**1. Linear Regression: Write the Normal Equation formula (Matrix form) for estimating coefficients.**
\( \hat{w} = (X^T X)^{-1} X^T y \)
Where:
*   \(\hat{w}\) is the vector of coefficients (including the intercept).
*   \(X\) is the matrix of input features (with a column of 1s for the intercept).
*   \(y\) is the vector of target values.

**2. Logistic Regression: What function is used to map output to [0,1]? What is it used for (prediction or classification)?**
*   **Function:** The **Sigmoid (or Logistic) Function**: \( P(y=1|x) = \frac{1}{1 + e^{-(w^Tx + b)}} \)
*   **Use:** It is used for **classification** (specifically, binary classification), not prediction of a continuous value.

**3. What does the \(R^{2}\) coefficient measure?**
The \(R^{2}\) (R-squared) coefficient, or the **coefficient of determination**, measures the proportion of the variance in the dependent variable that is predictable from the independent variable(s). It indicates how well the regression model fits the data.

### **Chapter 10: Advanced Techniques**

**1. Match the architecture to the data type: CNN, RNN, Transformer → (Text, Images, Sequential Data).**
*   **CNN (Convolutional Neural Network):** **Images**
*   **RNN (Recurrent Neural Network):** **Sequential Data** (e.g., Time Series, Text)
*   **Transformer:** **Text** (and other sequential data, but revolutionized NLP)

**2. BERT vs. GPT: Which one is an Encoder (Understanding)? Which one is a Decoder (Generation)?**
*   **BERT (Bidirectional Encoder Representations from Transformers):** It is an **Encoder**. It is designed for deep **understanding** of language (e.g., question answering, sentiment analysis).
*   **GPT (Generative Pre-trained Transformer):** It is a **Decoder**. It is designed for **generating** text (e.g., writing essays, translation, conversation).

### **Chapter 11: Visualization**

**1. High-Dimensional Data: Name two methods for visualizing multivariate data.**
1.  **Parallel Coordinates**
2.  **Scatter Plot Matrix (SPLOM)**

**2. Graph Visualization: What is the main disadvantage of Node-Link diagrams for dense graphs? What is the alternative?**
*   **Main Disadvantage:** They can become a "hairball" or visually cluttered and unread