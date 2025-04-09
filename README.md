# LinkedIn Profile Analyzer

A web application that helps users analyze LinkedIn profiles through their LinkedIn URLs.

## Features

- Input a LinkedIn profile URL
- Extract and display profile information including:
  - Name
  - Headline
  - About section
  - Work experience

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask server:
   ```bash
   python app.py
   ```

The backend server will run on `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

The frontend will run on `http://localhost:3000`

## Usage

1. Open your browser and navigate to `http://localhost:3000`
2. Enter a LinkedIn profile URL in the input field
3. Click "Analyze" to view the profile information

## Note

This application uses web scraping to extract information from LinkedIn profiles. Please be aware that:
- LinkedIn's terms of service may restrict automated access
- The application may not work if LinkedIn changes their HTML structure
- Some profile information might not be accessible if the profile is private

## Technologies Used

- Backend: Python, Flask, BeautifulSoup4
- Frontend: React.js
- Styling: CSS 