import requests




url = "https://cve.circl.lu/api/cve/CVE-2021-44228"
try:
    r = requests.get(url, timeout=3)
    print(f"[{r.status_code}] {url}")
    if r.status_code == 200:
        data = r.json()
        print("cveMetadata:",data['cveMetadata'])
        print ("providerMetadata:",data['containers']['cna']['providerMetadata'])
except Exception as e:
    print("Error:", e)

