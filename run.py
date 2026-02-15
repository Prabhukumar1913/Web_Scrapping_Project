from module import scraping

obj=scraping()
df=obj.response()
df.to_csv("EV_EXTRACTED.csv",index=False)



