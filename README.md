<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <h1 style="margin: 10px 0;">Chat Application</h1>
  <h3 style="margin: 10px 0;">A Lightweight TCP and UDP Chat Server and Client</h3>
  
  <p style="text-align: left; max-width: 700px; margin: 0 auto;">
    This project demonstrates the fundamentals of network programming using Python sockets and multithreading. The chat application supports multiple clients for real-time message broadcasting through TCP and UDP connections.
  </p>
  
  <ul style="text-align: left; list-style-type: none; padding-left: 0; max-width: 700px; margin: 0 auto;">
    <li>🌐 <span class="icon">Reliable Messaging:</span> Real-time messaging between clients using TCP for reliable delivery.</li>
    <li>🚀 <span class="icon">High-Speed Messaging:</span> Optional UDP for faster, less reliable communication.</li>
    <li>🤝 <span class="icon">Scalable Architecture:</span> Supports multiple clients with a threaded design for simultaneous message handling.</li>
    <li>💡 <span class="icon">Perfect for Learning:</span> A great way to understand socket programming, threading, and client-server architectures.</li>
  </ul>
  
  <div class="section future-enhancements">
    <h3>Future Enhancements:</h3>
    <ul>
      <li>🔒 Adding user authentication for secure access</li>
      <li>🔑 Implementing encryption for secure messaging</li>
      <li>📈 Building a GUI interface for ease of use</li>
    </ul>
  </div>

  <div class="section architecture">
    <h3>Architecture</h3>
    <p>
      The chat server maintains two types of connections:
    </p>
    <ul>
      <li>🔹 <span class="icon">TCP Connection:</span> Provides reliable, ordered, and persistent message exchange between the server and clients.</li>
      <li>🔹 <span class="icon">UDP Connection:</span> Allows for faster but less reliable message broadcasting, enabling quicker communication.</li>
    </ul>
    <p>
      Clients can connect via TCP and optionally send messages via UDP for faster, real-time message broadcasting.
    </p>
  </div>

  <div class="section project-structure">
    <h3>Project Structure</h3>
    <ul>
      <li>📄 <strong>Server.py:</strong> Manages TCP and UDP connections, handling message broadcasts to all connected clients.</li>
      <li>📄 <strong>Client1.py and Client2.py:</strong> Client applications that connect to the server, allowing users to send and receive messages over TCP and optionally via UDP.</li>
    </ul>
  </div>

  <div class="section usage">
    <h3>Usage</h3>
    <ul>
      <li>▶️ <strong>Start the Server:</strong> Run <code>Server.py</code> to initialize TCP and UDP connections.</li>
      <li>▶️ <strong>Start Clients:</strong> Run <code>Client1.py</code> and <code>Client2.py</code>, or multiple instances, to simulate users in the chatroom.</li>
      <li>💬 <strong>Messaging:</strong> Type messages in the client terminal to send via TCP for reliable delivery. Use UDP for faster, less reliable delivery if needed.</li>
      <li>📣 <strong>Message Broadcast:</strong> Messages sent by one client are broadcast to all other connected clients.</li>
    </ul>
  </div>

  <div class="section getting-started">
    <h3>Getting Started</h3>
    <p><strong>Prerequisites:</strong> <code>Python 3.x</code> installed on your machine.</p>
    
  <h4>Installation</h4>
    <ul>
      <h3>1. Clone the repository:</h3>
      <li><code>cd Chat</code></li>
      <h3>2. Run the server:</h3>
      <li><code>python Server.py</code></li>
      <h3>3. In separate terminal windows, run each client:</h3>
      <li><code>python Client1.py</code></li>
      <li><code>python Client2.py</code></li>
    </ul>
  </div>
</body>
</html>
