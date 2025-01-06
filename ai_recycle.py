from openai import OpenAI
import requests

def get_user_country():
    # Fetch the user's IP address (this works for most scenarios)
    response = requests.get("https://api64.ipify.org?format=json")
    ip_address = response.json()["ip"]

    # Use the IP to get geolocation data
    geo_response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    geo_data = geo_response.json()

    # Return the country
    return geo_data.get("country", "Unknown")

def get_user_object():
    # Simulate grabbing the user's object
    print("Grabbing user object...")
    return "plastic bottle"  # Example object

def generate_chat_completion(client, user_object, user_location):
    # Create a chat completion
    print("Generating chat completion...")
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": f"What is the best way to recycle the {user_object} in the image in {user_location}?"},
                ],
            },
        ],
    )
    return completion.choices[0].message

# Main Execution Flow
if __name__ == "__main__":
    # Run tasks in sequence
    user_location = get_user_country()
    user_object = get_user_object()

    # Assuming 'client' is already initialized
    client = OpenAI(api_key="your-api-key") # Initialize your OpenAI client here
    chat_response = generate_chat_completion(client, user_object, user_location)

    # Print the chat response
    print(chat_response)
