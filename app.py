import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load('high_risk_street_model_with_city.joblib')

# Load city and weather condition options
data = pd.read_csv("high_risk_data.csv")  
# Set wide mode
st.set_page_config(layout="wide")
# Streamlit app title
st.title("High-Risk Street Recommendations by City")
# Convert Weather_Condition to strings, filling NaNs if present
data['Weather_Condition'] = data['Weather_Condition'].fillna("Unknown").astype(str)



# User Inputs
city = st.selectbox("Select City", sorted(data['City'].unique()))
hour = st.slider("Select Hour of the Day", 0, 23, 12)
visibility = st.number_input("Visibility (miles)", min_value=0.0, max_value=10.0, value=5.0)
weather_condition = st.selectbox("Weather Condition", sorted(data['Weather_Condition'].unique()))
precipitation = st.number_input("Precipitation (inches)", min_value=0.0, max_value=5.0, value=0.0)

# "Submit" button
if st.button("Submit"):
    # Prepare user input data
    user_input = pd.DataFrame({
        'City': [city],
        'Street': [''],  # Placeholder, we'll iterate through all streets in the selected city
        'Hour': [hour],
        'Weather_Condition': [weather_condition],
        'Visibility(mi)': [visibility],
        'Precipitation(in)': [precipitation]
    })

    # Predict risk for each street in the selected city
    high_risk_streets = []
    streets = model.named_steps['preprocessor'].transformers_[0][1].categories_[1]  # Filter only streets from the encoder

    # Iterate through each street to get predictions
    for street in streets:
        user_input['Street'] = street
        user_input_encoded = model.named_steps['preprocessor'].transform(user_input)
        prediction = model.named_steps['classifier'].predict(user_input_encoded)[0]
        prediction_proba = model.named_steps['classifier'].predict_proba(user_input_encoded)[0][1]
        
        # Add street with high-risk prediction and probability to the list
        if prediction == 1:
            high_risk_streets.append({
                'City': city,
                'Street': street,
                'Hour': hour,
                'Weather_Condition': weather_condition,
                'Visibility(mi)': visibility,
                'Precipitation(in)': precipitation,
                'High_Risk_Prediction': prediction,
                'High_Risk_Probability': prediction_proba
            })

    # Convert the results to a DataFrame and filter for high-risk streets
    result_df = pd.DataFrame(high_risk_streets)
    result_df = result_df.sort_values(by='High_Risk_Probability', ascending=False)

    # Display the results
    st.subheader(f"Streets to Avoid in {city}")
    if not result_df.empty:
        st.write(result_df[['City', 'Street', 'Hour', 'Weather_Condition', 'Visibility(mi)', 'Precipitation(in)', 'High_Risk_Probability']])
    else:
        st.write(f"No high-risk streets found in {city} for the selected conditions.")

