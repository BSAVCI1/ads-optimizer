import streamlit as st

# Simple in‐memory store (replace with database later)
if "conversions" not in st.session_state:
    st.session_state.conversions = []

def main():
    st.title("Ads Optimizer")

    st.header("Log Your Conversions")
    date = st.date_input("Conversion date")
    count = st.number_input("Number of conversions", min_value=0, step=1)

    if st.button("Add conversion"):
        st.session_state.conversions.append({"date": date, "count": count})
        st.success(f"Logged {count} conversions on {date}")

    st.subheader("Your logged conversions")
    st.write(st.session_state.conversions)

if __name__ == "__main__":
    main()
