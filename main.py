import streamlit as st

st.image("UniwolverhamptonImage.png")
st.title("Awareness App")
#st.subheader("Hi! I am your Subheader")
st.header("Welcome to this Awareness App")
#st.write("This app provides valuable information to help you stay healthy in your mindFor more detailed and professional health advice, visit the NHS website.")
st.write("This app will provide information for health providers available in Herefordshire and Worcestershire Communities and signpost you to how to access these facilities.")
st.header("Please provide answers to the question below")



Q1=st.selectbox("**Question 1:** Which Ethnic group closely defines your ethnicity?:", options= (" ", "Black/African", "White/British/Irish/Any other White","Asian" ), key="select1")
print(Q1)


st.subheader("Check the following symptoms")
st.write("""
1. A lack of interest in things
2. Feeling disconnected from your emotions
2. Difficulty concentrating
3. Wanting to avoid people hallucinations, such as hearing voices or seeing things others don't
   delusions (strong beliefs that others don't share).
4. Disorganised thinking and speech
5. Not wanting to look after yourself.""")

Q2=st.selectbox("**Question 2:** Do you know where to go or who to speak to if you experience any of this symptoms? :", options= (" ", "Yes", "No"), key="select2")
print(Q2)


if Q2 == "No":
        st.write("Inform your GP now or contact us here:")
        #st.write("""
        #Check the Herefordshire and Worcestershire Health and Care NHS Trust for more information:""")
        st.markdown("[Herefordshire and Worcestershire](https://www.talkingtherapies.hwhct.nhs.uk/home)")
if Q2 =="Yes":
        st.write("Just to confirm, inform your GP and here are some information we have for you")       
        st.markdown("[Herefordshire and Worcestershire](https://www.talkingtherapies.hwhct.nhs.uk/home)")
# Footer


st.header("Stay healthy and take care of yourself!")