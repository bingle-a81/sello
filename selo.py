import time
import logging
import logging.config
import settings


logging.config.dictConfig(settings.log_dict)
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
settings.get_logger()
a_log=logging.getLogger(__name__)
a_log.info('start')
a_log.info('start1')
def sel():
    # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
    driver = webdriver.Chrome()

    # команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
    time.sleep(5)

    # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
    driver.get("https://suninjuly.github.io/text_input_task.html")
    time.sleep(5)

    # Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
    # Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
    # Ищем поле для ввода текста
    textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

    # Напишем текст ответа в найденное поле
    textarea.send_keys("get()")
    time.sleep(5)

    # Найдем кнопку, которая отправляет введенное решение
    submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

    # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
    submit_button.click()
    time.sleep(5)

    # После выполнения всех действий мы должны не забыть закрыть окно браузера
    driver.quit()

if __name__ == "__main__":
    # sel()
    pass
            