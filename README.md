# YaCut - URL shortener

Quick and simple Flask-based module to cut loooong links.
You could create your own short link name or get one completely uniqe and automatic-generate!

## Start & Usage

### Installing

```
git clone https://github.com/ani-zia/yacut.git
```

```
cd yacut
```

```
python3 -m venv venv && source venv/bin/activate
```

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```


### Introducing

Command to start project on local server:

```
flask run
```

Client interface will be available on your localhost adress and for API's opportunetes try ready-made request examples in `request.http` file.


### Tuning

Тow the allowable length of a custom link is 16 characters, and an automatic link is 6 characters (4 in bytes).

These parameters can be changed in the `settings` file.

---

Author Anya Simanova