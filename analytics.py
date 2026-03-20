import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -------------------------------
# STYLE SETTINGS (IMPORTANT)
# -------------------------------
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 120

# -------------------------------
# CREATE OUTPUT FOLDER
# -------------------------------
output_dir = "graphs"
os.makedirs(output_dir, exist_ok=True)

# -------------------------------
# LOAD DATASET
# -------------------------------
df = pd.read_csv("social_media_engagement1.csv")
df['post_time'] = pd.to_datetime(df['post_time'])

# -------------------------------
# GRAPH 1: Likes per Platform
# -------------------------------
plt.figure()
sns.barplot(
    x='platform',
    y='likes',
    hue='platform',        # ✅ add this
    data=df,
    estimator=sum,
    palette="Set2",
    errorbar=None,
    legend=False           # ✅ prevents duplicate legend
)
plt.title("Total Likes per Platform", fontsize=14, weight='bold')
plt.xlabel("Platform")
plt.ylabel("Total Likes")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(f"{output_dir}/graph1_likes_platform.png")
plt.close()

# -------------------------------
# GRAPH 2: Comments vs Shares
# -------------------------------
plt.figure()
sns.scatterplot(
    x='comments',
    y='shares',
    hue='platform',
    palette="Set1",
    data=df,
    s=80,
    alpha=0.7
)
plt.title("Comments vs Shares by Platform", fontsize=14, weight='bold')
plt.xlabel("Comments")
plt.ylabel("Shares")
plt.legend(title="Platform")
plt.tight_layout()
plt.savefig(f"{output_dir}/graph2_comments_shares.png")
plt.close()

# -------------------------------
# GRAPH 3: Engagement Distribution
# -------------------------------
plt.figure()
colors = ["#66c2a5", "#fc8d62", "#8da0cb"]

df[['likes', 'comments', 'shares']].sum().plot.pie(
    autopct='%1.1f%%',
    colors=colors,
    startangle=140,
    wedgeprops={'edgecolor': 'black'}
)

plt.title("Overall Engagement Distribution", fontsize=14, weight='bold')
plt.ylabel("")
plt.tight_layout()
plt.savefig(f"{output_dir}/graph3_engagement_pie.png")
plt.close()

# -------------------------------
# GRAPH 4: Posts Over Time
# -------------------------------
plt.figure()
posts_per_day = df.groupby(df['post_time'].dt.date).size()

posts_per_day.plot(marker='o')
plt.title("Posting Activity Over Time", fontsize=14, weight='bold')
plt.xlabel("Date")
plt.ylabel("Number of Posts")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig(f"{output_dir}/graph4_posts_time.png")
plt.close()

# -------------------------------
# GRAPH 5: Sentiment Distribution
# -------------------------------
plt.figure()
sns.countplot(
    x='sentiment_score',
    hue='sentiment_score',   # ✅ add this
    data=df,
    palette="pastel",
    legend=False             # ✅ remove legend if not needed
)

plt.title("Sentiment Distribution", fontsize=14, weight='bold')
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(f"{output_dir}/graph5_sentiment.png")
plt.close()

print(f"✅ All styled graphs saved in '{output_dir}' folder!")
