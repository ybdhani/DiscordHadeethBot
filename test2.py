import requests
import random

# List of topics you want to use for randomization
topics = ["visiting the sick"]

# Randomly select a topic from the list
random_topic = random.choice(topics)

url = "https://www.hadithgpt.com/api/context"
headers = {
    "Content-Type": "application/json",
}

payload = {
    "question": random_topic,
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
if response.status_code == 200:
    data = response.json()
    similar_hadiths = data.get("similarHadith")

    if similar_hadiths:
        # Randomly select a Hadith from the list
        random_hadith = random.choice(similar_hadiths)

        # Print the selected random Hadith text
        hadith_text = random_hadith.get("text")
        print("Random Hadith on topic:", random_topic)
        print("Random Hadith:")
        print(hadith_text + '""')
    else:
        print("No similar Hadiths found in the response.")
else:
    print("Request failed with status code:", response.status_code)
