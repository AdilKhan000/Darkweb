import subprocess




def Scrape():
    # Run the Scrapy crawl command
    subprocess.run(["scrapy", "crawl", "DRL"])


# Default = 'http://g66ol3eba227auhq5ezffxzb7tk7qay7zlm3gtauh6qbrqlxvo4dvfyd.onion/d/DarkNetMarkets'

# if not userInput:
#     result = Scrape(userInput)
# else:
result = Scrape()