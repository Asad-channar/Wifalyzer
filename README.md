# 📶 Wifalyzer - WiFi Signal Analyzer

## Overview

**Wifalyzer** is a cross-platform WiFi signal analysis tool designed to provide real-time insights into wireless networks. The application scans nearby WiFi networks, analyzes signal strength, tracks connectivity changes, and visualizes wireless coverage through graphs and heat maps.

Built using C++, Wifalyzer aims to support multiple platforms including Windows, Linux, macOS, and Android while providing an intuitive graphical user interface for network monitoring and optimization.

---

## Features

### 🔍 Network Scanning and Analysis

* Scan and identify nearby WiFi networks in real-time.
* Display detailed network information including:

  * SSID (Network Name)
  * BSSID (MAC Address)
  * Network Type
  * Security Information
* Automatic refresh every 5 seconds.

### 📡 Signal Strength Detection

* Measure WiFi signal strength in **dBm (Decibel-Milliwatts)**.
* Real-time signal updates.
* Display signal quality indicators and strength percentages.

### 🖧 Access Point Details

* Retrieve Access Point (AP) information:

  * SSID
  * BSSID/MAC Address
  * Channel Information
  * Frequency Band
  * Encryption Type
* Target specific networks for focused analysis.

### 📈 Dynamic Signal Tracking

* Monitor signal strength changes as users move between locations.
* Real-time graphical representation of signal fluctuations.
* Detect signal instability and interference patterns.

### 🎯 Targeted Network Analysis

* Detailed analysis of selected networks.
* Display:

  * Connected client information (where legally permitted)
  * Signal quality metrics
  * Encryption standards
  * Password strength assessment
* Designed to comply with applicable privacy and legal standards.

### 🗺️ Signal Strength Mapping

* Generate heat maps of WiFi coverage.
* Visualize strong and weak signal zones.
* Assist in optimal router placement and network planning.

### 🖥️ User-Friendly GUI

* Modern graphical user interface.
* Interactive charts and visualizations.
* Easy navigation between network data and analytics.
* Professional dashboard for monitoring wireless environments.

### 💾 SSID Cache Management

* Maintain a cache of previously detected networks.
* Faster analysis of known networks.
* Reduced redundant scanning operations.

---

## Technical Specifications

| Feature          | Details                        |
| ---------------- | ------------------------------ |
| Language         | C++                            |
| Platforms        | Windows, Linux, macOS, Android |
| Architecture     | Cross-Platform                 |
| Data Processing  | Real-Time & Asynchronous       |
| Refresh Interval | Every 5 Seconds                |
| GUI              | Interactive Desktop Interface  |
| Visualization    | Graphs & Heat Maps             |
| Storage          | SSID Cache System              |

---

## Planned Architecture

```text
+-------------------+
|      GUI Layer    |
+---------+---------+
          |
          v
+-------------------+
| Analysis Engine   |
+---------+---------+
          |
          v
+-------------------+
| WiFi Scanner      |
+---------+---------+
          |
          v
+-------------------+
| Network Interface |
+-------------------+
```

---

## Future Enhancements

* Export reports in PDF and CSV formats.
* Historical signal tracking and trend analysis.
* GPS-assisted WiFi mapping.
* Advanced interference detection.
* Dark mode support.
* Mobile companion application.
* Cloud synchronization of scan results.

---

## Installation

### Prerequisites

* C++17 or later
* CMake 3.20+
* Supported Operating System:

  * Windows
  * Linux
  * macOS
  * Android (Planned)

### Build Instructions

```bash
git clone https://github.com/Asad-Channar/Wifalyzer.git

cd Wifalyzer

mkdir build
cd build

cmake ..
cmake --build .
```

---

## Usage

1. Launch Wifalyzer.
2. Start a network scan.
3. View detected WiFi networks.
4. Select a network for detailed analysis.
5. Monitor signal strength changes in real-time.
6. Generate graphs or heat maps for coverage visualization.

---

## Security and Legal Compliance

Wifalyzer is intended for legitimate network analysis, troubleshooting, educational purposes, and wireless optimization.

The application:

* Does not perform unauthorized access.
* Does not collect private user data.
* Operates within legal and ethical network analysis boundaries.
* Encourages responsible and authorized usage.

Users are responsible for complying with local laws and regulations regarding wireless network monitoring.

---

## Project Status

🚧 **Currently Under Development**

Core modules being developed:

* [ ] WiFi Scanner
* [ ] Signal Strength Analyzer
* [ ] GUI Dashboard
* [ ] Graph Visualization Engine
* [ ] Heat Map Generator
* [ ] SSID Cache Manager
* [ ] Android Support

---

## Author

**Asad Muhammad Channar**

Cybersecurity Student | Software Developer | Network Security Enthusiast

---

## License

This project is licensed under the MIT License.

Feel free to contribute, report issues, and suggest new features.
