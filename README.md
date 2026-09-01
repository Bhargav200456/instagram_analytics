# Instagram Analytics & Insight Generation

An AI-powered web application that collects publicly available Instagram posts, groups related posts into meaningful clusters, and generates a combined AI insight for each cluster.

The project is currently under development. The core data collection, clustering, AI insight generation, and dashboard integration are working, while additional features such as improved semantic clustering, analytics, history, and advanced filtering are planned.

---

## Project Overview

The main goal of this project is to simplify the analysis of Instagram content.

Instead of manually going through hundreds of Instagram posts, the system collects posts from a public Instagram profile and automatically identifies groups of related content.

For example:

Instagram Posts:

- Messi Argentina Jersey
- New Messi Jersey
- Argentina Home Kit
- Messi Football Shirt
- Messi Jersey Collection

The system can group these posts into:

    Messi Jersey

The AI then analyzes all posts in that cluster and generates ONE combined insight.

Example:

    The cluster shows strong interest in Messi-associated
    Argentina merchandise, with recurring emphasis on new
    kit releases and player branding.

---

## Main Features

### 1. Instagram Post Collection

The application uses Bright Data to collect publicly available Instagram post information from a selected profile.

The collected information includes fields such as:

- Post ID
- Username
- Caption
- Content type
- Date
- Hashtags
- Image URL
- Instagram post URL

---

### 2. Automatic Post Clustering

The collected posts are grouped into clusters based on their content.

The current prototype uses:

- TF-IDF
- K-Means clustering

This allows related posts to be grouped together automatically.

Semantic embedding-based clustering is planned as a future improvement.

---

### 3. Cluster-Level AI Insights

OpenAI is used to analyze the complete group of posts belonging to a cluster.

The system generates:

- One insight per cluster
- A summary of the common theme
- Common content patterns
- Possible audience interests
- Content strategy observations

The AI does NOT generate a separate insight for every post.

Instead:

    Multiple related posts
            ↓
        One Cluster
            ↓
          OpenAI
            ↓
      One Combined Insight

---

### 4. Interactive Dashboard

The React dashboard allows users to enter an Instagram username and start an analysis.

The dashboard displays:

- Instagram username
- Number of posts analyzed
- Number of clusters
- Cluster names
- Number of posts in each cluster
- AI-generated insights
- Posts belonging to each cluster
- Post images and captions

---

## Current System Architecture

    User
      |
      v
    React Frontend
      |
      v
    Flask Backend
      |
      +-------------------+
      |                   |
      v                   v
    Bright Data        OpenAI
      |                   |
      v                   |
    Instagram Posts       |
      |                   |
      v                   |
    Post Cleaning         |
      |                   |
      v                   |
    Clustering -----------+
      |
      v
    Cluster-Level Insights
      |
      v
    React Dashboard

---

## Technology Stack

### Frontend

- React
- JavaScript
- React Router
- Vite
- Inline CSS

### Backend

- Python
- Flask
- Flask-CORS
- REST API

### Data Collection

- Bright Data Instagram data collection API

### Machine Learning

- Scikit-learn
- TF-IDF
- K-Means clustering

### Artificial Intelligence

- OpenAI API
- OpenAI embeddings and language models are planned for improved semantic clustering and insights

### Environment

- Python Virtual Environment
- Node.js
- npm
- Git
- GitHub

---

## Project Structure

    instagram-project/
    |
    ├── backend/
    │   |
    │   ├── routes/
    │   │   ├── __init__.py
    │   │   ├── instagram.py
    │   │   ├── insights.py
    │   │   └── auth.py
    │   │
    │   ├── services/
    │   │   ├── __init__.py
    │   │   ├── instagram_service.py
    │   │   ├── clustering_service.py
    │   │   └── insight_service.py
    │   │
    │   ├── .env
    │   ├── .env.example
    │   ├── app.py
    │   └── requirements.txt
    │
    ├── public/
    │
    ├── src/
    │   |
    │   ├── components/
    │   ├── hooks/
    │   ├── layouts/
    │   ├── pages/
    │   ├── services/
    │   └── ...
    │
    ├── .gitignore
    ├── index.html
    ├── package.json
    ├── package-lock.json
    ├── vite.config.js
    └── README.md

