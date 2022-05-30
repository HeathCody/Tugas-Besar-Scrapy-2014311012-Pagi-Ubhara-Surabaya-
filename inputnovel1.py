import scrapy
import csv

# TF-IDF
# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from math import log10

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

class BlogSpider(scrapy.Spider):
    name = "novels"
    def start_requests(self):
        urls = [
        'https://www.worldnovel.online/super-detective-in-the-fictional-world/chapter-1/',
        'https://www.worldnovel.online/super-detective-in-the-fictional-world/chapter-2/',
        'https://www.worldnovel.online/super-detective-in-the-fictional-world/chapter-3/',
        'https://www.worldnovel.online/super-detective-in-the-fictional-world/chapter-4/',
        'https://www.worldnovel.online/super-detective-in-the-fictional-world/chapter-5/',
        'https://www.worldnovel.online/super-detective-in-the-fictional-world/chapter-6/',
        'https://www.worldnovel.online/super-detective-in-the-fictional-world/chapter-7/',
        'https://www.worldnovel.online/super-detective-in-the-fictional-world/chapter-8/',
        'https://www.worldnovel.online/super-detective-in-the-fictional-world/chapter-9/',
        'https://www.worldnovel.online/super-detective-in-the-fictional-world/chapter-10/'
        ]
        for url in urls:
            headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'
            }
            yield scrapy.Request(url=url, headers=headers)

    def parse(self, response):
        #print(response.url)

                yield {
                'paragraf' : response.css('#soop > p ::text').extract()
            }

def get_list_of_word(list_of_chapNovel):
        list_of_word = []

        for kalimat in list_of_chapNovel:
            for word in stemmer.stem(kalimat).split(' '):
                if word not in list_of_chapNovel:
                    list_of_word.append(word)
            
        return list_of_word


# List yang berisi kumpulan teks chapter novel dan ukuran dari list tersebut
list_of_chapNovel = [open('novel1.csv', encoding='utf-8').read()]
length_of_chapNovel = len(list_of_chapNovel)

# berisi kata-kata yang berasal dari list text chapNovel
list_of_word = get_list_of_word(list_of_chapNovel)
print(list_of_word[9])
print(list_of_word[20])
print(list_of_word[47])
print(list_of_word[73])
print(list_of_word[129])
print(list_of_word[176])
print(list_of_word[220])
print(list_of_word[333])
print(list_of_word[369])
print(list_of_word[400])
