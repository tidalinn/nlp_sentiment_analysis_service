# sentiment_analysis_service

Свойство | Значение
-|-
Задача сервиса | Анализ тональности отзывов
Инструменты | Python, Docker, FastAPI, SQLite, Linters


## Запуск

Запуск сервиса:
```
make run
```

### Ссылки

Сервис | Ссылка
-|-
Swagger | [http://localhost:8080/docs](http://localhost:8080/docs)

## Файлы

Расположение | Предназначение
-|-
`configs/app.yml` | Настройка словаря
`database/reviews.db` | База данных


## Запросы

### **POST** `/reviews`

Запрос:
```
curl -X 'POST' \
  'http://localhost:8080/reviews/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "ТЕКСТ ОТЗЫВА"
}'
```
Ответ:
```
{
    "text": "ТЕКСТ ОТЗЫВА",
    "id": ID,
    "sentiment": "ТОНАЛЬНОСТЬ",
    "created_at": "ДАТА"
}
```

### **GET** `/reviews?sentiment=negative`:

Запрос:
```
curl -X 'GET' \
  'http://localhost:8080/reviews?sentiment=negative' \
  -H 'accept: application/json'
```
Ответ:
```
[
    {
        "text": "ТЕКСТ ОТЗЫВА",
        "id": ID,
        "sentiment": "ТОНАЛЬНОСТЬ",
        "created_at": "ДАТА"
    },
    ...
]
```
