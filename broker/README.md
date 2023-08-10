Setting up MQTT broker:
1. flash raspberry pi OS with wifi config, enable ssh, and set host name to mqtt-pi (or whatever is descriptive and unique to its function)
2. plug in the pi, let it boot for a bit
3. find the local ip address using ping mqtt-pi.local (make sure you're on the same network!)
4. try to ssh into the new pi

5. install mosquitto 
5a. update `sudo apt update && sudo apt upgrade`
5b. install mosquitto `sudo apt install -y mosquitto mosquitto-clients`
5c. setup autostart on boot `sudo systemctl enable mosquitto.service`
5d. test by getting the version `mosquitto -v`

6. configure the broker
6a. add user and password `sudo mosquitto_passwd -c /etc/mosquitto/passwd [YOUR_USERNAME]`
6b. open the config file `sudo nano /etc/mosquitto/mosquitto.conf`
6c. add the following:
        at the top:
            `per_listener_settings true`
        at the bottom:
            `allow_anonymous false`
            `listener [port]` port (typically 1883)
            `password_file /etc/mosquitto/passwd` (the passwd file might be named something else)
6d. restart mosquitto `sudo systemctl restart mosquitto`
6e. check if mosquitto is running `sudo systemctl status mosquitto`

7. test the broker
        i got a connection refused error when testing so something with the user/password isn't correct. setting `allow_anonymous true` and restarting fixed the issue temporaily
