import socket
import subprocess
import sys

# Find a free port
s = socket.socket()
s.bind(('', 0))  # Bind to a free port assigned by the OS
port = s.getsockname()[1]
s.close()

print(f"Starting Streamlit dashboard on port {port}...")

# Run Streamlit on the free port
subprocess.run([
    sys.executable, "-m", "streamlit", "run",
    "dynamic_estimation_dashboard_full.py",
    "--server.port", str(port)
])
