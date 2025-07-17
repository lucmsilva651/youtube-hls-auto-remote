import subprocess

youtube_id = "1oh9IEwBbFY"
url = f"https://www.youtube.com/watch?v={youtube_id}"

result = subprocess.run(
    ["yt-dlp", "-g", "-f", "best[height<=720]", url],
    capture_output=True,
    text=True
)

hls_url = result.stdout.strip()

with open("url.txt", "w", encoding="utf-8") as f:
    f.write(hls_url + "\n")

print("✅ url.txt atualizado com:", hls_url)
