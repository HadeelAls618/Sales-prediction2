#!/bin/bash

# Running the Streamlit app
!streamlit run app.py &>/dev/null&

# Authenticating with Ngrok and connecting
!ngrok authtoken 2jqcFzoNjjYuhUnH7sp3UFyFKlk_6qhJvSzzP87gFpsfQG2vT

public_url=$(ngrok connect '8501')

echo "App is running and accessible at: $public_url"
