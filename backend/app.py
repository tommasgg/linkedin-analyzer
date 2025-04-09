from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

def analyze_linkedin_profile(url):
    try:
        # Basic URL validation
        parsed_url = urlparse(url)
        if not parsed_url.netloc.endswith('linkedin.com'):
            return {"error": "Invalid LinkedIn URL"}

        # Send request to LinkedIn profile
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            return {"error": "Could not fetch LinkedIn profile"}

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract basic information
        name = soup.find('h1', {'class': 'text-heading-xlarge'})
        headline = soup.find('div', {'class': 'text-body-medium'})
        about = soup.find('div', {'class': 'display-flex ph5 pv3'})
        
        # Extract experience
        experience = []
        experience_section = soup.find('section', {'id': 'experience'})
        if experience_section:
            for exp in experience_section.find_all('li', {'class': 'artdeco-list__item'}):
                title = exp.find('h3', {'class': 't-16 t-black t-bold'})
                company = exp.find('p', {'class': 'pv-entity__secondary-title'})
                duration = exp.find('span', {'class': 'pv-entity__bullet-item'})
                if title and company:
                    experience.append({
                        'title': title.text.strip(),
                        'company': company.text.strip(),
                        'duration': duration.text.strip() if duration else None
                    })

        return {
            'name': name.text.strip() if name else None,
            'headline': headline.text.strip() if headline else None,
            'about': about.text.strip() if about else None,
            'experience': experience
        }

    except Exception as e:
        return {"error": str(e)}

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    result = analyze_linkedin_profile(url)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True) 