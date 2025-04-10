import requests

url = "https://bus-time.centro.org/bustime/api/v3/getpredictions?key=PUZXP7CxWkPaWnvDWdacgiS4M&stpid=15521,15527,15529,16164,16168,16169,16170,16182,16183,16184&format=json"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    if "bustime-response" in data and "prd" in data["bustime-response"]:
        predictions = data["bustime-response"]["prd"]
        for p in predictions:
            print(
                f"Route: {p['rt']}, "
                f"Destination: {p['des']}, "
                f"Vehicle ID: {p['vid']}, "
                f"Stop: {p['stpnm']}, "
                f"Arriving in: {p['prdctdn']} minutes, "
                f"Predicted Time: {p['prdtm']}, "
                f"Delayed: {p['dly']}"
            )
    elif "error" in data["bustime-response"]:
        error_msg = data["bustime-response"]["error"][0]["msg"]
        print(f"API Error: {error_msg}")
    else:
        print("No predictions available at this time.")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
except ValueError:
    print("Failed to parse JSON.")
except KeyError as e:
     print(f"Missing expected field in response: {e}")