import argparse
from win_events_db import EVENTS_DB

def main():
    parser = argparse.ArgumentParser(description="Lookup Windows Event ID info for SOC analysis.")
    parser.add_argument("--event-id", type=int, required=True, help="The Windows Event ID to look up.")
    args = parser.parse_args()
    event_id = args.event_id

    event = EVENTS_DB.get(event_id)

    if event:
        print(f"Event ID: {event_id}")
        print(f"Legacy Event ID: {event['legacy_id'] if event['legacy_id'] else 'N/A'}")
        print(f"Criticality: {event['criticality']}")
        print(f"Summary: {event['summary']}")
    else:
        print(f"Error: Event ID {event_id} not found in the current database.")

if __name__ == "__main__":
    main()
