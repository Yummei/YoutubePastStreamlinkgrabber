import requests

def get_past_live_links(api_key, channel_id):
    base_url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'key': api_key,
        'channelId': channel_id,
        'order': 'date',
        'eventType': 'completed',
        'type': 'video',
        'maxResults': 50
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    links = []

    for item in data.get('items', []):
        video_id = item['id']['videoId']
        link = f'https://www.youtube.com/watch?v={video_id}'
        links.append(link)

    return links

api_key = 'YOUR_API_KEY'  # Replace with your API key
channel_id = 'UCt9H_RpQzhxzlyBxFqrdHqA'  # Channel ID

# Define file path for C:\Downloads
file_path = r'C:\Downloads\past_live_links.txt'

links = get_past_live_links(api_key, channel_id)

with open(file_path, 'w') as file:
    for link in links:
        file.write(link + '\n')

print(f'Found {len(links)} past live links. Saved to {file_path}')
