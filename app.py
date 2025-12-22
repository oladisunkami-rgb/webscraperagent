import streamlit as st

# Initialize session state
if 'ncc_students' not in st.session_state:
    st.session_state.ncc_students = {
        "HND/NCC/001": "08012345678",
        "HND/NCC/002": "08087654321",
        "HND/NCC/003": "08123456789"
    }
if 'ncc_voted' not in st.session_state:
    st.session_state.ncc_voted = set()
if 'ncc_votes' not in st.session_state:
    st.session_state.ncc_votes = {
        "Candidate A": 0,
        "Candidate B": 0
    }
if 'logged_in_user' not in st.session_state:
    st.session_state.logged_in_user = None

st.title("NCC HND 1 ONLINE VOTING SYSTEM")

# Login Form
if not st.session_state.logged_in_user:
    st.header("Login")
    matric = st.text_input("Enter your Matric Number:")
    phone = st.text_input("Enter your registered mobile number:", type="password")

    if st.button("Login"):
        if matric in st.session_state.ncc_students and st.session_state.ncc_students[matric] == phone:
            if matric in st.session_state.ncc_voted:
                st.error("❌ You have already voted.")
            else:
                st.session_state.logged_in_user = matric
                st.success("✅ Login successful!")
                # Rerun to show the voting page
                st.rerun()
        else:
            st.error("❌ Invalid Matric Number or Mobile Number.")

# Voting Page
if st.session_state.logged_in_user and st.session_state.logged_in_user not in st.session_state.ncc_voted:
    st.header("Candidates")

    candidate_choice = st.radio("Choose a candidate:", list(st.session_state.ncc_votes.keys()))

    if st.button("Vote"):
        st.session_state.ncc_votes[candidate_choice] += 1
        st.session_state.ncc_voted.add(st.session_state.logged_in_user)
        st.success("✅ Vote successfully recorded!")
        st.session_state.logged_in_user = None # Log out after voting
        st.rerun()


# Results
st.header("Live Results")
for candidate, votes in st.session_state.ncc_votes.items():
    st.write(f"{candidate}: {votes}")
