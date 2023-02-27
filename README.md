# MIB_project
Итоговый проект (пример) курса "Машинное обучение в бизнесе"

__Стек:__

* ML: sklearn, pandas, numpy, catboost

* API: flask 

Данные: с kaggle - https://www.kaggle.com/datasets/mrsohelrana/bank-marketing-data

__Задача:__ предсказать откроет ли клиент срочный вклад (поле y). Бинарная классификация

Используемые признаки:

* duration
* contact
* poutcome

__Модель:__ catboost

## Инструкция

Клонируем репозиторий и создаем образ

$ git clone https://github.com/PolinaNik/MIB_project.git
$ cd MIB_project
$ docker build -t catboost_model .
