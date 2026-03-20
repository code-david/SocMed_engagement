"""
DOMINGO, DAVID ARNOLD R.
BS CPE-4A
Containerizing a Python Data Analytics Application

This script performs data analysis and visualization on a social media engagement dataset.
The generated graphs are saved in the 'graphs' folder and displayed using Streamlit for an
interactive experience.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# -------------------------------
# STYLE SETTINGS (IMPORTANT)
# -------------------------------
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 120

st.set_page_config(
    page_title="📊 Social Media Engagement Analytics",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .block-container {
        margin-left: auto;
        margin-right: auto;
        max-width: 1200px;
    }
    .stImage > div {
        display: flex;
        justify-content: center;
    }
    h1, h2, h3, h4, h5, h6 {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------------
# CREATE OUTPUT FOLDER
# -------------------------------
OUTPUT_DIR = "graphs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

st.title("📊 Social Media Engagement Analytics")

# -------------------------------
# LOAD DATASET
# -------------------------------
df = pd.read_csv("social_media_engagement1.csv")
df['post_time'] = pd.to_datetime(df['post_time'])

# -------------------------------
# GRAPH 1: Likes per Platform
# -------------------------------
st.subheader("Total Likes per Platform")

fig1, ax1 = plt.subplots()
sns.barplot(
    x='platform',
    y='likes',
    hue='platform',        # ✅ add this
    data=df,
    estimator=sum,
    palette="Set2",
    errorbar=None,
    legend=False,           # ✅ prevents duplicate legend
    ax=ax1
)
plt.title("Total Likes per Platform", fontsize=14, weight='bold')
plt.xlabel("Platform")
plt.ylabel("Total Likes")
plt.xticks(rotation=15)
plt.tight_layout()
fig1.savefig(f"{OUTPUT_DIR}/graph1_likes_platform.png")
plt.close(fig1)

st.image(f"{OUTPUT_DIR}/graph1_likes_platform.png")

# -------------------------------
# GRAPH 2: Comments vs Shares
# -------------------------------
st.subheader("Comments vs Shares by Platform")

fig2, ax2 = plt.subplots()
sns.scatterplot(
    x='comments',
    y='shares',
    hue='platform',
    palette="Set1",
    data=df,
    s=80,
    alpha=0.7,
    ax=ax2
)
ax2.set_title("Comments vs Shares by Platform", fontsize=14, weight='bold')
ax2.set_xlabel("Comments")
ax2.set_ylabel("Shares")
ax2.legend(title="Platform")
plt.tight_layout()
fig2.savefig(f"{OUTPUT_DIR}/graph2_comments_shares.png")
plt.close(fig2)

st.image(f"{OUTPUT_DIR}/graph2_comments_shares.png")

# -------------------------------
# GRAPH 3: Engagement Distribution
# -------------------------------
st.subheader("Overall Engagement Distribution")

fig3, ax3 = plt.subplots()
colors = ["#66c2a5", "#fc8d62", "#8da0cb"]

labels = df[['likes', 'comments', 'shares']].sum().index
values = df[['likes', 'comments', 'shares']].sum().values
ax3.pie(
    values,
    labels=labels,
    autopct='%1.1f%%',
    colors=colors,
    startangle=140,
    wedgeprops={'edgecolor': 'black'}
)

ax3.set_title("Overall Engagement Distribution", fontsize=14, weight='bold')
ax3.set_ylabel("")
plt.tight_layout()
fig3.savefig(f"{OUTPUT_DIR}/graph3_engagement_pie.png")
plt.close(fig3)

st.image(f"{OUTPUT_DIR}/graph3_engagement_pie.png")

# -------------------------------
# GRAPH 4: Posts Over Time
# -------------------------------
st.subheader("Posting Activity Over Time")

fig4, ax4 = plt.subplots()
posts_per_day = df.groupby(df['post_time'].dt.date).size()

posts_per_day.plot(ax=ax4, marker='o')
ax4.set_title("Posting Activity Over Time", fontsize=14, weight='bold')
ax4.set_xlabel("Date")
ax4.set_ylabel("Number of Posts")
ax4.tick_params(axis='x', rotation=45)
ax4.grid(True)
plt.tight_layout()
fig4.savefig(f"{OUTPUT_DIR}/graph4_posts_time.png")
plt.close(fig4)

st.image(f"{OUTPUT_DIR}/graph4_posts_time.png")

# -------------------------------
# GRAPH 5: Sentiment Distribution
# -------------------------------
st.subheader("Sentiment Distribution")

fig5, ax5 = plt.subplots()
sns.countplot(
    x='sentiment_score',
    hue='sentiment_score',   # ✅ add this
    data=df,
    palette="pastel",
    legend=False,            # ✅ remove legend if not needed
    ax=ax5
)

ax5.set_title("Sentiment Distribution", fontsize=14, weight='bold')
ax5.set_xlabel("Sentiment")
ax5.set_ylabel("Count")
plt.tight_layout()
fig5.savefig(f"{OUTPUT_DIR}/graph5_sentiment.png")
plt.close(fig5)

st.image(f"{OUTPUT_DIR}/graph5_sentiment.png")

st.success(f"✅ All styled graphs saved in '{OUTPUT_DIR}' folder!")
print(f"✅ All styled graphs saved in '{OUTPUT_DIR}' folder!")
