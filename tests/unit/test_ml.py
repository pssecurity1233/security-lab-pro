"""Unit tests for ML module"""
import pytest
from modules.ml.ssh_anomaly import SSHAnomalyDetector

def test_ssh_detector():
    detector = SSHAnomalyDetector()
    assert detector is not None
