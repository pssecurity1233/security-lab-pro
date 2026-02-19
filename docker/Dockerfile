FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    suricata python3 python3-pip && \
    pip3 install flask elasticsearch

COPY . /opt/security-lab-pro
WORKDIR /opt/security-lab-pro

CMD ["python3", "dashboards/backend/app.py"]
