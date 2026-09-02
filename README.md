# Instagram Analytics & Insight Generation

An AI-powered web application designed to discover publicly available Instagram content based on a product or topic, process the collected data, and group related posts into meaningful clusters.

The current implementation focuses on the complete workflow up to **Instagram post collection, data processing, and machine-learning-based clustering**. Future enhancements will extend the system with AI-generated insights, semantic clustering, advanced analytics, authentication, database support, history, filtering, and other intelligent features.

---

## Project Overview

Social media platforms contain large amounts of content related to products, brands, events, people, and topics. Manually reviewing this content to identify common themes can be time-consuming.

This project aims to automate that process.

A user can search for a product or topic such as:

- Argentina Jersey
- Messi Jersey
- Nike Shoes
- Football Boots
- Travel
- Wildlife

The system discovers publicly available Instagram posts related to the search term, collects available post information, processes the data, and groups similar posts into clusters.

### Example

User searches:

```text
Argentina Jersey
```

The system may discover posts related to:

```text
Argentina National Team Jersey
Messi Argentina Jersey
Argentina Football Shirt
Argentina Home Kit
Football Jersey Collection
```

The collected posts are then processed and grouped into related content clusters.

Example:

```text
Cluster 1 → Argentina National Team
Cluster 2 → Messi Jersey
Cluster 3 → Football Merchandise
```

The current project milestone ends at this clustering stage.

---

# Current Implementation

The project has currently been implemented up to the **content clustering stage**.

The completed workflow is:

```text
User enters Product / Topic
          ↓
Keyword Search
          ↓
SERP API
          ↓
Instagram Post URLs
          ↓
Instagram Data Collection
          ↓
Data Cleaning
          ↓
Text Processing
          ↓
TF-IDF
          ↓
K-Means Clustering
          ↓
Related Instagram Post Clusters
```

The AI insight generation and advanced analytics stages are planned as future enhancements.

---

# Features Implemented

## 1. Product / Topic Search

The application accepts a product or topic keyword from the user.

Examples:

```text
Argentina Jersey
Messi Jersey
Nike Shoes
Football Boots
```

The keyword is used to discover relevant publicly indexed Instagram posts.

---

## 2. Instagram Post Discovery

The system uses the Bright Data SERP API to search for Instagram posts related to the entered keyword.

A search query is constructed around Instagram post URLs.

Example:

```text
site:instagram.com/p/ "Argentina Jersey"
```

The search results are processed to extract Instagram post URLs.

### Workflow

```text
Search Keyword
      ↓
Bright Data SERP API
      ↓
Google Search Results
      ↓
Instagram Results
      ↓
Instagram Post URLs
```

---

## 3. Instagram Data Collection

The discovered Instagram post URLs are passed to Bright Data's Instagram data collection service.

The service is used to retrieve available information associated with the public Instagram posts.

Depending on the returned data, available fields can include:

- Post ID
- Username
- Caption
- Content type
- Date
- Hashtags
- Image URL
- Instagram post URL

The system is designed to handle cases where some fields are unavailable.

---

## 4. Data Cleaning and Normalization

The collected data is cleaned before being passed to the machine learning pipeline.

The application converts different possible field names into a common internal structure.

The normalized post structure contains fields such as:

```text
id
username
caption
content_type
date
hashtags
image_url
post_url
```

This creates a consistent format for downstream processing.

---

## 5. Text Processing

Available textual information is used to represent each Instagram post.

The primary sources of text are:

```text
Caption
Hashtags
```

Additional text fields can also be considered when available.

Example:

```text
Caption:
New Messi Argentina jersey available now

Hashtags:
#Messi #Argentina #Jersey
```

The text is combined into a representation that can be processed by the clustering algorithm.

---

# 6. TF-IDF Based Feature Extraction

The current clustering implementation uses **TF-IDF (Term Frequency-Inverse Document Frequency)**.

TF-IDF converts the textual content of Instagram posts into numerical vectors.

The technique gives higher importance to words that are useful for distinguishing one post from another.

### Processing Flow

```text
Instagram Post
      ↓
Caption + Hashtags
      ↓
Text Representation
      ↓
TF-IDF Vectorization
      ↓
Numerical Feature Vector
```

These vectors are then used as input to the clustering algorithm.

---

# 7. K-Means Clustering

The current project uses **K-Means clustering** from Scikit-learn.

K-Means groups posts with similar text representations into clusters.

### Example

Suppose the system receives:

