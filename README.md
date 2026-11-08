# 🎓 Attendance System

A Python-based attendance system for **students and teachers**. Teachers mark and manage attendance for their classes, and students can view their own attendance records.

> **Note:** Items marked `[ ... ]` are placeholders. Replace or delete them to match your code.

---

## ✨ Features

### 👩‍🏫 Teacher
- Secure login
- Mark attendance for a class / subject by date `[manually / face recognition / QR]`
- Edit attendance records
- View class-wise and student-wise attendance
- Export attendance reports `[CSV / Excel / PDF]`

### 🎓 Student
- Secure login
- View personal attendance (date-wise and subject-wise)
- See overall attendance percentage
- `[Download attendance report]`

### ⚙️ General
- Data stored in `[SQLite / MySQL / CSV]`
- Simple, easy-to-use interface `[Tkinter / Flask / Django / CLI]`

## 🛠️ Tech Stack

| Area | Tools |
|------|-------|
| Language | Python 3.9+ |
| Interface | `[Tkinter / Flask / Django / CLI]` |
| Database | `[SQLite / MySQL]` |
| Libraries | `[OpenCV, pandas, ...]` |

## 📁 Project Structure

```
attendance-system/
├── [main.py / app.py]      # Entry point
├── [database/]             # Database files and setup scripts
├── [teacher/]              # Teacher module
├── [student/]              # Student module
├── requirements.txt        # Dependencies
├── .env.example            # Environment variable template
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- `pip` and `git`
- `[MySQL server, if using MySQL]`

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Srashannayak2004/[repo-name].git
   cd [repo-name]
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables** *(if used)*
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your own values. Never commit this file.

5. **Set up the database** *(if needed)*
   ```bash
   python [init_db.py]
   ```

## ▶️ Usage

```bash
python [main.py]
```

**For teachers**
1. Log in with your teacher credentials
2. Select the class / subject and date
3. Mark students present or absent
4. Save, then view or export the report

**For students**
1. Log in with your student credentials
2. View your attendance by date or subject
3. Check your overall attendance percentage

## 🗄️ Database Overview

| Table | Purpose |
|-------|---------|
| `students` | Student details (ID, name, class) |
| `teachers` | Teacher details (ID, name, subject) |
| `attendance` | Date, student, subject and status (Present / Absent) |

*(Adjust table names to match your schema.)*

## 📸 Screenshots

<!-- ![Teacher dashboard](screenshots/teacher.png) -->
<!-- ![Student view](screenshots/student.png) -->

## 🗺️ Roadmap

- [ ] Email notifications for low attendance
- [ ] Attendance charts and analytics
- [ ] Leave request feature for students
- [ ] Mobile-friendly interface

## 🤝 Contributing

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m "Add your feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for details.

## 👤 Author

**Srashan Nayak**
- GitHub: [@Srashannayak2004](https://github.com/Srashannayak2004)
