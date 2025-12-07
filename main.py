# GMfinOS.py

# --- Cài đặt thư viện cần thiết ---
# pip install fastapi uvicorn sqlalchemy pydantic python-multipart pydantic-settings

import logging
from datetime import datetime
from typing import Optional, List
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, JSON, ForeignKey, Text, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from pydantic import BaseModel, ConfigDict
from pydantic_settings import BaseSettings
import os

# --- CẤU HÌNH (config.py) ---
class Settings(BaseSettings):
    app_name: str = "GmFinn OS API"
    database_url: str = "sqlite:///./gmfinnos.db"
    allowed_origins: List[str] = ["http://localhost", "http://127.0.0.1"] # Cập nhật cho phù hợp

    model_config = ConfigDict(env_file=".env", extra="ignore") # Cho phép đọc từ .env

settings = Settings()

# --- DATABASE SETUP (database.py & models/database_models.py) ---
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

DATABASE_URL = settings.database_url
engine = create_engine(DATABASE_URL, echo=False) # Tắt echo cho production
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class App(Base):
    __tablename__ = "apps"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    slug = Column(String, unique=True, index=True)
    icon = Column(String)
    category = Column(String)
    is_core = Column(Boolean, default=False)
    version = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class UserAppInstance(Base):
    __tablename__ = "user_app_instances"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    app_id = Column(Integer, ForeignKey("apps.id"))
    config = Column(JSON, default=dict)
    enabled = Column(Boolean, default=True)
    position_x = Column(Integer, default=100)
    position_y = Column(Integer, default=100)
    created_at = Column(DateTime, default=datetime.utcnow)

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    description = Column(String)
    amount = Column(Integer)
    category = Column(String, default="other")
    created_at = Column(DateTime, default=datetime.utcnow)

class ScheduleEvent(Base):
    __tablename__ = "schedule_events"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    description = Column(Text, nullable=True)
    start_time = Column(String) # Có thể nên là DateTime nếu cần xử lý phức tạp hơn
    end_time = Column(String, nullable=True)
    is_completed = Column(Boolean, default=False)
    event_date = Column(String) # Có thể nên là Date
    created_at = Column(DateTime, default=datetime.utcnow)

class Vocabulary(Base):
    __tablename__ = "vocabularies"
    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, unique=True)
    pronunciation = Column(String)
    definition = Column(Text)
    example = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True) # Có thể để null nếu là từ chung
    learned = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

# --- PYDANTIC SCHEMAS (schemas/schemas.py) ---
class ExpenseCreate(BaseModel):
    description: str
    amount: int
    category: str = "other"
    model_config = ConfigDict(from_attributes=True)

class ExpenseOut(BaseModel):
    id: int
    description: str
    amount: int
    category: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class ScheduleEventCreate(BaseModel):
    title: str
    description: Optional[str] = None
    start_time: str
    end_time: Optional[str] = None
    event_date: str
    model_config = ConfigDict(from_attributes=True)

class ScheduleEventOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    start_time: str
    end_time: Optional[str]
    is_completed: bool
    model_config = ConfigDict(from_attributes=True)

class ScheduleEventUpdate(BaseModel):
    is_completed: bool
    model_config = ConfigDict(from_attributes=True)

class VocabularyOut(BaseModel):
    id: int
    word: str
    pronunciation: str
    definition: str
    example: Optional[str]
    learned: bool
    model_config = ConfigDict(from_attributes=True)

class AppOut(BaseModel):
    id: int
    name: str
    slug: str
    icon: str
    category: str
    description: str
    config: dict
    position: dict
    model_config = ConfigDict(from_attributes=True)

class SystemInfo(BaseModel):
    app_name: str
    database_url: str
    total_users: int
    total_apps: int

# --- DATABASE SESSION DEPENDENCY ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Database error: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")
    finally:
        db.close()

