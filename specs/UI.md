# <a name="top">Интерфейсы пользователя</a>

1. Регистрация
    1. Форма регистрации ([UI_frm_register][UI_frm_register])
    1. Форма подтверждения регистрации ([UI_frm_regconfirm][UI_frm_regconfirm])
1. Аутентификация
    1. Форма аутентификации ([UI_frm_auth][UI_frm_auth])
1. Опросники
    1. Страница Опросников ([UI_page_querylists][UI_page_querylists])
    1. Форма редактирования Опросника ([UI_frm_edit_querylist][UI_frm_edit_querylist])
    1. Таблица Опросников ([UI_tab_querylists][UI_tab_querylists])
    1. Форма фильтра Опросников ([UI_frm_filter_querylist][UI_frm_filter_querylist])
1. Наполнение Опросника
    1. Таблица Наполнения Опросника ([UI_tab_querycontents][UI_tab_querycontents]) (блок для других страниц)
    1. Форма изменения Наполнения Опросника ([UI_frm_edit_querycontents][UI_frm_edit_querycontents])
1. Вопросы
    1. Форма редактирования Вопроса ([UI_frm_edit_question][UI_frm_edit_question])
    1. Таблица Ответов ([UI_tab_answers][UI_tab_answers]) (блок для других страниц)
    1. Форма редактирвоания Ответа общая ([UI_frm_edit_answer][UI_frm_edit_answer])
    1. Форма редактирвоания Ответа "Путанка" ([UI__frm_edit_answerll][UI__frm_edit_answerll])
    1. Форма ответа на Вопрос при выполнении Задания ([UI_frm_run_query][UI_frm_run_query])
1. Задачи
    1. Страница Задач ([UI_page_tasks][UI_page_tasks])
    1. Форма редактирования Задачи ([UI_frm_edit_task][UI_frm_edit_task])
    1. Таблица Задач ([UI_tab_tasks][UI_tab_tasks])
1. Расписания
    1. Страница Расписаний ([UI_page_tasks][UI_page_schedules])
    1. Форма редактирования Расписания ([UI_frm_edit_schedule][UI_frm_edit_schedule])
    1. Таблица Расписаний ([UI_tab_schedules][UI_tab_schedules])
1. Задания
    1. Таблица Заданий ([UI_tab_surveys][UI_tab_surveys])
    1. Форма фильтра Заданий ([UI_frm_filter_surveys][UI_frm_filter_surveys])
    1. Страница начала выполнения Задания ([UI_frm_begin_survey][UI_frm_begin_survey])
    1. Страница завершения выполнения Задания ([UI_frm_end_survey][UI_frm_end_survey])
    1. Форма подтверждения завершения Задания ([UI_frm_finalize_survey][UI_frm_finalize_survey])


## Регистрация

[в начало][top]


### Форма регистрации (<a name="UI_frm_register">UI_frm_register</a>)

[в начало][top]


### Форма подтверждения регистрации (<a name="UI_frm_regconfirm">UI_frm_regconfirm</a>)

[в начало][top]


## Аутентификация

[в начало][top]


### Форма аутентификации (<a name="UI_frm_auth">UI_frm_auth</a>)
![Рис.P2.Login.AuthForm Форма авторизации][P2-Login-AuthForm]

[в начало][top]


## Опросники

### Страница Опросников (<a name="UI_page_querylists">UI_page_querylists</a>)

![Рис.P9.QueryLists Страница Опросников][P9.QueryLists]

#### Активные элементы

Value | input type | input name | Описание
---|---|---|---

Под таблицей находится кнопка "Новый Опросник", по которой производится запуск "Создать Опросник" ([UC_new_querylist][UC_new_querylist]).

[в начало][top]


### Форма редактирования Опросника (<a name="UI_frm_edit_querylist">UI_frm_edit_querylist</a>)

#### Блок полей атрибутов

Заголовок поля | Атрибут | widget | Описание
---|---|---|---
#id | [querylist][FR_querylist].id | positive integer| Если Опросник новый, то пустое значение.
Название | [querylist][FR_querylist].name | string |
Описание | [querylist][FR_querylist].description | textfield |

