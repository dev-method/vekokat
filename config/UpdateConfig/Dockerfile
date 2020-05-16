# pull official base image
FROM python:3.6.9-alpine
WORKDIR /usr/src/vekokat.ru/vekokat_ver2/
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN set -e; \
        apk add --no-cache --virtual .build-deps \
                gcc \
                libc-dev \
                linux-headers \
                mariadb-dev \
                python3-dev \
                postgresql-dev \
				jpeg-dev \
				zlib-dev \
				libxslt-dev\
				libxml2-dev\
				libwebp\
				libwebp-dev\
				nano\
				nodejs\
				nodejs-npm\
        ;
RUN apk add --update supervisor
COPY requirements_vekokat.txt requirements_vekokat.txt
RUN pip install -r requirements_vekokat.txt
RUN npm install gulp-cli -g
CMD ["/usr/bin/supervisord"]
