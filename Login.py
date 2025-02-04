import streamlit as st

USER_CREDENTIALS = {"username": "admin", "password": "password123"}


def authenticate(username, password):
    if username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
        return True
    return False




def show_login_form():
    st.title("Login Page")
    
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    
    if st.button("Login"):
        if authenticate(username, password):
            st.success("Login successful!")
            
            st.write("Welcome to the main app!")
            
        else:
            st.error("Invalid username or password")


if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False


if not st.session_state['logged_in']:
    show_login_form()
else:
    
    st.write("You are logged in!")