---

## Backend API

### Health Check

    GET /health

Used to verify that the Flask backend is running.

Example:

    http://127.0.0.1:5000/health

---

### Get Instagram Posts

    GET /api/instagram/posts

Parameters:

    username

Example:

    http://127.0.0.1:5000/api/instagram/posts?username=natgeo

The endpoint collects publicly available Instagram posts through Bright Data and returns cleaned post information.

---

### Generate Clusters

    GET /api/instagram/cluster

Parameters:

    username
    clusters

Example:

    http://127.0.0.1:5000/api/instagram/cluster?username=natgeo&clusters=3

This endpoint:

1. Collects Instagram posts
2. Cleans the post data
3. Creates text representations
4. Applies clustering
5. Returns the generated clusters

---

### Generate AI Insights

    GET /api/insights/generate

Parameters:

    username
    clusters

Example:

    http://127.0.0.1:5000/api/insights/generate?username=natgeo&clusters=3

This endpoint performs the complete analysis:

    Instagram Profile
          ↓
    Bright Data
          ↓
    Posts
          ↓
    Clustering
          ↓
    Cluster 1
    Cluster 2
    Cluster 3
          ↓
    OpenAI
          ↓
    One insight per cluster

---

## Example Output

A successful analysis returns information similar to:

    {
        "success": true,
        "username": "natgeo",
        "total_posts": 12,
        "total_clusters": 3,
        "clusters": [
            {
                "cluster_id": 0,
                "cluster_name": "Wildlife Content",
                "post_count": 4,
                "insight": "The cluster focuses on..."
            },
            {
                "cluster_id": 1,
                "cluster_name": "Space Exploration",
                "post_count": 5,
                "insight": "The cluster centers around..."
            }
        ]
    }

---

## How Clustering Works

### Current Approach

The current prototype uses TF-IDF and K-Means.

### Step 1: Collect Posts

Instagram posts are collected using Bright Data.

### Step 2: Combine Text

The caption and hashtags of each post are combined.

Example:

    Caption:
    New Messi Argentina jersey available now

    Hashtags:
    #Messi #Argentina #Jersey

The combined text becomes the input for clustering.

### Step 3: TF-IDF

TF-IDF converts text into numerical vectors based on the importance of words within the collected posts.

### Step 4: K-Means

K-Means groups similar vectors into a specified number of clusters.

Example:

    Posts
      |
      +---- Cluster 1
      |      Messi Jersey
      |
      +---- Cluster 2
      |      Football Boots
      |
      +---- Cluster 3
             Football News

---

## How AI Insights Work

The AI insight generation happens at the cluster level.

For example:

    Cluster: Messi Jersey

    Post 1:
    Messi Argentina jersey

    Post 2:
    New Argentina kit

    Post 3:
    Messi football shirt

    Post 4:
    Argentina home jersey

All four posts are provided to the AI together.

The AI generates:

    One combined insight

This prevents the system from generating repetitive insights for every individual post.

---

## Frontend Workflow

The current dashboard follows this workflow:

    Login
      ↓
    Dashboard
      ↓
    Enter Instagram Username
      ↓
    Analyze Profile
      ↓
    Backend API
      ↓
    Bright Data
      ↓
    Clustering
      ↓
    OpenAI
      ↓
    Display Results

---

## Installation

### Prerequisites

Make sure the following are installed:

- Python 3.13+
- Node.js
- npm
- Git

---

## Backend Setup

Navigate to the backend:

    cd backend

Create a virtual environment:

    py -3.13 -m venv venv

Activate the virtual environment on Windows:

    .\venv\Scripts\Activate.ps1

Install dependencies:

    pip install -r requirements.txt

---

## Environment Variables

Create a file:

    backend/.env

Add:

    BRIGHTDATA_API_KEY=your_brightdata_api_key
    OPENAI_API_KEY=your_openai_api_key

Do NOT upload the real `.env` file to GitHub.

