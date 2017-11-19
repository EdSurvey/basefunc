# <a name="top">Сценарии использования</a>


1. [Управление Пользователями][usermgmt]
    1. Регистрация
        1. Зарегистрироваться - [UC_register][UC_register]
        1. Подтверить регистрацию - [UC_reg_confirm][UC_reg_confirm]
    1. Изменение параметров Пользователя - [UC_chg_usr_attr][UC_chg_usr_attr]
    1. Аутентификация
        1. Вход - [UC_login][UC_login]
        1. Выход - [UC_logoff][UC_logoff]
1. [Управление Контентом][contentmgmt]
    1. Опросники
        1. Создать Опросник - [UC_new_querylist][UC_new_querylist]
        1. Найти Опросник - [UC_search_querylist][UC_search_querylist]
        1. Изменить параметры Опросника - [UC_chg_querylist][UC_chg_querylist]
        1. Активировать/Деактивировать Опросник - [UC_active_querylist][UC_active_querylist]
        1. Изменить наполнение Опросника - [UC_chg_querycontent][UC_chg_querycontent]
        1. Эмуляция Опросника - [UC_emu_querylist][UC_emu_querylist]
        1. Перейти к Задачам по Опроснику - [UC_goto_task_by_querylist][UC_goto_task_by_querylist]
        1. Архивировать Опросник - [UC_archive_querylist][UC_archive_querylist]
        1. Удалить Опросник - [UC_del_querylist][UC_del_querylist]
    1. Вопрос
        1. Создать Вопрос - [UC_new_question][UC_new_question]
        1. Изменить Вопрос - [UC_chg_question][UC_chg_question]
            1. Добавить вариант Ответ - [UC_new_answer][UC_new_answer]
            1. Изменить вариант Ответа - [UC_chg_answer][UC_chg_answer]
            1. Удалить вариант Ответа - [UC_del_answer][UC_del_answer]
        1. Предпросмотр Вопроса - [UC_emu_question][UC_emu_question]
        1. Удалить Вопрос - [UC_del_question][UC_del_question]
    1. Задачи
        1. Добавить Задачу - [UC_new_task][UC_new_task]
        1. Найти Задачи
            1. по Опроснику - [UC_search_task_by_querylist][UC_search_task_by_querylist] (через Опросник)
            1. по Расписанию - [UC_search_task_by_schedule][UC_search_task_by_schedule] (через Задание)
        1. Изменить параметры Задачи - [UC_chg_task][UC_chg_task]
        1. Активировать/Деактивировать Задачу - [UC_active_task][UC_active_task]
        1. Перейти к Опроснику этой Задачи - [UC_goto_querylist_by_task][UC_goto_querylist_by_task]
        1. Перейти к Расписаниям по этой Задаче - [UC_goto_schedule_by_task][UC_goto_schedule_by_task]
        1. Архивировать Задачу - [UC_archive_task][UC_archive_task]
        1. Удалить Задачу - [UC_del_task][UC_del_task]
1. [Выполнение Задания][survey]
    1. Выбор доступного Задания - [UC_choice_survey][UC_choice_survey]
    1. Запустить Задание - [UC_run_survey][UC_run_survey]
    1. Ответить на Вопрос - [UC_run_query][UC_run_query]
    1. Завершение Задания - [UC_finalize_survey][UC_finalize_survey]
    1. Найти выполненные Задания - [UC_search_finished_survey][UC_search_finished_survey]
    1. Просмотреть свои Ответы - [UC_view_results][UC_view_results]
1. [Контроль Заданий][surveymgmt]
    1. Статистика - [UC_dashboard][UC_dashboard]
    1. Отчёты - [UC_report][UC_report]


## <a name="usermgmt">Управление Пользователями</a>

[в начало][top]


### Регистрация

[в начало][top]


#### Зарегистрироваться - <a name="UC_register">UC_register</a>

[в начало][top]


#### Подтверить регистрацию - <a name="UC_reg_confirm">UC_reg_confirm</a>

[в начало][top]


