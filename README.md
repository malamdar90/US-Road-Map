# US-Road-Map

```
SELECT
    ROUND(Lat, 3) AS Lat,
    ROUND(Lng, 3) AS Lng,
    COUNT(*) AS Freq,
    AVG(speed) AS Speed
FROM
    gps_data
GROUP BY
    ROUND(Lat, 3),
    ROUND(Lng, 3)
INTO OUTFILE '/Average_speed.csv'
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
```

### Sample of the outputs: 

States of DC, MD, PA, NY, and MA:
![DC_MD_PA_NY_MA](https://github.com/malamdar90/US-Road-Map/assets/87002822/0c4ea967-4c5e-471f-aa00-3b5ed2223525)

State of Florida:
![FL](https://github.com/malamdar90/US-Road-Map/assets/87002822/fb86c3a8-a919-4169-a69f-41eadf8da944)







