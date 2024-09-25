# Smart City Traffic Assistant

## Overview

**Smart City Traffic Assistant** is an AI-powered application that provides real-time traffic advice using the [TomTom Traffic API](https://developer.tomtom.com/traffic-api) and integrates with OpenAI's GPT-4 model. The assistant fetches current traffic data and offers personalized route suggestions for drivers navigating busy city streets.

The project aims to demonstrate real-world AI integration with live data, focusing on optimizing travel time and route planning.

---

## Features

- **Real-Time Traffic Data**: Retrieves up-to-the-minute traffic information using the TomTom Traffic API.
- **AI-Powered Advice**: Uses GPT-4 to provide smart and personalized route suggestions based on real-time data.
- **Dynamic Responses**: Provides detailed, human-like responses for optimal navigation.
- **Scalability**: Future updates will include public transport information, carbon footprint estimates, and multi-route suggestions.

---

## Technology Stack

- **Backend**: Python
- **AI Integration**: OpenAI GPT-4 via `openai` API
- **Traffic Data**: TomTom Traffic API for real-time traffic conditions
- **Environment Management**: Python virtual environments (`venv`)
- **Version Control**: Git and GitHub

---

## Installation

### Prerequisites

- **Python 3.x**
- **TomTom API Key**: Sign up for a key at the [TomTom Developer Portal](https://developer.tomtom.com/).
- **OpenAI API Key**: Sign up for a key at [OpenAI](https://platform.openai.com/signup).

### Clone the Repository

```bash
git clone https://github.com/danrmzz/smart-city-traffic-assistant.git
cd smart-city-traffic-assistant
```

### Set Up Virtual Environment

1. Create and activate a Python virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/macOS
   .\venv\Scripts\activate    # For Windows
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Set Up Environment Variables

1. Create a `.env` file in the project root.
2. Add the following environment variables to the `.env` file:

   ```bash
   OPENAI_API_KEY=your_openai_api_key
   TOMTOM_API_KEY=your_tomtom_api_key
   ```

---

## Usage

1. **Run the Application**:

   After setting up the environment variables, you can run the application by executing:

   ```bash
   python app.py
   ```

2. **Example Output**:

   The assistant will provide route suggestions based on real-time traffic data fetched from TomTom and processed through GPT-4, such as:

   ```
   To get to Central Park from Times Square, the best route will depend on traffic conditions.

   - Start heading southeast towards W 41st St.
   - Then, turn left onto 6th Avenue, also known as Avenue of the Americas.
   - Continue straight on 6th Ave until you reach Central Park S.
   - Turn right onto Central Park S, and the entrance to Central Park should be visible.

   Please note that traffic conditions are dynamic, and this guidance is based on current congestion data. Always aim to leave extra time for your journey.

   It will approximately take under 20 minutes to reach by road, which is a short distance of about 3.41 miles.
   ```

---

## Roadmap

- **Public Transport Integration**: Include public transportation options using additional APIs.
- **Carbon Footprint Estimation**: Suggest greener routes and calculate environmental impact.
- **Web Interface**: Develop a web-based UI to enhance user interaction with the traffic assistant.
- **Multiple Route Suggestions**: Offer alternative routes based on real-time traffic.

---

## Contributing

Contributions are welcome! Please follow the steps below to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'feat: add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.
