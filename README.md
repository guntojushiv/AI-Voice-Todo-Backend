AI Voice-Controlled To-Do App - Backend

![Screenshot 2025-03-26 170105](https://github.com/user-attachments/assets/fa0e3443-25b9-41f2-be8e-f351d736be19)
![Screenshot 2025-03-26 170424](https://github.com/user-attachments/assets/f014b077-92ce-4861-87e7-315805ece5b5)



This is the backend service for the AI Voice-Controlled To-Do App, built using Python (FastAPI) and MongoDB. It handles API requests for managing to-do tasks and integrates with speech recognition for voice commands.

🚀 Features
✅ RESTful API for CRUD operations on tasks
✅ Voice command processing for task management
✅ MongoDB database integration
✅ User authentication & session management
✅ Deployment-ready with Render/Heroku

🛠️ Tech Stack
Backend: Python, FastAPI

Database: MongoDB

Authentication: JWT

Hosting: Render/Heroku

Others: SpeechRecognition, Pydantic, Uvicorn


⚡ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/guntojushiv/AI-Voice-Todo-Backend.git
cd AI-Voice-Todo-Backend

2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Setup environment variables
Create a .env file and add:


MONGO_URI="your_mongodb_connection_string"
JWT_SECRET="your_secret_key"

5️⃣ Run the backend server
uvicorn app.main:app --reload
Backend will be live at: http://127.0.0.1:8000/

🌐 API Endpoints
Method	Endpoint	Description
GET	/tasks	Get all tasks
POST	/tasks	Add a new task
PUT	/tasks/{id}	Update a task
DELETE	/tasks/{id}	Delete a task


📞 Contact
For any issues or suggestions, feel free to reach out!
