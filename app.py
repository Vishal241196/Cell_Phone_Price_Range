import pickle
import streamlit as st

pickle_in = open("cell_classifier.pkl","rb")
classifier = pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict(battery_power, front_camera, Four_G, internal_memory,mobile_weight, no_cores_processor, primary_camera, pixel_height_resolution, pixel_width_resolution, ram, screen_height, screen_width):
    
    prediction = classifier.predict([[battery_power, front_camera, Four_G, internal_memory, mobile_weight, no_cores_processor, primary_camera, pixel_height_resolution, pixel_width_resolution, ram, screen_height, screen_width]])
#    print(prediction)
    return prediction

def main():
    st.title("Cell Phone Price Range Prediction")
    html_temp = '''
    <div style = "background-color:tomato;padding:10px">
    <h2 style = "color:white;text-align:center;">Streamlit Cell Phone ML App</h2>
    </div>
    '''

    st.markdown(html_temp, unsafe_allow_html=True)
    battery_power = st.text_input("Battery Power","Type Here")
    front_camera = st.text_input("Front Camera","Type Here")
    Four_G = st.text_input("4G","Type Here")
    internal_memory = st.text_input("Internal Memory","Type Here")
    mobile_weight = st.text_input("Mobile Weight","Type Here")
    no_cores_processor = st.text_input("Processor","Type Here")
    primary_camera = st.text_input("Primary Camera","Type Here")
    pixel_height_resolution = st.text_input("Pixel Height Resolution","Type Here")
    pixel_width_resolution = st.text_input("Pixel Width Resolution","Type Here")
    ram = st.text_input("Ram","Type Here")
    screen_height = st.text_input("Screen Height","Type Here")
    screen_width = st.text_input("Screen Width","Type Here")
    result=""
    if st.button("Predict"):
        result=predict(battery_power, front_camera, Four_G, internal_memory,mobile_weight, no_cores_processor, primary_camera, pixel_height_resolution, pixel_width_resolution, ram, screen_height, screen_width)
    st.success('The Output is {}'.format(result))

if __name__ =='__main__':
        main()