# File-Share

This Python script sets up a simple HTTP server on your local network and generates a QR code for accessing the server's content. The server allows you to share files from the current directory within your local network.

## Requirements

- Python 3.x
- `os` module (built-in)
- `socket` module (built-in)
- `pyqrcode` library
- `webbrowser` module (built-in)
- `time.sleep` function (built-in)
- `http.server.CGIHTTPRequestHandler` module (built-in)
- `http.server.HTTPServer` module (built-in)

## How to Use

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script using the following command:

   ```
   python script.py
   ```

4. The script will display your PC name, IP address, and the current directory it is serving content from.

5. A QR code will be generated with the server address (e.g., "http://<IP>:<port>") and saved as `myqr.png` in the same directory.

6. The script will automatically open the `myqr.png` image in your default web browser after a short delay.

7. You can access the server from any device connected to your local network by scanning the QR code or entering the server address in a web browser.

8. To stop the server, press `Ctrl + C` in the terminal or command prompt.
