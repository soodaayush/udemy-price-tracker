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
    titles = []

    coursesInfo = await url.querySelectorAll("div .ud-sr-only > span")
    courseTitles = await url.querySelectorAll("div .course-card--has-price-text--1c0ze > h3 > a")

    courseObj = {}

    for courseTitle in courseTitles:
        courseTitle = await courseTitle.getProperty("textContent")

        if "<strong>" not in await courseTitle.jsonValue() and ":" not in await courseTitle.jsonValue():
            titles.append(await courseTitle.jsonValue())

        print(await courseTitle.jsonValue())

    for courseInfo in coursesInfo:
        i = 0

        courseInfo = await courseInfo.getProperty("textContent")

        # print(await courseInfo.jsonValue())

        title = titles[i]

        courseObj.update(title=titles[i])

        if "Original" in await courseInfo.jsonValue():
            courseObj.update(originalPrice=await courseInfo.jsonValue())
        elif "Current" in await courseInfo.jsonValue():
            courseObj.update(currentPrice=await courseInfo.jsonValue())

        if "originalPrice" in courseObj and "currentPrice" in courseObj:
            arr.append(courseObj)
            courseObj = {}
            i = i + 1

    print(arr)

    # html = await url.content()
    await browserObj.close()


print(asyncio.get_event_loop().run_until_complete(main()))
