## Use with python resquests:

```
import requests
```

### Devices:

  - Create:
    - post:
    ```
    data = {'device_ip': '110.0.0.11', 'device_mac': '12:52:12:92', 'devicestate': 1, 'label': 'dispo2'}
    r = requests.post("http://localhost:8000/devices/create", data=data)
    r.text
    r.url
    ```

  - List Devices:
  ```
  r = requests.get("http://localhost:8000/devices/")
  r.text
  r.url
  ```

  - Device Detail:
  ```
  r = requests.get("http://localhost:8000/devices/<device_id>")
  r.text
  r.url
  ```

  - Device <id> Data:
  ```
  r = requests.get("http://localhost:8000/devices/<device_id>/data")
  r.text
  r.url
  ```

  - Device <id> Data en un dia especifico (dd/mm/yyyy):
  ```
  r = requests.get("http://localhost:8000/devices/<device_id>/data/dd/mm/yyyy")
  r.text
  r.url
  ```
