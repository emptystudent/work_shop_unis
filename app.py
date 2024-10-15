import streamlit as st
from jamaibase import JamAI, protocol as p

# Set your API Key and Project ID directly in the script
API_KEY = "YOUR API KEY HERE"
PROJECT_ID = "YOUR PROJECT ID HERE"
TABLE_ID = "user_input"

# Initialize JamAI client
jamai = JamAI(api_key=API_KEY, project_id=PROJECT_ID)

# Title of the app
st.title("User Input Action Table App")

# Create UI for user to provide inputs
input_1 = st.text_input("Enter the first input:")
input_2 = st.text_input("Enter the second input:")

# Process the inputs and interact with JamAI
if st.button("Submit"):
    # Add user inputs to the action table
    if input_1 and input_2:
        try:
            completion = jamai.add_table_rows(
                "action",
                p.RowAddRequest(
                    table_id=TABLE_ID,
                    data=[{"additonal_data": input_1, "comments": input_2}],
                    stream=False
                )
            )

            # Display the output generated in the "commentor" column
            if completion.rows:
                commentor_output = completion.rows[0].columns.get("commentor")
                if commentor_output:
                    st.success(f"Generated Commentor Output: {commentor_output.text}")
                else:
                    st.error("No output found in the 'commentor' column.")
            else:
                st.error("Failed to get a response. Please try again.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in both input fields.")

