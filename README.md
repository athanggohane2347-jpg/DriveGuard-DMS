# 🚗 DriveGuard DMS

## AI-Powered Driver Monitoring, Drowsiness, Fatigue & Distraction Detection System

**DriveGuard DMS** is a real-time AI and computer-vision research prototype designed to monitor driver behavior and identify potential safety risks such as **drowsiness, fatigue, prolonged eye closure, yawning, head movement, gaze deviation, distraction, and smartphone usage**.

The system follows the pipeline:

```text
Driver Camera
      ↓
AI / Computer Vision Analysis
      ↓
Driver State Detection
      ↓
Risk Assessment
      ↓
Safety Score
      ↓
Real-Time Alert
      ↓
Dashboard
      ↓
Event & Trip History
```

---

# 👨‍💻 Project Information

| Information | Details |
|---|---|
| **Project Name** | DriveGuard DMS |
| **Project Type** | AI / Computer Vision / Full-Stack Application |
| **Developer** | **Athang Gohane** |
| **Institution** | **Yeshwantrao Chavan College of Engineering (YCCE), Nagpur** |
| **Domain** | Artificial Intelligence & Computer Vision |
| **Backend** | FastAPI |
| **Frontend** | React + TypeScript |
| **Database** | SQLite |
| **Communication** | REST API + WebSocket |
| **Deployment** | Docker-ready |
| **Project Status** | Research / Prototype |

---

# 🎯 Project Objective

The objective of DriveGuard DMS is to develop an intelligent driver-monitoring system capable of analyzing the driver's behavior in real time using a camera.

The system attempts to identify:

- Drowsiness
- Fatigue
- Prolonged eye closure
- Abnormal blinking
- Yawning
- Head nodding
- Looking away from the road
- Gaze deviation
- Smartphone distraction
- Driver absence
- Low-light conditions
- Camera obstruction
- Increasing fatigue trends

The system converts these signals into an **explainable Driver Safety Score** and provides real-time alerts when potentially dangerous behavior is detected.

---

# ⚠️ Safety & Research Disclaimer

> **DriveGuard DMS is a research and educational prototype. It is NOT a certified automotive safety system and must NOT be used as the sole safety mechanism in a real vehicle.**

The system provides probabilistic estimates and may produce incorrect results.

Important limitations:

- Drowsiness detection is probabilistic.
- Fatigue detection is probabilistic.
- Gaze estimation is approximate.
- Phone detection can produce false positives and false negatives.
- Results depend on camera quality and lighting conditions.
- Facial behavior cannot reliably prove alcohol intoxication.
- Facial expressions should not be used as a medical or legal diagnosis.
- Any impairment-related signal is treated only as **possible impairment / abnormal behavior** and requires manual verification.

---

# ✨ Key Features

## 👤 Driver Monitoring

DriveGuard DMS continuously analyzes the driver's face and behavior.

Features include:

- Face presence detection
- Facial landmark analysis
- Eye-state monitoring
- Eye closure detection
- Blink analysis
- Yawning detection
- Head-pose estimation
- Head-nodding detection
- Gaze / attention estimation
- Looking-away detection
- Driver presence monitoring
- Low-light detection
- Camera obstruction detection
- Camera tampering detection

---

# 😴 Drowsiness & Fatigue Detection

The system combines multiple indicators instead of relying on a single frame.

### Eye Analysis

Uses eye landmarks and Eye Aspect Ratio (EAR) concepts to identify:

- Open eyes
- Partially closed eyes
- Closed eyes
- Long eye closures

### Blink Analysis

Tracks:

- Blink count
- Blink frequency
- Blink duration
- Long blinks
- Changes in blinking behavior

### Yawning

Analyzes mouth landmarks to detect:

- Mouth opening
- Yawn duration
- Number of yawns
- Yawning frequency

### Head Nodding

Detects repeated downward head movements that may indicate fatigue or drowsiness.

---

# 👀 Attention & Gaze Monitoring

The system estimates the approximate direction of the driver's attention.

Possible states:

```text
FORWARD
LEFT
RIGHT
DOWN
UNKNOWN
```

