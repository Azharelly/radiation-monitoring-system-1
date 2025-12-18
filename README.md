Radiation Monitoring System
Application Overview
The Radiation Monitoring System is a web application designed to record and visualise radiation measurements for analysis and monitoring purposes. The application allows users to manually submit radiation readings associated with a sensor ID and stores these records in a persistent database. A historical view enables users to review previously recorded measurements.
The long‑term vision of the project is to support integration with real radiation sensors and to enable automated risk assessment (low, medium, or high exposure). In its current state, the application focuses on demonstrating a complete cloud‑based architecture, secure database connectivity, and a full deployment workflow using Google Cloud Platform (GCP).

 Key Features
•	Manual submission of radiation measurements via a web form
•	Persistent storage of data using a managed SQL database
•	Historical view displaying stored radiation records
•	Containerised application architecture using Docker
•	Deployed on a virtual machine using Google Compute Engine
•	Automated image build pipeline using Cloud Build

Architecture Overview
The project follows a containerised deployment model running on a virtual machine, with external managed database services.

Architecture flow
GitHub (source code)
→ Cloud Build (image build pipeline)
→ Docker Image
→ Artifact Registry
→ Compute Engine VM
→ Docker Container (Flask + Gunicorn)
↔ Cloud SQL (MySQL)
→ User Browser
This architecture separates application logic, infrastructure, and data persistence, allowing each component to scale or be modified independently.

Technology Stack
Backend: Python (Flask)
Web Server:  Gunicorn
Frontend: HTML, JavaScript
Containerisation: Docker
CI/CD:  Google Cloud Build
Compute: Google Compute Engine (VM)
Database: Google Cloud SQL (MySQL)
Container Registry: Artifact Registry

GCP Services Used
Google Compute Engine
Compute Engine is used to host a virtual machine that runs the Docker container containing the application. This service was chosen to provide full control over the runtime environment, networking, and container lifecycle. It allows the application to run continuously and exposes the application to the public internet via a static external IP and port configuration.

Google Cloud SQL (MySQL)
Cloud SQL provides a managed relational database used to persist radiation records. It was chosen to ensure data durability, automated backups, and separation between the application and its data layer. The database remains available even if the application container or virtual machine is restarted.

Google Cloud Build
Cloud Build is used to automate the build process of the application. Each time code is pushed to GitHub, Cloud Build builds a Docker image using the Dockerfile and pushes the resulting image to Artifact Registry. 

Artifact Registry
Artifact Registry stores the Docker images produced by Cloud Build. The Compute Engine VM pulls the latest image from this registry when starting or updating the application container.

Deployment Workflow

1. Source Code
The application source code is stored in a GitHub repository. Key files include:

•	`main.py`: Flask application logic and routes
•	`templates/`: HTML templates (form and history pages)
•	`requirements.txt`: Python dependencies
•	`Dockerfile`: Instructions to build the application image
•	`cloudbuild.yaml`: Cloud Build pipeline configuration

2. Automated Build with Cloud Build
When code is pushed to GitHub:
1. A Cloud Build trigger is activated
2. Cloud Build reads `cloudbuild.yaml`
3. Docker builds an image using the Dockerfile
4. The image is pushed to Artifact Registry

3. Docker Image Creation
The Dockerfile defines how the application runs inside the container:
•	Uses Python 3.11
•	Copies application files into `/app`
•	Installs dependencies
•	Starts the application using Gunicorn on port 8080

4. Application Execution on Compute Engine
The Compute Engine VM pulls the latest Docker image from Artifact Registry and runs it using Docker. The container exposes port 8080, allowing external users to access the application through the VM’s public IP address.

5. Database Connectivity
The application connects to Cloud SQL using environment variables for database credentials and connection details. This allows secure configuration without hard‑coding sensitive values into the application code.

Runtime Request Flow

1.	A user accesses the application via a browser
2.	The request reaches the Compute Engine VM
3.	Docker forwards the request to the container
4.	Gunicorn passes the request to Flask
5.	Flask renders HTML templates or processes API requests
6.	 Data is stored or retrieved from Cloud SQL
7.	A response is returned to the user

Security Considerations
•	Database credentials are injected using environment variables
•	Cloud SQL is isolated from direct public access
•	The application container does not store persistent data

Limitations and Future Improvements
Current limitations:
•	Manual data entry only (no real sensor integration)
•	No user authentication or access control
•	Manual container restart on VM

Potential future improvements:
•	Integration with real radiation sensors
•	Automated risk classification logic
•	Fully automated deployment from Cloud Build to VM
•	Authentication and role‑based access control

Conclusion
This project demonstrates a complete end‑to‑end deployment of a web application on Google Cloud Platform. It highlights core cloud concepts including containerisation, virtual machines, managed databases, and CI pipelines. The system is intentionally simple in functionality but robust in architecture, making it suitable as a learning and demonstration project for cloud application deployment.