# --- SEED DATA ---
def seed_database(db: Session):
    # Check if data already exists
    if db.query(User).first():
        return

    # Create default user
    user = User(username="gmfinn", email="gmfinn@example.com")
    db.add(user)
    db.commit()
    db.refresh(user) # Cập nhật ID sau khi commit

    # Create core apps
    apps_data = [
        {"name": "English Master AI", "slug": "english", "icon": "fa-graduation-cap", "category": "education", "is_core": True, "version": "1.0", "description": "AI-powered English learning"},
        {"name": "Money Tracker", "slug": "spending", "icon": "fa-wallet", "category": "finance", "is_core": True, "version": "1.0", "description": "Personal expense manager"},
        {"name": "Daily Plan", "slug": "schedule", "icon": "fa-calendar-alt", "category": "productivity", "is_core": True, "version": "1.0", "description": "Smart schedule planner"},
        {"name": "Settings", "slug": "settings", "icon": "fa-cogs", "category": "system", "is_core": True, "version": "1.0", "description": "System configuration"}
    ]
    app_instances = []
    for app_data in apps_data:
        app = App(**app_data)
        db.add(app)
        db.commit()
        db.refresh(app) # Cập nhật ID
        # Tạo instance
        instance = UserAppInstance(
            user_id=user.id,
            app_id=app.id,
            enabled=True,
            position_x=100 + app.id * 50,
            position_y=100 + app.id * 30
        )
        app_instances.append(instance)
    db.add_all(app_instances)

    # Add sample vocabularies
    vocabs = [
        {"word": "Serendipity", "pronunciation": "/ˌser.ənˈdɪp.ə.ti/", "definition": "(n) Sự tình cờ may mắn, khả năng phát hiện ra những điều thú vị một cách ngẫu nhiên."},
        {"word": "Ethereal", "pronunciation": "/iˈθɪə.ri.əl/", "definition": "(adj) Nhẹ nhàng, thanh tao, như thuộc về cõi khác."},
        {"word": "Resilience", "pronunciation": "/rɪˈzɪl.jəns/", "definition": "(n) Khả năng phục hồi, sự kiên cường."},
        {"word": "Ephemeral", "pronunciation": "/ɪˈfem.ər.əl/", "definition": "(adj) Phù du, sớm nở tối tàn."}
    ]
    for vocab_data in vocabs:
        vocab = Vocabulary(**vocab_data)
        db.add(vocab)

    # Add sample expenses
    expenses = [
        {"user_id": user.id, "description": "Cafe sáng", "amount": 35000, "category": "food"},
        {"user_id": user.id, "description": "Đổ xăng", "amount": 50000, "category": "transport"}
    ]
    for exp_data in expenses:
        expense = Expense(**exp_data)
        db.add(expense)

    # Add sample schedule
    today = datetime.now().strftime("%Y-%m-%d")
    events = [
        {"user_id": user.id, "title": "Thức dậy & Vệ sinh", "start_time": "07:00", "end_time": "07:30", "event_date": today, "is_completed": True},
        {"user_id": user.id, "title": "Làm việc sâu (Deep Work)", "description": "Soạn giáo án tiếng Anh", "start_time": "08:00", "end_time": "11:00", "event_date": today, "is_completed": False},
        {"user_id": user.id, "title": "Ăn trưa", "start_time": "12:00", "event_date": today, "is_completed": False},
        {"user_id": user.id, "title": "Họp Online", "start_time": "14:00", "end_time": "16:00", "event_date": today, "is_completed": False}
    ]
    for event_data in events:
        event = ScheduleEvent(**event_data)
        db.add(event)

    db.commit()
    logger.info("Database seeded successfully.")

# --- FASTAPI APP & MIDDLEWARE (main.py) ---
app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"], # Cập nhật nếu cần giới hạn
    allow_headers=["*"], # Cập nhật nếu cần giới hạn
)

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_database(db)
    finally:
        db.close()

# --- API ENDPOINTS (api/endpoints.py) ---

@app.get("/", response_class=HTMLResponse)
def read_root():
    return HTMLResponse(FRONTEND_HTML)

@app.get("/api/system/info", response_model=SystemInfo)
def get_system_info(db: Session = Depends(get_db)):
    total_users = db.query(User).count()
    total_apps = db.query(App).count()
    return SystemInfo(
        app_name=settings.app_name,
        database_url=settings.database_url,
        total_users=total_users,
        total_apps=total_apps
    )

@app.get("/api/user/{user_id}/apps", response_model=List[AppOut])
def get_user_apps(user_id: int, db: Session = Depends(get_db)):
    # Trong thực tế, cần xác thực user_id từ token với user_id trong path
    try:
        instances = db.query(UserAppInstance, App).join(App).filter(
            UserAppInstance.user_id == user_id,
            UserAppInstance.enabled == True
        ).all()
        apps = []
        for inst, app_model in instances:
            apps.append(AppOut(
                id=app_model.id,
                name=app_model.name,
                slug=app_model.slug,
                icon=app_model.icon,
                category=app_model.category,
                description=app_model.description,
                config=inst.config,
                position={"x": inst.position_x, "y": inst.position_y}
            ))
        return apps
    except Exception as e:
        logger.error(f"Error fetching user apps: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/api/user/{user_id}/expenses")
def get_expenses(user_id: int, db: Session = Depends(get_db)):
    # Trong thực tế, cần xác thực user_id từ token với user_id trong path
    try:
        expenses = db.query(Expense).filter(Expense.user_id == user_id).order_by(desc(Expense.created_at)).limit(20).all()
        total = sum([e.amount for e in expenses])
        return {
            "expenses": [
                ExpenseOut(
                    id=e.id,
                    description=e.description,
                    amount=e.amount,
                    category=e.category,
                    created_at=e.created_at
                ).model_dump()
                for e in expenses
            ],
            "total_week": total
        }
    except Exception as e:
        logger.error(f"Error fetching expenses: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/api/user/{user_id}/expenses", response_model=ExpenseOut)
def create_expense(user_id: int, expense: ExpenseCreate, db: Session = Depends(get_db)):
    # Trong thực tế, cần xác thực user_id từ token với user_id trong path
    try:
        new_expense = Expense(
            user_id=user_id,
            description=expense.description,
            amount=expense.amount,
            category=expense.category
        )
        db.add(new_expense)
        db.commit()
        db.refresh(new_expense)
        return ExpenseOut(
            id=new_expense.id,
            description=new_expense.description,
            amount=new_expense.amount,
            category=new_expense.category,
            created_at=new_expense.created_at
        )
    except Exception as e:
        logger.error(f"Error creating expense: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")

