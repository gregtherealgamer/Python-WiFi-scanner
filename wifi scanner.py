import subprocess

def scan_wifi():
    # run the iwlist command and get the output
    output = subprocess.run(["iwlist", "scan"], capture_output=True).stdout.decode()

    # split the output into a list of lines
    lines = output.split("\n")

    # parse the lines to get the WiFi details
    wifi_networks = []
    current_network = {}
    for line in lines:
        if "Cell" in line:
            # new network found, store the current one and create a new one
            if current_network:
                wifi_networks.append(current_network)
            current_network = {"cell_number": line.split()[1]}
        elif "ESSID" in line:
            # get the WiFi name
            current_network["ssid"] = line.split('"')[1]
        elif "Address" in line:
            # get the WiFi MAC address
            current_network["mac_address"] = line.split()[4]
        elif "Frequency" in line:
            # get the WiFi frequency
            current_network["frequency"] = line.split()[1]
        elif "Quality" in line:
            # get the WiFi signal quality
            current_network["quality"] = line.split()[1].split("/")[0]
        elif "Encryption key" in line:
            # get the WiFi encryption type
            current_network["encryption"] = line.split(":")[1].strip()
        elif "Bit Rates" in line:
            # get the WiFi bit rates
            current_network["bit_rates"] = line.split(":")[1].strip()
        elif "IE" in line:
            # get the WiFi protocols
            current_network["protocols"] = line.split(":")[1].strip()
        elif "Group Cipher" in line:
            # get the WiFi cipher
            current_network["cipher"] = line.split(":")[1].strip()
    # add the last network
    wifi_networks.append(current_network)

    # print the WiFi networks
    for network in wifi_networks:
        print("=" * 40)
        print(f"Cell number: {network['cell_number']}")
        print(f"SSID: {network['ssid']}")
        print(f"MAC address: {network['mac_address']}")
        print(f"Frequency: {network['frequency']}")
        print(f"Quality: {network['quality']}")
        print(f"Encryption: {network['encryption']}")
        print(f"Bit rates: {network['bit_rates']}")
        print(f"Protocols: {network['protocols']}")
        print(f"Cipher: {network['cipher']}")

scan_wifi()
