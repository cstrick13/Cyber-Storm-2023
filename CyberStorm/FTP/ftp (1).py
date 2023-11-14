from ftplib import FTP
import sys


def binary_to_char(binary_str):
    decimal_value = int(binary_str, 2)
    return chr(decimal_value)


def main():
    if len(sys.argv) != 7:
        print("Usage: python ftp_permissions.py IP PORT USER PASSWORD FOLDER USE_7_BITS")
        return

    IP = sys.argv[1]
    PORT = int(sys.argv[2])
    USER = sys.argv[3]
    PASSWORD = sys.argv[4]
    FOLDER = sys.argv[5]
    USE_7_BITS = sys.argv[6].lower() == "true"

    ftp = FTP()
    ftp.connect(IP, PORT)
    ftp.login(USER, PASSWORD)
    ftp.set_pasv(True)

    ftp.cwd(FOLDER)
    files = []
    ftp.dir(files.append)

    ftp.quit()

    result_string = ""

    permission_whole = ""

    for file in files:
        permissions = file[:10]
        permissions = ''.join(['1' if c.isalpha() else '0' for c in permissions])
        if USE_7_BITS and permissions[:3] != "000":
            continue
        if USE_7_BITS:
            permissions = permissions[3:]

        permission_whole += permissions

    padding = 7 - len(permission_whole) % 7

    bit_sequence = permission_whole + "0" * padding

    for i in range(0, len(bit_sequence), 7):
        seven_bits = bit_sequence[i:i + 7]

        char = binary_to_char(seven_bits)
        result_string += char

    print(result_string)


if __name__ == "__main__":
    main()
