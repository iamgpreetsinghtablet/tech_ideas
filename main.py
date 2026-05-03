import os
import json
from datetime import datetime
from openai import OpenAI
from publisher import TechIdeasPublisher

# Configuration
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
DEFAULT_MODEL = "meta/llama-3.1-405b-instruct"

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=NVIDIA_API_KEY
)

def generate_tech_idea():
    prompt = """
    Act as a Visionary Tech Futurist. Generate one "Latest Tech Idea" that is innovative, plausible for the year 2026-2030, and addresses a real-world problem.
    
    Provide the response in JSON format with the following fields:
    - title: A catchy title for the idea.
    - description: A concise 1-2 sentence description of the concept and its impact.
    - tags: A list of 3 relevant hashtags (e.g., #AI, #Sustainabilty).
    - date: Today's date in 'Month Day, Year' format (e.g., May 3, 2026).
    """
    
    try:
        completion = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            response_format={ "type": "json_object" }
        )
        return json.loads(completion.choices[0].message.content)
    except Exception as e:
        print(f"Error generating idea: {e}")
        return None

def format_idea_to_html(idea):
    tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in idea['tags']])
    return f"""
            <div class="idea-card">
                <span class="idea-date">{idea['date']}</span>
                <h2 class="idea-title">{idea['title']}</h2>
                <p class="idea-description">{idea['description']}</p>
                <div class="idea-tags">
                    {tags_html}
                </div>
            </div>"""

def main():
    print("🚀 Generating new tech idea...")
    idea = generate_tech_idea()
    
    if idea:
        print(f"Found idea: {idea['title']}")
        html_fragment = format_idea_to_html(idea)
        
        publisher = TechIdeasPublisher()
        success = publisher.publish(html_fragment)
        
        if success:
            print("✅ Blog updated and published successfully!")
        else:
            print("❌ Failed to publish update.")
    else:
        print("❌ Could not generate a valid idea.")

if __name__ == "__main__":
    main()
