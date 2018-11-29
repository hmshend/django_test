	show databases;
###创建数据库
	create database mylogs charset=utf8;
###赋予权限
	grant all privileges on mylogs.* To 'dj_user'@'%';
###指定进入指定表
	mysql -uroot -p -A mylogs
###安装redis
	pip install django-redis
###配置redis
	CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # "CONNECTION_POOL_KWARGS": {"max_connections": 100}
            # "PASSWORD": "密码",
        	}
    	}
	}
###配置mysql
	DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        # 'NAME': 'mydb',         # 你要存储数据的库名，事先要创建之
        # 'USER': 'root',         # 数据库用户名
        # 'PASSWORD': '1234',     # 密码
        # 'HOST': 'localhost',    # 主机
        # 'PORT': '3306',         # 数据库使用的端口
        'OPTIONS':{
            'read_default_file': 'utils/dbs/my.cnf'
        	}
    	}
	}

###静态文件保存位置
	STATIC_URL = '/static/'
	STATICFILES_DIRS = {
    os.path.join(BASE_DIR, 'static'),  #用于存放静态文件
    }

###设置中文
	# LANGUAGE_CODE = 'en-us'
	LANGUAGE_CODE = 'zh-hans'
	# TIME_ZONE = 'UTC'
	TIME_ZONE = 'Asia/Beijing'

###设置git不提交的方式
	touch .gitignore
	vim .gitignore
	添加my.cnf

###配置logger
	LOGGING = {
    # 版本
    'version': 1,
    # 是否禁用已存在的日志器
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logs/dj_youkou.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],
            'propagate': True,
            'level': 'INFO',  # 日志器接收的最低日志级别
        	},
    	}
	}