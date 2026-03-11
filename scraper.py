import os
import json
from firecrawl import FirecrawlApp
import google.generativeai as genai

# ==========================================
# 1. SETUP & API KEYS
# ==========================================
# Replace these with your actual API keys
FIRECRAWL_API_KEY = "YOUR_FIRECRAWL_KEY"
GEMINI_API_KEY = "YOUR_GEMINI_KEY"

firecrawl = FirecrawlApp(api_key=FIRECRAWL_API_KEY)
genai.configure(api_key=GEMINI_API_KEY)

# Using Gemini 1.5 Flash for fast, accurate data extraction
model = genai.GenerativeModel('gemini-1.5-flash')

# ==========================================
# 2. THE AI EXTRACTION FUNCTION
# ==========================================
def scrape_college_to_json(college_url, official_website_link):
    print(f"🕵️‍♂️ Crawling: {college_url}...")
    
    # Scrape the website content
    scraped_data = firecrawl.scrape_url(college_url, params={'formats': ['markdown']})
    web_text = scraped_data['markdown']

    print("🧠 Processing data with Gemini...")
    
    # Prompting Gemini to format the data EXACTLY as your frontend requires
    prompt = f"""
    You are an expert educational data extractor for the 'VidyaVantage' career platform.
    Read the following text from a college website and extract the key details.
    
    Output the data STRICTLY as a valid JSON object with the following keys. Do not include markdown blocks like ```json. Just the raw JSON.
    
    {{
      "name": "Full Name of the College",
      "location": "City and specific area (e.g., 'Bengaluru South' or 'New Delhi NCR')",
      "displayLocation": "City name for UI display (e.g., 'Bengaluru')",
      "category": "Space-separated lowercase keywords based on courses offered (pick from: engineering, architecture, management, science, medicine, pharmacy, law, hospitality, arts)",
      "theme": "A dark, professional hex color code representing the college (e.g., '#1E3A8A')",
      "image": "A realistic image URL representing a college campus (you can use a placeholder like '[https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=600](https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=600)' if you cannot find one)",
      "accreditation": "Short accreditation text (e.g., 'NAAC A+ Grade', 'NIRF Rank #5', 'Est. 1990')",
      "description": "A punchy, 2-sentence description of the college and its top courses, written for high school students.",
      "url": "{official_website_link}"
    }}
    
    Website Text:
    {web_text[:20000]}
    """
    
    response = model.generate_content(prompt)
    
    try:
        # Clean up the response to ensure it's pure JSON
        raw_json = response.text.strip().replace("```json", "").replace("```", "")
        college_data = json.loads(raw_json)
        return college_data
    except Exception as e:
        print(f"❌ Error parsing JSON from AI: {e}")
        print("Raw output:", response.text)
        return None

# ==========================================
# 3. SAVING TO YOUR DATABASE
# ==========================================
def add_to_database(new_college_data, db_file="colleges.json"):
    # Load existing data
    if os.path.exists(db_file):
        with open(db_file, 'r', encoding='utf-8') as file:
            try:
                database = json.load(file)
            except json.JSONDecodeError:
                database = []
    else:
        database = []
        
    # Add the new college
    database.append(new_college_data)
    
    # Save it back to the file
    with open(db_file, 'w', encoding='utf-8') as file:
        json.dump(database, file, indent=2, ensure_ascii=False)
        
    print(f"✅ Successfully added {new_college_data['name']} to {db_file}!")

# ==========================================
# 4. RUN THE SCRIPT
# ==========================================
if __name__ == "__main__":
    # Example: Let's scrape Christ University's Wikipedia or About page
    target_url = "[https://en.wikipedia.org/wiki/Christ_University](https://en.wikipedia.org/wiki/Christ_University)"
    official_link = "[https://christuniversity.in/](https://christuniversity.in/)"
    
    new_data = scrape_college_to_json(target_url, official_link)
    
    if new_data:
        add_to_database(new_data)
