import matplotlib.pyplot as plt, mpld3
from matplotlib.pyplot import pie, axis, show
import io

from wordcloud import STOPWORDS, WordCloud


def get_videoid(video_id):

    from plot import yt_connect
    pol_comments = yt_connect.generate(video_id)

    print("Video Id:", video_id, "and total comments:", len(pol_comments))
    neutral = 0;
    positive = 0;
    negative = 0;

    for com in pol_comments[0]:
        # print(com[1])
        if (com[1] >= 0.01):
            positive = positive + 1;
        elif (com[1] <= -0.01):
            negative = negative + 1;
        else:
            neutral = neutral + 1;

    names = ["Neutral", "Negative", "Positive"]
    values = [neutral, negative, positive]

    # names = ["Positive", "Negative"]
    # values = [positive, negative]

    adj_list = pol_comments[1]
    a_list = []
    if(positive > negative):
        for adj in adj_list:
            if(adj[1] >= 0.01):
                a_list.append(adj)
    elif(positive < negative):
        for adj in adj_list:
            print("adj",adj[0])
            if(adj[1] <= -0.01):
                a_list.append(adj)

    print("a_list", len(a_list))
    adj_fig = plot_tags_word_cloud(a_list)

    fig, ax = plt.subplots()
    explode = (0, 0, 0.01)
    ax.pie(values, labels=names, autopct='%1.0f%%', explode=explode,
           shadow=False, startangle=0, labeldistance=1.05)
    ax.axis('equal')
    list = [mpld3.fig_to_html(fig), mpld3.fig_to_html(adj_fig)]
    return list


def plot_tags_word_cloud(adj_list):
    plt.axis('off')
    fig = plt.figure(figsize=(8, 8))
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud( background_color= 'black', stopwords = stopwords, max_words = 200, max_font_size = 120, random_state = 42).generate(str(adj_list))
    plt.imshow(wordcloud)
    # plt.title('Word Cloud for Tags', fontsize = 20)
    return fig