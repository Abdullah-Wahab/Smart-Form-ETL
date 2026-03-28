# Smart-Form-ETL 🚀📄

An automated Data Extraction pipeline designed to solve the manual data-entry bottleneck. This utility batch-processes unstructured PDF forms (e.g., registrations, applications, KYC documents) and converts them into structured, queryable data formats. 

## 💼 Business Impact
In standard business operations, forms often use inconsistent labeling (e.g., "Full Name" vs. "Candidate Name"). This tool uses intelligent pattern matching to overcome varied label styles and missing fields, drastically reducing human error and processing time.

## 🛠 Key Features
* **Batch Processing Engine**: Capable of reading multi-page PDFs where each page represents a distinct user form.
* **Intelligent Regex Matching**: Uses flexible regular expressions to capture specific data points (Name, Phone, Email) regardless of slight variations in form design.
* **Constant-Time Data Structuring**: Extracted records are stored in dictionaries, allowing for $O(1)$ constant-time lookups and clean data structuring.
* **Fault Tolerance**: Automatically handles missing or incomplete fields by substituting default "N/A" values without crashing.

## 🚀 Tech Stack
* **Language**: Python 3.x
* **Data Extraction**: `PyMuPDF` (fitz) for high-speed, accurate document parsing.
* **Pattern Recognition**: Python `re` module for linear-time string matching.

## ⚙️ Installation & Usage

### 1. Setup Environment
Ensure your virtual environment is active, then install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. Run the Extractor
The script is modularized. You can process single forms or batch-process multi-page documents:

```bash
python extractinfo.py
```

## 📊 Performance Analysis
This tool is optimized for scaling across large document batches.

* **Time Complexity**: $O(n \cdot m)$. 
  * Scales linearly based on the number of pages ($n$) and the average characters per page ($m$).
* **Space Complexity**: $O(n \cdot m)$. 
  * Memory is managed efficiently per page, with minimal overhead from regex match objects.

---
Developed with ❤️ by [Abdullah Wahab](https://github.com/Abdullah-Wahab)