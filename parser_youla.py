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