The system can detect prolonged periods of looking away.

Example:

```text
Looking away briefly
        ↓
      Normal

Looking away for longer
        ↓
      Warning

Repeated / prolonged
        ↓
   High Distraction
```

The system uses temporal behavior rather than treating a single frame as proof of distraction.

---

# 📱 Smartphone & Distraction Detection

DriveGuard supports integration with object-detection models such as YOLO.

Potential detections include:

- Smartphone
- Handheld objects
- Other distracting objects

Phone detection is not automatically classified as dangerous.

The risk engine can combine:

```text
Phone Detection
      +
Gaze Direction
      +
Head Pose
      +
Detection Duration
      ↓
Phone Distraction Risk
```

---

# 🧠 Driver State Engine

The system combines multiple signals to estimate the driver's current state.

Possible states:

```text
🟢 ATTENTIVE
🟡 DISTRACTED
🟠 FATIGUED
🔴 DROWSY
🚨 CRITICAL
⚪ FACE NOT DETECTED
```

The state engine considers multiple behavioral signals rather than relying on a single detection.

---

# 📊 Explainable Safety Score

DriveGuard generates a configurable **0–100 Driver Safety Score**.

Example:

```text
Safety Score: 42 / 100

Long Eye Closure       -25
Yawning                -10
Head Nodding           -15
Looking Away            -8
Phone Distraction       -0
```

The dashboard explains which factors contributed to the current score.

### Score interpretation

```text
90–100    🟢 Excellent
75–89     🟢 Good
60–74     🟡 Caution
40–59     🟠 High Risk
0–39      🔴 Critical
```

These ranges are configurable and should not be interpreted as certified safety thresholds.

---

# 🚨 Real-Time Alert System

DriveGuard provides multiple alert levels.

| Level | Status | Example |
|---|---|---|
| 0 | Normal | Driver attentive |
| 1 | Information | Minor attention change |
| 2 | Warning | Driver looking away |
| 3 | High Risk | Increasing fatigue |
| 4 | Critical | Severe drowsiness |

Example alerts:

```text
⚠️ DRIVER LOOKING AWAY

⚠️ FATIGUE INCREASING

⚠️ LONG EYE CLOSURE DETECTED

🚨 SEVERE DROWSINESS DETECTED

🚨 CRITICAL DRIVER STATE
```

Alert cooldown and debouncing help prevent the same alert from being triggered continuously.

---

# 📈 Fatigue Trend Analysis

DriveGuard does not only analyze the driver's current condition.

It can also track how fatigue changes throughout a session.

Example:

```text
Time →

Fatigue
10 ── 15 ── 18 ── 27 ── 35 ── 48 ── 61
                                  ↑
                           Fatigue Increasing
```

If fatigue continuously increases, the system can display:

> **Fatigue trend increasing — consider taking a break.**

This is a recommendation, not a medical assessment.

---

# 🧑‍✈️ Personalized Driver Baseline

DriveGuard supports optional driver calibration.

During calibration, the system can estimate approximate baseline values for:

- Blink behavior
- Eye openness
- Normal head position
- Gaze behavior
- Driver position

The system can then compare later behavior against that baseline.

The stored baseline contains approximate numerical behavioral parameters and does not store raw biometric templates.

---

# 🌙 Low-Light & Night Driving

The system includes low-light detection and preprocessing.

Possible lighting states:

```text
DAY
LOW LIGHT
NIGHT
```

Supported image-processing techniques may include:

- Gamma correction
- Contrast enhancement
- CLAHE
- Denoising

The architecture is designed so an **IR/NIR camera** can be integrated in future versions.

> Software image enhancement should not be considered equivalent to true night vision.

---

# 🎥 Camera & Video Modes

DriveGuard supports three operating modes.

## 📷 Camera Mode

Uses a local camera through OpenCV.

## 🎬 Video Mode

Allows recorded video to be used for testing and development.

## 🧪 Simulation Mode

Provides deterministic telemetry for demonstrations without requiring a camera or AI model.

Simulation values are clearly marked:

```text
SIMULATION MODE
```

