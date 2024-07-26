# Reddit Sentiment Analysis Dashboard

Welcome to the Reddit Sentiment Analysis Dashboard project! This project involves creating a web application that analyzes sentiments from Reddit posts and visualizes the results. We will use Flask as the web framework and integrate various libraries for data processing and visualization.

## Table of Contents

1. [Introduction](#introduction)
2. [Step 1: Set Up Flask Project](#step-1-set-up-flask-project)
    - [What is Flask?](#what-is-flask)
    - [Setting Up the Environment](#setting-up-the-environment)
    - [Detailed Steps](#detailed-steps)
3. [Testing the Setup](#testing-the-setup)
4. [Summary](#summary)

## Introduction

The Reddit Sentiment Analysis Dashboard project aims to build a web application that fetches data from Reddit, analyzes the sentiment of the posts, and visualizes the results using various charts and graphs.

## Step 1: Set Up Flask Project

### What is Flask?

Flask is a lightweight web framework for Python. It’s designed to be simple and easy to get started with, making it a great choice for building small to medium-sized web applications. Flask provides the necessary tools to create a web server, handle HTTP requests, and manage routes.

### Setting Up the Environment

1. **Install Flask and SQLAlchemy**:
   - Flask: The core web framework.
   - SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.

2. **Create the Project Structure**:
   - Organize your files and directories for better maintainability and scalability.

### Detailed Steps

#### 1. Install Flask and SQLAlchemy

First, we need to install Flask and SQLAlchemy. We'll use a virtual environment to manage our dependencies.

- **Virtual Environment**:
  A virtual environment is a tool that helps to keep dependencies required by different projects in separate places by creating isolated environments for them. This is especially useful when working on multiple projects with different dependencies.

   ```bash
   # Install virtualenv if you haven't already
   pip install virtualenv

   # Create a virtual environment
   virtualenv venv

   # Activate the virtual environment
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
