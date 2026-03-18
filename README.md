# IntrusionX

IntrusionX is a cybersecurity monitoring dashboard built with Python and Flask.
It analyzes SSH authentication logs, detects brute-force attacks, and visualizes suspicious activity in real time.

## Features

* SSH log analysis
* Brute-force attack detection
* Real-time dashboard
* Interactive world map of attacking IPs
* Attack statistics graph
* Automatic IP blocking (Linux) or simulation (Windows)

## Technologies Used

* Python
* Flask
* JavaScript
* Chart.js
* Leaflet.js
* HTML / CSS
* Git & GitHub

## Project Structure

```
IntrusionX/
│
├── app.py
├── log_analysis.py
├── blocker.py
├── attack_simulator.py
│
├── sample_logs/
│   └── auth.log
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   ├── images/
│   └── audio/
│
└── README.md
```

## How It Works

1. The system reads SSH authentication logs.
2. Failed login attempts are extracted.
3. Attempts are grouped by IP address.
4. If an IP exceeds a defined threshold, it is marked as suspicious.
5. The dashboard displays the attack data in real time.

## Attack Simulation

You can simulate SSH attacks using:

```
python attack_simulator.py
```

This script generates fake failed SSH attempts inside the log file.

## Running the Project

Start the server:

```
python app.py
```

Open the dashboard:

```
http://127.0.0.1:5000
```

## Educational Purpose

This project is designed as a cybersecurity learning project demonstrating:

* log analysis
* threat detection
* security monitoring dashboards

## Author

Cybersecurity student project.
