# **AI-Enhanced Cybersecurity Threat Detection**

This research uses machine learning and natural language processing (NLP) techniques to identify cybersecurity vulnerabilities by analysing network traffic data and system logs. It uses an Isolation Forest technique to discover anomalies in network traffic, and a Logistic Regression classifier with TF-IDF vectorisation to detect threats in system logs. The system has a simple Flask web interface that allows for easy interaction and intuitive visualisation of outcomes.

Project Features:
-Network Traffic Anomaly Detection: Uses the Isolation Forest method to identify strange patterns and abnormalities in network traffic data, hence improving early threat detection.
-System Log Threat Classification: Using Logistic Regression and TF-IDF vectorisation, system log entries are classified as normal or potential security concerns, allowing for proactive monitoring.
-Web Interface: The Flask web interface is intuitive and user-friendly, allowing users to upload network traffic and log data files, as well as conduct threat analysis with minimal input.
-Pre-trained Models: Includes pre-trained models for detecting network traffic anomalies and classifying log files, allowing for faster deployment and analysis without the need for model training from start.

AI-Cybersecurity-Threat-Detection/
│
├── app.py                          # Main Flask application to handle web requests and interactions
├── model.py                        # Machine learning models for anomaly detection and log classification
├── requirements.txt                # List of Python dependencies for the project
├── README.md                       # Documentation with project overview and setup instructions
├── static/
│   ├── style.css                   # CSS file for styling the web interface
├── templates/
│   ├── index.html                  # Main HTML template for the web interface
├── utils/
│   ├── data_loader.py              # Helper functions to load and preprocess network traffic and log data
├── data/
│   ├── network_traffic.csv         # Sample dataset for network traffic analysis
│   ├── system_logs.txt             # Sample system log entries for threat detection
├── models/
│   ├── anomaly_detector.pkl        # Pre-trained Isolation Forest model for network traffic anomaly detection
│   ├── log_classifier.pkl          # Pre-trained Logistic Regression model for system log classification

```

Key Files Explained:
app.py: This is the core application file that runs the Flask server, enabling user interactions through the web interface for analyzing both network traffic data and system logs.
model.py: Contains the code for applying machine learning models, specifically for anomaly detection in network traffic and classification of system logs.
requirements.txt: Lists all the required dependencies such as Flask, pandas, scikit-learn, and transformers that need to be installed for the project to run.
static/style.css: A basic CSS file responsible for the styling of the web interface, ensuring a simple and intuitive design.
templates/index.html: Provides the structure of the web interface where users can upload files and view analysis results for both network traffic and system logs.
utils/data_loader.py: Contains helper functions used to load and preprocess the network traffic data and system logs before they are passed to the machine learning models for analysis.
data/network_traffic.csv: A sample CSV file that holds network traffic data, including fields like source_ip, destination_ip, protocol, and packet_size. This is the dataset for anomaly detection.
data/system_logs.txt: A sample text file with system log entries, including login attempts and suspicious events. It is used for detecting potential security threats through log analysis.
models/anomaly_detector.pkl: The pre-trained Isolation Forest model saved in a .pkl format. It detects anomalies in the network traffic data provided by the user.
models/log_classifier.pkl: A pre-trained Logistic Regression model that uses TF-IDF vectorization to classify system log entries, identifying potential threats.
Data
The project includes two sample datasets:

network_traffic.csv:

A dataset containing network traffic records with columns like source_ip, destination_ip, port, protocol, and packet_size.
It is used by the Isolation Forest model to detect abnormal patterns in network traffic, which could signal security threats.
system_logs.txt:

A file containing sample system log entries such as login attempts, error logs, and security alerts.
The Logistic Regression model with TF-IDF vectorization uses this data to classify log entries as normal or indicative of security threats.
Models
anomaly_detector.pkl:

A pre-trained Isolation Forest model designed to detect anomalies in the network traffic dataset.
If not available, the system can train the model using the provided network_traffic.csv dataset, allowing users to adapt the tool to their specific data.
log_classifier.pkl:

A pre-trained Logistic Regression model that classifies system log entries using TF-IDF vectorization.
This model identifies potential security threats by analyzing log data for suspicious patterns. If the pre-trained model is unavailable, it can be retrained using sample log entries.


Setup Instructions

1. Clone the Repository:
Start by cloning the repository to your local machine:


git clone https://github.com/Shashwat1729/AI-Cybersecurity-Threat-Detection.git
cd AI-Cybersecurity-Threat-Detection

2. Install Dependencies:
Install the required Python libraries listed in the requirements.txt file:
pip install -r requirements.txt

3. Run the Flask Application:
After all dependencies are installed, you can start the Flask server with:
python app.py

4. Open the Application:
Open your browser and visit the following URL to access the application:


http://127.0.0.1:5000/
How to Use
Analyze Network Traffic:

Navigate to the home page and click the "Analyze Network Traffic" button.
The system will process the network_traffic.csv file and highlight any anomalies detected in the network traffic.
Detected anomalies will flag unusual or suspicious network activities that might require further investigation.
Analyze System Logs:

Click the "Analyze System Logs" button to analyze the system_logs.txt file.
The system will classify log entries and flag any potential threats, such as failed login attempts or suspicious activity.
Threats will be clearly displayed, allowing users to identify areas of concern.
Data Example
network_traffic.csv:

timestamp,source_ip,destination_ip,port,protocol,packet_size,label
2023-09-01 10:45:23,192.168.1.1,10.0.0.1,80,TCP,500,normal
2023-09-01 10:46:10,10.0.0.5,192.168.1.1,443,TCP,450,suspicious
...
system_logs.txt:


Failed login attempt from IP 192.168.1.1
User admin logged in successfully
Error: Disk space low on /dev/sda1
Suspicious activity detected from IP 10.0.0.5
...


Future Enhancements

Real-time Monitoring: Integrate real-time data streams to provide live monitoring of network traffic and logs, allowing for instant threat detection.

Enhanced Visualizations: Add dynamic visualizations like interactive graphs and charts to better display trends and anomaly patterns in network traffic and log files.

Deep Learning Integration: Explore advanced deep learning models such as LSTM or GRU for enhanced log analysis and time-series prediction of network anomalies.

License
This project is licensed under the MIT License, allowing you the freedom to use, modify, and distribute it as you see fit.











