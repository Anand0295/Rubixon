from flask import Flask, render_template, request, redirect, url_for
import os
from models import detect_anomalies, classify_logs
from utils.data_loader import load_network_data, load_log_data

app = Flask(__name__)

# Load sample data at start
try:
    network_data = load_network_data('data/network_traffic.csv')
    log_data = load_log_data('data/system_logs.txt')
except Exception as e:
    print(f"Error loading data: {e}")
    network_data = None
    log_data = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze_network', methods=['POST'])
def analyze_network():
    if network_data is None:
        return "Error: Network data not loaded", 500
    try:
        anomalies = detect_anomalies(network_data)
        return render_template('index.html', anomalies=anomalies.to_html())
    except Exception as e:
        return f"Error analyzing network data: {e}", 500

@app.route('/analyze_logs', methods=['POST'])
def analyze_logs():
    if log_data is None:
        return "Error: Log data not loaded", 500
    try:
        threats = classify_logs(log_data)
        return render_template('index.html', threats=threats.to_html())
    except Exception as e:
        return f"Error analyzing log data: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)