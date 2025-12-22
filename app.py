import streamlit as st

# Pre-verified NCC students (Matric : Phone)
ncc_students = {
    "HND/NCC/001": "08012345678",
    "HND/NCC/002": "08087654321",
    "HND/NCC/003": "08123456789"
}

# Use st.cache_resource to create a shared state for all users
@st.cache_resource
def get_voting_state():
    return {
        "ncc_voted": set(),
        "ncc_votes": {
            "Candidate A": 0,
            "Candidate B": 0
        }
    }

voting_state = get_voting_state()


# Initialize session state variables
if 'page' not in st.session_state:
    st.session_state.page = "login"

st.title("NCC HND 1 ONLINE VOTING SYSTEM")

def login_page():
    st.header("Login")
    matric = st.text_input("Enter your Matric Number")
    phone = st.text_input("Enter your registered mobile number", type="password")

    if st.button("Login"):
        if matric in ncc_students and phone == ncc_students[matric]:
            if matric in voting_state["ncc_voted"]:
                st.warning("You have already voted.")
            else:
                st.session_state.page = "voting"
                st.session_state.matric = matric
                st.rerun()
        else:
            st.error("Invalid Matric Number or mobile number.")

def voting_page():
    st.header("Candidates")
    st.write(f"Welcome, {st.session_state.matric}!")

    candidate = st.radio("Choose a candidate:", ("Candidate A", "Candidate B"))

    if st.button("Vote"):
        voting_state["ncc_votes"][candidate] += 1
        voting_state["ncc_voted"].add(st.session_state.matric)
        st.session_state.page = "results"
        st.rerun()

def results_page():
    st.header("NCC FINAL RESULTS")
    for c, v in voting_state["ncc_votes"].items():
        st.write(f"{c}: {v}")

    if st.button("Logout"):
        st.session_state.page = "login"
        st.session_state.matric = ""
        st.rerun()


if st.session_state.page == "login":
    login_page()
elif st.session_state.page == "voting":
    voting_page()
elif st.session_state.page == "results":
    results_page()
