import os
import uuid
from flask import Flask, request, jsonify
from pdf_utils import extract_text_from_pdfs, fill_pdf_form, get_form_fields
from ai_service import analyze_text_and_map_to_fields

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_pdf():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
        
    input_files = data.get('input_files', [])
    form_file = data.get('form_file')
    
    if not input_files or not form_file:
        return jsonify({"error": "Missing input_files or form_file"}), 400
        
    # Validate files exist
    for f in input_files:
        if not os.path.exists(f):
            return jsonify({"error": f"Input file not found: {f}"}), 404
    if not os.path.exists(form_file):
        return jsonify({"error": f"Form file not found: {form_file}"}), 404

    try:
        # 1. Extract Text
        print("Extracting text...")
        extracted_text = extract_text_from_pdfs(input_files)
        
        # 2. Get Form Fields
        print("Reading form fields...")
        form_fields = get_form_fields(form_file)
        if not form_fields:
             return jsonify({"error": "No fields found in form PDF"}), 400
             
        # 3. AI Analysis
        print("Analyzing with AI...")
        mapped_data = analyze_text_and_map_to_fields(extracted_text, form_fields)
        
        # 4. Fill PDF
        print("Filling PDF...")
        output_file = data.get('output_file')
        if output_file:
            output_path = output_file
            # Ensure directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
        else:
            output_filename = f"filled_{uuid.uuid4().hex}.pdf"
            output_dir = os.path.dirname(form_file) # Save in same dir as form for now, or temp
            output_path = os.path.join(output_dir, output_filename)
        
        success = fill_pdf_form(form_file, mapped_data, output_path)
        
        if success:
            return jsonify({
                "status": "success",
                "output_file": output_path,
                "metadata": mapped_data
            })
        else:
            return jsonify({"error": "Failed to fill PDF"}), 500

    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
