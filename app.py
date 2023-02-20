from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

start_datetime_str = "2023-06-09 12:00:00"


# Initialize the start datetime
start_datetime = datetime.strptime(start_datetime_str, "%Y-%m-%d %H:%M:%S")

# Define a route for getting the elapsed time
@app.route("/elapsed_time")
def get_elapsed_time():
    # Get the current date and time
    end_datetime = datetime.now()

    # Calculate the difference between end datetime and start datetime
    delta = end_datetime - start_datetime

    # Get the number of days between the two datetimes
    days = delta.days

    # Get the total number of seconds between the two datetimes
    total_seconds = delta.total_seconds()

    # Convert total seconds to hours, minutes, and seconds
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Return the elapsed time as a JSON response
    return jsonify({
        "days": days,
        "hours": int(hours),
        "minutes": int(minutes),
        "seconds": int(seconds)
    })

# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)
