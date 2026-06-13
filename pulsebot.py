import text
from datetime import datetime
#weather
def get_weather(city="Palakkad"): 
    try:
        response = requests.get(f"https://wttr.in/{city}?format=3", timeout=10)
        response.raise_for_status()
        return response.text.strip()  # Strip removes accidental newlines
    except Exception as e:
        return f"Weather error: {e}"
  #quote
 def get_quote(): 
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=10)
        response.raise_for_status()
        data = response.json()
        return f"{data[0]["q"]} — {data[0]["a"]}"
    except Exception as e:
        return f"Quote error: {e}"
#summary
def build_summary():
    today = date.today().strftime("%A, %B %d, %Y")
    weather = get_weather()
    quote = get_quote()
    
    summary = f"""
=========================================
PULSE Daily Summary
Date: {today}
=========================================

WEATHER:
{weather}

TODAY'S QUOTE:
{quote}

=========================================
"""
    return summary
def run():
    summary = build_summary()
    print(summary)
    
    with open("daily_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)
        
    print("Pulse ran successfully.")

if __name__ == "__main__":
    run()
