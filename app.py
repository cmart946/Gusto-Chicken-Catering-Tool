import streamlit as st

from logic import cooked_to_raw
from logic import total_cases_needed



st.title("🛠️ Gusto Chicken Catering Tool 🛠️")
st.write("") # adds a blank line for spacing
st.subheader("Insert information to calculate chicken needed for catering orders")

#1️⃣ asking for required input

#day of the week selection 
day_of_week = st.selectbox (
    "select the day of the week",
    [
        "Monday",
        "tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
)


#number of chicken cases in the walk in
current_cases = st.number_input (
    "enter the number of cases in the walk in 📦",
    min_value=0,
    step = 1
)
#catering orders for the week input 
catering_orders = st.number_input (
    "Enter the number of catering orders this week (as of now) 📅",
    min_value=0,
    step = 1
)

#dynamic inputs, asking for the number of cooked chicken for the catering orders

cooked_pounds_lists = []

for i in range (catering_orders):
    pounds = st.number_input(
      f"Enter the number of cooked pounds of chicken needed for catering order #{i +1}🍗 (Round Up)",
      min_value=0,
      step = 1, 
      key=f"order_{i}"
    )
    cooked_pounds_lists.append(pounds)





#2️⃣ user submits, when ready to calculate




if st.button("Calculate Report 📊"):


    yield_percent = 0.75 #percent of chicken lost after cooking 
    pounds_per_case = 40 #pounds of raw chicken in one case

    total_cooked = sum(cooked_pounds_lists)
    st.subheader("results:")

    if day_of_week in ["Monday", "Wednesday", "Friday"]:
        st.write("New inventory arrives today.")
    else:
        st.write("No new inventory arrives on this day.")


    st.write("total cooked pounds needed for these catering orders:", total_cooked)
    st.write("total raw pounds needed for these catering orders: ", round(cooked_to_raw (total_cooked),2))
    st.write("") # adds a blank line for spacing
    
    for i, pounds in enumerate(cooked_pounds_lists):
        raw_pounds  = pounds / yield_percent
        st.write(f"Catering order #{i + 1}:  {round(raw_pounds, 2)} raw pounds of chicken🐓")

        cases_needed = raw_pounds / pounds_per_case
        if cases_needed < 1:
            st.write("cases needed: less than 1 full case")
            st.write("") # adds a blank line for spacing
        else:
            st.write("Cases needed: " + str(round(cases_needed, 2)))
            st.write("")


    total_cooked = sum(cooked_pounds_lists)
    #st.subheader("In total these catering orders will require ", round(total_cases_needed (total_cooked), 2), "cases of raw chicken.")
    cases_needed = round(total_cases_needed (total_cooked), 2)
    st.subheader(
        f"in total these catering orders will require {cases_needed} cases of raw chicken."
    )

    st.success(f"Order {round(cases_needed+1)} case(s) of chicken to fullfill this weeks catering orders. (rounded up for a safety buffer)")



st.write("") # adds a blank line for spacing
st.write("") # adds a blank line for spacing
st.write("") # adds a blank line for spacing