```text
Post 1:
Argentina football jersey Messi

Post 2:
Argentina national team jersey

Post 3:
Messi Argentina shirt collection

Post 4:
Nike running shoes for training

Post 5:
Best Nike shoes for athletes
```

The algorithm can identify groups such as:

```text
Cluster 1
Argentina Football / Messi Jersey

Cluster 2
Nike Running Shoes
```

The number of requested clusters can be configured.

---

## Dynamic Cluster Handling

The clustering service also handles cases where the requested number of clusters is not appropriate for the available data.

For example, if five posts contain almost identical text representations, forcing three different clusters would not produce meaningful results.

The system therefore checks the available data before applying K-Means and can reduce the effective number of clusters when necessary.

This prevents unnecessary clustering warnings and avoids creating artificial groups from identical or insufficient data.

---

# Current System Architecture

The current implemented architecture is:

```text
                         USER
                           |
                           v
                   React Frontend
                           |
                           v
                    Flask Backend
                           |
                           v
                    Keyword Search
                           |
                           v
                 Bright Data SERP API
                           |
                           v
                Instagram Post URLs
                           |
                           v
             Bright Data Data Collection
                           |
                           v
                    Data Cleaning
                           |
                           v
                  Text Processing
                           |
                           v
                       TF-IDF
                           |
                           v
                  K-Means Clustering
                           |
                           v
               Related Post Clusters
```

---

# Technology Stack

## Frontend

- React
- JavaScript
- React Router
- Vite
- HTML
- CSS

## Backend

- Python
- Flask
- Flask-CORS
- REST API

## Data Collection

- Bright Data SERP API
- Bright Data Instagram data collection

## Machine Learning

- Scikit-learn
- TF-IDF
- K-Means

## Development Tools

- Python Virtual Environment
- Node.js
- npm
- Git
- GitHub
- Visual Studio Code

---

# Project Structure

```text
instagram-project/
│
├── backend/
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── db.py
│   │   └── ...
│   │
│   ├── models/
│   │   └── ...
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── insights.py
│   │   └── instagram.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── clustering_service.py
│   │   ├── insight_service.py
│   │   ├── instagram_keyword_service.py
│   │   ├── instagram_search.py
│   │   ├── instagram_service.py
│   │   └── keyword_pipeline.py
│   │
│   ├── .env
│   ├── .env.example
│   ├── app.py
│   └── requirements.txt
│
├── public/
│
├── src/
│   │
│   ├── components/
│   ├── hooks/
│   ├── layouts/
│   ├── pages/
│   ├── services/
│   ├── App.jsx
│   ├── index.css
│   └── main.jsx
│
├── .gitignore
├── eslint.config.js
├── index.html
├── package.json
├── package-lock.json
├── vite.config.js
└── README.md
```

---

# Backend API

## Health Check

```text
GET /health
```

Used to verify that the Flask backend is running.

Example:

```text
http://127.0.0.1:5000/health
```

Expected response:

```json
{
    "status": "healthy"
}
```

---

# Keyword Analysis Endpoint

```text
GET /api/insights/search
```

### Parameters

```text
keyword
clusters
```

### Example

```text
http://127.0.0.1:5000/api/insights/search?keyword=Argentina%20Jersey&clusters=3
```

The endpoint performs the implemented keyword analysis workflow:

```text
Keyword
   ↓
SERP API
   ↓
Instagram URLs
   ↓
Bright Data
   ↓
Post Collection
   ↓
Data Cleaning
   ↓
TF-IDF
   ↓
K-Means
   ↓
Clusters
```

---

# Example Clustering Result

A clustering response can contain information similar to:

```json
{
    "success": true,
    "keyword": "Argentina Jersey",
    "total_posts": 5,
    "total_clusters": 3,
    "clusters": [
        {
            "cluster_id": 0,
            "cluster_name": "Cluster 1",
            "post_count": 2,
            "posts": []
        },
        {
            "cluster_id": 1,
            "cluster_name": "Cluster 2",
            "post_count": 2,
            "posts": []
        },
        {
            "cluster_id": 2,
            "cluster_name": "Cluster 3",
            "post_count": 1,
            "posts": []
        }
    ]
}
```

The exact number and composition of clusters depend on the available Instagram data and the selected number of clusters.

---

# How the Current System Works

## Step 1: User Input

The user enters a product or topic.

Example:

```text
Argentina Jersey
```

## Step 2: Keyword Search

The keyword is passed to the SERP API to discover relevant Instagram posts.

