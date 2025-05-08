import requests

def main():
    response = requests.get("https://httpbin.org/get", params={"test_phrase": "Hello, World!"})
    data = response.json()
    print(data['args']['test_phrase'])
    
if __name__ == "__main__":
    main()