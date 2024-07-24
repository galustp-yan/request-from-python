import requests
import random
import time

url = "https://tonationdo.netlify.app"

randArr = ["/signIN", "/signUP", "/home", "/"]

i = 0
while True:
    random_element = random.choice(randArr)
    
    try:
        response = requests.get(url + random_element)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        # Access the response content (text or JSON depending on the server)
        content = response.text

        print(f"GET request to {url} was successful!")
        print(f"Response content:\n{content[:100]}...")  # Print first 100 characters

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    i+=1
    time.sleep(10)
