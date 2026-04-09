#!/usr/bin/env python3

try:
    from scapy.all import sniff
except ImportError:
    print("Scapy is not installed. Install it with: pip install scapy")
    exit(1)


def packet_handler(packet):
    try:
        print(packet.summary())
    except Exception as e:
        print(f"Error processing packet: {e}")


def main():
    try:
        print("Listening for the first 30 network packets...\n")

        sniff(
            # this will sniff
            prn=packet_handler,
            count=30,
            store=False
        )

        print("\nCapture completed.") # 100 51 32 97 113 117 49 32 97 32 117 78 32 77 51 83

    except PermissionError:
        print("Permission denied. Run the script as administrator/root.")

    except Exception as e:
        print(f"Unexpected error: {e}")




if __name__ == "__main__":
    main()