##### Блок кнопок для полей атрибутов

Value | input type | input name | Описание
---|---|---|---
Сбросить | submit | reset | Отображает страницу без сохранения внесённых изменений, используя последние сохранённые в БД значения.
Сохранить | submit | save | Сохранить в БД изменённые значения атрибутов
Удалить | submit | delete | Реализует "Удалить Опросник" ([UC_del_querylist][UC_del_querylist])
Наполнение | submit | querycontent | Реализует "Изменить наполнение Опросника" ([UC_chg_querycontent][UC_chg_querycontent])
Предпросмотр | submit | preview | Реализует "Эмуляция Опросника" ([UC_emu_querylist][UC_emu_querylist])

#### Блок наполнения Опросника

Использует "Таблица Наполнения Опросника" ([UI_tab_querycontents][UI_tab_querycontents])

##### Блок кнопок для полей атрибутов

Value | input type | input name | Описание
---|---|---|---
Добавить вопрос | submit | addcontent | Реализует "Создать Вопрос" ([UC_new_question][UC_new_question])

[в начало][top]


### Таблица Опросников (<a name="UI_tab_querylists">UI_tab_querylists</a>)

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


### Форма фильтра Опросников (<a name="UI_frm_filter_querylist">UI_frm_filter_querylist</a>)

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


### Таблица Наполнения Опросника (<a name="UI_tab_querycontents">UI_tab_querycontents</a>) (блок для других страниц)

[в начало][top]


### Форма изменения Наполнения Опросника (<a name="UI_frm_edit_querycontents">UI_frm_edit_querycontents</a>)

[в начало][top]


## Вопросы

[в начало][top]


### Форма редактирования Вопроса (<a name="UI_frm_edit_question">UI_frm_edit_question</a>)

[в начало][top]


### Таблица Ответов (<a name="UI_tab_answers">UI_tab_answers</a>) (блок для других страниц)

[в начало][top]


### Форма редактирвоания Ответа общая (<a name="UI_frm_edit_answer">UI_frm_edit_answer</a>)

[в начало][top]


### Форма редактирвоания Ответа "Путанка" (<a name="UI__frm_edit_answerll">UI__frm_edit_answerll</a>)

[в начало][top]


### Форма ответа на Вопрос при выполнении Задания (<a name="UI_frm_run_query">UI_frm_run_query</a>)

[в начало][top]


## Задачи

[в начало][top]


### Страница Задач (<a name="UI_page_tasks">UI_page_tasks</a>)

[в начало][top]


### Форма редактирования Задачи (<a name="UI_frm_edit_task">UI_frm_edit_task</a>)

[в начало][top]


### Таблица Задач (<a name="UI_tab_tasks">UI_tab_tasks</a>)

[в начало][top]


## Расписания

[в начало][top]


### Страница Расписаний (<a name="UI_page_schedules">UI_page_schedules</a>)

[в начало][top]


### Форма редактирования Расписания (<a name="UI_frm_edit_schedule">UI_frm_edit_schedule</a>)

[в начало][top]


### Таблица Расписаний (<a name="UI_tab_schedules">UI_tab_schedules</a>)

[в начало][top]


## Задания

[в начало][top]


### Таблица Заданий (<a name="UI_tab_surveys">UI_tab_surveys</a>)

[в начало][top]


### Форма фильтра Заданий (<a name="UI_frm_filter_surveys">UI_frm_filter_surveys</a>)

[в начало][top]


### Страница начала выполнения Задания (<a name="UI_frm_begin_survey">UI_frm_begin_survey</a>)

[в начало][top]


### Страница завершения выполнения Задания (<a name="UI_frm_end_survey">UI_frm_end_survey</a>)

[в начало][top]


### Форма подтверждения завершения Задания (<a name="UI_frm_finalize_survey">UI_frm_finalize_survey</a>)

[в начало][top]


[top]: #top

