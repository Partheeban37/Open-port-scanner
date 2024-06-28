# CODTECH-task2

### Name:PARTHEEBAN R

### Company:CODTECH IT SOLUTIONS

### ID:CTO8DS161

### Domain:CYBER SECURITY & ETHICAL HACKING

### Duration:june to july

### Mentor:SRAVANI GOUNI

# Simple Port Scanner

This is a simple port scanner implemented in Python using the `socket` module. The program scans a predefined list of ports on a target host to check if they are open.

## Features

- Scans a list of common ports (21, 22, 80, 443, 3306) to determine if they are open on the target host.
- Uses the `socket` module for network communication.
- Provides real-time feedback on the status of each port.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/simple-port-scanner.git
    ```
2. Navigate to the project directory:
    ```bash
    cd simple-port-scanner
    ```

### Usage

Run the scanner with the target host as an argument:

```bash
python scanner.py <target_host>
```

###Example:
  ```bash
 python scanner.py 192.168.1.1
  ```
## Code Overview

The script consists of the following functions and structure:

scan_host(target_host, port)
  Creates a socket object and attempts to connect to the target host and port.
  If the connection is successful, it prints that the port is open.
  Handles socket errors and prints an error message if the connection fails.
main()
 Checks for the correct number of command-line arguments.
 Defines a list of ports to scan.
 Iterates over the list of ports and calls scan_host for each one.
 __main__ block
 Calls the main function to start the program.


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

Inspired by various network scanning tools and tutorials available online.

# Output

![Screenshot 2024-06-18 195306](https://github.com/Partheeban37/CODTECH-task2/assets/144414138/9c64c2ba-3515-449e-a191-cc11357bd1e9)