A safe example file is provided as:

    backend/.env.example

Example:

    BRIGHTDATA_API_KEY=your_brightdata_api_key_here
    OPENAI_API_KEY=your_openai_api_key_here

---

## Run the Backend

From the backend directory:

    python app.py

The backend will run on:

    http://127.0.0.1:5000

---

## Frontend Setup

Open another terminal and navigate to the project root.

Install dependencies:

    npm install

Start the React development server:

    npm run dev

Vite will provide the local frontend URL, usually:

    http://localhost:5173

---

## Running the Complete Application

Two terminals are required.

### Terminal 1 - Backend

    cd backend
    .\venv\Scripts\Activate.ps1
    python app.py

### Terminal 2 - Frontend

    npm run dev

Then open the frontend URL shown by Vite.

---

## Example Analysis

For example, enter:

    natgeo

and click:

    Analyze Profile

The application will:

1. Send the username to the Flask backend.
2. Request publicly available Instagram data from Bright Data.
3. Retrieve the posts.
4. Clean the post information.
5. Group posts into clusters.
6. Send each cluster to OpenAI.
7. Generate one insight for each cluster.
8. Display the results on the React dashboard.

---

## Security

API keys are stored in environment variables.

The following files should NOT be committed to GitHub:

    .env

The `.gitignore` file contains rules for environment files and other local development files.

API keys should never be placed directly inside:

- React components
- Python source files
- README files
- GitHub repositories
- Screenshots

---

## Current Project Status

The project is currently in the development/prototype stage.

### Completed

- React frontend
- Dashboard
- Navigation
- Flask backend
- Bright Data integration
- Instagram post collection
- Post cleaning
- TF-IDF based text processing
- K-Means clustering
- OpenAI integration
- Cluster-level AI insight generation
- Frontend and backend integration
- GitHub repository setup
- Environment variable protection

### Currently Working

The complete workflow is functional:

    Instagram Profile
          ↓
    Bright Data
          ↓
    Instagram Posts
          ↓
    Clustering
          ↓
    AI Insight
          ↓
    Dashboard

---

# Development Roadmap

The following features are planned for the next stages of development.

## Phase 1 - Improve Semantic Clustering

Replace or improve the current TF-IDF approach with semantic embeddings.

Current:

    Caption
      ↓
    TF-IDF
      ↓
    K-Means

Planned:

    Caption + Hashtags
          ↓
    Semantic Embeddings
          ↓
    Similarity
          ↓
    Clustering

This should improve the ability to group posts based on meaning rather than only shared words.

---

## Phase 2 - Improve Cluster Naming

The current cluster names are generated from the cluster content.

The planned system will generate clearer topic names such as:

    Messi Jersey
    Football Merchandise
    Wildlife Conservation
    Space Exploration
    Travel Content

---

## Phase 3 - Advanced AI Insights

The insight system will be expanded to provide:

- Cluster summary
- Common themes
- Audience interest
- Content patterns
- Content recommendations
- Potential trends

Example:

    Topic:
    Messi Jersey

    Posts Analyzed:
    18

    Summary:
    ...

    Common Themes:
    ...

    Audience Interest:
    ...

    Recommendation:
    ...

---

## Phase 4 - Dedicated Clusters Page

Create a dedicated page for viewing all generated clusters.

The page will show:

- Cluster name
- Number of posts
- AI insight
- Post previews
- Cluster details

---

## Phase 5 - Cluster Details

Users will be able to open a cluster and view:

- Complete cluster insight
- All posts in the cluster
- Images
- Captions
- Dates
- Original Instagram links

---

## Phase 6 - Profile Page

The profile page will display:

- Instagram username
- Account information
- Posts analyzed
- Last analysis
- Connection status
- Re-analysis option

---

## Phase 7 - Authentication

The current login interface will be improved into a proper authentication system.

Possible future implementation:

- User accounts
- Password authentication
- JWT authentication
- Protected dashboard routes

---

## Phase 8 - Settings

The settings page can allow users to configure:

- Number of clusters
- Number of posts to analyze
- AI insight settings
- Analysis preferences

---

