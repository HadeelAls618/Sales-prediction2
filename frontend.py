""
# frontend-related code 
# installing pyngrok
!pip install -q pyngrok
# installing streamlit
!pip install -q streamlit
# 1- write the script
%%writefile app.py

# 2-importing required libraries
import pickle
import streamlit as st

# 3-loading the trained model
pickle_in = open('Model_XGBR.pkl', 'rb')
Regrissor = pickle.load(pickle_in)

def main():
    # Set up the HTML and CSS for the title and description
  
    st.markdown(
    '<style>'
    '.main-title {'
    '    font-size: 36px;'
    '    color: white;' /* Text color */
    '    background-color: #4682B4;' /* Steel Blue background */
    '    text-align: center;'
    '    font-weight: bold;'
    '    padding: 20px;'
    '    border-radius: 10px;'
    '}'
    '.sub-title {'
    '    font-size: 20px;'
    '    color: #4682B4;' /* Steel Blue */
    '    text-align: center;'
    '}'
    '.sidebar .stSelectbox, .sidebar .stNumberInput {'
    '    background-color: #f0f8ff;' /* Alice Blue background */
    '    border: 2px solid #4682B4;' /* Steel Blue border */
    '    border-radius: 10px;'
    '    padding: 10px;'
    '    margin: 10px 0;'
    '}'
    '.predict-button {'
    '    background-color: #4682B4;' /* Steel Blue */
    '    color: white;'
    '    border: None;'
    '    border-radius: 10px;'
    '    font-size: 18px;'
    '    padding: 10px;'
    '    margin: 20px 0;'
    '    width: 100%;'
    '}'
    '.result-text {'
    '    font-size: 24px;'
    '    color: #4682B4;' /* Steel Blue */
    '    text-align: center;'
    '    margin-top: 20px;'
    '}'
    '</style>',
    unsafe_allow_html=True
)

    # Title and subtitle
    st.markdown("<div class='main-title'>Big Mart Sales Prediction</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Predict the sales of products in different stores.</div>", unsafe_allow_html=True)

# create boxes in which user can enter data required to make prediction
    ItemFatContent = st.selectbox('Item_Fat_Content',(" Low Fat","Regular"))
    OutletSize = st.selectbox('Outlet_Size',("Small","Medium","High"))
    ItemType= st.selectbox('Item_Type',("Dairy","Drinks","Fruits","Others"))
    ItemWeight = st.number_input("Item Weight")
    ItemMRP = st.number_input("Item MRP ")

    result=""
    if st.button("Predict", key='predict_button', use_container_width=True):
        result = prediction(ItemFatContent, OutletSize, ItemType, ItemWeight, ItemMRP)
    st.success('The sales for this item is {}'.format(result))