```text
Argentina Jersey
        ↓
SERP API
        ↓
Instagram Search Results
```

## Step 3: URL Extraction

Relevant Instagram post URLs are extracted from the search results.

```text
Instagram Search Results
        ↓
Instagram Post URLs
```

## Step 4: Instagram Data Collection

The discovered URLs are submitted to the Instagram data collection service.

```text
Instagram Post URLs
        ↓
Bright Data
        ↓
Available Post Information
```

## Step 5: Data Cleaning

The returned information is normalized into a consistent structure.

```text
Raw Data
   ↓
Cleaning
   ↓
Normalized Post Data
```

## Step 6: Text Representation

Available captions and hashtags are combined to create text representations.

```text
Caption + Hashtags
        ↓
Post Text
```

## Step 7: TF-IDF

The text is converted into numerical feature vectors.

```text
Post Text
    ↓
TF-IDF
    ↓
Numerical Vectors
```

## Step 8: K-Means

The numerical vectors are grouped using K-Means.

```text
Numerical Vectors
        ↓
    K-Means
        ↓
Related Post Clusters
```

---

# Installation

## Prerequisites

Install the following:

- Python 3.13+
- Node.js
- npm
- Git

---

# Backend Setup

Navigate to the backend directory:

```powershell
cd backend
```

Create a virtual environment:

```powershell
py -3.13 -m venv venv
```

Activate the environment on Windows:

```powershell
.env\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

---

# Environment Variables

Create:

```text
backend/.env
```

Add the required credentials:

```env
BRIGHTDATA_API_KEY=your_brightdata_api_key
BRIGHTDATA_SERP_ZONE=your_brightdata_serp_zone
OPENAI_API_KEY=your_openai_api_key
```

The OpenAI key is included for the AI functionality planned in the next development stage.

Do not commit the real `.env` file to GitHub.

Use `.env.example` as the safe template:

```env
BRIGHTDATA_API_KEY=your_brightdata_api_key_here
BRIGHTDATA_SERP_ZONE=your_brightdata_serp_zone_here
OPENAI_API_KEY=your_openai_api_key_here
```

---

# Run the Backend

From the backend directory:

```powershell
python app.py
```

The Flask backend runs at:

```text
http://127.0.0.1:5000
```

---

# Frontend Setup

From the project root:

```powershell
npm install
```

Start the React development server:

```powershell
npm run dev
```

Vite will provide the frontend URL, usually:

```text
http://localhost:5173
```

---

# Running the Application

## Terminal 1 - Backend

```powershell
cd backend
.env\Scripts\Activate.ps1
python app.py
```

## Terminal 2 - Frontend

```powershell
npm run dev
```

Open the URL displayed by Vite.

---

# Testing

The project contains local development tests for validating individual components.

Examples include:

```text
backend/test_search.py
backend/test_collect_posts.py
backend/test_keyword_pipeline.py
backend/test_clustering.py
backend/test_clustering_openai.py
backend/test_openai.py
```

These files are ignored by Git using:

```gitignore
backend/test_*.py
```

Local clustering tests can be executed without using Bright Data credits.

---

# Current Project Status

## Completed Milestone

The project is currently completed up to the **machine-learning-based clustering stage**.

### Completed

- React project setup
- Dashboard interface
- Flask backend
- REST API structure
- Product/topic keyword search
- Bright Data SERP API integration
- Instagram post URL discovery
- Bright Data Instagram data collection
- Post data cleaning
- Post normalization
- Text processing
- TF-IDF feature extraction
- K-Means clustering
- Dynamic cluster handling
- Frontend-backend communication
- Environment variable protection
- GitHub repository setup

### Current Working Pipeline

```text
Product / Topic
      ↓
Keyword Search
      ↓
SERP API
      ↓
Instagram Post URLs
      ↓
Bright Data
      ↓
Instagram Data
      ↓
Data Cleaning
      ↓
TF-IDF
      ↓
K-Means
      ↓
Content Clusters
```

The next stages will build AI-powered analysis and advanced analytics on top of these generated clusters.

---

# Future Enhancements

## 1. AI-Generated Cluster Insights

The next major enhancement is to pass each generated cluster to an OpenAI model.

Instead of analyzing every post independently, the complete cluster will be analyzed together.

```text
Cluster
   ↓
All Posts in Cluster
   ↓
OpenAI
   ↓
