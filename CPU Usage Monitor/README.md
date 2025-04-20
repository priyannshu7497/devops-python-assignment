# CPU Usage Monitor 🖥️

This is a simple Python script to continuously monitor CPU usage on a local machine.  
If the CPU usage exceeds a predefined threshold (default is 80%), the program displays an alert message in the terminal.

## 🚀 Features

- Monitors CPU usage in real-time
- Alerts when CPU usage crosses a specified threshold
- Runs indefinitely until manually stopped
- Includes error handling for robustness

## 🛠️ Requirements

- Python 3.x
- psutil library

Install `psutil` using pip if not already installed:

```bash
pip install psutil

How to Use
1.Clone or download this project.

2.Open a terminal in the project directory.

3.Run the script

python cpu_monitor.py

OUTPUT

Monitoring CPU usage...
Press Ctrl+C to stop.

Current CPU Usage: 12.3%
Current CPU Usage: 21.7%
Alert! CPU usage exceeds threshold: 85.2%
Current CPU Usage: 45.6%
...


Customization
CPU_THRESHOLD = 80       # Set your desired CPU usage threshold
CHECK_INTERVAL = 1       # Time interval (in seconds) between checks


 Stop Monitoring
To stop the script, simply press:


Project Structure
CPU Usage Monitor/
│
├── cpu_monitor.py      # Main monitoring script
└── README.md           # Documentation file


Author
Your PRIYANSHU GUPTA


