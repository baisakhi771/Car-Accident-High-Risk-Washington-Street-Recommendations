import streamlit as st
import pandas as pd
import joblib
import gdown

# Set wide mode
st.set_page_config(layout="wide")

# Cache the model loading function so the model is loaded only once
@st.cache_resource
def load_model():
    # Google Drive file ID
    file_id="1jdP2oiToh24oa58tIKftH1CiQUmL08sV"# tuned balanced random forest classifier model
    #file_id="17SYk-DlgJLtla-ZTbKNcfa7OCMW5d2dr" #balanced random forest classifier model
    #file_id = "1Rd0IE4ODS10hitJi06SVgefRKqY2l3TN" # base random forest classifier model
    url = f"https://drive.google.com/uc?id={file_id}"

    # Download the model file
    output = "high_risk_street_model.joblib"
    gdown.download(url, output, quiet=False)

    # Load and return the model
    return joblib.load(output)

# Cache the data loading function to load the data only once
@st.cache_data
def load_data():
    data = pd.read_csv("high_risk_data.csv")
    data['Weather_Condition'] = data['Weather_Condition'].fillna("Unknown").astype(str)
    return data

# Cache the prediction function to store results for unique inputs
@st.cache_data
def predict_high_risk(city, hour, visibility, weather_condition, precipitation):
    # Prepare user input data with a placeholder street
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
    
    return result_df

# Load the model and data once
# Display custom loading message
with st.spinner("Loading model and data, please wait..."):
    model = load_model()
    data = load_data()

# Streamlit app title
st.title("High-Risk Street Recommendations by City")

# User Inputs
city = st.selectbox("Select City", sorted(data['City'].unique()))
hour = st.slider("Select Hour of the Day", 0, 23, 12)
visibility = st.number_input("Visibility (miles)", min_value=0.0, max_value=10.0, value=5.0)
weather_condition = st.selectbox("Weather Condition", sorted(data['Weather_Condition'].unique()))
precipitation = st.number_input("Precipitation (inches)", min_value=0.0, max_value=5.0, value=0.0)

# "Submit" button
if st.button("Submit"):
    # Run the prediction
    # Display custom loading message
    with st.spinner("Loading Recommendations, please wait..."):
        result_df = predict_high_risk(city, hour, visibility, weather_condition, precipitation)

    # Display the results
    st.subheader(f"Streets to Avoid in {city}")
    if not result_df.empty:
        st.write(result_df[['City', 'Street', 'Hour', 'Weather_Condition', 'Visibility(mi)', 'Precipitation(in)', 'High_Risk_Probability']])
    else:
        st.write(f"No high-risk streets found in {city} for the selected conditions.")