[UI_frm_register]: #UI_frm_register
[UI_frm_regconfirm]: #UI_frm_regconfirm
[UI_frm_auth]: #UI_frm_auth
[UI_page_querylists]: #UI_page_querylists
[UI_frm_edit_querylist]: #UI_frm_edit_querylist
[UI_tab_querylists]: #UI_tab_querylists
[UI_frm_filter_querylist]: #UI_frm_filter_querylist
[UI_tab_querycontents]: #UI_tab_querycontents
[UI_frm_edit_querycontents]: #UI_frm_edit_querycontents
[UI_frm_edit_question]: #UI_frm_edit_question
[UI_tab_answers]: #UI_tab_answers
[UI_frm_edit_answer]: #UI_frm_edit_answer
[UI__frm_edit_answerll]: #UI__frm_edit_answerll
[UI_page_tasks]: #UI_page_tasks
[UI_frm_edit_task]: #UI_frm_edit_task
[UI_tab_tasks]: #UI_tab_tasks
[UI_page_schedules]: #UI_page_schedules
[UI_frm_edit_schedule]: #UI_frm_edit_schedule
[UI_tab_schedules]: #UI_tab_schedules
[UI_frm_run_query]: #UI_frm_run_query
[UI_tab_surveys]: #UI_tab_surveys
[UI_frm_filter_surveys]: #UI_frm_filter_surveys
[UI_frm_begin_survey]: #UI_frm_begin_survey
[UI_frm_end_survey]: #UI_frm_end_survey
[UI_frm_finalize_survey]: #UI_frm_finalize_survey

[P2-Login-AuthForm]: basefunc-P2-Login-AuthForm.png "Рис.P2.Login.AuthForm Форма авторизации"
[P9.QueryLists]: basefunc-P9-QueryLists.png "Рис.P9.QueryLists Страница Опросников"
[P9.QueryLists.FilterForm]: basefunc-P9-QueryLists-FilterForm.png "Рис.P9.QueryLists.FilterForm Форма фильтра Опросников"

[UC_register]: UC.md#UC_register
[UC_reg_confirm]: UC.md#UC_reg_confirm
[UC_chg_usr_attr]: UC.md#UC_chg_usr_attr
[UC_login]: UC.md#UC_login
[UC_logoff]: UC.md#UC_logoff
[UC_new_querylist]: UC.md#UC_new_querylist
[UC_search_querylist]: UC.md#UC_search_querylist
[UC_chg_querylist]: UC.md#UC_chg_querylist
[UC_active_querylist]: UC.md#UC_active_querylist
[UC_chg_querycontent]: UC.md#UC_chg_querycontent
[UC_emu_querylist]: UC.md#UC_emu_querylist
[UC_goto_task_by_querylist]: UC.md#UC_goto_task_by_querylist
[UC_archive_querylist]: UC.md#UC_archive_querylist
[UC_del_querylist]: UC.md#UC_del_querylist
[UC_new_question]: UC.md#UC_new_question
[UC_chg_question]: UC.md#UC_chg_question
[UC_new_answer]: UC.md#UC_new_answer
[UC_chg_answer]: UC.md#UC_chg_answer
[UC_del_answer]: UC.md#UC_del_answer
[UC_emu_question]: UC.md#UC_emu_question
[UC_emu_question]: UC.md#UC_emu_question
[UC_del_question]: UC.md#UC_del_question
[UC_new_task]: UC.md#UC_new_task
[UC_search_task_by_querylist]: UC.md#UC_search_task_by_querylist
[UC_search_task_by_schedule]: UC.md#UC_search_task_by_schedule
[UC_chg_task]: UC.md#UC_chg_task
[UC_active_task]: UC.md#UC_active_task
[UC_goto_querylist_by_task]: UC.md#UC_goto_querylist_by_task
[UC_goto_schedule_by_task]: UC.md#UC_goto_schedule_by_task
[UC_archive_task]: UC.md#UC_archive_task
[UC_del_task]: UC.md#UC_del_task
[UC_choice_survey]: UC.md#UC_choice_survey
[UC_run_survey]: UC.md#UC_run_survey
[UC_run_query]: UC.md#UC_run_query
[UC_finalize_survey]: UC.md#UC_finalize_survey
[UC_search_finished_survey]: UC.md#UC_search_finished_survey
[UC_view_results]: UC.md#UC_view_results
[UC_dashboard]: UC.md#UC_dashboard
[UC_report]: UC.md#UC_report