The system does not present simulated values as real AI detections.

---

# 🎥 Event & Safety Recorder

Important safety events can be recorded and logged.

Each event can contain:

- Event ID
- Timestamp
- Session ID
- Event type
- Severity
- Confidence
- Safety score
- Description
- Optional snapshot path
- Optional video clip path

The architecture supports a black-box-style event recorder.

Concept:

```text
5–10 seconds before event
          ↓
        EVENT
          ↓
5–10 seconds after event
```

The recording duration can be configured.

> Full production-grade post-event recording should be validated and hardened before real-world deployment.

---

# 📊 Analytics Dashboard

The dashboard provides visual analytics for driver sessions.

Charts include:

- Safety score over time
- Fatigue trend
- Drowsiness trend
- Distraction trend
- Events by type
- Events by severity
- Blink frequency
- Yawning frequency

Session statistics include:

- Total sessions
- Session duration
- Average safety score
- Warning count
- Critical event count
- Drowsiness events
- Distraction events

---

# 🗂️ Session & Trip Management

When a monitoring session begins, DriveGuard creates a session record.

A session can contain:

```text
Session ID
Start Time
End Time
Duration
Average Safety Score
Minimum Safety Score
Drowsiness Events
Fatigue Events
Distraction Events
Phone Events
Critical Events
```

At the end of the session, a summary can be generated.

---

# 🤖 Computer Vision & AI

The architecture uses modular computer-vision services so models can be replaced or upgraded independently.

### Technologies

- OpenCV
- MediaPipe
- NumPy
- YOLO-compatible object detection
- PyTorch-compatible model integration
- Scikit-learn

---

# 📱 YOLO Phone Detection

Phone detection can be enabled using a compatible object-detection model.

Example setup:

```text
models/
└── yolov8n.pt
```

Configure:

```env
YOLO_MODEL_PATH=./models/yolov8n.pt
```

Then restart the backend.

The application is designed to fall back safely if the optional model is unavailable.

---

# 🏗️ System Architecture

```text
                     ┌──────────────────┐
                     │  DRIVER CAMERA   │
                     └────────┬─────────┘
                              │
                              ▼
                     ┌──────────────────┐
                     │ VIDEO PROCESSING │
                     └────────┬─────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
        Face / Pose       Eye / Mouth      Object
         Analysis          Analysis       Detection
              │               │               │
              └───────────────┼───────────────┘
                              ▼
                     ┌──────────────────┐
                     │ TEMPORAL ENGINE  │
                     └────────┬─────────┘
                              ▼
                     ┌──────────────────┐
                     │ DRIVER STATE     │
                     │ ENGINE           │
                     └────────┬─────────┘
                              ▼
                     ┌──────────────────┐
                     │   RISK ENGINE    │
                     └────────┬─────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
           Alerts          Database       Dashboard
                              │
                              ▼
                       Event / Trip History
```

---

# 🛠️ Technology Stack

## Backend

- Python 3.11+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- SQLite
- WebSockets

## AI / Computer Vision

- OpenCV
- MediaPipe
- NumPy
- YOLO integration
- PyTorch integration
- Scikit-learn

## Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- Recharts / Chart.js
- Lucide Icons

## Infrastructure

- Docker
- Docker Compose
- Environment variables

---

# 📁 Project Structure

```text
DriveGuard-DMS/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth.py
│   │   │   ├── dashboard.py
│   │   │   ├── sessions.py
│   │   │   ├── events.py
│   │   │   ├── analytics.py
│   │   │   └── settings.py
│   │   │
│   │   ├── core/
│   │   │   └── security.py
│   │   │
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── driver.py
│   │   │   ├── session.py
│   │   │   ├── event.py
│   │   │   └── baseline.py
│   │   │
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── vision/
│   │   ├── websocket/
│   │   ├── main.py
│   │   ├── config.py
│   │   └── database.py
│   │
│   ├── tests/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── types/
│   │   └── utils/
│   │
│   ├── package.json
│   └── vite.config.*
│
├── models/
├── data/
├── recordings/
├── logs/
│
├── docker/
├── docker-compose.yml
├── .env.example
└── README.md
```

