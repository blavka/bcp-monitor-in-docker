
## První spuštění

* Vytvoř si perzistentní uložiště pro data
    ```
    docker volume create --name=monitor-data
    ```

* Spust kontejnery pomocí
    ```
    docker-compose up
    ```

* V InfluxDB založ databázi `node` do Query vyplň
    * Použi příkaz
        ```
        curl --data "q=CREATE+DATABASE+%22node%22&db=_internal" http://localhost:8086/query
        ```
    * Nebo v prohlížeči otevři administraci InfuxDB [http://localhost:8083/](http://localhost:8083/)
        ```
        CREATE DATABASE "node"
        ```
        a dej `ENTER`

* Nainstaluj dependecies
    ```
    sudo -H pip3 install -r requirements.txt
    ```

* Spuštění bc-gateway
    ```
    python3 bc-gateway.py -W -d /dev/ttyACM0
    ```

* Spust script na překopírovávíní dat z MQTT do InfluxDB
    ```
    python3 mqtt_to_influxdb.py
    ```

* Nastavení Grafana

    * Připoj se na Grafana [http://localhost:3000](http://localhost:3000)  Uživatel `admin` a heslo `admin`

    * Vytvoření datasource:

    * Klikneme na `Add data source` a vyplníme následující hodnoty:
        * Name: node
        * Type: InfluxDB
        * Url: http://influxdb:8086
        * Database: node

    * Klikneme na `Add`, Grafana se pokusí připojit na InfluxDB - úspěch oznámí takovouto hláškou `Data source is working`.

    * Importuj Dashboard
