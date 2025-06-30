from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import logging
import os

# === Directories and Paths ===
LOG_DIR = "logs"
FTP_ROOT = "ftp_root"
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(FTP_ROOT, exist_ok=True)

# === Logging Setup ===
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "ftp_audit.log"),
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# === Bait Files ===
with open(os.path.join(FTP_ROOT, "secrets.txt"), "w") as f:
    f.write("admin:admin123\nuser:testpass\n")
with open(os.path.join(FTP_ROOT, "emergency_update_required.txt"), "w") as f:
    f.write("""EMERGENCY UPDATE REQUIRED

To IT,

I gained access to a user account using a default password — no protection, no changes, nothing.

The account? It's mine.

That should never happen.

This isn’t just a security gap. It’s a sign that someone’s not doing their job.

- Change the password immediately.
- Conduct an internal audit.

Sincerely,
Concerned Admin
""")

# === FTP User Auth Setup (Anonymous Access) ===
authorizer = DummyAuthorizer()
authorizer.add_anonymous(homedir=FTP_ROOT, perm='elr')  # e: change dir, l: list, r: read

# === FTP Handler with Logging ===
class HoneypotFTPHandler(FTPHandler):
    def on_connect(self):
        logging.info(f"FTP Connected: {self.remote_ip}:{self.remote_port}")

    def on_login(self, username):
        logging.info(f"FTP Login: {username} from {self.remote_ip}")

    def on_disconnect(self):
        logging.info(f"FTP Disconnected: {self.remote_ip}")

    def on_file_sent(self, file):
        logging.info(f"File downloaded: {file}")

    def on_file_received(self, file):
        logging.info(f"File uploaded: {file}")

    def on_incomplete_file_received(self, file):
        logging.warning(f"Incomplete file upload: {file}")

    def on_command(self, command, arg):
        logging.info(f"Command issued: {command} {arg if arg else ''}")

# === FTP Server Setup ===
handler = HoneypotFTPHandler
handler.authorizer = authorizer
handler.banner = (
    "220 Welcome to Abdullah FTP\n"
    "This server is for authorized use only. All activity is monitored.\n"
)

address = ("0.0.0.0", 21)
server = FTPServer(address, handler)

print("[+] FTP Honeypot running on port 21...")
if __name__ == "__main__":
    server.serve_forever()
