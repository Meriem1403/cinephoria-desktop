import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview
import requests

API_URL = "http://192.168.1.103:8000/api-client"

app = tb.Window(themename="superhero")
app.title("Cinéphoria Employee Dashboard")
app.geometry("1400x820")

sidebar = tb.Frame(app, width=220, bootstyle="dark")
sidebar.pack(side=LEFT, fill=Y)

sections = [
    ("dashboard", "🏠 Dashboard"),
    ("movies", "🎞️ Movies"),
    ("incidents", "⚠️ Incidents"),
    ("showtimes", "🎬 Showtimes"),
    ("reservations", "📅 Reservations"),
    ("rooms", "🪑 Rooms & Seats"),
    ("users", "👤 Users"),
    ("reviews", "⭐ Reviews"),
    ("logout", "🚪 Logout"),
]
sidebar_buttons = {}

main = tb.Frame(app, bootstyle="light")
main.pack(side=LEFT, fill=BOTH, expand=True, padx=0, pady=0)

current_section = ["dashboard"]

def clear_main():
    for child in main.winfo_children():
        child.destroy()
def show_movies():
    clear_main()
    tb.Label(main, text="🎞️ Movies", font=("Segoe UI", 18, "bold")).pack(anchor="w", padx=18, pady=(18,8))
    try:
        res = requests.get(f"{API_URL}/movies", timeout=5)
        res.raise_for_status()
        data = res.json()
        if isinstance(data, dict) and "member" in data:
            movies = data["member"]
        elif isinstance(data, dict):
            movies = [data]
        elif isinstance(data, list):
            movies = data
        else:
            movies = []
    except Exception as e:
        movies = []
        tb.Label(main, text=f"API Error: {e}", font=("Segoe UI", 12)).pack(pady=8)
    if not movies:
        tb.Label(main, text="No movies found.", font=("Segoe UI", 14)).pack(pady=30)
        return
    coldata = [
        {"text": "Title", "stretch": True, "width": 260},
        {"text": "Genre", "width": 130},
        {"text": "Duration", "width": 80},
        {"text": "Release", "width": 110},
        {"text": "Rating", "width": 90},
        {"text": "At Cinema", "width": 90},
    ]
    rowdata = []
    for m in movies:
        rowdata.append([
            m.get("title", ""),
            ", ".join(m.get("genre", [])) if "genre" in m else "",
            m.get("duration", ""),
            m.get("releaseDate", "")[:10] if m.get("releaseDate", "") else "",
            m.get("rating", ""),
            "Yes" if m.get("atCinema") else "No"
        ])
    Tableview(main, coldata=coldata, rowdata=rowdata, paginated=True, searchable=True, autofit=True, bootstyle=SECONDARY).pack(fill=BOTH, expand=True, padx=10, pady=5)
def show_incidents():
    clear_main()
    tb.Label(main, text="⚠️ Incidents", font=("Segoe UI", 18, "bold")).pack(anchor="w", padx=18, pady=(18,8))
    try:
        res = requests.get(f"{API_URL}/incidents", timeout=5)
        res.raise_for_status()
        data = res.json()
        if isinstance(data, dict) and "member" in data:
            incidents = data["member"]
        elif isinstance(data, dict):
            incidents = [data]
        elif isinstance(data, list):
            incidents = data
        else:
            incidents = []
    except Exception as e:
        incidents = []
        tb.Label(main, text=f"API Error: {e}", font=("Segoe UI", 12)).pack(pady=8)
    if not incidents:
        tb.Label(main, text="No incidents found.", font=("Segoe UI", 14)).pack(pady=30)
        return
    coldata = [
        {"text": "Status", "width": 110},
        {"text": "Type", "width": 120},
        {"text": "User", "width": 200},
        {"text": "Room", "width": 100},
        {"text": "Date", "width": 120},
        {"text": "ID", "width": 70},
    ]
    rowdata = []
    for inc in incidents:
        user = inc.get("user", "Unknown")
        room = inc.get("room", "/api-client/rooms/0").split("/")[-1]
        date = inc.get("createdAt", "")[:10]
        rowdata.append([
            inc.get("status", ""),
            inc.get("type", ""),
            user,
            f"Room {room}",
            date,
            inc.get("id", "")
        ])
    Tableview(main, coldata=coldata, rowdata=rowdata, paginated=True, searchable=True, autofit=True, bootstyle=SECONDARY).pack(fill=BOTH, expand=True, padx=10, pady=5)
