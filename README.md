# WinEventLookup
Basic Python utility to look up Windows Event IDs.
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
* Download the files within this repo
* Run this in your terminal: `python win_event_lookup.py --event-id 1234`

## References:
* [Windows Server AD DS Appendix L: Events to Monitor](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/appendix-l--events-to-monitor)
> I used the Windows Server AD DS Appendix L: Events to Monitor to create an Excel spreadsheet, I then used Python and Pandas to create the dictionary of event IDs `win_events_db.py`
