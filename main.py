import sys,os
import concurrent.futures
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))

from flowlauncher import FlowLauncher
import webbrowser
import requests
requests.packages.urllib3.util.connection.HAS_IPV6 = False

class AutoRenderSearch(FlowLauncher):
 
    def format_time(self, time_hundredths):
        if time_hundredths is None:
            return "Unknown Time"
        total_seconds = time_hundredths / 100
        minutes, seconds = divmod(total_seconds, 60)
        formatted_time = f"{int(seconds)}.{'' if seconds != 1 else ''}{int((total_seconds % 1) * 100)}"

        if minutes >= 1:
            formatted_time = f"{int(minutes)}:{'s' if minutes != 1 else ''} " + formatted_time

        return formatted_time

    def fetch_result(self, query, result):
        video = result['share_id']
        user = result.get('user', 'Unknown User')
        time_hundredths = result.get('time', 0)
        comment = result.get('comment', '')
        original_rank = result.get('orig_rank')
        map_id = result.get('map')
        autorender_url = f'https://autorender.portal2.sr/videos/{video}'
        default_thumbnail_path = r"assets\app.png"
        formatted_time = self.format_time(time_hundredths)
        subtitle = f"User: {user} | Rank: {original_rank} | Comment: {comment}"

        return {
            "Title": f"{map_id} - {formatted_time}",
            "SubTitle": subtitle,
            "IcoPath": default_thumbnail_path,
            "JsonRPCAction": {
                "method": "open_url",
                "parameters": [autorender_url]
            }
        }

    def query(self, query):
        try:
            search_string = query.replace(' ', '+')
            url = f'https://autorender.portal2.sr/api/v1/search?q={search_string}'
            r = s.get(url)
            
            results = r.json()['results']
            if results:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    result_list = list(executor.map(lambda result: self.fetch_result(query, result), results))

                return result_list
            else:
                return [
                    {
                        "Title": "No results found",
                        "SubTitle": "Try a different search term",
                        "IcoPath": "assets/app.png",
                    }
                ]
        except Exception as e:
            print(f"Error in query: {e}")
            return []

    def open_url(self, url):
        if url:
            webbrowser.open(url)

if __name__ == "__main__":
    s = requests.Session()
    AutoRenderSearch()