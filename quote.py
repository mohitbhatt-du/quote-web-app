import streamlit as st
import requests
import time

def quote():
    # category = 'happiness'
    api_url = 'https://api.api-ninjas.com/v1/quotes'

    response = requests.get(api_url, headers={'X-Api-Key': 'biqXTnOztIAda0hUa5UHiA==BeLdbQdOqtuxP9Bw'})

    if response.status_code == requests.codes.ok:
        data = response.json()  # Convert the JSON response to a Python list
        if data:  # Check if the list is not empty
            quote_dict = data[0]  # Access the first dictionary in the list
            return [quote_dict.get('quote'), quote_dict.get('author'),quote_dict.get('category')]
            

    else:
        return [response.status_code, response.text]
    

def refresh():
    return quote()
    
def main(): 
    st.title(":red[Quote of the day!] :wave:")
    st.divider()

    with st.container():
        quote_list = quote()

        with st.spinner('reloading...'):
            time.sleep(1)

            st.subheader(quote_list[0])
            st.write(f"**Author:** :red[***{quote_list[1]}***]")
            st.write(f"**category:** :red[***{quote_list[2]}***]")

            st.divider()
        st.button('**Refresh**', on_click=refresh)
    



if __name__ == "__main__":
    main()
   