def show_showtimes():
    clear_main()
    tb.Label(main, text="🎬 Showtimes", font=("Segoe UI", 18, "bold")).pack(anchor="w", padx=18, pady=(18,8))
    try:
        res = requests.get(f"{API_URL}/showtimes", timeout=5)
        res.raise_for_status()
        data = res.json()
        if isinstance(data, dict) and "member" in data:
            showtimes = data["member"]
        elif isinstance(data, dict):
            showtimes = [data]
        elif isinstance(data, list):
            showtimes = data
        else:
            showtimes = []
    except Exception as e:
        showtimes = []
        tb.Label(main, text=f"API Error: {e}", font=("Segoe UI", 12)).pack(pady=8)
    if not showtimes:
        tb.Label(main, text="No showtimes found.", font=("Segoe UI", 14)).pack(pady=30)
        return
    coldata = [
        {"text": "ID", "width": 60},
        {"text": "Movie", "width": 130},
        {"text": "Room", "width": 80},
        {"text": "Date", "width": 110},
        {"text": "Start", "width": 80},
        {"text": "End", "width": 80},
        {"text": "Status", "width": 90},
    ]
    rowdata = []
    for s in showtimes:
        movie_id = s.get("movie", "").split("/")[-1] if "movie" in s else ""
        room_id = s.get("room", "").split("/")[-1] if "room" in s else ""
        movie_title = f"Movie {movie_id}" if movie_id else ""
        room_name = f"Room {room_id}" if room_id else ""
        rowdata.append([
            s.get("id", ""),
            movie_title,
            room_name,
            s.get("date", "")[:10],
            s.get("startTime", "")[11:16] if s.get("startTime", "") else "",
            s.get("endTime", "")[11:16] if s.get("endTime", "") else "",
            s.get("status", ""),
        ])
    Tableview(main, coldata=coldata, rowdata=rowdata, paginated=True, searchable=True, autofit=True, bootstyle=SECONDARY).pack(fill=BOTH, expand=True, padx=10, pady=5)
def show_reservations():
    clear_main()
    tb.Label(main, text="📅 Reservations", font=("Segoe UI", 18, "bold")).pack(anchor="w", padx=18, pady=(18,8))
    try:
        res = requests.get(f"{API_URL}/reservations", timeout=5)
        res.raise_for_status()
        data = res.json()
        if isinstance(data, dict) and "member" in data:
            reservations = data["member"]
        elif isinstance(data, dict):
            reservations = [data]
        elif isinstance(data, list):
            reservations = data
        else:
            reservations = []
    except Exception as e:
        reservations = []
        tb.Label(main, text=f"API Error: {e}", font=("Segoe UI", 12)).pack(pady=8)
    if not reservations:
        tb.Label(main, text="No reservations found.", font=("Segoe UI", 14)).pack(pady=30)
        return
    coldata = [
        {"text": "ID", "width": 60},
        {"text": "User", "width": 120},
        {"text": "Showtime", "width": 110},
        {"text": "Date", "width": 120},
        {"text": "Status", "width": 80},
        {"text": "Total", "width": 80}
    ]
    rowdata = []
    for r in reservations:
        user_id = r.get("user", "").split("/")[-1] if "user" in r else ""
        showtime_id = r.get("showtime", "").split("/")[-1] if "showtime" in r else ""
        rowdata.append([
            r.get("id", ""),
            f"User {user_id}" if user_id else "",
            f"Showtime {showtime_id}" if showtime_id else "",
            r.get("reservationDate", "")[:10],
            r.get("status", ""),
            r.get("totalPrice", "")
        ])
    Tableview(main, coldata=coldata, rowdata=rowdata, paginated=True, searchable=True, autofit=True, bootstyle=SECONDARY).pack(fill=BOTH, expand=True, padx=10, pady=5)
def show_rooms():
    clear_main()
    tb.Label(main, text="🪑 Rooms & Seats", font=("Segoe UI", 18, "bold")).pack(anchor="w", padx=18, pady=(18,8))
    try:
        res = requests.get(f"{API_URL}/rooms", timeout=5)
        res.raise_for_status()
        data = res.json()
        if isinstance(data, dict) and "member" in data:
            rooms = data["member"]
        elif isinstance(data, dict):
            rooms = [data]
        elif isinstance(data, list):
            rooms = data
        else:
            rooms = []
    except Exception as e:
        rooms = []
        tb.Label(main, text=f"API Error: {e}", font=("Segoe UI", 12)).pack(pady=8)
    if not rooms:
        tb.Label(main, text="No rooms found.", font=("Segoe UI", 14)).pack(pady=30)
        return
    coldata = [
        {"text": "Name", "width": 120},
        {"text": "Capacity", "width": 80},
        {"text": "Cinema", "width": 110},
        {"text": "Showtimes", "width": 140},
        {"text": "Equipments", "width": 180},
    ]
    rowdata = []
    for r in rooms:
        showtimes = ", ".join([x.split("/")[-1] for x in r.get("showtimes", [])])
        equipment = ", ".join(r.get("projectionEquipment", []))
        cinema_id = r.get("cinema", "").split("/")[-1] if "cinema" in r else ""
        rowdata.append([
            r.get("name", ""),
            r.get("capacity", ""),
            f"Cinema {cinema_id}" if cinema_id else "",
            showtimes,
            equipment
        ])
    Tableview(main, coldata=coldata, rowdata=rowdata, paginated=True, searchable=True, autofit=True, bootstyle=SECONDARY).pack(fill=BOTH, expand=True, padx=10, pady=5)
