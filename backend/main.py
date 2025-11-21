from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import get_connection
from models import ChatInput

app = FastAPI()

app.middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.post("/chat")
async def chat_endpoint(data: ChatInput):  
  user_message = data.message

  bot_response = await generate_response(user_message)

  conn = get_connection()
  cursor =conn.cursor()

  cursor.execute(
    "INSERT INTO messages (user_message, bot_message) VALUES (?,?)",
        (user_message, bot_response)
    )

  conn.comit()
  conn.close()

  return {"response":bot_response}

@app.get("/history")
  def get_history():
    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("SELECT * FROM messages ORDER BY id DESC LIMIT 50")
    rows = cursor.fetchall()

    history = [
        {"user": row["user_message"], "bot": row["bot_message"], "time": row["timestamp"]}
        for row in rows
    ]

return {"history": history}