### Изменение параметров Пользователя - <a name="UC_chg_usr_attr">UC_chg_usr_attr</a>

[в начало][top]


### Аутентификация

[в начало][top]


#### Вход - <a name="UC_login">UC_login</a>

Атрибут | Значение
---|---
Выполняется | [Посетитель][guest].
Цель | Получить возожность выполнять на Сайте операции, требующие авторизации Пользователя.
Входящие данные и документы | 1. Имя и пароль Пользователя.
Данные поступают из | 1. Внешней среды.
Выходящие данные и документы | Домашняя страница или страница требующая авторизации, с которой был произведён перевод Посетителя.


##### Предусловия выполнения процесса
1. Посетитель Сайта ещё не выполнил Вход и находится на странице, которая не требует авторизации.
1. Пользователь предваритально выполнил "Выход" ([UC_logoff][UC_logoff]) и нажал на ссылку "Вход".
1. Посетитель переходит на страницу, коорая требует авторизации.

##### Описание выполнения процесса

1. Сайт отображает страницу с интерфейсом "Форма аутентификации" ([UI_frm_auth][UI_frm_auth]).
1. Пользователь заполнениет поля формы и нажимает кнопку "Ок".
1. Если данные корректны, то Сайт переводит Пользователя
    1. _если_ для входа использовалась сссылка "Вход", _то_ Сайт переводит Пользователя на домашнюю страницу
    1. _если_ Пользователь был переведён со страницы требующей авторизации, _то_ Сайт переводит Пользователя на предыдущую страницу.

[в начало][top]


#### Выход - <a name="UC_logoff">UC_logoff</a>

[в начало][top]


## <a name="contentmgmt">Управление Контентом</a>

[в начало][top]


### Опросники

[в начало][top]


#### Создать Опросник - <a name="UC_new_querylist">UC_new_querylist</a>

[в начало][top]


#### Найти Опросник - <a name="UC_search_querylist">UC_search_querylist</a>

[в начало][top]


#### Изменить параметры Опросника - <a name="UC_chg_querylist">UC_chg_querylist</a>

[в начало][top]


#### Активировать/Деактивировать Опросник - <a name="UC_active_querylist">UC_active_querylist</a>

[в начало][top]


#### Изменить наполнение Опросника - <a name="UC_chg_querycontent">UC_chg_querycontent</a>

[в начало][top]


#### Эмуляция Опросника - <a name="UC_emu_querylist">UC_emu_querylist</a>

[в начало][top]


#### Перейти к Задачам по Опроснику - <a name="UC_goto_task_by_querylist">UC_goto_task_by_querylist</a>

[в начало][top]


#### Архивировать Опросник - <a name="UC_archive_querylist">UC_archive_querylist</a>

[в начало][top]


#### Удалить Опросник - <a name="UC_del_querylist">UC_del_querylist</a>

[в начало][top]


### Вопрос

[в начало][top]


##### Создать Вопрос - <a name="UC_new_question">UC_new_question</a>

[в начало][top]


##### Изменить Вопрос - <a name="UC_chg_question">UC_chg_question</a>

[в начало][top]


###### Добавить вариант Ответ - <a name="UC_new_answer">UC_new_answer</a>

[в начало][top]


###### Изменить вариант Ответа - <a name="UC_chg_answer">UC_chg_answer</a>

[в начало][top]


###### Удалить вариант Ответа - <a name="UC_del_answer">UC_del_answer</a>

[в начало][top]


##### Предпросмотр Вопроса - <a name="UC_emu_question">UC_emu_question</a>

[в начало][top]


##### Удалить Вопрос - <a name="UC_del_question">UC_del_question</a>

[в начало][top]


### Задачи

[в начало][top]


#### Добавить Задачу - <a name="UC_new_task">UC_new_task</a>
через Опросник

[в начало][top]


#### Найти Задачи

[в начало][top]


##### по Опроснику - <a name="UC_search_task_by_querylist">UC_search_task_by_querylist</a> (через Опросник)

[в начало][top]


