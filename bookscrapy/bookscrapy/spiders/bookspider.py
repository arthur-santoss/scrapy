import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["cartoesmaisbarato.com.br"]
    start_urls = ["https://www.cartoesmaisbarato.com.br/todos-os-produtos/1924"]

    def parse(self, response):
        with open('dados.txt', 'a', encoding='utf-8') as arquivo:
            books = response.css('div .col-most')

            for book in books:
                name = book.css('div h3::text').get()
                price = book.css('b span::text').get()
                url = book.css('div a').attrib['href']

                # Escrever os dados no arquivo de texto
                arquivo.write(f'Nome: {name}\n')
                arquivo.write(f'Preço: {price}\n')
                arquivo.write(f'URL: {url}\n')
                arquivo.write('\n')

                yield {
                    'name': name,
                    'price': price,
                    'url': url
                }

        print("Dados salvos em dados.txt")

                

                # # Pegando todos os dados da próxima página
                # next_page = response.css('li.next a::attr(href)').get()
                
                # if next_page is not None:
                #     if 'catalogue/' in next_page:
                #         next_page_url = 'https://books.toscrape.com/'+next_page
                #     else:
                #         next_page_url = 'https://books.toscrape.com/catalogue/'+next_page

                #     yield response.follow(next_page_url, callback=self.parse)
            
