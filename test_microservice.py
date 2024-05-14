import requests

# URL of the microservice
microservice_url = "http://127.0.0.1:5000/search"

# Sending a request to the microservice
response = requests.post(microservice_url)

# Checking if the request was successful
if response.status_code == 200:
    # Displaying that the request was successful
    print("Microservice request was successful.")
    
    # Displaying the retrieved data
    print("Here's the information we retrieved from a random Wikipedia page:\n")
    print(response.json()['result'])
else:
    print("Error:", response.status_code)