---

# ⚙️ Requirements

Before installing DriveGuard DMS, make sure you have:

- **Python 3.11+**
- **Node.js 20+**
- npm
- Git
- Optional webcam

The application can run without a webcam using **Simulation Mode**.

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd DriveGuard-DMS
```

---

# 🐍 Backend Setup

Open PowerShell or Terminal:

```powershell
cd backend
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Create the environment file:

```powershell
Copy-Item ..\.env.example ..\.env
```

Start the backend:

```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Backend:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

---

# ⚛️ Frontend Setup

Open a **second terminal**:

```powershell
cd frontend
```

Install dependencies:

```powershell
npm install
```

Start the development server:

```powershell
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 🔐 Demo Account

You can create an account using the **Register** page.

Alternatively:

```bash
curl -X POST http://127.0.0.1:8000/api/auth/register ^
  -H "Content-Type: application/json" ^
  -d "{\"email\":\"demo@driveguard.local\",\"password\":\"DriveGuard123!\",\"name\":\"Demo Driver\"}"
```

For security, change demo credentials before deploying publicly.

---

# 🔌 API Endpoints

## Authentication

```text
POST /api/auth/register
POST /api/auth/login
```

## Dashboard

```text
GET /api/dashboard
GET /api/driver
GET /api/system/status
```

## Sessions

```text
GET  /api/sessions
GET  /api/sessions/{id}
POST /api/session/start
POST /api/session/stop
```

## Events

```text
GET /api/events
GET /api/events/{id}
```

## Analytics

```text
GET /api/analytics
```

## Settings

```text
GET /api/settings
PUT /api/settings
```

## Real-Time Monitoring

```text
WS /ws/driver-monitor
```

---

# 🧪 Testing

Run backend tests:

```powershell
cd backend
pytest
```

Testing includes components such as:

- Eye Aspect Ratio
- Mouth Aspect Ratio
- Head-pose logic
- Risk scoring
- Alert cooldown
- Session management
- Event management
- Selected API endpoints

---

# 🐳 Docker

Build and start the application:

```bash
docker compose up --build
```

Frontend:

```text
http://localhost:5173
```

Backend:

```text
http://localhost:8000
```

API documentation:

```text
http://localhost:8000/docs
```

---

# 🔧 Environment Variables

Create `.env` from `.env.example`.

Example:

```env
DATABASE_URL=sqlite:///./driveguard.db

SECRET_KEY=change-this-secret

YOLO_MODEL_PATH=

CAMERA_INDEX=0

RECORDING_ENABLED=false

CORS_ORIGINS=http://localhost:5173
```

> Never commit real secrets, passwords, API keys, or private credentials to GitHub.

---

# 🔒 Privacy

DriveGuard DMS follows a privacy-first architecture.

### Principles

- Camera frames should be processed locally where possible.
- Recording is disabled by default.
- Event recordings can be deleted.
- Raw biometric templates are not stored.
- Driver baselines contain approximate numerical behavioral parameters.
- Secrets are stored using environment variables.
- Raw camera footage should not be uploaded to the cloud unless explicitly required and consented to.

---

# 🌐 Deployment

The frontend can be built using:

```bash
cd frontend
npm run build
```

The resulting production build can be deployed to a static hosting provider.

The backend can be deployed using Docker on a cloud VM or container platform.

Configure:

```env
DATABASE_URL=
SECRET_KEY=
CORS_ORIGINS=
RECORDING_PATH=
YOLO_MODEL_PATH=
```

## Camera Access

A browser-hosted website cannot silently access a physical camera.

The browser must request permission using:

```javascript
navigator.mediaDevices.getUserMedia()
```

For real-time driver monitoring, **local/edge AI inference is recommended** because it provides:

- Lower latency
- Better privacy
- Reduced bandwidth
- Greater control over camera data

---

# 🛠️ Troubleshooting

### Camera unavailable

Switch to:

```text
SIMULATION MODE
```

or check:

```env
CAMERA_INDEX=0
```

---

### Webcam permission denied

Allow camera access in the browser and reload the application.

