#!/usr/bin/env python3
"""Compare HAR capture hosts vs declared App Store privacy label. Local only."""
import json, sys
from urllib.parse import urlparse
SDKS = {  # host suffix -> (sdk, typical data types)  -- extend via PR
 "app-measurement.com": ("Firebase Analytics", ["Identifiers", "Usage Data"]),
 "firebaselogging-pa.googleapis.com": ("Firebase", ["Usage Data", "Diagnostics"]),
 "crashlytics.com": ("Crashlytics", ["Diagnostics"]),
 "graph.facebook.com": ("Meta SDK", ["Identifiers", "Usage Data"]),
 "api2.amplitude.com": ("Amplitude", ["Identifiers", "Usage Data"]),
 "api.mixpanel.com": ("Mixpanel", ["Identifiers", "Usage Data"]),
 "sentry.io": ("Sentry", ["Diagnostics"]),
 "api.revenuecat.com": ("RevenueCat", ["Purchases", "Identifiers"]),
 "appsflyer.com": ("AppsFlyer", ["Identifiers", "Usage Data"]),
 "adjust.com": ("Adjust", ["Identifiers", "Usage Data"]),
}
def main(har="sample.har", label="label.example.json"):
    hosts = sorted({urlparse(e["request"]["url"]).hostname for e in json.load(open(har))["log"]["entries"]})
    declared = set(json.load(open(label)).get("data_types", []))
    for h in hosts:
        m = next((v for k, v in SDKS.items() if h and h.endswith(k)), None)
        if not m: print(f"UNMAPPED  {h}"); continue
        miss = [t for t in m[1] if t not in declared]
        print(f"{'REVIEW' if miss else 'OK':9} {h}  [{m[0]}]  missing: {', '.join(miss) or '-'}")
if __name__ == "__main__": main(*sys.argv[1:3])
