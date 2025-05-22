Python Chat App with File Transfer

A simple multi-client chat application built in Python using sockets and Tkinter, enabling real-time text messaging and basic file transfer between clients over a local network.

Features

  1. Real-time text chat between multiple clients and a central server.

  2. GUI client built with Tkinter featuring a clean dark-themed interface.

  3. Send and receive messages asynchronously using threading.

  4. Basic file transfer support: send files from client to client.

  5. User login by entering a display name.

  6. Server manages multiple client connections and broadcasts messages.

Architecture

  Server: Listens for incoming client connections, manages connected clients, and broadcasts messages.

  Client: Connects to the server, sends/receives messages, and supports file sending/receiving with a user-friendly GUI.

How to Use

  1. Run the server script on a machine accessible by all clients in the network.

  2. Run the client script on each user’s machine.

  3. Enter a username when prompted.

  4. Use the GUI to send text messages or files.

  5. Messages and file notifications appear in the chat window.

Requirements

  1. Python 3.x

  2. Tkinter (usually included with Python)

  3. Network access (all clients and server must be on the same network or properly routed)

Setup

  1. Update the IP address and port in both scripts (ip = "192.168.100.7", port = 55554) to match your server’s IP and desired port.

  2. Run server.py first to start the chat server.

  3. Then run client.py to connect to the server.

Limitations & Notes

  1. File transfer is basic and may not handle very large files or simultaneous transfers well.

  2. The server broadcasts all messages except those sent by the sender.

  3. No encryption or authentication is implemented.

  4. Designed for local network use.

Future Improvements

  1. Add better file transfer protocol (chunk management, progress indicators).

  2. Support for private messaging.

  3. User authentication and encryption.

  4. Improved UI/UX enhancements.
