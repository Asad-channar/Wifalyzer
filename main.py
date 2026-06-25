import subprocess
import os
import time
import platform
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def detect_wifi_networks():
    """Detect and display WiFi networks with detailed information."""
    try:
        os.system("cls" if platform.system() == "Windows" else "clear")  # Clear the terminal screen based on OS
        print("Scanning for WiFi Networks...\n")

        # Check the OS type
        if platform.system() == "Windows":
            # Use netsh command for Windows
            command = "netsh wlan show networks mode=bssid"
        elif platform.system() == "Linux":
            # Use iwlist or nmcli command for Linux
            command = "nmcli dev wifi"  # You can also use 'iwlist wlan0 scan' if nmcli is unavailable
        else:
            raise EnvironmentError("Unsupported OS")

        result = subprocess.check_output(command, shell=True, text=True, encoding="utf-8")
        networks = parse_networks(result)

        # Sort networks by signal strength in descending order
        networks.sort(key=lambda x: x.get("Signal Strength", 0), reverse=True)

        # Display detected networks
        if networks:
            print("Detected WiFi Networks with Detailed Information:\n")
            for idx, network in enumerate(networks, start=1):
                print(f"Network {idx}:")
                print(f"    SSID: {network['SSID']}")
                print(f"    Signal Strength: {network['Signal Strength']}%")
                print(f"    Channel: {network['Channel']}")
                print(f"    Authentication: {network['Authentication']}")
                print(f"    Encryption: {network['Encryption']}")
                print(f"    BSSID: {network['BSSID']}")
                print(f"    Band: {network['Band']}")
                print()
        else:
            print("No WiFi networks detected.")
        
        return networks

    except subprocess.CalledProcessError as e:
        print("Error scanning for WiFi networks.")
        print(e)
        return []


def parse_networks(output):
    """Parse the output of netsh wlan command to extract detailed information."""
    networks = []
    lines = output.splitlines()
    current_network = {}

    for line in lines:
        line = line.strip()

        if line.startswith("SSID ") and " :" in line:  # Start of a new network
            if current_network:  # Save the previous network
                networks.append(current_network)
            current_network = {"SSID": line.split(":", 1)[1].strip()}
        elif "Network type" in line:
            current_network["Network Type"] = line.split(":", 1)[1].strip()
        elif "Authentication" in line:
            current_network["Authentication"] = line.split(":", 1)[1].strip()
        elif "Encryption" in line:
            current_network["Encryption"] = line.split(":", 1)[1].strip()
        elif "BSSID" in line:
            current_network["BSSID"] = line.split(":", 1)[1].strip()
        elif "Signal" in line:
            current_network["Signal Strength"] = int(line.split(":", 1)[1].strip().replace("%", ""))
        elif "Radio type" in line:
            current_network["Radio Type"] = line.split(":", 1)[1].strip()
        elif "Band" in line:
            current_network["Band"] = line.split(":", 1)[1].strip()
        elif "Channel" in line:
            current_network["Channel"] = line.split(":", 1)[1].strip()
        elif "Connected Stations" in line:
            current_network["Connected Stations"] = line.split(":", 1)[1].strip()
        elif "Channel Utilization" in line:
            current_network["Channel Utilization"] = int(line.split(":", 1)[1].strip().replace("%", ""))
        elif "Medium Available Capacity" in line:
            current_network["Medium Available Capacity"] = line.split(":", 1)[1].strip()

    # Add the last network to the list
    if current_network:
        networks.append(current_network)

    return networks

def visualize_signal_strength(networks):
    """Visualize signal strength using a bar chart."""
    ssids = [network["SSID"] for network in networks]
    signal_strengths = [network["Signal Strength"] for network in networks]

    plt.figure(figsize=(10, 6))
    plt.barh(ssids, signal_strengths, color="green", alpha=0.9)
    plt.xlabel("Signal Strength (%)", fontsize=12)
    plt.ylabel("Network Name (SSID)", fontsize=12)
    plt.title("WiFi Signal Strength Distribution", fontsize=14)
    plt.gca().invert_yaxis()  # Strongest at the top
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

def visualize_heatmap(networks):
    """Visualize signal strength distribution as a heatmap."""
    # For heatmap, let's use an arbitrary position for each network
    # Assuming the networks are scattered randomly across a grid
    x_positions = np.random.randint(0, 10, len(networks))
    y_positions = np.random.randint(0, 10, len(networks))
    signal_strengths = [network["Signal Strength"] for network in networks]

    # Create a grid for the heatmap
    grid = np.zeros((10, 10))  # 10x10 grid of WiFi signal strengths
    for x, y, strength in zip(x_positions, y_positions, signal_strengths):
        grid[x, y] = strength

    # Plot the heatmap using seaborn
    plt.figure(figsize=(8, 6))
    sns.heatmap(grid, cmap="twilight", annot=True, fmt=".2f", cbar_kws={'label': 'Signal Strength (%)'})
    plt.title("WiFi Signal Strength Heatmap")
    plt.xlabel("Position X")
    plt.ylabel("Position Y")
    plt.show()

def main():
    """Main function to run the WiFi analyzer."""
    while True:
        # Detect and display networks
        networks = detect_wifi_networks()

        # Wait for 1 seconds before showing the menu
        print("\nAnalyzing Networks...")
        time.sleep(1)

        # Display menu and force refresh
        print("\nMenu:")
        print("1. View WiFi Signal Strength Graph")
        print("2. View WiFi Signal Strength Heatmap")
        print("3. Refresh WiFi list")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            visualize_signal_strength(networks)  # Display the graph
        elif choice == "2":
            visualize_heatmap(networks)  # Display the heatmap
        elif choice == "3":
            os.system("cls")  # Clear screen and refresh
            continue  # Go back to scanning
        elif choice == "4":
            print("Exiting WiFi Analyzer...")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
