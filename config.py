valid_email = "kroshass@mail.ru"
valid_pass = "mkO54637"

invalid_email = 'kroshss@mail.ru'
invalid_pass = 'njO54637'

name = 'София'
surname = 'Голицына'
region = 'Свердловская обл'
email = 'sofiafol_99@gmail.com'
password = 'Dcfr7890'

false_email = '91222222'
false_mobile_max = 891212345678'
false_mobile_mini = '8912123456'
false_name_mini = 'А'
name_two_letters = "Ия"
thirty_letters = 'Софийя-Фредерика-Мария-Дагмара'
thirty_one_letters = 'Софийя-Фредерика-Марийя-Дагмара'

class TestData:
    BASE_URL = 'https://b2c.passport.rt.ru/'

    #Заголовки названий элементов
    FORM_AUTH_MAIL = 'Почта'
    AUTH = 'Авторизация'
    RECOVERY = 'Восстановление пароля'
    CHECK = 'Регистрация'
    VERIFICATION_EMAIL = 'Подтверждение email'
    VERIFICATION_INVALID_EMAIL = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    VERIFICATION_INVALID_NAME = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    ENTRY_VK = 'Войти'
    OK = 'Одноклассники'
    CHOICE_ACCOUNT = 'Вход'
    MM = 'Войти и разрешить'
