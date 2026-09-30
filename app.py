from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

next_id = 3

@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome to the Events RESTful API!"}), 200

# Get All Events Route (Required by Rubric Criteria 2)
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events]), 200


# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    global next_id
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json()
    
    # Input Validation Challenge
    if not data or "title" not in data:
        return jsonify({"error": "Missing required field: title"}), 400

    # TODO: Task 3 - Implement the Loop and Process Each Element
    # (Optional verification loop to ensure no duplicate titles exist)
    for event in events:
        if event.title == data["title"]:
            return jsonify({"error": "Event title already exists"}), 400

    # TODO: Task 4 - Return and Handle Results
    new_event = Event(next_id, data["title"])
    events.append(new_event)
    next_id += 1
    
    return jsonify(new_event.to_dict()), 201


# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Missing title field for update"}), 400

    # TODO: Task 3 - Implement the Loop and Process Each Element
    target_event = None
    for event in events:
        if event.id == event_id:
            target_event = event
            break

    # TODO: Task 4 - Return and Handle Results
    if not target_event:
        return jsonify({"error": f"Event with ID {event_id} not found"}), 404
        
    target_event.title = data["title"]
    return jsonify(target_event.to_dict()), 200


# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    target_event = None

    # TODO: Task 3 - Implement the Loop and Process Each Element
    for event in events:
        if event.id == event_id:
            target_event = event
            break

    # TODO: Task 4 - Return and Handle Results
    if not target_event:
        return jsonify({"error": f"Event with ID {event_id} not found"}), 404
        
    events.remove(target_event)
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)