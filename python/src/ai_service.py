import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Warning: OPENAI_API_KEY not found.")
        return None
    return OpenAI(api_key=api_key)

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Moved to inside function

def analyze_text_and_map_to_fields(text_content, form_fields):
    """
    Analyzes the text content and maps it to the provided form fields using OpenAI.
    
    Args:
        text_content (str): The text extracted from input PDFs.
        form_fields (list): List of field names available in the target PDF form.
        
    Returns:
        dict: A dictionary mapping field names to values.
    """
    
    prompt = f"""
    You are a data extraction assistant. 
    I have a text extracted from documents and a list of target form fields.
    Your goal is to extract information from the text that corresponds to the form fields.
    
    Target Form Fields: {json.dumps(form_fields)}
    
    Extracted Text:
    {text_content[:10000]} 
    (Text truncated to 10k chars to fit context if necessary)
    
    Return a JSON object where keys are the Form Fields and values are the extracted data.
    If a field cannot be found, use an empty string "".
    Do not include any markdown formatting or explanations, just the raw JSON string.
    """
    
    client = get_client()
    if not client:
        return {}

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that extracts data into JSON format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0
        )
        
        content = response.choices[0].message.content.strip()
        
        # Clean up potential markdown code blocks if GPT adds them
        if content.startswith("```json"):
            content = content[7:]
        if content.endswith("```"):
            content = content[:-3]
            
        return json.loads(content)
        
    except Exception as e:
        print(f"Error during AI analysis: {e}")
        return {}
