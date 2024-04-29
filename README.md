# US-Road-Map

Welcome to the US-Road-Map repository! This project takes you on a detailed exploration of how raw GPS trajectory data was leveraged to craft a comprehensive traffic map of the entire United States. The provided steps guide you through the process of generating these maps using the included SQL and Python scripts. Our dataset is robust, comprising around 1.5 billion observations collected over three years from approximately 10 thousand vehicles, with data recorded at 15-minute intervals. Immerse yourself in the resulting maps that vividly visualize the summarized data, showcasing specific states and regions.

## About the Dataset

### Sample GPS Trajectory:

| Vehicle ID | Datetime            | Latitude       | Longitude       | Speed |
|------------|---------------------|----------------|-----------------|-------|
|   100214   | 2023-01-01 12:34:56 | 38.123456      | -95.678901      |  75   |
|   126540   | 2023-01-01 15:45:23 | 41.987654      | -112.345678     |  50   |
|   113027   | 2023-01-01 18:01:10 | 35.678901      | -89.012345      |  65   |
|   100952   | 2023-01-01 20:30:45 | 30.987654      | -76.543210      |  25   |
|   136279   | 2023-01-01 22:55:12 | 37.654321      | -88.765432      |  45   |

The maps below were generated based on a dataset with:

- **Observations:** ~1.5 billion
- **Vehicles:** ~10 thousand
- **Data Duration:** ~3 years
- **Data Frequency:** Datetime collected on average every 15 minutes

## Steps to Generate US Road Maps:

**Step 1:** Run [query.sql](query.sql) code to summarize the data and find the frequency and average speed of each partition.
- Summarized ~1.5 billion records to ~11.2 million records.

**Step 2:** Run [create_map.py](create_map.py) code to generate maps.
- Used ~11.2 million records to create maps.

## Some of the Output Maps:

- **New York City:**
![1690776412593](https://private-user-images.githubusercontent.com/87002822/326539058-33062638-2f0b-49b9-bb03-4998be04eae2.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTQ0MTQxMzUsIm5iZiI6MTcxNDQxMzgzNSwicGF0aCI6Ii84NzAwMjgyMi8zMjY1MzkwNTgtMzMwNjI2MzgtMmYwYi00OWI5LWJiMDMtNDk5OGJlMDRlYWUyLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA0MjklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNDI5VDE4MDM1NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTYzMGM4NmEzZjg5ODcwNWMyNmJhNTAwYmY3MTJkMTNjYTljYjZmZTNkNjZmYWUyM2NlMDA3Yzk1MjJiNjQ4NjgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.Y2YQ0Iy1ZmsBTMtvADjPLPPKNgwgxoZBeaWPmxpiN1o)


- **States of DC, MD, PA, NY, and MA:**
  
  ![DC_MD_PA_NY_MA](https://github.com/malamdar90/US-Road-Map/assets/87002822/0c4ea967-4c5e-471f-aa00-3b5ed2223525)


- **Southern California:**
  
  ![SoCal](https://github.com/malamdar90/US-Road-Map/assets/87002822/1056a0f2-24d7-49a2-8760-fd5ad8e652be)

- **State of Florida:**
  
  ![FL](https://github.com/malamdar90/US-Road-Map/assets/87002822/fb86c3a8-a919-4169-a69f-41eadf8da944)
