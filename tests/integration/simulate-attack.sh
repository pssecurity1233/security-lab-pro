#!/usr/bin/env bash
echo "=== Security Lab Pro Attack Simulation ==="
echo "[1] ICMP flood..."
ping -c 100 -f 127.0.0.1 > /dev/null 2>&1 || true
echo "[2] Port scan..."
nmap -sS -T4 -p 1-1000 127.0.0.1 > /dev/null 2>&1 || true
echo "Simulation complete. Check alerts."
