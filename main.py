import sys,os
import concurrent.futures
import urllib.parse

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))

from flowlauncher import FlowLauncher
import webbrowser
import requests

s = requests.Session()
_ICON_PATH = os.path.join(parent_folder_path, "assets", "app.png")

class AutoRenderSearch(FlowLauncher):
  
    def format_time(self, time_hundredths):
        if time_hundredths is None:
            return "Unknown Time"

        try:
            hundredths_total = int(time_hundredths)
        except (TypeError, ValueError):
            return "Unknown Time"

        minutes, remainder = divmod(hundredths_total, 6000)
        seconds, hundredths = divmod(remainder, 100)

        if minutes:
            return f"{minutes}:{seconds:02}.{hundredths:02}"

        return f"{seconds}.{hundredths:02}"

    def fetch_result(self, query, result):
        share_id = result.get('share_id')
        user = result.get('user', 'Unknown User')
        time_hundredths = result.get('time', 0)
        comment = result.get('comment', '')
        original_rank = result.get('orig_rank')
        map_id = result.get('map', 'Unknown Map')
        default_thumbnail_path = _ICON_PATH
        formatted_time = self.format_time(time_hundredths)
        rank_text = original_rank if original_rank is not None else 'Unknown Rank'
        comment_text = comment if comment else 'No comment'
        subtitle = f"User: {user} | Rank: {rank_text} | Comment: {comment_text}"

        item = {
            "Title": f"{map_id} - {formatted_time}",
            "SubTitle": subtitle,
            "IcoPath": default_thumbnail_path,
        }

        if share_id:
            autorender_url = f'https://autorender.p2sr.org/videos/{share_id}'
            item["JsonRPCAction"] = {
                "method": "open_url",
                "parameters": [autorender_url]
            }

        return item

    def query(self, query):
        sanitized_query = query.strip()
        if not sanitized_query:
            return [
                {
                    "Title": "Enter a search term",
                    "SubTitle": "Type a map or runner name to search autorender",
                    "IcoPath": _ICON_PATH,
                }
            ]

        try:
            search_string = urllib.parse.quote_plus(sanitized_query)
            url = f'https://autorender.p2sr.org/api/v1/search?q={search_string}'
            response = s.get(url, timeout=5)
            response.raise_for_status()

            payload = response.json()
            results = payload.get('results', [])
            if results:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    items = [item for item in executor.map(lambda result: self.fetch_result(query, result), results) if item]
                if items:
                    return items

            return [
                {
                    "Title": "No results found",
                    "SubTitle": "Try a different search term",
                    "IcoPath": _ICON_PATH,
                }
            ]
        except requests.exceptions.RequestException as exc:
            print(f"Network error in query: {exc}")
            return [
                {
                    "Title": "Network error",
                    "SubTitle": "Check your connection and try again",
                    "IcoPath": _ICON_PATH,
                }
            ]
        except ValueError as exc:
            print(f"Error parsing response: {exc}")
            return [
                {
                    "Title": "Unexpected response",
                    "SubTitle": "The autorender API returned data in an unexpected format",
                    "IcoPath": _ICON_PATH,
                }
            ]

    def open_url(self, url):
        if url:
            webbrowser.open(url)

if __name__ == "__main__":
    AutoRenderSearch()
