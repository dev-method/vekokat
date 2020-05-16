# pull official base image
FROM devmethod/vekokat
WORKDIR /usr/src/vekokat.ru/vekokat_ver2/
COPY supervisord.conf /etc/supervisord.conf
COPY root  /etc/crontabs/
RUN chown root:root /etc/crontabs/root
CMD ["/usr/bin/supervisord"]
