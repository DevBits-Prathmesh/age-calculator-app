import streamlit as st
import datetime as dt
default=dt.date(2000,1,1)
min_v=dt.date(1900,1,1)
max_v=dt.date.today()
today=dt.date.today()
st.title('🤞HELLO!')
st.title('Welcome To Age Calculater😁')
gender=st.radio('Please Enter Your Gender✨:',["Male","Female","Keep Private"])
if gender=='Male':
    st.text('Gentleman 😎')
    r=st.date_input('Select Your Birth Of Date',value=default,min_value=min_v,max_value=max_v)
    age=dt.date.today().year-r.year
    if (today.month, today.day)<(r.month,r.day):
        r-=1
    st.success(f'YOUR  AGE  IS  {age}👀,still  YOUNG!!  ALWAYS  BE  BRAVE 💪🕊️')
elif gender=='Female':
    st.text('Hey Beautifull !💕')
    r=st.date_input('Select Your Birth Of Date',value=default,min_value=min_v,max_value=max_v)
    age=dt.date.today().year-r.year
    if (today.month, today.day)<(r.month,r.day):
        r-=1
    st.success(f'YOUR AGE IS {age} — EMBRACE EVERY MOMENT! YOU ARE STRONG, SMART, AND BEAUTIFUL 💖💫')
else:
    st.text('Hey Awesomly Brave !🫵')
    r=st.date_input('Select Your Birth Of Date',value=default,min_value=min_v,max_value=max_v)
    age=dt.date.today().year-r.year
    if (today.month, today.day)<(r.month,r.day):
        r-=1
    st.success(f'YOUR AGE IS {age} — YOU ARE UNIQUE, STRONG, AND WORTH CELEBRATING EVERY DAY 🌈✨')

st.markdown("""
    <hr style="margin-top:50px;">
    <div style='text-align: center; color: gray;'>
        © 2025 Prathmesh Sonawane | I JUST LOVE ❤️ TO BUILD STUFF
    </div>
""", unsafe_allow_html=True)
