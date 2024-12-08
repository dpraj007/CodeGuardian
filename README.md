# CodeGuardian

## Table of Contents
1. [What is CodeGuardian?](#What-is-CodeGuardian)
2. [Features](#Features)
3. [Getting Started](#Getting-Started)
    - [Prerequisites](#Prerequisites)
    - [Installation Steps](#Installation-Steps)
4. [Usage](#Usage)
    - [Access the Web Interface](#Access-the-Web-Interface)
    - [Endpoints](#Endpoints)
5. [Development](#Development)
    - [File Structure Overview](#File-Structure-Overview)
    - [Commands for Development](#Commands-for-Development)
6. [Contributing](#Contributing)
7. [License](#License)
8. [Support](#Support)
9. [Contributors](#Contributors)

---

## What is CodeGuardian?

**CodeGuardian** is a real-time, on-device AI-powered tool designed for comprehensive code security. It eliminates the limitations of traditional cloud-based vulnerability scanners by providing a local, in-depth scan of your codebase. CodeGuardian identifies security vulnerabilities and offers actionable remediation suggestions directly within your development environment.

Built using LM Studio's on-device AI, CodeGuardian ensures developers get instant feedback on their code, reducing the time between vulnerability introduction and remediation. This approach is ideal for industries with stringent data security requirements, such as defense, healthcare, and critical infrastructure, where cloud solutions may not be viable.

Unlike cloud-based tools, CodeGuardian operates entirely offline, ensuring security and privacy by processing code locally on your device. Additionally, it periodically syncs with trusted vulnerability databases like CVE, NVD, and OWASP to update its threat models, ensuring that your code stays protected against emerging threats.

With its energy-efficient design, CodeGuardian is optimized for use on resource-constrained platforms, making it especially useful for mobile and IoT developers.

---

## Features

- Analyze GitHub or local repositories for vulnerabilities.
- View detailed reports with severity levels.
- Chat with reports for interactive analysis.
- Simple and elegant user interface.

---

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

1. **Python 3.8+**
2. **pip** (Python package installer)
3. **Django Framework**

### Installation Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/dpraj007/CodeGuardian
   cd CodeGuardian


2. Install the required dependencies
```bash
pip install -r requirements.txt
```

3. Start the development server
```bash
python manage.py runserver
```

### Usage

Access the Web Interface
* Open the browser and navigate to http://127.0.0.1:8000.
* Use the GitHub Repository URL or Local Repository options to analyze your code.


### Endpoints
* Main Page: Navigate to http://127.0.0.1:8000 to access the tool.
* View Reports: Navigate to http://127.0.0.1:4321 to download or view generated reports.
* Chat with Reports: Navigate to http://127.0.0.1:3000 for an interactive chat-based analysis of your reports.


## License

This project is licensed under the MIT License. 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## Support

For any issues, questions, or feedback, please feel free to:

- Open an issue on the [GitHub repository](https://github.com/CodeGuardian/issues).

Your feedback helps us improve CodeGuardian!

---

## Contributors

The following individuals have contributed to the development of CodeGuardian:

- **Alper Mumcular**  
  GitHub: [AlperMumcular](https://github.com/AlperMumcular)

- **Abhinav Gupta**  
  GitHub: [AbhinavGupta](https://github.com/abg0148)

- **Dhairyasheel Patil**  
  GitHub: [DhairyaPatil](https://github.com/dpraj007)

- **Sahil Sarnaik**  
  GitHub: [SahilSarnaik](https://github.com/sahilms48)

We appreciate everyone's efforts in making this project a success!
