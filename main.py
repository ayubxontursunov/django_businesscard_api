import requests
import os

name = "John"  # or "John.jpg"
upload_url = f'http://127.0.0.1:8000/card/{name}'

response = requests.get(upload_url)

# Check if the response is successful
if response.status_code == 200:
    # Define the directory where you want to save the file
    download_dir = "downloads"
    os.makedirs(download_dir, exist_ok=True)  # Create the directory if it doesn't exist

    # Save the file locally in the specified directory
    file_path = os.path.join(download_dir, name)
    with open(file_path, 'wb') as f:
        f.write(response.content)
    print(f"File {name} downloaded successfully to {file_path}.")
else:
    print("Failed to retrieve the file.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)


