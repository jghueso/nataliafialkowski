import urllib.request, re, os, json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "es-AR,es;q=0.9,en;q=0.8",
}

username = "nataliafialkowskifotografa"

# Try picuki
for base_url in [
    f"https://www.picuki.com/profile/{username}",
    f"https://gramhir.com/profile/{username}",
    f"https://imginn.com/{username}/",
]:
    print(f"\nTrying: {base_url}")
    try:
        req = urllib.request.Request(base_url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as r:
            body = r.read().decode("utf-8", errors="ignore")

        # Look for image URLs
        imgs = re.findall(r'https?://[^\s"\'<>]+\.(?:jpg|jpeg|png)(?:\?[^\s"\'<>]*)?', body)
        imgs = [i for i in imgs if any(k in i for k in ["cdninstagram", "instagram", "fbcdn", "picuki", "imginn"])]

        profile = [i for i in imgs if "profile" in i.lower() or "avatar" in i.lower() or "150x150" in i or "s150x150" in i]
        posts = [i for i in imgs if i not in profile]

        print(f"  Profile pics found: {len(profile)}")
        for p in profile[:3]:
            print(f"    {p}")
        print(f"  Post images found: {len(posts)}")
        for p in posts[:12]:
            print(f"    {p}")

        if imgs:
            break

    except Exception as e:
        print(f"  Failed: {e}")
