from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>TCP/IP Protocol Suite</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
    }
    table {
      width: 70%;
      border-collapse: collapse;
      margin: auto;
      text-align: center;
    }
    th, td {
      border: 1px solid #444;
      padding: 12px;
    }
    th {
      background-color: #4CAF50;
      color: white;
    }
    tr:nth-child(even) {
      background-color: #f2f2f2;
    }
    caption {
      font-size: 1.5em;
      margin-bottom: 15px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <table>
    <caption>TCP/IP Protocol Suite</caption>
    <tr>
      <th>Layer</th>
      <th>Description</th>
      <th>Protocols / Examples</th>
    </tr>
    <tr>
      <td>Application Layer</td>
      <td>Provides network services to end-users</td>
      <td>HTTP, FTP, SMTP, DNS, Telnet</td>
    </tr>
    <tr>
      <td>Transport Layer</td>
      <td>Provides end-to-end communication, reliability, flow control</td>
      <td>TCP, UDP</td>
    </tr>
    <tr>
      <td>Internet Layer</td>
      <td>Responsible for logical addressing and routing</td>
      <td>IP, ICMP, ARP, RARP</td>
    </tr>
    <tr>
      <td>Network Access Layer</td>
      <td>Handles physical addressing and data link control</td>
      <td>Ethernet, Wi-Fi, PPP</td>
    </tr>
  </table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()