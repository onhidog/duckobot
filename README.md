# Duck-o-bot

bot para patos, encontra-se na folder duck. O resto do projecto vem do [discord.py][.py].
pra ja nao ha grande readme, mas com tempo sera feito. O bot para ja tambem e pequeno, conseguem ainda perceber o que la esta.

Va fica...

Uses: https://github.com/Rapptz/discord.py

## Installing

To install the library without full voice support, you can just run the following command:

```
python3 -m pip install -U discord.py
```

Otherwise to get voice support you should run the following command:

```
python3 -m pip install -U discord.py[voice]
```

To install the development version, do the following:

```
python3 -m pip install -U https://github.com/Rapptz/discord.py/archive/master.zip#egg=discord.py[voice]
```

## Requirements

- Python 3.4.2+
- `aiohttp` library
- `websockets` library
- `PyNaCl` library (optional, for voice only)
    - On Linux systems this requires the `libffi` library. You can install in
      debian based systems by doing `sudo apt-get install libffi-dev`.

Usually `pip` will handle these for you.
