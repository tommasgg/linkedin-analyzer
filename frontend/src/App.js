import React, { useState } from 'react';
import './App.css';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

function App() {
  const [url, setUrl] = useState('');
  const [analysis, setAnalysis] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    
    try {
      const response = await fetch(`${API_URL}/analyze`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url }),
      });
      
      const data = await response.json();
      
      if (data.error) {
        setError(data.error);
      } else {
        setAnalysis(data);
      }
    } catch (err) {
      setError('Failed to analyze LinkedIn profile');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>LinkedIn Profile Analyzer</h1>
        <form onSubmit={handleSubmit} className="url-form">
          <input
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Enter LinkedIn profile URL"
            required
          />
          <button type="submit" disabled={loading}>
            {loading ? 'Analyzing...' : 'Analyze'}
          </button>
        </form>
        
        {error && <div className="error">{error}</div>}
        
        {analysis && (
          <div className="analysis-results">
            <h2>Profile Analysis</h2>
            <div className="profile-info">
              <h3>{analysis.name}</h3>
              <p className="headline">{analysis.headline}</p>
              {analysis.about && <p className="about">{analysis.about}</p>}
            </div>
            
            {analysis.experience && analysis.experience.length > 0 && (
              <div className="experience">
                <h3>Experience</h3>
                {analysis.experience.map((exp, index) => (
                  <div key={index} className="experience-item">
                    <h4>{exp.title}</h4>
                    <p className="company">{exp.company}</p>
                    {exp.duration && <p className="duration">{exp.duration}</p>}
                  </div>
                ))}
              </div>
            )}
          </div>
        )}
      </header>
    </div>
  );
}

export default App; 