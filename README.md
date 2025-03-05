# Групповой проект №2. Извлечение данных и анализ продаж автомобилей с разных сайтов

## **1. Бизнес - задача: Анализ рынка автомобилей**

Мы стремимся предоставить автолюбителям и предпринимателям удобный инструмент для изучения рынка автомобилей. Данный проект позволит автоматически собирать данные об автомобилях с двух популярных сайтов, включая информацию о марке, модели, годе выпуска, пробеге, цене, городе и типе коробки передач.

Собранные данные будут анализироваться, чтобы выявить тенденции и аномалии на рынке автомобилей. Мы определим лучшие предложения и поможем автолюбителям выбрать оптимальный вариант, а предпринимателям — оценить перспективы для бизнеса.

Платформа будет полезна как частным лицам, так и компаниям, заинтересованным в покупке или продаже автомобилей. Она поможет определить оптимальные цены, выявить наиболее востребованные модели и регионы, а также оценить состояние рынка в целом.

### **Сбор данных:**
Автоматически извлечь с двух сайтов информацию об автомобилях: марка, модель, год, пробег, цена, город, коробка передач и др.

### **Анализ:**
Сравнить цены на авто, выявить тренды, распознать аномалии и выделить лучшие предложения.

## **2. Обоснование бизнес-задачи**

Мы предполагаем, что цены на одинаковые автомобили могут значительно различаться в зависимости от площадки, на которой они представлены. Это связано с множеством факторов, включая локацию, репутацию продавца, условия доставки и даже время года. Автоматизация сбора и сравнительного анализа данных с двух сайтов позволит покупателям сэкономить время и деньги, а продавцам — рационализировать свои ценовые стратегии. 

Наш проект со сбором предложений конкурентов и выявлением оптимальной цены станет ценным инструментом для обеих сторон. Для покупателей это будет гарантом прозрачности и честности, а для продавцов — возможностью выйти на новый уровень конкурентоспособности. Монетизация алгоритма через сбор данных о предложениях и анализ рынка создаст устойчивый источник дохода, одновременно улучшая качество обслуживания клиентов.

## **3. Выбор источников данных и методологии их сбора**

В процессе изучения рынка подержанных автомобилей мы исследовали множество популярных платформ, но не смогли найти открытый API или такой, который можно было бы оформить быстро и бесплатно. Поэтому мы решили выбрать несколько источников данных для парсинга и дальнейшего анализа.

После изучения различных платформ, мы остановились на Дром.ру и Юла.ру, поскольку хотели увидеть насколько сильные данные могут разниться на таких непохожих сайтах. 

## **4. Логирование**
Часть кода, использующегося для логирования при парсинге, вынесена для наглядности в отдельный файл: [логи](https://github.com/anlika301/gp2_hse_cry/blob/f8a202092061dfff0bc86376291e9fe6a3358b93/logger.txt).

## **5. Извлечение данных с сайта _youla.ru_ с помощью библиотеки Selenium**
Ссылка на раздел проекта с извлечением данных с сайта Юла: [Юла](https://github.com/anlika301/gp2_hse_cry/tree/f8a202092061dfff0bc86376291e9fe6a3358b93/data%20collection%20of%20youla).

## **6. Извлечение данных с сайта _drom.ru_ с помощью библиотеки Selenium**
Ссылка на раздел проекта с извлечением данных с сайта Дром: [Дром](https://github.com/anlika301/gp2_hse_cry/tree/f8a202092061dfff0bc86376291e9fe6a3358b93/data%20collection%20of%20drom).

## **7. Первичная обработка данных (EDA)**

## **8. Агрегация результатов. Выводы**
