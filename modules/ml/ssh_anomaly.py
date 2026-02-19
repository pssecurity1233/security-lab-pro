"""SSH Anomaly Detection using Isolation Forest"""
from sklearn.ensemble import IsolationForest
import numpy as np

class SSHAnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)
    
    def train(self, data):
        self.model.fit(data)
    
    def predict(self, data):
        return self.model.predict(data)
