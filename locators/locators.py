lk_button = "//span[text()='Личный кабинет']"
login_button = "//a[text()='Вход']"
login_field = "//input[@name='login']"
pass_field = "//input[@name='pass']"
submit_login_button = "//button[(text())='Войти']"
login_error = "//div[text()='Неверный e-mail или пароль']"
name_account = "//span[(text())='Иван Иванов']"

catalog_button = "//button[.//span[normalize-space(text())='Каталог']]"
electronic_category = "//span[normalize-space(text())='Электроника']"
planshety_categoty = "//a[@href='/catalog/planshety/']"
digma_category = "//a[@href='/catalog/digma/']"
planshet = "//a[contains(@class, 'item-product-img')]"


#product_card = "//a[contains(@class, 'item-card__title')]"
product_card = "//a[@href='/product/Planshet-Digma-iDx10-8Gb/']"
text_planshet = "//h1[@class='mb-lg-4']"
add_to_card_button = "//button[contains(@class, 'rs-buy') and contains(@class, 'rs-to-cart')]"
to_cart = "//a[text()='Перейти в корзину']"
product_in_card = "//a[@class='cart-checkout-item__title']"
clear_cart_button = "//a[text()='Очистить']"
card_button_from_home = "//span[text()='Корзина']"
empty_cart = "//h2[text()='Корзина пуста']"
#planshet_digma = "//a[@href='/product/Planshet-Digma-iDx10-8Gb/']"

add_to_favorites_button = "//span[text()='В избранное']"
to_favorite_button = "//a[@href='/favorite/']"
product_in_favorite = "//a[@class='item-card__title rs-to-product']"
delete_from_favorite = "//a[@data-title='В избранное']"
empty_fav = "//div[text()='Нет товаров в избранном']"