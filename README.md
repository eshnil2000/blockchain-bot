# Chatbot
AI Based Chatbot

### Requirements
    Python = 2.x.x
    Flask
    Aiml
    pip

## Installation

1. Clone and navigate to chatbot directory.

2. Install the required packages.
    ```bash
    pip install -r requirements.txt
    ```

3. Run the python server.
    ```bash
    python main.py
    ```
4. Open **http://127.0.0.1:5000** in your browser.

5. You're done and let's chat with your Robot via browser.

### within Docker
```[ "env", "FLASK_APP=main.py", "flask", "run" ,"--host", "0.0.0.0"]```
### at terminal
```env FLASK_APP=main.py flask run --host 0.0.0.0```

### at terminal as container
```docker run -d -e VIRTUAL_HOST=bot.proxy.chainapp.live --net nginx-proxy -t eshnil2000/blockchain-bot```

### configure chain address
```
@chain http://1572844919.proxy.chainapp.live/
```

### Call chain APIs
```/chain```
```/transactions/new Nick DappsUni 1000```
```/mine```
```/chain```