## Phase 9 - Analysis History

Store previous analyses so users can compare results.

Example:

    @natgeo
    12 Posts
    3 Clusters
    September 2026

    @nike
    30 Posts
    5 Clusters
    September 2026

Users will be able to open previous analyses without running the scraper again.

---

## Phase 10 - Database

A database will be introduced to persist:

- Users
- Instagram profiles
- Posts
- Clusters
- AI insights
- Analysis history

SQLite can be used initially, with PostgreSQL as a possible future production database.

---

## Phase 11 - Analytics

Analytics will be added after the core clustering and insight workflow is stable.

Possible analytics include:

- Total posts
- Cluster distribution
- Content type distribution
- Posting frequency
- Top topics
- Engagement analysis
- Cluster growth
- Content trends

Charts and visualizations will be added to the Analytics page.

---

## Phase 12 - Engagement Analysis

If engagement information is available from the collected data, the system can analyze:

- Likes
- Comments
- Views
- Average engagement
- Engagement by cluster

Example:

    Wildlife
    35% of posts
    52% of engagement

This can help identify which content topics perform better.

---

## Phase 13 - Search and Filtering

Future filtering options:

- Search by keyword
- Filter by cluster
- Filter by content type
- Filter by date
- Search specific topics

---

## Phase 14 - UI Improvements

The final UI will include:

- Responsive design
- Better cards
- Improved navigation
- Loading states
- Error handling
- Empty states
- Improved typography
- Better spacing
- Interactive components

---

## Future Architecture

The planned final architecture is:

    User
      |
      v
    React Frontend
      |
      v
    Flask REST API
      |
      +-------------------+
      |                   |
      v                   v
    Bright Data        Database
      |                   |
      v                   |
    Instagram Posts       |
      |                   |
      v                   |
    Data Cleaning         |
      |                   |
      v                   |
    Semantic Embeddings   |
      |                   |
      v                   |
    Clustering -----------+
      |
      v
    Clustered Posts
      |
      v
    OpenAI
      |
      v
    Cluster-Level Insights
      |
      v
    React Dashboard
      |
      +---- Clusters
      |
      +---- Profile
      |
      +---- History
      |
      +---- Analytics
      |
      +---- Settings

---

## Limitations

This project works with publicly available Instagram data through the selected Bright Data data collection service.

The application should not be described as guaranteeing access to every historical Instagram post from every profile.

The available data depends on:

- Profile visibility
- Instagram availability
- Bright Data scraper capabilities
- Available post fields
- API limitations

The project is intended to analyze publicly accessible content.

---

## Responsible Use

This project is intended for:

- Educational purposes
- Internship/project demonstration
- Social media content analysis
- Research and experimentation

Users should respect Instagram's terms, applicable laws, and the terms of the data collection service being used.

---

## Future Improvements

Possible future improvements include:

- Better semantic clustering
- Automated topic detection
- Sentiment analysis
- Trend detection
- Engagement prediction
- Advanced recommendation generation
- Historical comparison
- Real-time analysis
- Multi-profile comparison
- More detailed analytics
- Improved visualization
- Production database
- User authentication

---

## Project Goal

The long-term goal is to create a platform that turns large amounts of Instagram content into understandable, actionable insights.

Instead of manually reviewing hundreds of posts:

    Hundreds of Instagram Posts
              ↓
        Automatic Analysis
              ↓
        Related Content
              ↓
           Clusters
              ↓
        AI Analysis
              ↓
       Actionable Insights

This allows users to understand the major topics, content patterns, and audience interests present in an Instagram profile.

---

## Development Status

Status: In Development

Current milestone:

    Data Collection
        ✓

    Post Processing
        ✓

    Basic Clustering
        ✓

    Cluster-Level AI Insights
        ✓

    React Dashboard Integration
        ✓

    Semantic Clustering
        Planned

    Advanced Analytics
        Planned

    Analysis History
        Planned

    Database
        Planned

---

## Author

Bhargav

This project is being developed as part of an internship project focused on Python development, AI, data processing, and web application development.

---

## License

This project is currently intended for educational and internship purposes.