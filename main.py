import discord
from discord.ext import commands
import requests, json, datetime, asyncio, aiohttp, random

intents = discord.Intents.default()
intents.message_content = True
intents.members = False

client = commands.Bot(command_prefix='bot ', intents=intents)

# List of topics for randomization (define it globally)
topics = [
    "marriage", "prayer", "fasting", "charity", "faith", "family", "friends", "knowledge",
    "education", "time management", "stress management", "career goals", "self-discipline",
    "goal setting", "study habits", "motivation", "mental health", "leadership",
    "communication skills", "teamwork", "peer pressure", "technology and social media",
    "health and wellness"
]

@client.command(name="hi")
async def SendMessage(ctx):
    await ctx.send('Hello!')

@client.command(name="salam")
async def SendMessage(ctx):
    await ctx.send("Assalamualaikum")

@client.command(name="random")
async def getHadith(ctx):
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

    if response.status_code == 200:
        data = response.json()
        similar_hadiths = data.get("similarHadith")

        if similar_hadiths:
            # Randomly select a Hadith from the list
            random_hadith = random.choice(similar_hadiths)

            # Extract the selected random Hadith details
            hadith_text = random_hadith.get("text")
            book = random_hadith.get("book")
            reference_book = random_hadith.get("reference_book")
            reference_hadith = random_hadith.get("reference_hadith")

            # Create the random Hadith message with details
            random_hadith_message = (
                    f"**Topic:** {random_topic}\n"
                    f"**Book:** {book}\n"
                    f"**Reference Book:** {reference_book}\n"
                    f"**Reference Hadith:** {reference_hadith}\n\n"
                    "**Random Hadith:**\n"
                    f"{hadith_text}"
            )

            # Send the random Hadith message to the Discord channel
            await ctx.send(random_hadith_message)
        else:
            await ctx.send("No similar Hadiths found in the response.")
    else:
        await ctx.send(f"Request failed with status code: {response.status_code}")

async def scheduleDailyMessage():
    now = datetime.datetime.now()
    print("Current time:", now)  # Add this line for debugging
    then = now.replace(hour=0, minute=27)
    wait_time = (then - now).total_seconds()
    print("Wait time (seconds):", wait_time)  # Add this line for debugging
    await asyncio.sleep(wait_time)

    channel = client.get_channel(701491616346669070)
    await channel.send("Good day!!")
    await getHadith(channel)
    print("Daily message sent.")  # Add this line for debugging


@client.event
async def on_ready():
    print("------------------------------")
    print(f"Logged in as: {client.user.name}")
    print("The bot is now ready for use! ")
    print("------------------------------")

    await scheduleDailyMessage()

if __name__ == '__main__':
    client.run("MTE0MDY3MjUyNjEyOTgzNjA3Mw.GgXyIw.BLCOWy-e7bdXzmlPptYKgiPCXW5ePhObzDV9g4")
