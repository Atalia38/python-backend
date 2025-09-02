



USE_HARDCODED = False  # EDIT HERE: set to True to use the values below
HARDCODED_SMTP_HOST = "smtp.gmail.com"     # EDIT HERE if USE_HARDCODED=True
HARDCODED_SMTP_PORT = 587                 
HARDCODED_SMTP_USER = "ataliarh64@gmail.com"  
HARDCODED_SMTP_PASS = "cuvdmpkeitavhwkx"        
# ---------------------------------------------------------------

import requests
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()

def fetch_news_content(api_key, country="us", category="general"):
    """Fetch top news headlines from NewsAPI"""
    try:
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            "country": country,
            "category": category,
            "apiKey": api_key
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data['status'] == 'ok' and data['totalResults'] > 0:
            articles = data['articles'][:3]  # Get top 3 articles
            return articles
        else:
            return None
    except Exception as e:
        print(f"Error fetching news: {e}")
        return None

def fetch_weather_content(api_key, city="New York"):
    """Fetch current weather data from OpenWeatherMap"""
    try:
        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        weather_info = {
            "city": data['name'],
            "temp": data['main']['temp'],
            "description": data['weather'][0]['description'],
            "humidity": data['main']['humidity'],
            "wind_speed": data['wind']['speed']
        }
        return weather_info
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return None

def fetch_fun_fact():
    """Fetch a random fun fact from an API"""
    try:
        # Using the API Ninjas Fun Facts API
        api_key = os.getenv('NINJAS_API_KEY')
        if api_key:
            url = "https://api.api-ninjas.com/v1/facts"
            headers = {'X-Api-Key': api_key}
            response = requests.get(url, headers=headers, params={'limit': 1})
            response.raise_for_status()
            data = response.json()
            return data[0]['fact'] if data else "Cats sleep for 70% of their lives."
        else:
            # Fallback facts if no API key
            fallback_facts = [
                "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
                "Octopuses have three hearts.",
                "A group of flamingos is called a 'flamboyance'.",
                "Bananas are berries, but strawberries aren't.",
                "The shortest war in history was between Britain and Zanzibar in 1896. Zanzibar surrendered after 38 minutes."
            ]
            import random
            return random.choice(fallback_facts)
    except Exception as e:
        print(f"Error fetching fun fact: {e}")
        return "The Great Wall of China is not visible from space with the naked eye."

def create_html_newsletter(news_articles, weather_info, fun_fact):
    """Create HTML newsletter content"""
    # Format news articles
    news_html = ""
    if news_articles:
        for article in news_articles:
            news_html += f"""
            <div style="margin-bottom: 20px; padding: 10px; border-left: 4px solid #4CAF50;">
                <h3 style="margin: 0 0 10px 0; color: #333;">{article['title']}</h3>
                <p style="margin: 0 0 10px 0; color: #666;">{article['description'] or 'No description available'}</p>
                <a href="{article['url']}" style="color: #4CAF50; text-decoration: none;">Read more</a>
            </div>
            """
    else:
        news_html = "<p>No news available at the moment.</p>"
    
    # Format weather info
    weather_html = ""
    if weather_info:
        weather_html = f"""
        <div style="background-color: #f5f5f5; padding: 15px; border-radius: 5px;">
            <h3 style="margin: 0 0 15px 0; color: #333;">Weather in {weather_info['city']}</h3>
            <p style="margin: 5px 0; color: #666;">Temperature: {weather_info['temp']}°C</p>
            <p style="margin: 5px 0; color: #666;">Conditions: {weather_info['description'].title()}</p>
            <p style="margin: 5px 0; color: #666;">Humidity: {weather_info['humidity']}%</p>
            <p style="margin: 5px 0; color: #666;">Wind Speed: {weather_info['wind_speed']} m/s</p>
        </div>
        """
    else:
        weather_html = "<p>Weather information currently unavailable.</p>"
    
    # Create the full HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Daily Newsletter</title>
    </head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto;">
        <div style="background-color: #4CAF50; padding: 20px; text-align: center;">
            <h1 style="color: white; margin: 0;">Daily Digest</h1>
            <p style="color: white; margin: 5px 0 0 0;">{datetime.now().strftime('%A, %B %d, %Y')}</p>
        </div>
        
        <div style="padding: 20px;">
            <h2 style="color: #4CAF50; border-bottom: 2px solid #4CAF50; padding-bottom: 10px;">Today's Weather</h2>
            {weather_html}
            
            <h2 style="color: #4CAF50; border-bottom: 2px solid #4CAF50; padding-bottom: 10px; margin-top: 30px;">Top News</h2>
            {news_html}
            
            <h2 style="color: #4CAF50; border-bottom: 2px solid #4CAF50; padding-bottom: 10px; margin-top: 30px;">Fun Fact of the Day</h2>
            <div style="background-color: #fff4e6; padding: 15px; border-radius: 5px; border-left: 4px solid #ffa94d;">
                <p style="margin: 0; font-style: italic;">{fun_fact}</p>
            </div>
            
            <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee; text-align: center;">
                <p style="color: #999; font-size: 12px;">
                    This newsletter was generated automatically. 
                    <br>You can unsubscribe at any time by replying to this email.
                </p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html_content

def send_newsletter(sender_email, sender_password, subscribers, subject, html_content):
    """Send newsletter to subscribers"""
    try:
        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        
        # Send to each subscriber
        for subscriber in subscribers:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = sender_email
            msg['To'] = subscriber
            
            # Attach HTML content
            msg.attach(MIMEText(html_content, 'html'))
            
            # Send email
            server.sendmail(sender_email, subscriber, msg.as_string())
            print(f"Newsletter sent to {subscriber}")
        
        server.quit()
        print("All newsletters sent successfully!")
        return True
        
    except Exception as e:
        print(f"Error sending newsletter: {e}")
        return False

def main():
    # Get API keys from environment variables
    news_api_key = os.getenv('NEWS_API_KEY')
    weather_api_key = os.getenv('OPENWEATHER_API_KEY')
    
    # Email configuration
    sender_email = os.getenv('email')
    sender_password = os.getenv('password')
    
    print(news_api_key)
    print(weather_api_key)
    print(sender_email)
    print(sender_password)
    # List of subscribers (in a real app, this would come from a database)
    subscribers = [
        "ataliarh64@gmail.com"
    ]
    
    # Fetch content from APIs
    print("Fetching content from APIs...")
    news_articles = fetch_news_content(news_api_key)
    weather_info = fetch_weather_content(weather_api_key, "New York")
    fun_fact = fetch_fun_fact()
    
    # Create HTML newsletter
    print("Creating newsletter...")
    html_content = create_html_newsletter(news_articles, weather_info, fun_fact)
    
    # Send newsletter
    subject = f"test"
    print(html_content)
    print("Sending newsletter...")
    success = send_newsletter(sender_email, sender_password, subscribers, subject, html_content)
    
    if success:
        print("Newsletter process completed successfully!")
    else:
        print("There was an error sending the newsletter.")

if __name__ == "__main__":
    main()