# Python PDF Processing Service

This service extracts data from input PDFs using OpenAI and fills a target PDF form.

## Setup

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Environment Variables:**
    Copy `.env.example` to `.env` and add your OpenAI API Key.
    ```bash
    cp .env.example .env
    # Edit .env
    ```

## Running the Service

```bash
python src/app.py
```
The server will start at `http://localhost:5000`.

## API Usage

**Endpoint:** `POST /process`

**Payload:**
```json
{
    "input_files": [
        "/absolute/path/to/input1.pdf",
        "/absolute/path/to/input2.pdf"
    ],
    "form_file": "/absolute/path/to/form_template.pdf"
}
```

**Response:**
```json
{
    "status": "success",
    "output_file": "/absolute/path/to/filled_randomid.pdf",
    "metadata": {
        "Field1": "Value1",
        "Field2": "Value2"
    }
}
```
