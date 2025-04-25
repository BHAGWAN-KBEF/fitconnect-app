fitconnect-app
🏋️ Full-stack contact platform for gyms and fitness businesses, built with Flask, PostgreSQL, NGINX, and Docker Compose. Enables users to reach out via a sleek frontend while securely storing inquiries in a PostgreSQL database.
💪 FitConnect App

Tech Stack
- Flask (Python)
- PostgreSQL
- NGINX
- Docker & Docker Compose
- HTML, CSS, JavaScript, Bootstrap

 📁 Project Structure
- `frontend/`: Static HTML site served via NGINX
- `backend/`: Flask API that receives and stores contact form submissions
- `db`: PostgreSQL container for storing submitted messages
- `docker-compose.yml`: Orchestrates all services

How to Run

1. Clone the repo*  
   ```bash
   git clone https://github.com/your-username/fitconnect-app.git
   cd fitconnect-app
2.Set environment variables
Create a .env file in the backend/ folder with the following content:
DB_HOST=db
DB_NAME=mydb
DB_USER=<your-database-username>
DB_PASS=<your-database-password>

3.Run the app with Docker Compose
Start the application in detached mode (background) using:
docker-compose up --build -d

4.Access the app
Frontend: http://localhost:8080
Backend API: http://localhost:5000

 Contact Form (Frontend)
![Contact Form](screenshots/contact-form-filled.png)
![image](https://github.com/user-attachments/assets/29531e56-4e83-4a01-8d7f-0214b28d8a8f)

Database (PostgreSQL)
![Database Screenshot](screenshots/database-contacts.png)
![Screenshot 2025-04-25 201147](https://github.com/user-attachments/assets/e03fb546-8643-4648-8a98-a17700a939e7)