One Combined Insight
```

The AI will generate:

- Cluster summary
- Common themes
- Content patterns
- Audience interests
- Product/topic observations
- Content strategy recommendations

---

## 2. Semantic Embedding-Based Clustering

The current system uses TF-IDF, which mainly relies on word frequency.

A future version will use semantic embeddings to understand the meaning of posts.

Planned workflow:

```text
Caption + Hashtags
        ↓
Semantic Embeddings
        ↓
Similarity Calculation
        ↓
Semantic Clustering
```

This should improve grouping when posts are related in meaning but use different words.

---

## 3. Automatic Cluster Naming

Future versions will generate meaningful names for clusters instead of generic cluster identifiers.

Example:

```text
Cluster 1
      ↓
Argentina Football Jerseys

Cluster 2
      ↓
Messi Merchandise

Cluster 3
      ↓
Football Fan Content
```

---

## 4. Advanced AI Analysis

The AI layer can be expanded to provide:

- Major themes
- Audience interests
- Product perception
- Common messaging
- Content patterns
- Potential trends
- Recommendations
- Content opportunities

Example:

```text
Topic:
Argentina Jersey

Summary:
...

Common Themes:
...

Audience Interest:
...

Observed Pattern:
...

Recommendation:
...
```

---

## 5. Dedicated Clusters Page

A dedicated Clusters page can provide a complete view of all generated groups.

Planned information includes:

- Cluster name
- Number of posts
- AI-generated insight
- Representative posts
- Topic information
- Cluster statistics

---

## 6. Cluster Details Page

Users will be able to open an individual cluster and inspect all related posts.

Possible information:

- Cluster name
- Cluster insight
- All posts
- Captions
- Images
- Hashtags
- Dates
- Original Instagram URLs

---

## 7. Advanced Analytics Dashboard

The Analytics section can provide visual representations of the collected data.

Possible analytics include:

- Total posts analyzed
- Cluster distribution
- Content type distribution
- Top topics
- Posting frequency
- Topic frequency
- Cluster sizes
- Topic trends

---

## 8. Engagement Analysis

If engagement information becomes available from the collected data, the system can analyze:

- Likes
- Comments
- Views
- Average engagement
- Engagement by cluster
- Top-performing topics

This can help identify which content themes perform better.

---

## 9. Sentiment Analysis

A future NLP module can classify available post text as:

```text
Positive
Neutral
Negative
```

Sentiment can be analyzed at:

- Post level
- Cluster level
- Topic level

---

## 10. Trend Detection

The application can identify topics whose presence increases over time.

Example:

```text
Week 1 → Messi Jersey → 5 posts
Week 2 → Messi Jersey → 12 posts
Week 3 → Messi Jersey → 25 posts
```

This can be used to identify growing topics and emerging trends.

---

## 11. Search and Filtering

Future filtering options can include:

- Keyword search
- Cluster filter
- Content type filter
- Date filter
- Topic filter
- Relevance filter

---

## 12. Analysis History

Previous searches and analyses can be stored for later comparison.

Example:

```text
Argentina Jersey
5 Posts
3 Clusters
September 2026

Nike Shoes
10 Posts
3 Clusters
September 2026
```

Users can revisit previous results without repeating the complete analysis process.

---

## 13. Database Integration

A database can be introduced to store:

- Users
- Search keywords
- Instagram posts
- Clusters
- AI insights
- Analysis results
- Analysis history

SQLite can be used initially, with PostgreSQL as a possible production database.

---

## 14. User Authentication

The application can be expanded with a complete authentication system.

Possible functionality:

- User registration
- Login
- Password authentication
- JWT authentication
- Protected routes
- User-specific analysis history

---

## 15. Settings

The Settings page can allow users to configure:

- Number of posts to collect
- Number of clusters
- AI analysis options
- Search preferences
- Date ranges
- Filtering preferences

---

## 16. Multi-Topic Comparison

Future versions can compare multiple products or topics.

Example:

```text
Argentina Jersey
        VS
Brazil Jersey
        VS
France Jersey
```

The system could compare:

- Number of posts
- Cluster distribution
- Content patterns
- Engagement
- Sentiment
- AI-generated observations

---

## 17. Multi-Profile Analysis

Future versions can support analysis across multiple public Instagram profiles or sources.

This can allow comparisons between different accounts and their content patterns.

---

## 18. Improved User Interface

Future UI improvements can include:

- Responsive design
- Improved dashboard layout
- Interactive charts
- Better cluster cards
- Search suggestions
- Loading indicators
- Improved empty states
- Better error messages
- Mobile support
- Improved navigation

---

## 19. Performance and Backend Improvements

Future backend improvements can include:

- Asynchronous processing
- Background jobs
- Caching
- API rate-limit handling
- Request optimization
- Better error recovery
- Duplicate-result prevention
- Result caching

These improvements can make the system more efficient for larger workloads.

---

## 20. Production Deployment

After the application is fully developed, it can be deployed using cloud infrastructure.

Possible deployment architecture:

```text
User
 ↓
