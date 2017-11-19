# <a name="top">Интерфейсы пользователя</a>

1. Регистрация
    1. Форма регистрации - [UI_frm_register][UI_frm_register]
    1. Форма подтверждения регистрации - [UI_frm_regconfirm][UI_frm_regconfirm]
1. Аутентификация
    1. Форма аутентификации - [UI_frm_auth][UI_frm_auth]
1. Опросники
    1. Форма редактирования Опросника - [UI_frm_edit_querylist][UI_frm_edit_querylist]
    1. Таблица Опросников - [UI_tab_querylists][UI_tab_querylists]
    1. Форма фильтра Опросников - [UI_frm_filter_querylist][UI_frm_filter_querylist]
1. Наполнение Опросника
    1. Таблица Наполнения Опросника - [UI_tab_querycontents][UI_tab_querycontents] (блок для других страниц)
    1. Форма изменения Наполнения Опросника - [UI_frm_edit_querycontents][UI_frm_edit_querycontents]
1. Вопросы
    1. Форма редактирования Вопроса - [UI_frm_edit_question][UI_frm_edit_question]
    1. Таблица Ответов - [UI_tab_answers][UI_tab_answers] (блок для других страниц)
    1. Форма редактирвоания Ответа общая - [UI_frm_edit_answer][UI_frm_edit_answer]
    1. Форма редактирвоания Ответа "Путанка" - [UI__frm_edit_answerll][UI__frm_edit_answerll]
    1. Форма ответа на Вопрос при выполнении Задания - [UI_frm_run_query][UI_frm_run_query]
1. Задания
    1. Таблица Заданий - [UI_tab_surveys][UI_tab_surveys]
    1. Форма фильтра Заданий - [UI_frm_filter_surveys][UI_frm_filter_surveys]
    1. Страница начала выполнения Задания - [UI_frm_begin_survey][UI_frm_begin_survey]
    1. Страница завершения выполнения Задания - [UI_frm_end_survey][UI_frm_end_survey]
    1. Форма подтверждения завершения Задания - [UI_frm_finalize_survey][UI_frm_finalize_survey]


## Регистрация

[в начало][top]


### Форма регистрации - <a name="UI_frm_register">UI_frm_register</a>

[в начало][top]


### Форма подтверждения регистрации - <a name="UI_frm_regconfirm">UI_frm_regconfirm</a>

[в начало][top]


## Аутентификация

[в начало][top]


### Форма аутентификации - <a name="UI_frm_auth">UI_frm_auth</a>
![Рис.P2.Login.AuthForm Форма авторизации][P2-Login-AuthForm]

[в начало][top]


## Опросники

![Рис.P9.QueryLists Страница Опросников][P9.QueryLists]

Под таблицей находится кнопка "Новый Опросник".

[в начало][top]


### Форма редактирования Опросника - <a name="UI_frm_edit_querylist">UI_frm_edit_querylist</a>

[в начало][top]


### Таблица Опросников - <a name="UI_tab_querylists">UI_tab_querylists</a>

#### Отображаемые атрибуты:

Заголовок колонки | Атрибут Опросника| Описание
---|---|---
Название | | является ссылкой на форму редактирования/просмотра Опросника
Описание | |

#### Влияние не отображаемых атрибутов
Атрибут Опросника | Описание влияния
---|---
Активный | Строка заполнена светло-коричневым фоном
Архивный | Шрифт в строке имеет красный цвет.

[в начало][top]


### Форма фильтра Опросников - <a name="UI_frm_filter_querylist">UI_frm_filter_querylist</a>

![Рис.P9.QueryLists.FilterForm Форма фильтра Опросников][P9.QueryLists.FilterForm]

Критерий | Смысл | Значение по-умолчанию
---------|-------|----------------------
Активные | Показать вопросы с атрибутом “Активный” - Да/Нет. <br> Обратный к фильтру “Скрытый”. | Да
неАктивные | Показывать вопросы с не установленным атрибутом “Активный” - Да/Нет. <br> Обратный к фильтру “Активный”. | Да
Архивные | Показывать вопросы с атрибутом “Архивный” - Да/Нет. | Нет
Последние | Отображать последние изменённые Опросники | 10


[в начало][top]


## Наполнение Опросника

[в начало][top]


### Таблица Наполнения Опросника - <a name="UI_tab_querycontents">UI_tab_querycontents</a> (блок для других страниц)

[в начало][top]


### Форма изменения Наполнения Опросника - <a name="UI_frm_edit_querycontents">UI_frm_edit_querycontents</a>

[в начало][top]


## Вопросы

[в начало][top]


### Форма редактирования Вопроса - <a name="UI_frm_edit_question">UI_frm_edit_question</a>

[в начало][top]


### Таблица Ответов - <a name="UI_tab_answers">UI_tab_answers</a> (блок для других страниц)

[в начало][top]


### Форма редактирвоания Ответа общая - <a name="UI_frm_edit_answer">UI_frm_edit_answer</a>

[в начало][top]


### Форма редактирвоания Ответа "Путанка" - <a name="UI__frm_edit_answerll">UI__frm_edit_answerll</a>

[в начало][top]


### Форма ответа на Вопрос при выполнении Задания - <a name="UI_frm_run_query">UI_frm_run_query</a>

[в начало][top]


## Задания

[в начало][top]


### Таблица Заданий - <a name="UI_tab_surveys">UI_tab_surveys</a>

[в начало][top]


### Форма фильтра Заданий - <a name="UI_frm_filter_surveys">UI_frm_filter_surveys</a>

[в начало][top]


### Страница начала выполнения Задания - <a name="UI_frm_begin_survey">UI_frm_begin_survey</a>

[в начало][top]


### Страница завершения выполнения Задания - <a name="UI_frm_end_survey">UI_frm_end_survey</a>

[в начало][top]


### Форма подтверждения завершения Задания - <a name="UI_frm_finalize_survey">UI_frm_finalize_survey</a>

[в начало][top]


[top]: #top

[UI_frm_register]: #UI_frm_register
[UI_frm_regconfirm]: #UI_frm_regconfirm
[UI_frm_auth]: #UI_frm_auth
[UI_frm_edit_querylist]: #UI_frm_edit_querylist
[UI_tab_querylists]: #UI_tab_querylists
[UI_frm_filter_querylist]: #UI_frm_filter_querylist
[UI_tab_querycontents]: #UI_tab_querycontents
[UI_frm_edit_querycontents]: #UI_frm_edit_querycontents
[UI_frm_edit_question]: #UI_frm_edit_question
[UI_tab_answers]: #UI_tab_answers
[UI_frm_edit_answer]: #UI_frm_edit_answer
[UI__frm_edit_answerll]: #UI__frm_edit_answerll
[UI_frm_run_query]: #UI_frm_run_query
[UI_tab_surveys]: #UI_tab_surveys
[UI_frm_filter_surveys]: #UI_frm_filter_surveys
[UI_frm_begin_survey]: #UI_frm_begin_survey
[UI_frm_end_survey]: #UI_frm_end_survey
[UI_frm_finalize_survey]: #UI_frm_finalize_survey

[P2-Login-AuthForm]: basefunc-P2-Login-AuthForm.png "Рис.P2.Login.AuthForm Форма авторизации"
[P9.QueryLists]: basefunc-P9-QueryLists.png "Рис.P9.QueryLists Страница Опросников"
[P9.QueryLists.FilterForm]: basefunc-P9-QueryLists-FilterForm.png "Рис.P9.QueryLists.FilterForm Форма фильтра Опросников"