##### по Расписанию - <a name="UC_search_task_by_schedule">UC_search_task_by_schedule</a> (через Задание)

[в начало][top]


#### Изменить параметры Задачи - <a name="UC_chg_task">UC_chg_task</a>

[в начало][top]


#### Активировать/Деактивировать Задачу - <a name="UC_active_task">UC_active_task</a>

[в начало][top]


#### Перейти к Опроснику этой Задачи - <a name="UC_goto_querylist_by_task">UC_goto_querylist_by_task</a>

[в начало][top]


#### Перейти к Расписаниям по этой Задаче - <a name="UC_goto_schedule_by_task">UC_goto_schedule_by_task</a>

[в начало][top]


#### Архивировать Задачу - <a name="UC_archive_task">UC_archive_task</a>

[в начало][top]


#### Удалить Задачу - <a name="UC_del_task">UC_del_task</a>

[в начало][top]


## <a name="survey">Выполнение Задания</a>

[в начало][top]


### Выбор доступного Задания - <a name="UC_choice_survey">UC_choice_survey</a>

[в начало][top]


### Запустить Задание - <a name="UC_run_survey">UC_run_survey</a>

[в начало][top]


### Ответить на Вопрос - <a name="UC_run_query">UC_run_query</a>

[в начало][top]


### Завершение Задания - <a name="UC_finalize_survey">UC_finalize_survey</a>

[в начало][top]


### Найти выполненные Задания - <a name="UC_search_finished_survey">UC_search_finished_survey</a>

[в начало][top]


## <a name="surveymgmt">Контроль Заданий</a>

[в начало][top]


### Статистика - <a name="UC_dashboard">UC_dashboard</a>

[в начало][top]


### Отчёты - <a name="UC_report">UC_report</a>

[в начало][top]


[top]: #top
[usermgmt]: #usermgmt
[contentmgmt]: #contentmgmt
[survey]: #survey
[surveymgmt]: #surveymgmt

[UC_register]: #UC_register
[UC_reg_confirm]: #UC_reg_confirm
[UC_chg_usr_attr]: #UC_chg_usr_attr
[UC_login]: #UC_login
[UC_logoff]: #UC_logoff
[UC_new_querylist]: #UC_new_querylist
[UC_search_querylist]: #UC_search_querylist
[UC_chg_querylist]: #UC_chg_querylist
[UC_active_querylist]: #UC_active_querylist
[UC_chg_querycontent]: #UC_chg_querycontent
[UC_emu_querylist]: #UC_emu_querylist
[UC_goto_task_by_querylist]: #UC_goto_task_by_querylist
[UC_archive_querylist]: #UC_archive_querylist
[UC_del_querylist]: #UC_del_querylist
[UC_new_question]: #UC_new_question
[UC_chg_question]: #UC_chg_question
[UC_new_answer]: #UC_new_answer
[UC_chg_answer]: #UC_chg_answer
[UC_del_answer]: #UC_del_answer
[UC_emu_question]: #UC_emu_question
[UC_emu_question]: #UC_emu_question
[UC_del_question]: #UC_del_question
[UC_new_task]: #UC_new_task
[UC_search_task_by_querylist]: #UC_search_task_by_querylist
[UC_search_task_by_schedule]: #UC_search_task_by_schedule
[UC_chg_task]: #UC_chg_task
[UC_active_task]: #UC_active_task
[UC_goto_querylist_by_task]: #UC_goto_querylist_by_task
[UC_goto_schedule_by_task]: #UC_goto_schedule_by_task
[UC_archive_task]: #UC_archive_task
[UC_del_task]: #UC_del_task
[UC_choice_survey]: #UC_choice_survey
[UC_run_survey]: #UC_run_survey
[UC_run_query]: #UC_run_query
[UC_finalize_survey]: #UC_finalize_survey
[UC_search_finished_survey]: #UC_search_finished_survey
[UC_view_results]: #UC_view_results
[UC_dashboard]: #UC_dashboard
[UC_report]: #UC_report

[guest]: TERMS.md#guest

[UI_frm_auth]: UI.md#UI_frm_auth