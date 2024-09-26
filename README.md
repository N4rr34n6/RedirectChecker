# Redirect Checker

## Overview
The Redirect Checker is a Python script designed to monitor and analyze URL redirects while utilizing the Tor network for anonymity. This tool helps in understanding how URLs redirect and can be valuable for security researchers, developers, and anyone interested in maintaining privacy while accessing web resources.

## Features
- **Tor Integration**: Routes requests through the Tor network to enhance anonymity.
- **Redirect Monitoring**: Checks for URL redirects and provides a detailed output of the redirect chain.
- **Customizable Redirect Limit**: Allows users to set a maximum number of redirects to follow, preventing infinite loops.
- **Error Handling**: Catches and displays errors encountered during HTTP requests.

## Installation
To run this project, you will need Python 3.x and the following packages:

```bash
pip3 install -r requirements.txt
```

## Usage
Run the script from the command line with a URL as an argument:

```bash
python3.7 redirect_checker.py <URL>

$ python3.7 redirect_checker.py https://www.example.com
Redirect chain:
Final destination: https://www.example.com/
Final status code: 200
```

## How It Works
1. The script sets up a SOCKS5 proxy to route traffic through the Tor network.
2. It checks if the Tor service is running.
3. It retrieves the specified URL, following any redirects up to a specified limit.
4. It outputs the redirect chain and final destination URL.

## Requirements
- Python 3.x
- `requests`
- `PySocks`

## License
This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0). See the [LICENSE](LICENSE) file for more details.
