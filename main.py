import asyncio
from pyppeteer import launch
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


# account_sid = os.getenv("TWILIO_ACCOUNT_ID")
# auth_token = os.getenv("TWILIO_AUTH_TOKEN")
# client = Client(account_sid, auth_token)
# message = client.messages.create(
#     body=f"{arr}",
#     from_=os.getenv("TWILIO_PHONE_NUMBER"),
#     to=os.getenv("RECIPIENT_PHONE_NUMBER")
# )


async def main():
    browserObj = await launch({"headless": False})
    url = await browserObj.newPage()

    await url.goto('http://127.0.0.1:5500/index.html')
    await url.waitFor(3000)

    arr = []

    courses = await url.querySelectorAll(".course-list--container--FuG0T")

    print(courses)
    #
    # for course in courses:
    #     element = await course.querySelector("h3")
    #     print(await element.jsonValue())

    coursesInfo = await url.querySelectorAll("div .ud-sr-only > span")
    courseTitles = await url.querySelectorAll("div .course-card--has-price-text--1c0ze > h3 > a")

    # for courseTitle in courseTitles:
    #     courseTitle = await courseTitle.getProperty("textContent")
    #
    #     print(await courseTitle.jsonValue())

    coursesObj = {}

    for courseInfo in coursesInfo:
        courseInfo = await courseInfo.getProperty("textContent")

        courseObj = {}

        # print(type(await courseInfo.jsonValue()))

        if "Original" in await courseInfo.jsonValue():
            courseObj.update(originalPrice=await courseInfo.jsonValue())
        elif "Current" in await courseInfo.jsonValue():
            courseObj.update(currentPrice=await courseInfo.jsonValue())

        arr.append(courseObj)

    print(arr)

    # html = await url.content()
    await browserObj.close()


print(asyncio.get_event_loop().run_until_complete(main()))