---

### YOLO model unavailable

Leave:

```env
YOLO_MODEL_PATH=
```

The system can continue using simulation/fallback functionality.

---

### No GPU

CPU processing is supported for lightweight processing and simulation.

GPU acceleration can be added for more demanding models.

---

### Low FPS

Try:

- Lowering camera resolution
- Increasing frame-skip interval
- Disabling expensive detectors
- Using a smaller object-detection model
- Using GPU acceleration

---

# 📌 Known Limitations

DriveGuard DMS is currently a **research/prototype system**.

Known limitations include:

- Gaze estimation is approximate.
- Phone detection requires compatible model weights.
- Camera quality affects detection accuracy.
- Extreme lighting can reduce performance.
- Drowsiness detection can produce false positives and false negatives.
- Full post-event black-box recording requires additional production hardening.
- Real-world automotive deployment requires extensive testing, validation, safety engineering, and certification.
- The system should never be the sole mechanism used to determine whether a driver is safe to drive.

---

# 🔮 Future Improvements

Future versions may include:

- IR/NIR night-vision camera
- Advanced gaze estimation
- Deep-learning-based fatigue classification
- Personalized driver models
- LSTM / Transformer temporal models
- Edge AI deployment
- Raspberry Pi integration
- NVIDIA Jetson deployment
- Vehicle CAN / OBD-II integration
- GPS integration
- Steering behavior analysis
- Physiological sensor integration
- Fleet management dashboard
- Cloud analytics
- Mobile notifications
- Multi-camera monitoring
- Advanced driver-risk prediction
- Integration with **DriveGuard AI Dashcam / Road Intelligence System**

---

# 🚗 Future DriveGuard AI Platform

DriveGuard DMS is designed as **Module 1** of a larger vehicle-safety platform.

## Module 1 — DriveGuard DMS

```text
Driver
   ↓
Face / Eyes / Head / Gaze / Behavior
   ↓
Driver State
   ↓
Driver Risk
```

## Module 2 — DriveGuard Vision

```text
Road
   ↓
Vehicles / Pedestrians / Lanes / Signs / Hazards
   ↓
Road Risk
```

## Combined Platform

```text
                  DRIVEGUARD AI
                       │
          ┌────────────┴────────────┐
          ↓                         ↓
   DRIVER MONITORING           AI DASHCAM
          ↓                         ↓
     Driver Risk               Road Risk
          └────────────┬────────────┘
                       ↓
                  RISK ENGINE
                       ↓
                  SAFETY SCORE
                       ↓
                 ALERT SYSTEM
```

---

# 🎓 Project Applications

DriveGuard DMS can be used as a research and educational platform for:

- Artificial Intelligence
- Machine Learning
- Computer Vision
- Driver Safety
- Human-Computer Interaction
- Real-Time Systems
- Full-Stack Development
- Edge AI
- Automotive Technology

The project is suitable for:

- 🎓 Final-Year Engineering Project
- 💼 AI/ML Portfolio
- 🏆 Hackathons
- 🔬 Research Prototype
- 💻 Internship Demonstration
- 🚗 Automotive AI Experimentation

---

# 👨‍💻 Author

## Athang Gohane

**B.Tech — Computer Science & Engineering (IoT)**  
**Yeshwantrao Chavan College of Engineering (YCCE), Nagpur**

### Areas of Interest

- Artificial Intelligence
- Machine Learning
- Computer Vision
- Web Development
- Data Science
- IoT
- Automotive AI

---

# 📌 Project Credits

**Developed by Athang Gohane**

**DriveGuard DMS**  
*AI-Powered Driver Monitoring, Drowsiness, Fatigue & Distraction Detection System*

---

# 📜 License

Add your preferred open-source or project-specific license here before publishing the repository.

---

## ⭐ Project Vision

> **"Making every journey safer through intelligent driver monitoring and real-time AI."**

DriveGuard DMS is the first module of a larger vision to build a **multimodal AI vehicle-safety platform** combining driver intelligence with road intelligence.

**DriveGuard DMS → DriveGuard Vision → DriveGuard AI**