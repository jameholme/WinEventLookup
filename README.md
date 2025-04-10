# WinEventLookup
Python utility to look up Windows Event IDs.
```
            ______              
         .-'      `-.           
       .'            `.         
      /                \        
     ;                 ;`       
     |         H       |;       
     ;                 ;|
     '\               / ;       
      \`.           .' /        
       `.`-._____.-' .'         
         / /`_____.-'           
        / / /                   
       / / /
      / / /
     / / /
    / / /
   / / /
  / / /
 / / /
/ / /
\/_/
```
## Usage
Download the files within this repo & run the `win_event_lookup.py` script in your terminal using the arguments below
```
  --event-id EVENT_ID              The Windows Event ID to look up.
  --legacy-id LEGACY_ID            The legacy Windows Event ID to look up.
  --criticality CRITICALITY        The potential criticality level to look up (Low, Medium, High).
```

## References:
* [Windows Server AD DS Appendix L: Events to Monitor](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/appendix-l--events-to-monitor)
> I used the Windows Server AD DS Appendix L: Events to Monitor to create an Excel spreadsheet, I then used Python and Pandas to create the dictionary of event IDs `win_events_db.py`
