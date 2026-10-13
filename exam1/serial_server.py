import flask
import builtin
import threading


app = flask.Flask(__name__, static_url_path="", static_folder="public")

serial_lock = threading.Lock()
builtinled = builtin.BuiltinLED("/dev/ttyACM1")

@app.get("/")
def handle_naked_domain():
    return flask.redirect("/index.html")


@app.get("/api/<command>")
def handle_arduino_commands(command):
    with serial_lock:
        response = builtinled.send_command(command)
    return response

@app.get("/api/led/on")
def handle_led_on():
    with serial_lock:
        response = builtinled.send_command("LED ON")
    return response

@app.get("/api/led/off")
def handle_led_off():
    with serial_lock:
        response = builtinled.send_command("LED OFF")
    return response

@app.get("/api/flash/<int:count>/<int:period>")
def handle_led_flash(count, period):
    with serial_lock:
        response = builtinled.send_command(f"FLASH {count} {period}")
    return response


if __name__ == "__main__":
    print("Running flask!")
    builtinled.connect()
    try:
        app.run(host="0.0.0.0", port=5000, use_reloader=False)
    finally:
        print("Disconnecting plate loader")
        builtinled.disconnect()