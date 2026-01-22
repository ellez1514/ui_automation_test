# TEST SUITE FOR TWITCH WEB APP (USING MOBILE EMULATION)
This repo contains automated test that tests the search for streamer in twitch

#### HOW TO EXECUTE TESTS:

1. Install requirements:
```sh
pip install -r requirements.txt
```

2. (Optional) Export following variables:
```sh
export USE_HEADLESS=1
export URL=https://www.twitch.tv
export MOBILE_DEVICE="Pixel 7"
```

If those parameters are not exported, then default values will be used 
which are the same values as seen above.

MOBILE DEVICE has only been tested with "Pixel 7"

2. Execute test:
```sh
pytest -rA -s -v tests/ui/test_twitch_web_app.py
or
cd tests/ui/test_twitch_web_app.py
pytest -rA -s -v -m "ui"

```

#### TEST EXECUTION
![Test Execution](ui_automation.gif)