# Udemy Price Tracker

![udemy](https://github.com/user-attachments/assets/0303a0ef-6397-4dc4-9e1e-426d44d4e748)

## Inspiration

While browsing Udemy, I realized that there wasn't an easy way to monitor course prices without visiting the website manually. This led me to build a solution that could automate this process and notify me when course prices change.

## Challenges

- Dealing with anti-bot detection and browser delays
- Parsing complex DOM structures to locate accurate price and title elements

## Lessons Learned

- How to automate browsers using Pyppeteer
- Fundamentals of web scraping, including DOM traversal and handling dynamic content
- How to send SMS messages using the Twilio API

## The Service

1. The program launches a headless browser using Pyppeteer.
2. It visits the Udemy course page(s) and scrapes course titles and prices based on a specified course topic.
3. The data is formatted (Course Title, Course Price, etc.) and sent as an SMS using Twilio.
