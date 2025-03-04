def get_content_page(html, collected_links):
    """Сбор данных с текущей страницы."""
    soup = BeautifulSoup(html, 'html.parser')
    blocks = soup.find_all('div', {"data-test-component": "ProductOrAdCard"})
    data_list = []

    for block in blocks:
        try:
            name = block.find('span', {'data-test-block': "ProductName"}).text.strip()
        except:
            name = 'нет названия'
            
        try:
            city = block.find('div', {'data-test-component': "Badges"}).text.split('%')[-1].strip()
        except:
            city = 'город не указан'

        try:
            price = block.find('p', {'data-test-block': "ProductPrice"}).text.replace('₽руб.', '').replace('\xa0', '').strip()
        except:
            price = 'нет цены'
        try:
             link = "https://youla.ru" + block.find('div').find('span').find('a').get('href')
        except:
            link = 'ссылка не найдена'

        if link not in collected_links and name != 'нет названия':
            collected_links.add(link)
            data_list.append({
                'name': name,
                'city': city,
                'price': price,
                'link': link
            })

    return data_list
    
def parser(url, data_list_count=1000):

    browser = webdriver.Chrome(options=chrome_options)

    try:
        browser.get(url)
        time.sleep(2)
        collected_links = set()
        data_list_pages = []
        last_count = 0

        while len(data_list_pages) < data_list_count:
            new_data = get_content_page(browser.page_source, collected_links)
            data_list_pages.extend(new_data)
            logger.debug(f'Собрано {len(data_list_pages)} позиций')


            browser.execute_script("window.scrollBy(0, 500);")
            # Ждем появления новых данных
            time.sleep(5)

            if last_count == len(data_list_pages):
                logger.info("Больше новых данных не найдено.")
                break
            last_count = len(data_list_pages)

        return data_list_pages[:data_list_count]

    except Exception as ex:
        logger.error(f'Ошибка: {ex}')
    finally:
        browser.quit()
