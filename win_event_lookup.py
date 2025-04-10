import argparse
from win_events_db import EVENTS_DB

def main():
    parser = argparse.ArgumentParser(description="Lookup Windows Event ID info.")

    parser.add_argument("--event-id", type=int, help="The Windows Event ID to look up.")
    parser.add_argument("--legacy-id", type=str, help="The legacy Windows Event ID to look up.")
    parser.add_argument("--criticality", type=str, help="The potential criticality level to look up (Low, Medium, High).")

    args = parser.parse_args()

    if args.event_id:
        event = EVENTS_DB.get(args.event_id)
        if event:
            print_event(args.event_id, event)
        else:
            print(f"Error: No events found with Event ID '{args.event_id}'.")

    elif args.legacy_id:
        found = False
        for eid, data in EVENTS_DB.items():
            legacy = data.get("legacy_id", "")
            if args.legacy_id in legacy.split(","):
                print_event(eid, data)
                found = True
        if not found:
            print(f"Error: No events found with legacy ID '{args.legacy_id}'.")

    elif args.criticality:
        crit_input = args.criticality.lower()
        found = False
        for eid, data in EVENTS_DB.items():
            if data.get("criticality", "").lower() == crit_input:
                print_event(eid, data)
                found = True
        if not found:
            print(f"Error: No events found with criticality '{args.criticality}'.")

    else:
        print("Please provide at least one lookup option: --event-id, --legacy-id, or --criticality")

def print_event(event_id, event):
    print(f"Event ID: {event_id}")
    print(f"Legacy Event ID: {event['legacy_id'] if event['legacy_id'] else 'N/A'}")
    print(f"Criticality: {event['criticality']}")
    print(f"Summary: {event['summary']}")
    print("-" * 40)

if __name__ == "__main__":
    main()
