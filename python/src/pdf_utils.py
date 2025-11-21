import os
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject

def extract_text_from_pdfs(file_paths):
    """
    Extracts text from a list of PDF files.
    
    Args:
        file_paths (list): List of absolute paths to PDF files.
        
    Returns:
        str: Combined text content from all PDFs.
    """
    combined_text = ""
    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f"Warning: File not found: {file_path}")
            continue
            
        try:
            reader = PdfReader(file_path)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    combined_text += text + "\n"
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            
    return combined_text

def fill_pdf_form(template_path, data, output_path):
    """
    Fills a PDF form with the provided data.
    
    Args:
        template_path (str): Path to the PDF form template.
        data (dict): Dictionary of field names and values.
        output_path (str): Path to save the filled PDF.
        
    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        reader = PdfReader(template_path)
        writer = PdfWriter()

        # Copy all pages from the reader to the writer
        for page in reader.pages:
            writer.add_page(page)

        # Copy AcroForm dictionary if present and fix NullObjects
        if "/AcroForm" in reader.trailer["/Root"]:
             acroform = reader.trailer["/Root"]["/AcroForm"]
             if "/Fields" in acroform:
                 fields_array = acroform["/Fields"]
                 
                 # Check if there are NullObjects
                 has_null_objects = any(f.__class__.__name__ == 'NullObject' for f in fields_array)
                 
                 if has_null_objects:
                     # Rebuild fields array from page annotations
                     print("Rebuilding fields array from page annotations in writer...")
                     new_fields = []
                     
                     for page in reader.pages:
                         if "/Annots" in page:
                             annots = page["/Annots"]
                             for annot in annots:
                                 try:
                                     if hasattr(annot, 'get_object'):
                                         obj = annot.get_object()
                                     else:
                                         obj = annot
                                     
                                     # Check if this is a form field widget
                                     if '/Subtype' in obj and obj['/Subtype'] == '/Widget' and '/T' in obj:
                                         # Add this field reference if not already in new_fields
                                         if annot not in new_fields:
                                             new_fields.append(annot)
                                 except:
                                     pass
                     
                     # Replace the fields array
                     while len(fields_array) > 0:
                         fields_array.pop()
                     fields_array.extend(new_fields)
                     
             writer._root_object.update({
                 NameObject("/AcroForm"): acroform
             })

        # Update the form fields
        # Note: pypdf's update_page_form_field_values is deprecated/removed in newer versions
        # We use the writer.update_page_form_field_values if available or manual update
        
        # In pypdf > 3.0, we can use writer.update_page_form_field_values
        # But let's try a robust way:
        
        writer.update_page_form_field_values(
            writer.pages[0], data
        )
        
        # If there are multiple pages with forms, we might need to loop. 
        # For now, assuming the form is on the first page or fields are global.
        # A safer approach for all pages:
        for page in writer.pages:
            writer.update_page_form_field_values(page, data)

        with open(output_path, "wb") as output_file:
            writer.write(output_file)
            
        return True
    except Exception as e:
        print(f"Error filling PDF: {e}")
        return False

def get_form_fields(template_path):
    """
    Returns a list of form field names from the PDF.
    """
    try:
        reader = PdfReader(template_path)
        # Handle potential NullObjects in fields
        if "/AcroForm" in reader.trailer["/Root"]:
            acroform = reader.trailer["/Root"]["/AcroForm"]
            if "/Fields" in acroform:
                fields = acroform["/Fields"]
                # Filter out NullObjects
                valid_fields = [f for f in fields if not isinstance(f, type(None)) and f.__class__.__name__ != 'NullObject']
                # We can't easily update the reader's internal cache, but get_fields iterates.
                # Let's try to use get_fields() and catch the specific error or iterate manually if needed.
                # But get_fields() is a high-level method.
                
        # If get_fields() crashes or returns incomplete results due to NullObjects,
        # we need to rebuild the /Fields array from page annotations
        if "/AcroForm" in reader.trailer["/Root"] and "/Fields" in reader.trailer["/Root"]["/AcroForm"]:
             fields_array = reader.trailer["/Root"]["/AcroForm"]["/Fields"]
             
             # Check if there are NullObjects
             has_null_objects = any(f.__class__.__name__ == 'NullObject' for f in fields_array)
             
             if has_null_objects:
                 # Rebuild fields array from page annotations
                 print("Rebuilding fields array from page annotations...")
                 new_fields = []
                 
                 for page in reader.pages:
                     if "/Annots" in page:
                         annots = page["/Annots"]
                         for annot in annots:
                             try:
                                 if hasattr(annot, 'get_object'):
                                     obj = annot.get_object()
                                 else:
                                     obj = annot
                                 
                                 # Check if this is a form field widget
                                 if '/Subtype' in obj and obj['/Subtype'] == '/Widget' and '/T' in obj:
                                     # Add this field reference if not already in new_fields
                                     if annot not in new_fields:
                                         new_fields.append(annot)
                             except:
                                 pass
                 
                 # Replace the fields array
                 while len(fields_array) > 0:
                     fields_array.pop()
                 fields_array.extend(new_fields)
                  
                 
        fields = reader.get_fields()
        if fields:
            return list(fields.keys())
        return []
    except Exception as e:
        print(f"Error reading fields: {e}")
        return []
