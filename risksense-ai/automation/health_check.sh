#!/bin/bash
# health_check.sh
# Script to check system health for RiskSense AI
#!/bin/bash
echo "Disk usage:"
df -h

echo "Memory usage:"
free -h
echo "CPU load:"
top -bn1 | grep "Cpu(s)"
