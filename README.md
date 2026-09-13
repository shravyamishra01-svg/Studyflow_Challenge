# StudyFlow 🎓

> **AI-Powered Lecture PDF → Revision Notes Web App**
> Turn dense lecture slides and readings into high-yield, scannable revision notes using the Google Gemini API with strict factual grounding.

---

## 🌟 Overview

**StudyFlow** is a focused, production-grade web application tailored for college students preparing for exams. It executes one streamlined workflow:
1. Student uploads a lecture PDF (via drag-and-drop or file picker) with an optional course/subject name.
2. The server extracts the text using `pypdf` and validates the document structure.
3. The server sends the text to the Google Gemini API with strict grounding instructions prohibiting external hallucinations or invented facts.
4. The notes are rendered into 6 exam-ready study sections with instant actions:
   - **Lecture Overview**
   - **Main Topics and Subtopics**
   - **Important Concepts and Definitions**
   - **Key Points as Concise Bullets**
   - **Important Formulas or Facts** *(only if explicitly present in the source)*
   - **Quick Revision (Top Takeaways)**
5. Students can download notes as Markdown (`.md`), print/save as clean study PDF, copy to clipboard, or start over with a new PDF.

---

## 🔑 How to Set `GEMINI_API_KEY` (Exact Steps)

StudyFlow runs the Gemini API strictly server-side. Your API key is **never** exposed in client bundles or network responses.

### Step 1: Get an API Key
1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Sign in with your Google account.
3. Click **Get API Key** and create or select a project.
4. Copy your key (starts with `AIzaSy...`).

### Step 2: Configure the Key

#### Option A: Using a `.env` file (Recommended)
In the project root folder (`f:\Python`), copy `.env.example` to `.env`:
```powershell
Copy-Item .env.example .env
```
Open `.env` and replace the placeholder with your actual key:
```ini
GEMINI_API_KEY=AIzaSyYourActualApiKeyHere
```

#### Option B: Using PowerShell Environment Variable
Before running the server in your terminal:
```powershell
$env:GEMINI_API_KEY="AIzaSyYourActualApiKeyHere"
```

> [!NOTE]
> If `GEMINI_API_KEY` is not set, StudyFlow fails fast with a clear, user-friendly setup prompt in both the UI and API responses (`HTTP 503`).

---

## 🚀 Installation & Running the App

### Prerequisites
- Python 3.10+ (tested with Python 3.13)
- Windows / macOS / Linux

### 1. Initialize Virtual Environment & Install Dependencies

```powershell
# Create virtual environment
py -3.13 -m venv .venv

# Activate virtual environment (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt
```

### 2. Start the StudyFlow Server

```powershell
# Using the virtual environment's uvicorn
.\.venv\Scripts\uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

### 3. Open StudyFlow in Your Browser
Navigate to:
```
http://127.0.0.1:8000
```

---

## 🧪 Testing & Verification

StudyFlow has been verified across key automated and manual test paths:

| Test Case | Description | Result |
| :--- | :--- | :--- |
| **PDF Text Extraction** | Multi-page lecture PDFs are parsed with clean page markers using `pypdf`. | ✅ Passed |
| **Empty / Scanned PDF Validation** | Image-only scans without text or empty files return user-friendly `HTTP 422`. | ✅ Passed |
| **Missing API Key Handling** | Backend fails fast with `HTTP 503` and setup instructions; UI displays warning banner. | ✅ Passed |
| **Zero Key Leakage** | API key is never serialized into `/api/health`, `/api/generate-notes`, or frontend code. | ✅ Passed |
| **Grounding Enforcement** | Gemini prompt strictly forbids external knowledge; non-existent formulas are flagged as absent. | ✅ Passed |
| **Export Actions** | Markdown file download, Clipboard copy, and browser Print-to-PDF formatting. | ✅ Passed |

---

## ⚠️ Known Limitations

1. **Scanned Image-Only PDFs**: PDFs containing only raster images without embedded OCR text cannot be extracted by standard PDF text parsers. The app detects this and prompts the user to provide a text-based lecture document.
2. **Password-Protected PDFs**: Encrypted documents require an unlock password before text can be read. The app detects encrypted files and requests an unlocked PDF.
3. **Massive Multi-Hundred-Page Textbooks**: While Gemini has a 1M+ token context window, single upload payloads are bounded to 30 MB to ensure smooth processing times for lecture slide decks.
