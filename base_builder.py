import json
import os
from google import genai

# 1. PASTE YOUR API KEY HERE
GEMINI_API_KEY = "AIzaSyAWaOkl84_dq9Jae3OOiz_AycK9eXFbqak"
client = genai.Client(api_key=GEMINI_API_KEY)

def generate_base_college_data(college_query):
    print(f"🔍 Searching the web for real-time data on: {college_query}...")
    
    prompt = f"""
    You are an expert higher education researcher. Search for the most up-to-date and official information for: "{college_query}".
    
    Output STRICTLY as a valid JSON object (NOT an array). Do not include markdown blocks like ```json.
    
    {{
      "name": "The official, exact name of the institution",
      "location": "City, State",
      "displayLocation": "Just the City (e.g., New Delhi)",
      "establishedYear": "The exact year it was founded (e.g., 1882)",
      "accreditation": "e.g., NAAC A++, UGC Approved, AICTE, etc. (Or N/A)",
      "nirfRanking": "The most recent NIRF ranking band (e.g., Top 100, 101-150) or N/A",
      "tuitionFee": "Estimated average yearly tuition (e.g., ₹2 Lakhs - ₹4 Lakhs/Year)",
      "hostelFee": "Estimated yearly hostel fee (e.g., ₹1.2 Lakhs/Year) or 'Check Prospectus'",
      "description": "A premium, 2-sentence summary of what the college is famous for.",
      "websiteUrl": "The exact official website link (e.g., [https://www.sju.edu.in](https://www.sju.edu.in))",
      "image": "[https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=800&auto=format&fit=crop](https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=800&auto=format&fit=crop)"
    }}
    """
    
    try:
        response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
        raw_json = response.text.strip().replace("```json", "").replace("```", "")
        return json.loads(raw_json)
    except Exception as e:
        print(f"❌ Failed to fetch base data for {college_query}: {e}")
        return None

if __name__ == "__main__":
    db_file = "colleges.json"
    
    # Load existing database
    if os.path.exists(db_file):
        with open(db_file, 'r', encoding='utf-8') as file:
            try:
                database = json.load(file)
            except json.JSONDecodeError:
                database = []
    else:
        database = []

    existing_names = [col['name'].lower() for col in database]

    # =========================================================
    # 2. 60 PREMIER INSTITUTIONS ACROSS INDIA
    # =========================================================
    NEW_COLLEGES = [
        # --- Elite Engineering (IITs, NITs, Private) ---
        "Indian Institute of Technology (IIT) Bombay, Mumbai",
        "Indian Institute of Technology (IIT) Delhi, New Delhi",
        "Indian Institute of Technology (IIT) Madras, Chennai",
        "Indian Institute of Technology (IIT) Kanpur, Kanpur",
        "Indian Institute of Technology (IIT) Kharagpur, Kharagpur",
        "Indian Institute of Technology (IIT) Roorkee, Roorkee",
        "Indian Institute of Technology (IIT) Guwahati, Guwahati",
        "Indian Institute of Technology (IIT) Hyderabad, Hyderabad",
        "Birla Institute of Technology and Science (BITS), Pilani",
        "Vellore Institute of Technology (VIT), Vellore",
        "SRM Institute of Science and Technology, Chennai",
        "National Institute of Technology (NIT), Tiruchirappalli",
        "National Institute of Technology (NIT), Warangal",
        "Motilal Nehru National Institute of Technology (MNNIT), Allahabad",
        "National Institute of Technology (NIT), Rourkela",
        "Delhi Technological University (DTU), New Delhi",
        "Thapar Institute of Engineering and Technology, Patiala",
        "Kalinga Institute of Industrial Technology (KIIT), Bhubaneswar",
        
        # --- Top Medical Institutions ---
        "All India Institute of Medical Sciences (AIIMS), New Delhi",
        "Christian Medical College (CMC), Vellore",
        "Jawaharlal Institute of Postgraduate Medical Education & Research (JIPMER), Puducherry",
        "Armed Forces Medical College (AFMC), Pune",
        "King George's Medical University (KGMU), Lucknow",
        
        # --- Elite Management Schools (IIMs & Private) ---
        "Indian Institute of Management (IIM) Ahmedabad",
        "Indian Institute of Management (IIM) Calcutta, Kolkata",
        "Indian Institute of Management (IIM) Lucknow",
        "Indian Institute of Management (IIM) Kozhikode",
        "Indian Institute of Management (IIM) Indore",
        "XLRI - Xavier School of Management, Jamshedpur",
        "S. P. Jain Institute of Management and Research (SPJIMR), Mumbai",
        "Management Development Institute (MDI), Gurgaon",
        "Faculty of Management Studies (FMS) Delhi University, New Delhi",
        "Narsee Monjee Institute of Management Studies (NMIMS), Mumbai",
        "Symbiosis International (Deemed University), Pune",
        
        # --- Premier Law Schools ---
        "NALSAR University of Law, Hyderabad",
        "National Law University (NLU), New Delhi",
        "The West Bengal National University of Juridical Sciences (WBNUJS), Kolkata",
        
        # --- Top Arts, Commerce & Liberal Arts ---
        "Shri Ram College of Commerce (SRCC), New Delhi",
        "St. Stephen's College, New Delhi",
        "Hindu College, New Delhi",
        "Lady Shri Ram College for Women (LSR), New Delhi",
        "Loyola College, Chennai",
        "Madras Christian College (MCC), Chennai",
        "St. Xavier's College, Mumbai",
        "Tata Institute of Social Sciences (TISS), Mumbai",
        
        # --- Modern Private Universities (Liberal Arts & Multidisciplinary) ---
        "Ashoka University, Sonipat",
        "O.P. Jindal Global University, Sonipat",
        "Krea University, Sri City",
        "Amity University, Noida",
        
        # --- Top Central & State Universities ---
        "Jadavpur University, Kolkata",
        "Jawaharlal Nehru University (JNU), New Delhi",
        "Banaras Hindu University (BHU), Varanasi",
        "University of Hyderabad, Hyderabad",
        "Anna University, Chennai",
        "Savitribai Phule Pune University, Pune",
        "Jamia Millia Islamia (JMI), New Delhi",
        
        # --- Elite Design & Architecture ---
        "National Institute of Design (NID), Ahmedabad",
        "National Institute of Fashion Technology (NIFT), New Delhi",
        "CEPT University, Ahmedabad",
        "Sir J.J. College of Architecture, Mumbai"
    ]

    print(f"🚀 Starting Base Builder for {len(NEW_COLLEGES)} colleges...\n")

    for target in NEW_COLLEGES:
        is_update = False
        update_index = -1
        
        for idx, existing_col in enumerate(database):
            if target.split(',')[0].lower().strip() in existing_col['name'].lower():
                is_update = True
                update_index = idx
                break
                
        new_data = generate_base_college_data(target)
        
        if new_data:
            if is_update:
                print(f"   🔄 UPDATING existing base info for: {new_data['name']}")
                for key in new_data:
                    database[update_index][key] = new_data[key]
            else:
                print(f"   ✨ ADDING entirely new college: {new_data['name']}")
                new_data["detailedCourses"] = [] 
                new_data["allCoursesList"] = []
                database.append(new_data)
                
            # Save immediately so you don't lose progress if it stops midway
            with open(db_file, 'w', encoding='utf-8') as f:
                json.dump(database, f, indent=2, ensure_ascii=False)
                
    print("\n🎉 Base building complete! Check your colleges.html page.")