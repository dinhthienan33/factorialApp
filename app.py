import streamlit as st
from factorial import fact
def main():
    st.title('Factorial App')
    number=st.number_input('Enter a number',min_value=1,max_value=1000)
    if st.button('Calculate'):
        result=fact(number)
        st.write(result)
        #st.balloons()
if __name__ == '__main__':
    main()