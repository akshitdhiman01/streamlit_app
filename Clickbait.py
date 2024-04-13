import streamlit as st

st.set_page_config(layout="wide")

# Pages logic 
if 'page' not in st.session_state: st.session_state.page = 0
def nextPage(): st.session_state.page += 1
def firstPage(): st.session_state.page = 0

# if 'login_attempted' not in st.session_state:
#         st.session_state.login_attempted = False


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

# Define your custom styles for buttons
st.markdown("""
<style>.element-container:has(#button-after) + div {
  text-align: center;
}
.element-container:has(#button-after) + div button {
 font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
 font-size: 16px;
 font-weight: 400;
 height: 100px;
 width: 120px;
 border: 0px solid;
 background-image: linear-gradient(45deg,blue,#00f0a0,blue);
 background-size: 500% 400%;
 color: white;
 border-radius: 50%;
 transition: 0.6s all;
}

button:hover {
 background-position: 75% 50%;
 transform: perspective(100px)
}

button:active {
 transform: scale(0.95);
 transition: 0.1s;
}
}</style>""", unsafe_allow_html=True)

# Define your custom styles for text fields 
st.markdown("""
<style>
/* Target the text input after an element with id 'textfield-after' */
.element-container:has(#textfield-after) + div input[type="text"] {
  border: none;
  outline: none;
  border-radius: 15px;
  padding: 1em;
  background-color: #ccc;
  box-shadow: inset 2px 5px 10px rgba(0,0,0,0.3);
  transition: 300ms ease-in-out;
  color:#222222;
}

input[type="text"]:focus {
  background-color: white;
  transform: scale(1.05);
  box-shadow: 13px 13px 100px #969696,
             -13px -13px 100px #ffffff;
}
</style>
""", unsafe_allow_html=True)

# Define your custom styles for password fields 
st.markdown("""
<style>
/* Target the text input after an element with id 'passwordfield-after' */
.element-container:has(#passwordfield-after) + div input[type="password"] {
  border: none;
  outline: none;
  border-radius: 15px;
  padding: 1em;
  background-color: #ccc;
  box-shadow: inset 2px 5px 10px rgba(0,0,0,0.3);
  transition: 300ms ease-in-out;
  color:#222222;
}

input[type="password"]:focus {
  background-color: white;
  transform: scale(1.05);
  box-shadow: 13px 13px 100px #969696,
             -13px -13px 100px #ffffff;
}
</style>
""", unsafe_allow_html=True)

# Define your custom styles for text area 
st.markdown("""
<style>
/* Target the text input after an element with id 'passwordfield-after' */
.element-container:has(#textarea-after) + div textarea {
  border: none;
  outline: none;
  border-radius: 15px;
  padding: 1em;
  background-color: #ccc;
  box-shadow: inset 2px 5px 10px rgba(0,0,0,0.3);
  transition: 300ms ease-in-out;
  color:#222222;
}

textarea:focus {
  background-color: white;
  transform: scale(1.05);
  box-shadow: 13px 13px 100px #969696,
             -13px -13px 100px #ffffff;
}
</style>
""", unsafe_allow_html=True)




# st.image("https://raw.githubusercontent.com/akshitdhiman01/streamlit_app/main/Header1.png")
# st.button("Light Mode") Implement css for light mode!!!!

## Page 0
if st.session_state.page == 0:
    st.image("https://raw.githubusercontent.com/akshitdhiman01/streamlit_app/main/Header2.png")

    st.markdown("""
    <style>
        h1 {
            font-size: 40px; 
            text-transform: uppercase;
            text-align: center;
            margin-top:2px
        }
        h3 {
            font-size: 20px;
        }
    </style>
        
""", unsafe_allow_html=True)
    
    _, headings, _ = st.columns([0.5,1,0.5])
    
    
    headings.title("Scientific Clickbait")
    headings.subheader("Crafting Captivating Titles for Academic Papers:")
    headings.subheader("Enhancing Engagement and Impact")
    # Check if the user is logged in
    if 'is_logged_in' not in st.session_state:
        st.session_state.is_logged_in = False
        st.session_state.username = None
        st.session_state.enter_pressed = False
        st.session_state.user_input = ""
        st.session_state.keywords = []
        st.session_state.selected_title = None

    _, col, _ = st.columns([0.5,0.5,0.5])
    
    # Default credentials
    default_username = "User1"
    default_password = "password"

    # Login/Signup section
    col.subheader("Login")
   
   #Applying custom css to username field 
    col.markdown('<div id="textfield-after"></div>', unsafe_allow_html=True)
    username_input = col.text_input("Username")

    #Applying custom css to password field
    col.markdown('<div id="passwordfield-after"></div>', unsafe_allow_html=True)
    password_input = col.text_input("Password", type='password')
    col.markdown('<span id="button-after"></span>', unsafe_allow_html=True)

    # Use session_state to track the login attempt
    if col.button("Login"):
        message_placeholder = col.empty()

        if username_input == default_username and password_input == default_password:
            on_click = nextPage()
            st.session_state.username = username_input
            message_placeholder.success(f"Logged in as {username_input}")
            st.session_state.is_logged_in = True
            st.rerun()
        else:
            message_placeholder.error("Invalid credentials. Please try again.")
    # Define columns for the images
    _, facebook, gmail, linkedin, _ = st.columns([1,0.3,0.3,0.3,1])
    
    col.markdown('<p style="text-align:center;">OR</p>', unsafe_allow_html=True)
    col.markdown('<p style="text-align:center;">Sign Up using....</p>', unsafe_allow_html=True)
    facebook.markdown('<a href="https://www.facebook.com"><img src="https://raw.githubusercontent.com/akshitdhiman01/streamlit_app/main/facebook.png" width="60"></a>', unsafe_allow_html=True)
    gmail.markdown('<a href="https://www.google.com"><img src="https://raw.githubusercontent.com/akshitdhiman01/streamlit_app/main/gmail.png" width="60"></a>', unsafe_allow_html=True)
    linkedin.markdown('<a href="https://www.linkedin.com"><img src="https://raw.githubusercontent.com/akshitdhiman01/streamlit_app/main/linkedin.png" width="50"></a>', unsafe_allow_html=True)




