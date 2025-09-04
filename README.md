# PDF Merger

A simple tool that lets you merge PDFs, since I didn't find any free versions that let you do that online.

## Usage

### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies
```bash
uv sync
```

### 3. Prepare your PDFs
Choose one of the following options:

**Option A: Use the pdfs/ folder**
- Save your PDF files into the `pdfs/` folder
- Update the PDFS_TO_MERGE list  in `main.py` to contain the names of the pdfs

**Option B: Use existing file locations**
- Update the paths in `main.py` to point directly to your PDF files wherever they're saved on your computer

### 4. Configure output
Specify the name of the merged PDF in the `main.py` file using the NEW_PDF_NAME variable

### 5. Run the merger
```bash
uv run main.py
```

### 6. Get your merged PDF
The merged PDF will be saved in the `merged/` folder.
