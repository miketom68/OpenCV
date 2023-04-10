import streamlit as st 
import pyfirmata
import time
from pyfirmata import util,OUTPUT
port='COM3'
board=pyfirmata.Arduino(port)
board.digital[7].mode=OUTPUT
time.sleep(2.0)
def main():
    st.title('MY SWITCH APP')
    length=st.sidebar.slider('brightness',0,100)
    if st.button('click'):
        board.digital[7].write(1)
    
    
if __name__=='__main__':
    main()