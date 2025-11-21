import requests
import os
import json
import shutil

def run_test():
    # Configuration
    base_url = "http://localhost:5003"
    
    # Define paths (relative to this script)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_pdf = os.path.join(current_dir, "input", "Haensel.pdf")
    output_pdf = os.path.join(current_dir, "output", "Ergebnis.pdf")
    
    # We need a form template. 
    # If output/Ergebnis.pdf exists and we want to write TO it, we should probably 
    # use a copy of it as the template, or assume a separate template exists.
    # For this test, we'll ensure a template exists.
    form_template = os.path.join(current_dir, "output", "FormTemplate.pdf")
    
    # Create a dummy template from existing pdf if needed (just for testing mechanics)
    if not os.path.exists(form_template):
        if os.path.exists(output_pdf):
            print(f"Creating template from {output_pdf}...")
            shutil.copy(output_pdf, form_template)
        elif os.path.exists(input_pdf):
             # Fallback to input if output doesn't exist, just to have a PDF
             print(f"Creating template from {input_pdf}...")
             shutil.copy(input_pdf, form_template)
        else:
            print("Error: No PDF found to use as form template.")
            return

    payload = {
        "input_files": [input_pdf],
        "form_file": form_template,
        "output_file": output_pdf
    }

    print(f"Sending request to {base_url}/process")
    print(json.dumps(payload, indent=2))

    try:
        response = requests.post(f"{base_url}/process", json=payload)
        
        print(f"\nStatus Code: {response.status_code}")
        try:
            print("Response:", json.dumps(response.json(), indent=2))
        except:
            print("Response:", response.text)
            
    except requests.exceptions.ConnectionError:
        print("\nError: Could not connect to the server. Is it running?")

if __name__ == "__main__":
    run_test()
