import requests
import os
import json
import shutil
import argparse

def run_test(input_file, output_file):
    # Configuration
    base_url = "http://localhost:5003"
    
    # Define paths (relative to this script)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Convert relative paths to absolute paths
    if not os.path.isabs(input_file):
        input_pdf = os.path.join(current_dir, input_file)
    else:
        input_pdf = input_file
    
    if not os.path.isabs(output_file):
        output_pdf = os.path.join(current_dir, "output", output_file)
    else:
        output_pdf = output_file
    
    # Check if input file exists
    if not os.path.exists(input_pdf):
        print(f"Error: Input file not found: {input_pdf}")
        return
    
    # We need a form template. 
    # If output/Ergebnis.pdf exists and we want to write TO it, we should probably 
    # use a copy of it as the template, or assume a separate template exists.
    # For this test, we'll ensure a template exists.
    form_template = os.path.join(current_dir, "output", "FormTemplate.pdf")
    
    # Create a dummy template from existing pdf if needed (just for testing mechanics)
    if not os.path.exists(form_template):
        # Try to find any PDF in output directory to use as template
        output_dir = os.path.join(current_dir, "output")
        if os.path.exists(output_dir):
            pdf_files = [f for f in os.listdir(output_dir) if f.endswith('.pdf')]
            if pdf_files:
                print(f"Creating template from {pdf_files[0]}...")
                shutil.copy(os.path.join(output_dir, pdf_files[0]), form_template)
            else:
                print("Error: No PDF found to use as form template.")
                return
        else:
            print("Error: No PDF found to use as form template.")
            return

    # Ensure output directory exists
    output_dir = os.path.dirname(output_pdf)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

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
    parser = argparse.ArgumentParser(description='Process PDF forms with AI')
    parser.add_argument('-in', '--input', dest='input_file', 
                        default='input/Haensel.pdf',
                        help='Input PDF file path (default: input/Haensel.pdf)')
    parser.add_argument('-out', '--output', dest='output_file',
                        default='Ergebnis.pdf',
                        help='Output PDF file name (default: Ergebnis.pdf)')
    
    args = parser.parse_args()
    run_test(args.input_file, args.output_file)