Cloud Frontend
 ↓
Cloud Backend API
 ↓
Data Collection Service
 ↓
Machine Learning Pipeline
 ↓
AI Service
 ↓
Database
```

Production improvements can include:

- Secure environment variables
- Cloud database
- Logging
- Monitoring
- Error tracking
- Production API configuration

---

# Future Architecture

The planned final architecture is:

```text
                         USER
                           |
                           v
                    React Frontend
                           |
                           v
                    Flask REST API
                           |
                           v
                    Keyword Search
                           |
                           v
                 Bright Data SERP API
                           |
                           v
                 Instagram Post URLs
                           |
                           v
                Instagram Data Collection
                           |
                           v
                    Data Cleaning
                           |
                           v
               Semantic Embeddings
                           |
                           v
                     Clustering
                           |
                           v
                  Clustered Content
                           |
                           v
                         OpenAI
                           |
                           v
                AI Cluster Insights
                           |
                           v
                    Analytics Layer
                           |
              +------------+------------+
              |            |            |
              v            v            v
          Clusters     Analytics     History
                           |
                           v
                       Database
                           |
                           v
                  React Dashboard
```

---

# Limitations

The system works with publicly available Instagram data obtained through external data collection services.

The application does not guarantee access to:

- Every Instagram post
- Private Instagram content
- Every historical post
- Every available post field

The available data depends on:

- Search engine indexing
- Instagram availability
- Profile visibility
- External data collection capabilities
- API limitations
- Available post metadata
- Network conditions

Some posts may contain limited textual information, which can affect clustering quality.

---

# Responsible Use

This project is intended for:

- Educational purposes
- Internship project demonstration
- Social media content analysis
- Research
- Machine learning experimentation
- AI experimentation

Users should respect:

- Instagram's applicable terms and policies
- Bright Data's applicable terms and policies
- Data privacy requirements
- Applicable laws and regulations

Only publicly accessible content should be considered for analysis.

---

# Security

API credentials are stored in environment variables.

The following file should never be committed:

```text
.env
```

The `.gitignore` file protects environment variables, virtual environments, test files, and other local development files.

API keys should never be placed directly inside:

- React components
- Python source files
- README files
- GitHub repositories
- Screenshots
- Public documentation

If an API key is exposed, it should be revoked and replaced immediately.

---

# Project Roadmap

```text
Phase 1
Keyword Search
        ✓

Phase 2
Instagram URL Discovery
        ✓

Phase 3
Instagram Data Collection
        ✓

Phase 4
Data Cleaning
        ✓

Phase 5
TF-IDF Processing
        ✓

Phase 6
K-Means Clustering
        ✓

Phase 7
AI Cluster Insights
        Planned

Phase 8
Semantic Clustering
        Planned

Phase 9
Automatic Cluster Naming
        Planned

Phase 10
Advanced Analytics
        Planned

Phase 11
Sentiment & Trend Analysis
        Planned

Phase 12
Analysis History
        Planned

Phase 13
Database Integration
        Planned

Phase 14
Authentication
        Planned

Phase 15
Advanced Filtering
        Planned

Phase 16
Multi-Topic / Multi-Profile Comparison
        Planned

Phase 17
Production Deployment
        Planned
```

---

# Project Goal

The long-term goal is to build an intelligent Instagram content analytics platform that transforms large amounts of publicly available social media content into structured information and actionable insights.

The intended evolution is:

```text
Large Amount of Instagram Content
              ↓
          Data Collection
              ↓
          Data Processing
              ↓
        Content Clustering
              ↓
       Semantic Understanding
              ↓
         AI Analysis
              ↓
       Advanced Analytics
              ↓
      Actionable Insights
```

The current implementation establishes the foundation by completing the data collection, processing, and clustering pipeline. Future enhancements will build an intelligent analysis layer on top of these clusters.

---

# Author

**Bhargav**

This project is developed as an internship project focused on:

- Python development
- React development
- REST API development
- Data collection
- Natural Language Processing
- Machine Learning
- AI-powered analytics

---

# License

This project is intended primarily for educational, internship, and demonstration purposes.
