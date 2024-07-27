# Reddit Sentiment Analysis Tool (FOR PERSONAL USAGE AND REFERENCE FOR FUTURE PROJECTS)

## Table of Contents

1. [Overview](#overview)
2. [Technologies](#technologies)
3. [Project Setup](#project-setup)
4. [Step-by-Step Guide](#step-by-step-guide)
    - [Step 1: Set Up Flask Project](#step-1-set-up-flask-project)
    - [Step 2: Integrate Reddit API](#step-2-integrate-reddit-api)
    - [Step 3: Perform Sentiment Analysis](#step-3-perform-sentiment-analysis)
    - [Step 4: Create API Endpoints](#step-4-create-api-endpoints)
    - [Step 5: Visualization](#step-5-visualization)
    - [Step 6: User Authentication](#step-6-user-authentication)
    - [Step 7: Deployment](#step-7-deployment)
5. [Testing the Setup](#testing-the-setup)
6. [Summary](#summary)

## Overview

The Reddit Sentiment Analysis tool aims to build a backend web application that fetches data from Reddit, analyzes the sentiment of the posts and comments using machine learning tools, and visualizes the results using charts and graphs

## Technologies

- **Flask (Python)**: Web framework
- **SQLAlchemy**: SQL toolkit and ORM
- **SQLite**: Database
- **Reddit API (PRAW)**: Python Reddit API Wrapper
- **Natural Language Toolkit (NLTK)**: Sentiment analysis
- **Plotly**: Visualization library
- **Flask-JWT-Extended**: User authentication

## Project Setup

### Step 1: Set Up Flask Framework

1. **Install Flask and Dependencies**: Set up a virtual environment and install Flask along with other necessary libraries such as SQLAlchemy for database management, Flask-Migrate for handling database migrations, and Flask-JWT-Extended for user authentication.
2. **Create Project Structure**: Organize your project files and directories for better maintainability. This includes setting up directories for your app, configuration, and running scripts.
3. **Initialize Flask App**: Create the Flask application and initialize the extensions (SQLAlchemy, Migrate, JWT) within the application.

### Step 2: Integrate Reddit API

1. **Register for Reddit API**: Create an account on Reddit and register your application to get the API credentials.
2. **Fetch Reddit Data**: Use PRAW (Python Reddit API Wrapper) to interact with the Reddit API and fetch posts and comments from specific subreddits.

### Step 3: Perform Sentiment Analysis

1. **Install NLTK**: Install the Natural Language Toolkit (NLTK) for sentiment analysis.
2. **Analyze Sentiment**: Use NLTK's VADER sentiment analysis tool to analyze the sentiment of the fetched Reddit posts and comments. This involves processing text data and calculating sentiment scores.

### Step 4: Create API Endpoints

1. **Define Models**: Use SQLAlchemy to create database models for storing user information and analyzed posts.
2. **Implement Endpoints**: Create API endpoints for user registration, login, and fetching sentiment analysis results. Implement necessary routes to handle these actions.

### Step 5: Visualization

1. **Install Plotly**: Install Plotly for creating visualizations.
2. **Create Visualizations**: Generate visual representations of the sentiment analysis results using Plotly and integrate them into the web dashboard.

### Step 6: User Authentication

1. **Set Up JWT Authentication**: Implement user authentication using Flask-JWT-Extended. This involves setting up routes for user registration and login and protecting endpoints with JWT.

### Step 7: Deployment

1. **Prepare for Deployment**: Create a `Procfile` for Heroku, install Gunicorn, and ensure all necessary configurations are set for deployment.
2. **Deploy to Heroku**: Initialize a git repository, commit code, create a Heroku app, push code to Heroku, and run database migrations.

## Testing the Setup

1. **Run the Application**: Start the Flask server locally and ensure everything is set up correctly.
2. **Check the Output**: Open your web browser and go to `http://127.0.0.1:5000/` to see the application running.

## Summary

- **Virtual Environment**: Manage project dependencies in an isolated environment.
- **Flask Installation**: Set up Flask, SQLAlchemy, and other required libraries.
- **Project Structure**: Organize project files and directories for maintainability.
- **Flask Initialization**: Set up the Flask application with necessary configurations and extensions.
- **Reddit API Integration**: Fetch data from Reddit using PRAW.
- **Sentiment Analysis**: Analyze sentiment of Reddit posts using NLTK.
- **API Endpoints**: Create endpoints for user registration, login, and data analysis.
- **Visualization**: Display sentiment analysis results using Plotly.
- **User Authentication**: Implement user authentication with JWT.
- **Deployment**: Deploy the application on Heroku.
