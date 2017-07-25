# Monitor

## Spuštění

* Vytvoř si perzistentní uložiště pro data
    ```
    docker volume create --name=monitor-data
    ```

* Spust kontejnery pomocí
    ```
    docker-compose up
    ```

* Nastavení Grafana

    * Připoj se na Grafana [http://localhost:3000](http://localhost:3000)  Uživatel `admin` a heslo `admin`

    * Vytvoření datasource:

    * Klikneme na `Add data source` a vyplníme následující hodnoty:
        * Name: data
        * Type: InfluxDB
        * Url: http://influxdb:8086
        * Database: node

    * Klikneme na `Add`, Grafana se pokusí připojit na InfluxDB - úspěch oznámí takovouto hláškou `Data source is working`.

    * Importuj Dashboard `Dashboard.json`
