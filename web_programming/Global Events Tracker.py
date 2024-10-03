from flask import Flask, render_template_string
import requests

app = Flask(__name__)

# Public APIs for real-time global data (you can replace or add more as needed)
COVID_API_URL = "https://disease.sh/v3/covid-19/countries"  # Get COVID-19 stats by country
NEWS_API_URL = "https://gnews.io/api/v4/top-headlines?token=YOUR_API_KEY&lang=en"  # Replace with your API key

# Base HTML template
BASE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Global Events Tracker</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
        header { background-color: #007bff; color: white; padding: 15px; text-align: center; }
        nav a { margin: 0 15px; color: white; text-decoration: none; }
        nav { margin-bottom: 20px; }
        main { padding: 20px; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 15px 0; padding: 10px; border: 1px solid #ddd; background-color: #f9f9f9; }
        .event-title { font-size: 1.2em; font-weight: bold; }
        .event-meta { font-size: 0.9em; color: #555; }
        .description { margin-top: 10px; }
    </style>
</head>
<body>
    <header>
        <h1>Global Events Tracker</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/covid-stats">COVID-19 Stats</a>
            <a href="/news">Global News</a>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
"""

# Index (Home) Template
INDEX_TEMPLATE = """
{% extends "base.html" %}
{% block content %}
<h2>Welcome to the Global Events Tracker</h2>
<p>Track live global events like COVID-19 stats and global news headlines from reliable sources.</p>
<ul>
    <li><a href="/covid-stats">View COVID-19 Global Stats</a></li>
    <li><a href="/news">View Latest Global News</a></li>
</ul>
{% endblock %}
"""

# COVID-19 Stats Template
COVID_TEMPLATE = """
{% extends "base.html" %}
{% block content %}
<h2>Global COVID-19 Stats</h2>
<p>Real-time data from the disease.sh API</p>
<ul>
    {% for country in covid_data %}
        <li>
            <div class="event-title">{{ country['country'] }}</div>
            <div class="event-meta">Cases: {{ country['cases'] }} | Deaths: {{ country['deaths'] }} | Recovered: {{ country['recovered'] }}</div>
        </li>
    {% else %}
        <li>No data available</li>
    {% endfor %}
</ul>
{% endblock %}
"""

# News Template
NEWS_TEMPLATE = """
{% extends "base.html" %}
{% block content %}
<h2>Latest Global News</h2>
<p>Real-time news fetched from the GNews API</p>
<ul>
    {% for article in news_data %}
        <li>
            <div class="event-title"><a href="{{ article['url'] }}" target="_blank">{{ article['title'] }}</a></div>
            <div class="event-meta">Source: {{ article['source']['name'] }} | Published: {{ article['publishedAt'][:10] }}</div>
            <p class="description">{{ article['description'] }}</p>
        </li>
    {% else %}
        <li>No news articles found</li>
    {% endfor %}
</ul>
{% endblock %}
"""

@app.route('/')
def index():
    return render_template_string(BASE_TEMPLATE + INDEX_TEMPLATE)

@app.route('/covid-stats')
def covid_stats():
    # Fetch COVID-19 stats from the public API
    try:
        response = requests.get(COVID_API_URL)
        covid_data = response.json() if response.status_code == 200 else []
    except requests.exceptions.RequestException as e:
        covid_data = []
        print(f"Error fetching COVID data: {e}")
    
    return render_template_string(BASE_TEMPLATE + COVID_TEMPLATE, covid_data=covid_data)

@app.route('/news')
def global_news():
    # Fetch global news using GNews API
    try:
        response = requests.get(NEWS_API_URL)
        news_data = response.json().get('articles', []) if response.status_code == 200 else []
    except requests.exceptions.RequestException as e:
        news_data = []
        print(f"Error fetching news data: {e}")
    
    return render_template_string(BASE_TEMPLATE + NEWS_TEMPLATE, news_data=news_data)

if __name__ == '__main__':
    app.run(debug=True)
