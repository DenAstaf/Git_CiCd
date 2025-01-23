В данном проекте реализован FastApi.<br>
Используется pylint, pytest и pytest-cov.

1. pylint (для приведения проекта в стандарт):
<br>Запуск: `pylint $(git ls-files '*.py')`
2. pytest и pytest-cov (для тестирования функционала и проверки на сколько покрыт тестами функционал)
<br>Запуск: `pytest -s --cov --cov-report html --cov-fail-under=50`

**Работа с GitHub**<br>
В GitHub выполняются Actions Pylint и Pytest за счет настроенных .yml.<br>
Необходимо запушить проект на GitHub и проверить как отработают Actions

**Работа с GitLab**
1. Установка GitLab с помощью Docker:<br>
`docker run --detach --hostname gitlab.local --publish 8000:80 --publish 443:443 --publish 22:22 --name gitlab --restart always --volume C:\srv\gitlab\config:/etc/gitlab --volume C:\srv\gitlab\logs:/var/log/gitlab --volume C:\srv\gitlab\data:/var/opt/gitlab gitlab/gitlab-ee:latest`
2. Открыть файл C:\Windows\System32\drivers\etc\hosts с правами администратора и добавить в конец файла:<br>
`127.0.0.1 gitlab.local`
3. Сбросить пароль и задать новый:<br>
`docker exec -it gitlab gitlab-rake "gitlab:password:reset[root]"`
4. Перейти на GitLab http://gitlab.local:8000/ и авторизоваться:<br>
`логин: root`<br>
`пароль: который был задан при сбросе старого пароля`