## Page 1
elif st.session_state.page == 1:
    st.image("https://raw.githubusercontent.com/akshitdhiman01/streamlit_app/main/Header2.png")
    
    st.markdown("""
    <style>
        h1 {
            font-size: 40px; 
            text-transform: uppercase;
            text-align: center;
            margin-top:2px
        }
        h3 {
            font-size: 20px;
        }
    </style>
        
""", unsafe_allow_html=True)
    _, headers, _ = st.columns([0.5,1,0.5])

    headers.title("Scientific Clickbait")
    headers.subheader("Crafting Captivating Titles for Academic Papers:")
    headers.subheader("Enhancing Engagement and Impact")
    _, col, _ = st.columns([0.5,1,0.5])

    # Applying custom css to text area
    col.markdown('<div id="textarea-after"></div>', unsafe_allow_html=True)
    input_text = col.text_area("Type in the abstract of the paper or paste here.")

    # Toggle switch for additional input
    use_keywords = col.checkbox("Use Keywords?")

    # Additional input field for keywords(visible when the checkbox is checked)
    if use_keywords:
        #Applying custom css to the text field
        col.markdown('<div id="textfield-after"></div>', unsafe_allow_html=True)
        user_input = col.text_input("Enter comma-separated keywords and press Enter")
        if st.session_state.user_input != user_input:
            st.session_state.user_input = user_input
            st.session_state.keywords = user_input.split(",")
        if user_input.strip() == "" and st.session_state.enter_pressed:
            st.session_state.keywords = []
            st.session_state.user_input = ""

        #!!!!!!!!!!!!Remember to remove this!!!!!!!!!!!
        reads = 200
    else:
        reads = 100

    # Display keywords
    if st.session_state.keywords:
        col.markdown(f'<p style="font-size: 20px;background-color: #f3efda;color: #222222;font-family: Helvetica;">"Keywords: {st.session_state.keywords}"</p>',unsafe_allow_html=True)
    # selected_title=''
    col.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
    # Generate title button
    if col.button('Generate Title'):
        # Placeholder for generated titles - this is where you integrate the title generating logic 
        generated_title_1 = "Generated Title 1"  # Replace with actual generated title 
        generated_title_2 = "Generated Title 2 "  # Replace with actual generated title
        generated_titles = [generated_title_1,generated_title_2]
        # Displaying generated titles as radio buttons for the user to select one
        selected_title = col.radio(
            "Select a Title:",
            (title for title in generated_titles),
            index=0
        )
        if st.session_state.selected_title != selected_title:
            st.session_state.selected_title = selected_title
            # st.rerun()


        # Display expected read counts and paper content based on the selected title
        if selected_title:
            # Store the selected title in the session state
            # if st.session_state.selected_title != selected_title:
            # st.session_state.selected_title = selected_title
            expected_read_counts = f'<p style="font-size: 20px;background-color: #f3efda;color: #222222;font-family: Helvetica;">The expected read counts for the title \'{st.session_state.selected_title}\' are: {reads}</p>'  
            col.markdown(expected_read_counts, unsafe_allow_html=True)
        
            # Write your headers
            gen_title = f'<p style="font-size: 30px;color: #222222;font-family: Helvetica;">{st.session_state.selected_title}</p>'
            separator = '<hr style="width:100%; border: 1px solid black;">'
            abstract_heading ='<p style="font-size: 20px;color: #222222;font-family: Helvetica;">ABSTRACT</p>'
            abstract =f'<p style="font-size: 20px;color: #3b3b3b;font-family: Helvetica;">{input_text}</p>'
        
            paper_content = "".join([gen_title, separator, abstract_heading, abstract])
        
            # Add style for white background and border
            styled_paper_content = f'''
                                    <div style="
                                        background-color: #f3efda;
                                        border: 1px solid #888;
                                        border-radius: 10px;
                                        padding: 20px;
                                        box-shadow: 15px 15px 25px rgba(0, 0, 0, 0.1);
                                        ">
                                    {paper_content}
                                    </div>
                                    '''
        
            col.markdown(styled_paper_content, unsafe_allow_html=True)
        
        