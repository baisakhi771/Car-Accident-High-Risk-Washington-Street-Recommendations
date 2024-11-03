# Streets to Avoid Recommender: High-Risk Street Prediction Model

### Currently only available for Washington, USA

### Baisakhi Sarkar
Master of Science in Data Science at University of Washington, Seattle

Contact Information: baisakhi771@gmail.com/bsarka@uw.edu

### Objective
The goal of this project is to **predict high-risk times on specific streets and recommend streets to avoid** based on accident likelihood. This model identifies times when certain streets are more prone to accidents, helping drivers, especially vulnerable groups like the elderly, to avoid these areas during high-risk periods. Traffic management agencies can also use this model to optimize resource allocation and proactively issue warnings.

### Approach

1. **Feature Selection**:
   - **Key Predictive Features**: `Street`, `Start_Time`, `Severity`, `Visibility(miles)`, `Precipitation(in)` and `Weather_Condition`.
   - **Data Transformation**:
     - **Time-Based Features**: Extract details like hour of the day, day of the week, and month from `Start_Time` to capture patterns in accident occurrences.
     - **Accident Severity**: This feature helps highlight higher-risk times with more severe accidents.
     - **Environmental Conditions**: `Visibility(miles)`, `Precipitation(in)` and `Weather_Condition` provide essential information, as weather has a major impact on accident risk.

2. **Modeling Approach**:
   - **Data Preprocessing**: Encode categorical variables (e.g., `Weather_Condition`, `Street`, `City`) and standardize continuous features like `Visibility`.
   - **Classification Models**:
     - **Random Forest**: A robust tree-based model effective for handling complex relationships. (Preferred)
     - **Gradient Boosting**: An ensemble approach that builds trees sequentially, which often excels with complex interactions.
   - **Rule-Based Models**: Simple rule-based models (e.g., "avoid icy streets at night") can complement machine learning predictions, adding interpretability to the model’s output.

3. **Training and Evaluation**:
   - **Evaluation Metrics**: Metrics like ROC-AUC, Precision, and Recall are essential as accident prediction involves imbalanced classes (high-risk vs. low-risk).
   - **Hyperparameter Tuning**: Use Grid Search or Randomized Search to fine-tune the model, focusing on accuracy and recall for high-risk predictions.

### Potential Models

1. **Random Forest**: Handles non-linear relationships and interacts well with complex data.
2. **Gradient Boosting**: Known for strong performance on complex data but requires tuning.
3. **Rule-Based Models**: These straightforward, interpretable models can act as baselines or complement more advanced models.

### Outcome

The model will recommend **streets to avoid at specific times** based on accident likelihood. The output will benefit:

- **Traffic Management**: Agencies can allocate resources, set up warnings, or divert traffic based on the model’s recommendations. By identifying high-risk times and locations, traffic control can be optimized for better safety and efficiency.

- **Driver Safety**: Helps drivers, especially those more vulnerable to accidents (e.g., elderly drivers), avoid high-risk streets during hazardous periods. Personalized recommendations based on time, weather, and road conditions offer an extra layer of security.

- **Seasonal and Time-Based Analysis**: Provides insights into seasonal accident trends (e.g., winter evenings or summer weekends with higher accident rates) to help traffic agencies plan **targeted safety campaigns** and allocate resources more effectively.

- **Infrastructure and Maintenance Planning**: Identifies roads with high accident likelihood over time, signaling the need for **road maintenance, better lighting, or additional traffic signals**. This data allows urban planners to prioritize infrastructure upgrades for high-risk locations.

- **Personalized Driver Recommendations**: Offers customized safety recommendations for drivers, especially those with specific needs (e.g., elderly drivers). This can suggest safer routes based on individual risk factors like visibility and road type.

- **Enhanced Emergency Response**: Enables **pre-positioning of emergency services** closer to high-risk areas during peak times, reducing response times in case of accidents.

- **Pedestrian and Cyclist Safety**: Helps identify zones with higher risks for non-motorized road users, allowing planners to design **safer pedestrian crossings or cyclist lanes** and consider time-based road restrictions in high-traffic areas.

These outputs make the **Streets to Avoid Recommender** a versatile tool for improving road safety, guiding urban planning, and supporting data-driven decision-making across various sectors.


### Future Work

- **Integration with Google Weather API**: Incorporate live weather conditions to enhance prediction accuracy.
  
  - **Automated Data Entry**: Automatically fill fields like weather and temperature with real-time conditions, reducing manual input and improving ease of use.
  - **Location-Based Risk Assessment**: Real-time weather updates will make predictions more relevant based on the user’s location.
  - **Real-Time Alerts**: Integration with navigation apps (e.g., Google Maps, Waze) can provide **real-time alerts** for high-risk areas, helping drivers adjust their routes dynamically based on live conditions.
  - **Weather-Dependent Risk Notifications**: By coupling predictions with live weather data, the model can send **dynamic risk alerts** when adverse weather conditions increase accident risks, enabling proactive adjustments to travel plans.

- **Additional Data Sources**: Integrate data from local traffic agencies or public road condition APIs for more accurate risk assessment.

This future work will make the **Streets to Avoid Recommender more user-friendly and dynamic**, providing location-based recommendations and enhancing road safety insights.
