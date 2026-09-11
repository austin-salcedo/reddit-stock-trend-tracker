# Reddit Stock Trend Tracker

A Python application that collects Reddit discussions, extracts relevant topics/tickers, and tracks trends over time.

> **Status:** 🚧 Early development

## Overview

The goal of this project is to build a practical Reddit data-processing application while developing strong Python and software engineering fundamentals.

The application will eventually:

- Collect Reddit posts and comments
- Identify relevant stock tickers and/or topics
- Aggregate mentions over time
- Track changes in popularity
- Store collected data
- Provide useful summaries and analysis

The project will evolve incrementally rather than being designed as a large application up front.

---

## Getting Started

### Requirements

* Python 3
* `pytest`
* `python-dotenv`
* [Alpha Vantage](https://www.alphavantage.co/support/#api-key) API key

### Setup

Clone the repository:

```bash
git clone git@github.com:austin-salcedo/reddit-stock-trend-tracker.git
cd reddit-stock-trend-tracker
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install the development dependencies:

```bash
python -m pip install pytest python-dotenv
```

Run the application:

```bash
python main.py
```

Run the tests:

```bash
python -m pytest
```


---

## Goals

### Primary Goals

- Build a useful Reddit data-processing application
- Develop strong Python fluency
- Practice data structures and algorithms
- Learn HTTP APIs and networking
- Learn how to structure a maintainable Python project
- Practice testing and debugging
- Learn persistence and databases
- Learn Git and professional development workflows
- Eventually introduce concurrency where it provides a real benefit

### Learning Goals

This project is also being used as a vehicle for learning software engineering.

Concepts will be introduced when the project creates a reason to learn them.

Examples:

- Need efficient lookups → dictionaries / hash tables
- Need duplicate removal → sets
- Need external data → HTTP / APIs
- Need structured data → JSON
- Need persistence → SQLite
- Need reliability → exceptions / retries
- Need verification → automated tests
- Need organization → modules / packages
- Need faster network operations → concurrency / async

---

## Current Functionality

### Implemented

- [ ] Basic Python project structure
- [ ] Read/process a collection of ticker symbols
- [ ] Normalize ticker symbols
- [ ] Count ticker mentions
- [ ] Basic command-line execution

### In Progress

- [ ] Reddit API integration
- [ ] Reddit post retrieval
- [ ] Data normalization
- [ ] Persistent storage

### Planned

- [ ] Comment processing
- [ ] Topic extraction
- [ ] Historical trend tracking
- [ ] SQLite database
- [ ] Automated tests
- [ ] Logging
- [ ] Error handling and retries
- [ ] Rate-limit handling
- [ ] Concurrent/async data collection
- [ ] Trend analysis
- [ ] Reporting / visualization
- [ ] Portfolio-quality documentation

---

## Project Architecture

The architecture will evolve as the application becomes more complex.

The current conceptual pipeline is:

```text
Reddit
   │
   ▼
Data Collection
   │
   ▼
Data Processing
   │
   ▼
Ticker / Topic Extraction
   │
   ▼
Aggregation
   │
   ▼
Persistence
   │
   ▼
Analysis / Reporting