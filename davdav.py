import requests
from concurrent.futures import ThreadPoolExecutor
import json
import time


def fetch_photo(photo_id):
    url = f"https://jsonplaceholder.typicode.com/photos/{photo_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


start_time = time.time()

photo_ids = range(1, 5001)

with ThreadPoolExecutor(max_workers=50) as executor:
    photos = list(executor.map(fetch_photo, photo_ids))

with open("photos.json", "w", encoding="utf-8") as file:
    json.dump(photos, file, ensure_ascii=False, indent=4)

end_time = time.time()

print(f"ყველა მონაცემი ჩაიწერა photos.json ფაილში")
print(f"შესრულების დრო: {end_time - start_time:.2f} წამი")