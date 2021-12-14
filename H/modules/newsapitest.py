from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='c337a1a23e364824816e7fea3ae6d502')



# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin')

print(len(all_articles["articles"]))
print()

for article in all_articles["articles"]:
    print(article["title"])
    print()
    print(article["description"])
    print()
    print(article["content"])
    print()
    print(article["url"])
    print()
    print(article["publishedAt"])
    print("__________________________________")
