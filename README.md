# velib_analysis
analysis of the data of the velib' (public bike system)

### cron auto download

```cron
*/10 * * * * python3 ~/velib_analysis/download_data.py >> ~/log.txt
```