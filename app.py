import streamlit as st
import requests
from datetime import date

st.set_page_config(page_title="On This Day")
st.title("🕰️ On This Day in History")

today = date.today()
url = f"https://en.wikipedia.org/api/rest_v1/feed/onthisday/events/{today.month}/{today.day}"
r = requests.get(url, headers={"User-Agent": "csci2521-demo/1.0"})
events = r.json()["events"]

years = sorted({e["year"] for e in events}, reverse=True)
year = st.selectbox("What happened on " + today.strftime("%B %d") + "... pick a year:", years)

for e in events:
    if e["year"] == year:
        st.markdown(f"**{e['year']}** — {e['text']}")
        if e.get("pages"):
            st.markdown(f"[Read more on Wikipedia]({e['pages'][0]['content_urls']['desktop']['page']})")
