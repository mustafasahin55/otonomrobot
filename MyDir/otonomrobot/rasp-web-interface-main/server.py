import socketio
import eventlet
from hybrid_astar import call_Path

sio = socketio.Server(cors_allowed_origins="http://localhost:3000")  
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print(f"Client {sid} connected to server on port 8080")

@sio.event
def pointSelected(sid, data):
    print(f"Received pointselected request event with data: {data}")
    x, y = data["x"], data["y"]
    yaw = 270
    response_x, response_y, response_yaw, response_direction = call_Path(x, y, yaw)
    print(f"Path result: x={response_x}, y={response_y}, yaw={response_yaw}, direction={response_direction}")

if __name__ == "__main__":
    print("Starting Python server on port 8080") 
    eventlet.wsgi.server(eventlet.listen(("localhost", 8080)), app)

