import streamlit as st
import yaml

def save_to_yaml(data, filename='data.yaml'):
    with open(filename, 'w') as file:
        yaml.dump(data, file)

st.title('Data Request')

name = st.selectbox('Select the IP', ['NVM', 'SRAM'])
size = st.number_input('Enter the size in sqmm')
mge = st.number_input('Enter the complexity in MGE')
utilisation_factor = st.number_input('Enter the utilisation factor in per cent')

submitted = st.button('Submit')
if submitted:
    collected_data = {
    'ip': name,
    'data': {
        'size': size,
        'complexity': mge,
        'utilisation': utilisation_factor
    },
    'additional_info': {
        'comments': 'This is a comment'
    }
}
    save_to_yaml(collected_data)
    st.write('Data submitted and saved to data.yaml:')
    st.write(collected_data)
    