@app.delete("/api/user/{user_id}/expenses/{expense_id}")
def delete_expense(user_id: int, expense_id: int, db: Session = Depends(get_db)):
    # Trong thực tế, cần xác thực user_id từ token với user_id trong path
    try:
        expense = db.query(Expense).filter(
            Expense.id == expense_id,
            Expense.user_id == user_id
        ).first()
        if not expense:
            raise HTTPException(status_code=404, detail="Expense not found for this user")
        db.delete(expense)
        db.commit()
        return {"status": "deleted"}
    except Exception as e:
        logger.error(f"Error deleting expense: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/api/user/{user_id}/schedule")
def get_schedule(user_id: int, date: Optional[str] = None, db: Session = Depends(get_db)):
    # Trong thực tế, cần xác thực user_id từ token với user_id trong path
    try:
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
        events = db.query(ScheduleEvent).filter(
            ScheduleEvent.user_id == user_id,
            ScheduleEvent.event_date == date
        ).order_by(ScheduleEvent.start_time).all()
        return {
            "date": date,
            "events": [
                ScheduleEventOut(
                    id=e.id,
                    title=e.title,
                    description=e.description,
                    start_time=e.start_time,
                    end_time=e.end_time,
                    is_completed=e.is_completed
                ).model_dump()
                for e in events
            ]
        }
    except Exception as e:
        logger.error(f"Error fetching schedule: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/api/user/{user_id}/schedule", response_model=ScheduleEventOut)
def create_schedule_event(user_id: int, event: ScheduleEventCreate, db: Session = Depends(get_db)):
    # Trong thực tế, cần xác thực user_id từ token với user_id trong path
    try:
        new_event = ScheduleEvent(
            user_id=user_id,
            title=event.title,
            description=event.description,
            start_time=event.start_time,
            end_time=event.end_time,
            event_date=event.event_date
        )
        db.add(new_event)
        db.commit()
        db.refresh(new_event)
        return ScheduleEventOut(
            id=new_event.id,
            title=new_event.title,
            description=new_event.description,
            start_time=new_event.start_time,
            end_time=new_event.end_time,
            is_completed=new_event.is_completed
        )
    except Exception as e:
        logger.error(f"Error creating schedule event: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")

@app.patch("/api/user/{user_id}/schedule/{event_id}")
def update_schedule_event(user_id: int, event_id: int, update: ScheduleEventUpdate, db: Session = Depends(get_db)):
    # Trong thực tế, cần xác thực user_id từ token với user_id trong path
    try:
        event = db.query(ScheduleEvent).filter(
            ScheduleEvent.id == event_id,
            ScheduleEvent.user_id == user_id
        ).first()
        if not event:
            raise HTTPException(status_code=404, detail="Event not found for this user")
        event.is_completed = update.is_completed
        db.commit()
        return {"status": "updated", "is_completed": event.is_completed}
    except Exception as e:
        logger.error(f"Error updating schedule event: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/api/vocabularies", response_model=List[VocabularyOut])
