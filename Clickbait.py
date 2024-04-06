import streamlit as st

st.set_page_config(layout="wide")

# Pages logic 
if 'page' not in st.session_state: st.session_state.page = 0
def nextPage(): st.session_state.page += 1
def firstPage(): st.session_state.page = 0

ph = st.empty()



def set_background():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://raw.githubusercontent.com/akshitdhiman01/app_design_flask/main/starry_night.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_background()
## Page 0
if st.session_state.page == 0:
    st.markdown("""
    <style>
        h1 {
            font-size: 40px;
            text-align: center;
            text-transform: uppercase;
        }
        h3 {
            font-size: 20px;
            text-align: center;
        }
        img {
            position: absolute;
            top: 0px;
            right: 0px;   
        }
    </style>
        
""", unsafe_allow_html=True)
        
    st.image('D:/Scientific clickbait/Scientific.png')
    st.title("Scientific Clickbait")
    st.subheader("Crafting Captivating Titles for Academic Papers:")
    st.subheader("Enhancing Engagement and Impact")
    # Check if the user is logged in
    if 'is_logged_in' not in st.session_state:
        st.session_state.is_logged_in = False
        st.session_state.username = None
        st.session_state.enter_pressed = False
        st.session_state.user_input = ""
        st.session_state.keywords = []
        # st.session_state.selected_title = None

    # Default credentials
    default_username = "User1"
    default_password = "password"

    # Login/Signup section
    st.subheader("Login/Signup")
    buff, col, buff2 = st.columns([1,2,1])

    

    username_input=col.text_input('Username:')
    password_input = col.text_input('Password', type='password')
    # username_input = st.text_input('Username:')
    # password_input = st.text_input('Password', type='password')

    if col.button("Login"):
        if username_input == default_username and password_input == default_password:
            # Successful login
            nextPage()
            st.session_state.is_logged_in = True
            st.session_state.username = username_input
            st.success(f"Logged in as {username_input}")
        else:
            st.error("Invalid credentials. Please try again.")

    # Display dashboard if user is logged in
    # if st.session_state.is_logged_in:

        # render_dashboard()

## Page 1
elif st.session_state.page == 1:
    st.markdown("""
    <style>
        h1 {
            font-size: 40px;
            text-align: center;
            text-transform: uppercase;
        }
        h3 {
            font-size: 20px;
            text-align: center;
        }
        img {
            position: absolute;
            top: 0px;
            right: 0px;   
        }
    </style>
        
""", unsafe_allow_html=True)

    st.image('D:/Scientific clickbait/Scientific.png')
    st.title("Scientific Clickbait")
    st.subheader("Crafting Captivating Titles for Academic Papers:")
    st.subheader("Enhancing Engagement and Impact")
    buff, col, buff2 = st.columns([1,2,1])

    # Check if the user has uploaded a file
    input_text = col.text_area("Type in the abstract of the paper or paste here.")

    # Toggle switch for additional input
    show_additional_input = col.checkbox("Use Keywords?")

    # Additional input field (visible when the checkbox is checked)
    if show_additional_input:
        user_input = col.text_input("Enter comma-separated keywords and press Enter")
        if st.session_state.user_input != user_input:
            st.session_state.user_input = user_input
            st.session_state.keywords = user_input.split(",")
        if user_input.strip() == "" and st.session_state.enter_pressed:
            st.session_state.keywords = []
            st.session_state.user_input = ""

    # Display keywords
    if st.session_state.keywords:
        col.write(f"Keywords: {st.session_state.keywords}")
    
    # Generate title button
    if col.button('Generate Title'):
        # Placeholder for generated titles - this is where you integrate the title generating logic 
        generated_title_1 = "Generated Title 1"  # Replace with actual generated title 
        generated_title_2 = "Generated Title 2"  # Replace with actual generated title

        # Displaying generated titles as radio buttons for user to select one
        selected_title = col.radio(
            "Select a Title:",
            (generated_title_1, generated_title_2),
            index=1
        )
        if 'selected_title' not in st.session_state:
            st.session_state.selected_title = None

        if selected_title:
            # Store the selected title in the session state
            st.session_state.selected_title = selected_title

            # Display expected read counts - this is where you integrate logic to estimate expected read counts based on selected title 
            reads = 100
            expected_read_counts = f"The expected read counts for the title \'{selected_title}\' are : {reads}"  
            col.write(expected_read_counts)
