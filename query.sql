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