def get_vocabularies(limit: int = 10, db: Session = Depends(get_db)):
    try:
        vocabs = db.query(Vocabulary).order_by(Vocabulary.id).limit(limit).all()
        return [
            VocabularyOut(
                id=v.id,
                word=v.word,
                pronunciation=v.pronunciation,
                definition=v.definition,
                example=v.example,
                learned=v.learned
            ) for v in vocabs
        ]
    except Exception as e:
        logger.error(f"Error fetching vocabularies: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.patch("/api/vocabularies/{vocab_id}")
def mark_vocabulary_learned(vocab_id: int, db: Session = Depends(get_db)):
    try:
        vocab = db.query(Vocabulary).filter(Vocabulary.id == vocab_id).first()
        if not vocab:
            raise HTTPException(status_code=404, detail="Vocabulary not found")
        vocab.learned = True
        db.commit()
        return {"status": "updated", "learned": True}
    except Exception as e:
        logger.error(f"Error updating vocabulary: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")

# --- FRONTEND HTML (Giữ nguyên như trước) ---
FRONTEND_HTML = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GmFinn OS - AI Powered Desktop</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        body { 
            font-family: 'Segoe UI', sans-serif; 
            overflow: hidden; 
            user-select: none; 
            background: url('https://images.unsplash.com/photo-1477346611705-65d1883cee1e?q=80&w=2070&auto=format&fit=crop') no-repeat center center fixed;
            background-size: cover;
        }
        .glass-window {
            background: rgba(30, 30, 30, 0.9);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6);
            border-radius: 12px;
            position: absolute;
            display: flex;
            flex-direction: column;
            min-width: 300px;
            min-height: 200px;
            overflow: hidden;
            color: white;
        }
        .glass-taskbar {
            background: rgba(10, 10, 10, 0.8);
            backdrop-filter: blur(10px);
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }
        .window-header {
            background: linear-gradient(90deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.0) 100%);
            padding: 10px 14px;
            cursor: grab;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }
        .window-header:active { cursor: grabbing; }
        .desktop-icon {
            width: 84px;
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 16px;
            padding: 10px;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.2s;
            text-align: center;
        }
        .desktop-icon:hover { background: rgba(255, 255, 255, 0.15); }
        .desktop-icon i { font-size: 36px; margin-bottom: 8px; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.6)); }
        .desktop-icon span { font-size: 12px; color: white; text-shadow: 0 2px 4px black; line-height: 1.2; font-weight: 500; }
        #start-menu {
            position: absolute;
            bottom: 54px;
            left: 10px;
            width: 320px;
            height: 420px;
            background: rgba(25, 25, 25, 0.95);
            backdrop-filter: blur(20px);
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            display: none;
            flex-direction: column;
            z-index: 9999;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
            animation: slideUp 0.2s ease-out;
        }
        @keyframes slideUp { from { transform: translateY(20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
        .ai-loading {
            display: inline-block;
            width: 16px;
            height: 16px;
            border: 2px solid rgba(255,255,255,0.3);
            border-radius: 50%;
            border-top-color: #fff;
            animation: spin 1s ease-in-out infinite;
            margin-right: 8px;
        }
        @keyframes spin { to { transform: rotate(360deg); } }
        .window-opening { animation: popIn 0.2s cubic-bezier(0.1, 0.9, 0.2, 1); }
        @keyframes popIn { from { transform: scale(0.95); opacity: 0; } to { transform: scale(1); opacity: 1; } }
    </style>
</head>
<body class="text-white h-screen w-screen overflow-hidden">
    <div id="desktop" class="w-full h-full relative p-2 flex flex-col flex-wrap content-start">
        <div id="desktop-icons-container"></div>
    </div>
    <div id="windows-container"></div>
    <div id="start-menu">
        <div class="p-5 bg-black/40 border-b border-white/5">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-full bg-gradient-to-br from-blue-600 to-purple-600 flex items-center justify-center text-lg font-bold shadow-lg">G</div>
                <div>
                    <div class="font-bold">GmFinn Admin</div>
                    <div class="text-xs text-gray-400 flex items-center gap-1"><div class="w-2 h-2 rounded-full bg-green-500"></div> Online</div>
                </div>
            </div>
        </div>
        <div id="start-menu-apps" class="p-2 flex-1 overflow-y-auto">
            <div class="text-xs text-gray-500 px-3 py-2 font-bold tracking-wider">PINNED APPS</div>
        </div>
        <div class="p-3 bg-black/40 border-t border-white/5 flex justify-between text-gray-400 rounded-b-xl">
            <button class="hover:text-white px-3 py-1.5 rounded hover:bg-white/10 transition"><i class="fas fa-lock"></i></button>
            <button class="hover:text-red-400 px-3 py-1.5 rounded hover:bg-white/10 transition"><i class="fas fa-power-off"></i></button>
        </div>
    </div>
    <div id="taskbar" class="glass-taskbar absolute bottom-0 w-full h-12 flex items-center justify-between px-2 z-[10000]">
        <div class="flex items-center gap-1 h-full">
            <button onclick="toggleStartMenu()" class="h-10 w-10 rounded hover:bg-white/10 flex items-center justify-center transition active:scale-95 group">
                <i class="fab fa-windows text-xl text-blue-300 group-hover:text-blue-200 transition-all"></i>
            </button>
            <div class="ml-2 hidden md:flex items-center bg-white/5 border border-white/5 rounded-md px-3 h-8 w-56 hover:bg-white/10 transition">
                <i class="fas fa-search text-gray-400 text-xs mr-2"></i>
                <input type="text" placeholder="Search apps..." class="bg-transparent border-none text-xs text-white focus:outline-none w-full placeholder-gray-500">
            </div>
            <div class="w-[1px] h-6 bg-gray-700 mx-3"></div>
            <div id="active-apps" class="flex items-center gap-1"></div>
        </div>
        <div class="flex items-center gap-2 px-2 text-xs text-gray-300 h-full">
            <div class="hover:bg-white/10 p-2 rounded cursor-pointer transition"><i class="fas fa-wifi"></i></div>
            <div class="hover:bg-white/10 p-2 rounded cursor-pointer transition"><i class="fas fa-volume-up"></i></div>
            <div class="text-right px-3 py-1 hover:bg-white/10 rounded cursor-pointer select-none transition">
                <div id="clock-time" class="font-bold text-white">10:30 AM</div>
                <div id="clock-date" class="text-[10px] text-gray-400">21/11/2024</div>
            </div>
        </div>
    </div>
    <script>
        const API_BASE = window.location.origin;
        const CURRENT_USER_ID = 1; // PHẢI ĐƯỢC LẤY TỪ XÁC THỰC TRONG THỰC TẾ
        let zIndexCounter = 100;
        let openWindows = {};
        // ==================== LOAD APPS FROM BACKEND ====================
        async function loadApps() {
            try {
                const res = await fetch(`${API_BASE}/api/user/${CURRENT_USER_ID}/apps`);
                const apps = await res.json();
                const desktopContainer = document.getElementById('desktop-icons-container');
                const startMenuContainer = document.getElementById('start-menu-apps');
                desktopContainer.innerHTML = '';
                apps.forEach(app => {
                    // Desktop icon
                    const icon = document.createElement('div');
                    icon.className = 'desktop-icon';
                    icon.innerHTML = `
                        <i class="fas ${app.icon} text-blue-400"></i>
                        <span>${app.name}</span>
                    `;
                    icon.onclick = () => openApp(app.slug);
                    desktopContainer.appendChild(icon);
                    // Start menu item
                    const menuItem = document.createElement('div');
                    menuItem.className = 'flex items-center gap-3 p-2 mx-1 hover:bg-white/10 rounded-lg cursor-pointer transition';
                    menuItem.innerHTML = `
                        <div class="w-9 h-9 bg-blue-500/20 rounded-lg flex items-center justify-center text-blue-400">
                            <i class="fas ${app.icon}"></i>
                        </div>
                        <span class="text-sm">${app.name}</span>
                    `;
                    menuItem.onclick = () => { openApp(app.slug); toggleStartMenu(); };
                    startMenuContainer.appendChild(menuItem);
                });
            } catch (e) {
                console.error("Failed to load apps:", e);
            }
        }
        // ==================== WINDOW MANAGEMENT ====================
        function openApp(slug) {
            if (openWindows[slug]) {
                focusWindow(slug);
                return;
            }
            let windowHTML = '';
            switch(slug) {
                case 'english':
                    windowHTML = createEnglishApp();
                    break;
                case 'spending':
                    windowHTML = createSpendingApp();
                    break;
                case 'schedule':
                    windowHTML = createScheduleApp();
                    break;
                case 'settings':
                    windowHTML = createSettingsApp();
                    break;
                default:
                    windowHTML = `<div class="p-6">App "${slug}" đang được phát triển...</div>`;
            }
            createWindow(slug, windowHTML, 400, 500);
            // Load app data
            if (slug === 'spending') loadExpenses();
            if (slug === 'schedule') loadSchedule();
            if (slug === 'english') loadVocabularies();
        }
        function createWindow(id, content, width = 400, height = 500) {
            const windowDiv = document.createElement('div');
            windowDiv.id = `window-${id}`;
            windowDiv.className = 'glass-window window-opening';
            windowDiv.style.cssText = `width: ${width}px; height: ${height}px; top: ${100 + Object.keys(openWindows).length * 30}px; left: ${200 + Object.keys(openWindows).length * 30}px; z-index: ${zIndexCounter++};`;
            windowDiv.innerHTML = content;
            document.getElementById('windows-container').appendChild(windowDiv);
            openWindows[id] = windowDiv;
            addToTaskbar(id);
            focusWindow(id);
        }
        function closeWindow(id) {
            const win = openWindows[id];
            if (win) {
                win.remove();
                delete openWindows[id];
                removeFromTaskbar(id);
            }
        }
        function focusWindow(id) {
            const win = openWindows[id];
            if (win) {
                win.style.zIndex = zIndexCounter++;
                win.style.display = 'flex';
            }
        }
        function minimizeWindow(id) {
            const win = openWindows[id];
            if (win) win.style.display = 'none';
        }
        function dragWindow(e, id) {
            const el = openWindows[id];
            if (!el) return;
            focusWindow(id);
            let shiftX = e.clientX - el.getBoundingClientRect().left;
            let shiftY = e.clientY - el.getBoundingClientRect().top;
            function moveAt(pageX, pageY) {
                let newLeft = Math.max(0, pageX - shiftX);
                let newTop = Math.max(0, pageY - shiftY);
                el.style.left = newLeft + 'px';
                el.style.top = newTop + 'px';
            }
            function onMouseMove(event) {
                moveAt(event.pageX, event.pageY);
            }
            document.addEventListener('mousemove', onMouseMove);
            document.onmouseup = function() {
                document.removeEventListener('mousemove', onMouseMove);
                document.onmouseup = null;
            };
        }
        // ==================== TASKBAR ====================
        function addToTaskbar(id) {
            if (document.getElementById(`taskbar-${id}`)) return;
            const iconMap = {
                'english': 'fa-graduation-cap text-blue-400',
                'spending': 'fa-wallet text-green-400',
                'schedule': 'fa-calendar-alt text-orange-400',
                'settings': 'fa-cogs text-gray-300'
            };
            const btn = document.createElement('div');
            btn.id = `taskbar-${id}`;
            btn.className = 'h-10 w-10 rounded hover:bg-white/10 flex items-center justify-center cursor-pointer relative group transition';
            btn.innerHTML = `
                <i class="fas ${iconMap[id] || 'fa-window-maximize'} text-lg"></i>
                <div class="absolute bottom-0 h-0.5 w-1/2 bg-gray-400 rounded group-hover:w-full transition-all"></div>
            `;
            btn.onclick = () => focusWindow(id);
            document.getElementById('active-apps').appendChild(btn);
        }
        function removeFromTaskbar(id) {
            const btn = document.getElementById(`taskbar-${id}`);
            if (btn) btn.remove();
        }
        function toggleStartMenu() {
            const menu = document.getElementById('start-menu');
            menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';
        }
        // ==================== ENGLISH APP ====================
        let currentVocabIndex = 0;
        let vocabularies = [];
        function createEnglishApp() {
            return `
                <div class="window-header" onmousedown="dragWindow(event, 'english')">
                    <div class="flex items-center gap-2">
                        <i class="fas fa-graduation-cap text-blue-400"></i>
                        <span class="text-sm font-semibold">English Master AI</span>
                    </div>
                    <div class="flex gap-2">
                        <button class="text-gray-400 hover:text-white" onclick="minimizeWindow('english')"><i class="fas fa-minus"></i></button>
                        <button class="text-red-400 hover:text-red-200" onclick="closeWindow('english')"><i class="fas fa-times"></i></button>
                    </div>
                </div>
                <div class="flex-1 p-6 flex flex-col">
                    <div class="text-xs text-blue-300 mb-2 tracking-widest font-bold">DAILY VOCABULARY</div>
                    <h1 class="text-5xl font-bold mb-2 text-white tracking-tight" id="vocab-word">Loading...</h1>
                    <p class="text-gray-400 italic mb-6 text-lg" id="vocab-pronun"></p>
                    <div class="bg-white/10 p-5 rounded-xl flex-1 border border-white/5 overflow-y-auto">
                        <div id="vocab-content" class="text-sm leading-relaxed text-gray-200"></div>
                    </div>
                    <div class="grid grid-cols-2 gap-3 mt-4">
                        <button class="py-2.5 bg-indigo-600/80 hover:bg-indigo-500 rounded-lg transition flex items-center justify-center gap-2 border border-indigo-400/30" onclick="speakWord()">
                            <i class="fas fa-volume-up"></i> <span>Nghe</span>
                        </button>
                        <button class="py-2.5 bg-gray-700/80 hover:bg-gray-600 rounded-lg transition border border-white/10" onclick="markLearned()">
                            <i class="fas fa-check"></i> Đã học
                        </button>
                        <button class="col-span-2 py-2.5 bg-blue-600 hover:bg-blue-500 rounded-lg transition font-bold text-white" onclick="nextVocab()">
                            Từ tiếp theo <i class="fas fa-arrow-right ml-1"></i>
                        </button>
                    </div>
                </div>
            `;
        }
        async function loadVocabularies() {
            try {
                const res = await fetch(`${API_BASE}/api/vocabularies`);
                vocabularies = await res.json();
                currentVocabIndex = 0;
                displayCurrentVocab();
            } catch (e) {
                console.error("Failed to load vocabularies:", e);
            }
        }
        function displayCurrentVocab() {
            if (vocabularies.length === 0) return;
            const vocab = vocabularies[currentVocabIndex];
            document.getElementById('vocab-word').textContent = vocab.word;
            document.getElementById('vocab-pronun').textContent = vocab.pronunciation;
            document.getElementById('vocab-content').innerHTML = vocab.definition;
        }
        function nextVocab() {
            currentVocabIndex = (currentVocabIndex + 1) % vocabularies.length;
            displayCurrentVocab();
        }
        function speakWord() {
            const word = document.getElementById('vocab-word').textContent;
            const utterance = new SpeechSynthesisUtterance(word);
            utterance.lang = 'en-US';
            speechSynthesis.speak(utterance);
        }
        async function markLearned() {
            if (vocabularies.length === 0) return;
            const vocab = vocabularies[currentVocabIndex];
            try {
                await fetch(`${API_BASE}/api/vocabularies/${vocab.id}`, {
                    method: 'PATCH'
                });
                alert('✅ Đã đánh dấu học xong!');
                nextVocab();
            } catch (e) {
                console.error("Failed to mark learned:", e);
            }
        }
        // ==================== SPENDING APP ====================
        function createSpendingApp() {
            return `
                <div class="window-header" onmousedown="dragWindow(event, 'spending')">
                    <div class="flex items-center gap-2">
                        <i class="fas fa-wallet text-green-400"></i>
                        <span class="text-sm font-semibold">Money Tracker</span>
                    </div>
                    <div class="flex gap-2">
                        <button class="text-gray-400 hover:text-white" onclick="minimizeWindow('spending')"><i class="fas fa-minus"></i></button>
                        <button class="text-red-400 hover:text-red-200" onclick="closeWindow('spending')"><i class="fas fa-times"></i></button>
                    </div>
                </div>
                <div class="flex-1 p-5 overflow-y-auto">
                    <div class="bg-gradient-to-br from-green-900/50 to-emerald-900/50 border border-green-500/30 rounded-xl p-4 mb-5 text-center">
                        <div class="text-xs text-green-300 uppercase font-bold tracking-wide">Tổng chi tuần này</div>
                        <div class="text-4xl font-bold text-white mt-1" id="total-spending">0đ</div>
                    </div>
                    <div class="mb-5">
                        <label class="text-xs text-gray-400 ml-1 font-semibold">NHẬP NHANH</label>
                        <div class="flex gap-2 mt-2">
                            <input id="expense-input" type="text" placeholder="VD: 30000 Cafe sáng" class="flex-1 bg-black/40 border border-gray-600 rounded-lg px-3 py-2.5 text-sm focus:border-green-500 focus:ring-1 focus:ring-green-500 outline-none text-white">
                            <button class="bg-green-600 px-3.5 rounded-lg hover:bg-green-500 transition" onclick="addExpense()">
                                <i class="fas fa-plus"></i>
                            </button>
                        </div>
                    </div>
                    <div class="text-xs text-gray-500 font-bold ml-1 tracking-wider mb-3">LỊCH SỬ GẦN ĐÂY</div>
                    <div id="expenses-list" class="space-y-3"></div>
                </div>
            `;
        }
        async function loadExpenses() {
            try {
                const res = await fetch(`${API_BASE}/api/user/${CURRENT_USER_ID}/expenses`);
                const data = await res.json();
                document.getElementById('total-spending').textContent = `${(data.total_week / 1000).toFixed(0)}k`;
                const listEl = document.getElementById('expenses-list');
                listEl.innerHTML = data.expenses.map(exp => `
                    <div class="flex justify-between items-center p-3 bg-white/5 hover:bg-white/10 rounded-lg transition cursor-pointer border border-white/5 group">
                        <div class="flex items-center gap-3 flex-1">
                            <div class="w-9 h-9 rounded-full bg-orange-500/20 flex items-center justify-center text-orange-400">
                                <i class="fas fa-shopping-bag"></i>
                            </div>
                            <div>
                                <div class="text-sm font-medium">${exp.description}</div>
                                <div class="text-[10px] text-gray-400">${exp.created_at}</div>
                            </div>
                        </div>
                        <div class="flex items-center gap-2">
                            <div class="text-red-400 font-mono text-sm font-bold">-${(exp.amount / 1000).toFixed(0)}k</div>
                            <button class="opacity-0 group-hover:opacity-100 text-red-400 hover:text-red-300 transition" onclick="deleteExpense(${exp.id})">
                                <i class="fas fa-trash text-xs"></i>
                            </button>
                        </div>
                    </div>
                `).join('');
            } catch (e) {
                console.error("Failed to load expenses:", e);
            }
        }
        async function addExpense() {
            const input = document.getElementById('expense-input');
            const text = input.value.trim();
            if (!text) return;
            // Parse input: "30000 Cafe sáng" or "30k Cafe"
            const match = text.match(/^(\d+)k?\s+(.+)$/i);
            if (!match) {
                alert('Format: số_tiền mô_tả (VD: 30000 Cafe sáng)');
                return;
            }
            let amount = parseInt(match[1]);
            if (text.toLowerCase().includes('k')) {
                amount *= 1000;
            }
            const description = match[2];
            try {
                await fetch(`${API_BASE}/api/user/${CURRENT_USER_ID}/expenses`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        description: description,
                        amount: amount,
                        category: 'other'
                    })
                });
                input.value = '';
                loadExpenses();
            } catch (e) {
                console.error("Failed to add expense:", e);
                alert('Lỗi khi thêm chi tiêu!');
            }
        }
        async function deleteExpense(expenseId) {
            if (!confirm('Xóa khoản chi này?')) return;
            try {
                await fetch(`${API_BASE}/api/user/${CURRENT_USER_ID}/expenses/${expenseId}`, {
                    method: 'DELETE'
                });
                loadExpenses();
            } catch (e) {
                console.error("Failed to delete expense:", e);
            }
        }
        // ==================== SCHEDULE APP ====================
        function createScheduleApp() {
            return `
                <div class="window-header" onmousedown="dragWindow(event, 'schedule')">
                    <div class="flex items-center gap-2">
                        <i class="fas fa-calendar-alt text-orange-400"></i>
                        <span class="text-sm font-semibold">Daily Plan</span>
                    </div>
                    <div class="flex gap-2">
                        <button class="text-gray-400 hover:text-white" onclick="minimizeWindow('schedule')"><i class="fas fa-minus"></i></button>
                        <button class="text-red-400 hover:text-red-200" onclick="closeWindow('schedule')"><i class="fas fa-times"></i></button>
                    </div>
                </div>
                <div class="flex-1 flex flex-col bg-[#1e1e1e]">
                    <div class="p-3 bg-gray-800/50 border-b border-white/5">
                        <div class="flex gap-2">
                            <input id="event-title" type="text" placeholder="Tiêu đề..." class="flex-1 bg-black/40 border border-gray-600 rounded px-2 py-1 text-xs text-white outline-none">
                            <input id="event-time" type="time" class="bg-black/40 border border-gray-600 rounded px-2 py-1 text-xs text-white outline-none">
                            <button onclick="addScheduleEvent()" class="bg-orange-600 hover:bg-orange-500 px-3 rounded text-xs transition">
                                <i class="fas fa-plus"></i>
                            </button>
                        </div>
                    </div>
                    <div class="p-4 relative overflow-y-auto flex-1" id="schedule-timeline">
                        <div class="absolute left-6 top-4 bottom-4 w-0.5 bg-gray-700"></div>
                    </div>
                </div>
            `;
        }
        async function loadSchedule() {
            try {
                const today = new Date().toISOString().split('T')[0];
                const res = await fetch(`${API_BASE}/api/user/${CURRENT_USER_ID}/schedule?date=${today}`);
                const data = await res.json();
                const timeline = document.getElementById('schedule-timeline');
                timeline.innerHTML = '<div class="absolute left-6 top-4 bottom-4 w-0.5 bg-gray-700"></div>';
                const now = new Date();
                const currentTime = `${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}`;
                data.events.forEach(event => {
                    const isActive = event.start_time <= currentTime && (!event.end_time || event.end_time >= currentTime);
                    const isPast = event.is_completed || (event.end_time && event.end_time < currentTime);
                    const eventEl = document.createElement('div');
                    eventEl.className = 'relative pl-8 mb-6 group';
                    eventEl.innerHTML = `
                        <div class="absolute left-[${isActive ? '3px' : '5px'}] top-1 w-${isActive ? '4' : '3'} h-${isActive ? '4' : '3'} bg-${isActive ? 'orange-500 animate-pulse shadow-[0_0_15px_rgba(249,115,22,0.6)]' : isPast ? 'gray-600' : 'gray-500'} rounded-full border-2 border-[#1e1e1e] z-10"></div>
                        <div class="text-xs ${isActive ? 'text-orange-400 font-bold' : 'text-gray-400'} mb-1">
                            ${isActive ? 'NOW: ' : ''}${event.start_time}${event.end_time ? ' - ' + event.end_time : ''}
                        </div>
                        <div class="${isActive ? 'p-3 bg-orange-500/10 border-l-2 border-orange-500 rounded-r backdrop-blur-sm' : ''} text-sm ${isPast ? 'line-through text-gray-500' : 'text-white'}">
                            <div class="font-bold ${isActive ? 'text-orange-100' : ''}">${event.title}</div>
                            ${event.description ? `<div class="text-xs text-gray-400 mt-1">${event.description}</div>` : ''}
                        </div>
                        ${!isPast ? `<button onclick="toggleEventComplete(${event.id}, ${!event.is_completed})" class="absolute right-0 top-0 opacity-0 group-hover:opacity-100 text-green-400 hover:text-green-300 text-xs transition">
                            <i class="fas fa-check-circle"></i>
                        </button>` : ''}
                    `;
                    timeline.appendChild(eventEl);
                });
            } catch (e) {
                console.error("Failed to load schedule:", e);
            }
        }
        async function addScheduleEvent() {
            const title = document.getElementById('event-title').value.trim();
            const time = document.getElementById('event-time').value;
            if (!title || !time) {
                alert('Vui lòng nhập đầy đủ thông tin!');
                return;
            }
            try {
                const today = new Date().toISOString().split('T')[0];
                await fetch(`${API_BASE}/api/user/${CURRENT_USER_ID}/schedule`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        title: title,
                        start_time: time,
                        event_date: today
                    })
                });
                document.getElementById('event-title').value = '';
                document.getElementById('event-time').value = '';
                loadSchedule();
            } catch (e) {
                console.error("Failed to add event:", e);
            }
        }
        async function toggleEventComplete(eventId, completed) {
            try {
                await fetch(`${API_BASE}/api/user/${CURRENT_USER_ID}/schedule/${eventId}`, {
                    method: 'PATCH',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ is_completed: completed })
                });
                loadSchedule();
            } catch (e) {
                console.error("Failed to toggle event:", e);
            }
        }
        // ==================== SETTINGS APP ====================
        function createSettingsApp() {
            return `
                <div class="window-header" onmousedown="dragWindow(event, 'settings')">
                    <div class="flex items-center gap-2">
                        <i class="fas fa-cogs text-gray-300"></i>
                        <span class="text-sm font-semibold">Settings</span>
                    </div>
                    <div class="flex gap-2">
                        <button class="text-red-400 hover:text-red-200" onclick="closeWindow('settings')"><i class="fas fa-times"></i></button>
                    </div>
                </div>
                <div class="p-4">
                    <h3 class="text-xs font-bold text-gray-500 uppercase mb-3">System</h3>
                    <div class="flex justify-between items-center mb-4">
                        <span>Dark Mode</span>
                        <i class="fas fa-toggle-on text-green-400 text-xl cursor-pointer"></i>
                    </div>
                    <div class="text-center mt-4">
                        <button class="text-red-400 text-xs hover:underline" onclick="location.reload()">Restart System</button>
                    </div>
                </div>
            `;
        }
        // ==================== SYSTEM CLOCK ====================
        setInterval(() => {
            const now = new Date();
            document.getElementById('clock-time').textContent = now.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
            document.getElementById('clock-date').textContent = now.toLocaleDateString('vi-VN');
        }, 1000);
        // ==================== EVENT LISTENERS ====================
        document.getElementById('desktop').addEventListener('click', (e) => {
            if (e.target.id === 'desktop' || e.target.id === 'desktop-icons-container') {
                document.getElementById('start-menu').style.display = 'none';
            }
        });
        document.ondragstart = () => false;
        // Allow Enter key in expense input
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && e.target.id === 'expense-input') {
                addExpense();
            }
        });
        // ==================== INITIALIZATION ====================
        document.addEventListener('DOMContentLoaded', () => {
            loadApps();
        });
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting GmFinn OS Full Stack System...")
    print(f"📊 Database: {settings.database_url}")
    print("🌐 Server: http://127.0.0.1:8000")
    print("✨ Features: Real-time data sync, Full CRUD operations")
    print("📋 API Docs: http://127.0.0.1:8000/docs (Swagger UI)")
    print("📋 API Docs: http://127.0.0.1:8000/redoc (ReDoc)")
    uvicorn.run(app, host="127.0.0.1", port=8000)