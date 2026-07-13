# Face Recognition Attendance System

A face recognition based attendance system with liveness detection (anti-spoofing).

## Features

- Face recognition using webcam
- Liveness detection to prevent photo/video spoofing
- User registration with face embeddings
- Login/Logout attendance tracking with timestamps

## Requirements

- Python 3.8+
- Webcam

## Installation

### Windows

```
pip install -r requirements_windows.txt
```

### Linux / Mac

```
pip install -r requirements.txt
```

## Usage

```
python main.py
```

### Buttons

- **Register New User** - Add a new user to the system
- **Login** - Mark attendance (login time)
- **Logout** - Mark departure (logout time)

Attendance logs are saved in `log.txt`.

## Project Structure

```
├── main.py                         # Main application
├── util.py                         # Utility functions
├── test.py                         # Liveness detection
├── requirements.txt                # Dependencies
├── db/                             # User face embeddings
├── log.txt                         # Attendance log
├── resources/                      # Model files
│   ├── anti_spoof_models/          # Anti-spoofing weights
│   └── detection_model/            # Face detection model
└── src/                            # Anti-spoofing module
    ├── anti_spoof_predict.py
    ├── generate_patches.py
    ├── utility.py
    ├── model_lib/
    └── data_io/
```

## Owner

Tushar Kakad
