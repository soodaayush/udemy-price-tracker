import asyncio
from pyppeteer import launch
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


async def main():
    browserObj = await launch({"headless": False})
    url = await browserObj.newPage()

    await url.goto('http://127.0.0.1:5500/index.html')
    await url.waitFor(3000)

    i = 0
    courses = []
    links = []
    titles = []
    courseObj = {}

    coursesInfo = await url.querySelectorAll("div .ud-sr-only > span")
    courseLinks = await url.querySelectorAll("div .course-card--has-price-text--1c0ze > h3 > a")
    courseTitles = await url.querySelectorAll("div .course-card--has-price-text--1c0ze > h3 > a")

    for courseTitle in courseTitles:
        courseTitle = await courseTitle.getProperty("innerHTML")

        stringTitle = str(await courseTitle.jsonValue()).split("<div")

        titles.append(stringTitle[0])

    for courseLink in courseLinks:
        courseLink = await courseLink.getProperty("href")

        splitLink = str(await courseLink.jsonValue()).split("/course/")

        links.append(f"https://www.udemy.com/course/{splitLink[1]}")

    for courseInfo in coursesInfo:
        courseInfo = await courseInfo.getProperty("textContent")

        courseObj.update(title=titles[i])
        courseObj.update(url=links[i])

        if "Original" in await courseInfo.jsonValue():
            split = str(await courseInfo.jsonValue()).split(": ")
            courseObj.update(originalPrice=split[1])
        elif "Current" in await courseInfo.jsonValue():
            split = str(await courseInfo.jsonValue()).split(": ")
            courseObj.update(currentPrice=split[1])

        if "originalPrice" in courseObj and "currentPrice" in courseObj:
            courses.append(courseObj)
            courseObj = {}
            i = i + 1

    textMessage = ""

    for course in courses[:5]:
        textMessage += f"\n Title: {course.get('title')}\n Link: {course.get('url')}\n Current Price: {course.get('currentPrice')}\n Original Price: {course.get('originalPrice')}\n"

        # account_sid = os.getenv("TWILIO_ACCOUNT_ID")
        # auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        # client = Client(account_sid, auth_token)
        # message = client.messages.create(
        #     body=f"{textMessage}",
        #     from_=os.getenv("TWILIO_PHONE_NUMBER"),
        #     to=os.getenv("RECIPIENT_PHONE_NUMBER")
        # )

    await browserObj.close()


print(asyncio.get_event_loop().run_until_complete(main()))