def show_users():
    clear_main()
    tb.Label(main, text="👤 Users", font=("Segoe UI", 18, "bold")).pack(anchor="w", padx=18, pady=(18,8))
    try:
        res = requests.get(f"{API_URL}/users", timeout=5)
        res.raise_for_status()
        data = res.json()
        if isinstance(data, dict) and "member" in data:
            users = data["member"]
        elif isinstance(data, dict):
            users = [data]
        elif isinstance(data, list):
            users = data
        else:
            users = []
    except Exception as e:
        users = []
        tb.Label(main, text=f"API Error: {e}", font=("Segoe UI", 12)).pack(pady=8)
    if not users:
        tb.Label(main, text="No users found.", font=("Segoe UI", 14)).pack(pady=30)
        return
    coldata = [
        {"text": "Name", "width": 170},
        {"text": "Email", "width": 220},
        {"text": "City", "width": 120},
        {"text": "Active", "width": 70},
        {"text": "Role", "width": 90},
    ]
    rowdata = []
    for u in users:
        name = f"{u.get('firstName', '')} {u.get('lastName', '')}".strip()
        active = "Yes" if u.get("isActive", False) else "No"
        role_id = u.get("role", "").split("/")[-1] if u.get("role", "") else ""
        city = u.get("city", "")
        rowdata.append([
            name,
            u.get("email", ""),
            city,
            active,
            f"Role {role_id}" if role_id else "",
        ])
    Tableview(main, coldata=coldata, rowdata=rowdata, paginated=True, searchable=True, autofit=True, bootstyle=SECONDARY).pack(fill=BOTH, expand=True, padx=10, pady=5)
def show_reviews():
    clear_main()
    tb.Label(main, text="⭐ Reviews", font=("Segoe UI", 18, "bold")).pack(anchor="w", padx=18, pady=(18,8))
    try:
        res = requests.get(f"{API_URL}/reviews", timeout=5)
        res.raise_for_status()
        data = res.json()
        if isinstance(data, dict) and "member" in data:
            reviews = data["member"]
        elif isinstance(data, dict):
            reviews = [data]
        elif isinstance(data, list):
            reviews = data
        else:
            reviews = []
    except Exception as e:
        reviews = []
        tb.Label(main, text=f"API Error: {e}", font=("Segoe UI", 12)).pack(pady=8)
    if not reviews:
        tb.Label(main, text="No reviews found.", font=("Segoe UI", 14)).pack(pady=30)
        return
    coldata = [
        {"text": "Movie", "width": 110},
        {"text": "User", "width": 110},
        {"text": "Rating", "width": 70},
        {"text": "Comment", "width": 340},
        {"text": "Date", "width": 110},
        {"text": "Approved", "width": 85},
    ]
    rowdata = []
    for r in reviews:
        movie_id = r.get("movie", "").split("/")[-1] if r.get("movie", "") else ""
        user_id = r.get("user", "").split("/")[-1] if r.get("user", "") else ""
        comment = r.get("comment", "")
        rating = r.get("rating", "")
        approved = "Yes" if r.get("isApproved", False) else "No"
        date = r.get("createdAt", "")[:10]
        rowdata.append([
            f"Movie {movie_id}" if movie_id else "",
            f"User {user_id}" if user_id else "",
            rating,
            comment,
            date,
            approved
        ])
    Tableview(main, coldata=coldata, rowdata=rowdata, paginated=True, searchable=True, autofit=True, bootstyle=SECONDARY).pack(fill=BOTH, expand=True, padx=10, pady=5)
def set_active(section_key):
    for key, btn in sidebar_buttons.items():
        if key == section_key:
            btn.config(bootstyle="secondary")
        else:
            btn.config(bootstyle="dark")
    clear_main()
    if section_key == "movies":
        show_movies()
    elif section_key == "incidents":
        show_incidents()
    elif section_key == "showtimes":
        show_showtimes()
    elif section_key == "reservations":
        show_reservations()
    elif section_key == "rooms":
        show_rooms()
    elif section_key == "users":
        show_users()
    elif section_key == "reviews":
        show_reviews()
    elif section_key == "dashboard":
        tb.Label(main, text="🏠 Dashboard (statistiques à venir)", font=("Segoe UI", 22, "bold")).pack(pady=30)
    elif section_key == "logout":
        app.quit()
    current_section[0] = section_key

for key, label in sections:
    b = tb.Button(
        sidebar,
        text=label,
        width=18,
        bootstyle="dark",
        cursor="hand2",
    )
    b.pack(pady=2, padx=18, ipady=7)
    b.config(command=lambda k=key: set_active(k))
    sidebar_buttons[key] = b

set_active("dashboard")
app.mainloop()
