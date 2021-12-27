> @quiet 2021-12-24


# gitea

文档： https://docs.gitea.io/zh-cn/

简单好用


> docker
```yaml
version: "3"

networks:
  gitea:
    external: false

services:
  server:
    image: gitea/gitea:1.15.8
    container_name: gitea
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - DB_TYPE=mysql
      - DB_HOST=db:3306
      - DB_NAME=gitea
      - DB_USER=gitea
      - DB_PASSWD=gitea
    restart: always
    networks:
      - gitea
    volumes:
      - ./gitea/data:/data
      - ./gitea/timezone:/etc/timezone:ro
      - ./gitea/localtime:/etc/localtime:ro
    ports:
      - "3000:3000"
      - "222:22"
    depends_on:
      - db
  db:
    image: mysql:8
    restart: always
    environment:
      - MYSQL_ROOT_PASSWORD=gitea
      - MYSQL_USER=gitea
      - MYSQL_PASSWORD=gitea
      - MYSQL_DATABASE=gitea
    networks:
      - gitea
    volumes:
      - ./mysql:/var/lib/mysql
```
```shell
 docker-compose up -d
```


配置
```ini
APP_NAME = 7doc
RUN_MODE = prod
RUN_USER = git

[repository]
ROOT = /data/git/repositories

[repository.local]
LOCAL_COPY_PATH = /data/gitea/tmp/local-repo

[repository.upload]
TEMP_PATH = /data/gitea/uploads

[server]
APP_DATA_PATH    = /data/gitea
DOMAIN           = localhost
SSH_DOMAIN       = localhost
HTTP_PORT        = 3000
ROOT_URL         = http://localhost:3000/
DISABLE_SSH      = false
SSH_PORT         = 22
SSH_LISTEN_PORT  = 22
LFS_START_SERVER = true
LFS_CONTENT_PATH = /data/git/lfs
LFS_JWT_SECRET   = uern5-JAxwL9lV0apLgP__QbLOVhzMog1Ytol9_1pK8
OFFLINE_MODE     = false

[database]
PATH     = /data/gitea/gitea.db
DB_TYPE  = mysql
HOST     = db:3306
NAME     = gitea
USER     = gitea
PASSWD   = gitea
LOG_SQL  = false
SCHEMA   = 
SSL_MODE = disable
CHARSET  = utf8mb4

[indexer]
ISSUE_INDEXER_PATH = /data/gitea/indexers/issues.bleve

[session]
PROVIDER_CONFIG = /data/gitea/sessions
PROVIDER        = file

[picture]
AVATAR_UPLOAD_PATH            = /data/gitea/avatars
REPOSITORY_AVATAR_UPLOAD_PATH = /data/gitea/repo-avatars
DISABLE_GRAVATAR              = false
ENABLE_FEDERATED_AVATAR       = true

[attachment]
PATH = /data/gitea/attachments

;[log]
;MODE      = console
;LEVEL     = info
;ROUTER    = console
;ROOT_PATH = /data/gitea/log
[log]
MODE = file
LOG_ROTATE = true
DAILY_ROTATE = true
MAX_SIZE_SHIFT = 28
MAX_DATS = 30
COMPRESS = true
COMPRESSION_LEVEL = -1
LEVEL = info
ROOT_PATH = /data/gitea/log


[security]
INSTALL_LOCK                  = true
SECRET_KEY                    = 57OsD7IX2yT1pv2Hc6tW4L49vMxtYAzA5aCSGt5Y8CFgc0QEUoWc4xwpi4NUKZqZ
REVERSE_PROXY_LIMIT           = 1
REVERSE_PROXY_TRUSTED_PROXIES = *
INTERNAL_TOKEN                = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE2NDAzMTczOTN9.6mwaX5_nHA267VGaoVRuVOEu6bQCz4QutajCnxcm7ZM
PASSWORD_HASH_ALGO            = pbkdf2

[service]
DISABLE_REGISTRATION              = false
REQUIRE_SIGNIN_VIEW               = false
REGISTER_EMAIL_CONFIRM            = false
ENABLE_NOTIFY_MAIL                = false
ALLOW_ONLY_EXTERNAL_REGISTRATION  = false
ENABLE_CAPTCHA                    = false
DEFAULT_KEEP_EMAIL_PRIVATE        = false
DEFAULT_ALLOW_CREATE_ORGANIZATION = true
DEFAULT_ENABLE_TIMETRACKING       = true
NO_REPLY_ADDRESS                  = noreply.localhost

[mailer]
ENABLED = true
FROM = ztwangjing@7doc.cn
MAILER_TYPE = smtp
HOST = hwsmtp.exmail.qq.com:465
IS_TLS_ENABLED = true
USER = ztwangjing@7doc.cn
PASSWD = ``

[openid]
ENABLE_OPENID_SIGNIN = false
ENABLE_OPENID_SIGNUP = false


```

