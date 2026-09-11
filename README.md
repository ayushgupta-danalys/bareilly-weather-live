#  Bareilly Live Weather & Go-Out Advisory Dashboard

A live, auto-updating weather monitoring system for Bareilly that fetches real-time weather data every 15 minutes, applies rule-based decision logic, and visualizes insights through an interactive Power BI dashboard.

##  Project Overview
This project answers a practical daily question: "Should I go out today, and what precautions should I take?" It combines automated data engineering with data analytics to deliver a real-time advisory system.

##  Architecture

```
[wttr.in Weather API] 
        ↓
[Python Script - Fetch & Parse Data]
        ↓
[CSV Storage - Auto-committed to GitHub]
        ↓
[cron-job.org - Reliable 15-min External Trigger]
        ↓
[GitHub Actions - Workflow Execution]
        ↓
[Power BI - Live Dashboard + Advisory Logic]
```

##  Tech Stack
- **Data Source:** wttr.in (free weather API, no auth required)
- **Automation:** Python, GitHub Actions (`workflow_dispatch`), external scheduler (cron-job.org) triggering every 15 minutes
- **Storage:** CSV (version-controlled via Git)
- **Visualization:** Power BI (Power Query, DAX measures)
- **Decision Logic:** Rule-based advisory system (Python + Power Query M language)

##  Key Features
- **Fully automated pipeline** — no manual intervention needed; data refreshes every 15 minutes via an external scheduler triggering GitHub Actions
- **Smart advisory system** — combines UV index, temperature, actual precipitation (mm), humidity, and wind speed to recommend Safe / Caution / Avoid status
- **Precision fix:** Uses measured precipitation (`precipMM`) rather than text-based weather descriptions to avoid false rain alerts
- **Live dashboard** — Power BI connects directly to the GitHub-hosted CSV via raw URL, no local sync required

##  Dashboard Highlights
- Real-time metric cards (Temperature, Humidity, UV Index, Advisory Status)
- Historical trend charts (Temperature & Humidity over time)
- Color-coded advisory table
- Advisory distribution analysis

##  Advisory Logic
| Condition | Trigger | Status |
|---|---|---|
| UV Index ≥ 8 | High UV exposure | Caution |
| Temp ≥ 40°C or Feels Like ≥ 42°C | Extreme heat | Avoid |
| Precipitation > 0mm | Actual rain detected | Caution |
| Humidity ≥ 80% + Temp ≥ 30°C | Humid heat | Caution |
| Wind Speed ≥ 30 km/h | Strong wind | Caution |

##  Challenges Solved
- Fixed a false-positive rain alert bug by prioritizing measured precipitation over text-based weather descriptions
- Debugged GitHub Actions permission (403) errors for automated commits
- Resolved timezone mismatch between UTC-based cron scheduling and IST
- Discovered GitHub's built-in scheduled cron is unreliable for frequent intervals (runs were delayed by hours instead of triggering hourly); solved by using an external scheduler (cron-job.org) to call the GitHub Actions `workflow_dispatch` API every 15 minutes for consistent, reliable execution

##  Future Scope
- SQL-based historical trend analysis (once sufficient data accumulates)
- Statistical hypothesis testing (seasonal pattern analysis)
- Migration to a cloud-hosted database for scalability

##  Files in this Repo
- `fetch_weather.py` — Data fetching script
- `bareilly_weather.csv` — Auto-updating dataset
- `.github/workflows/weather_fetch.yml` — Automation config
- `weather.pbix` — Power BI dashboard file

##  Author
**Ayush Kumar Gupta**
