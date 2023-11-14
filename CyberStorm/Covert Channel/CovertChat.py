#Team Pterodactyl 
#Code modified by Trey Thomas
#Used chat-client code as the base for the program provided by Dr. Andrey Timofeyev


import socket
import time

# Set the server's IP address and port
ip = "10.4.4.100"
port = 12345

# Create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect((ip, port))

overt_message = ""
timing_results = []

while True:
    # Start the "timer"
    t0 = time.perf_counter()

    data = s.recv(4096).decode()

    # End the "timer"
    t1 = time.perf_counter()

    # Calculate the time delta
    delta = round((t1 - t0) * 1000, 3)  # Convert to milliseconds

    # Append the delta to the list of timing results
    timing_results.append(delta)

    # Append the received data to overt_message
    overt_message += data

    # Print the delay (ms)
    print(f"Delay (ms): {delta}")

    # Check for "EOF" and stop data reception if found
    if "EOF" in overt_message:
        break

# Close the connection to the server
s.close()

# Output overt message
print("Overt Message:")
print(overt_message)

# Convert timing results to 1s and 0s based on the condition
binary_timing = ['1' if ms > 150 else '0' for ms in timing_results]

# Remove the first '0' if present
if binary_timing and binary_timing[0] == '0':
    binary_timing.pop(0)

# Output the list of timing results as binary
print("Binary Timing Results:")
binary_timing_string = ''.join(binary_timing)
print(binary_timing_string)

# Slice the binary string into 8-bit chunks
eight_bit_chunks = [binary_timing_string[i:i+8] for i in range(0, len(binary_timing_string), 8)]

# Convert 8-bit chunks to ASCII characters
ascii_characters = [chr(int(chunk, 2)) for chunk in eight_bit_chunks]

# Output the ASCII characters
print("ASCII Characters:")
print(''.join(ascii_characters))

