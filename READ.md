Mission Clock App

A simple microservice project with two Flask apps:

- `clock_app`: Displays the current time and allows decrementing it.
- `button_app`: Contains a button that sends a POST request to decrement the time shown in `clock_app`.

## Architecture

```plaintext
[button_app] --> POST /update_time --> [clock_app]
