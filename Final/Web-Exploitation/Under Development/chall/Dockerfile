# docker build -t ara .
# docker run --rm --name=ara -itd -p 80:80 ara
FROM ubuntu:16.04


RUN apt-get update -y && apt-get install -y libapache2-mod-php7.0 php7.0 php7.0-json php-xml libapache2-mod-php7.0

RUN a2enmod php7.0
RUN a2enmod autoindex
RUN a2enmod rewrite

RUN rm /var/www/html/index.html
COPY index.php /var/www/html/
COPY send.php /var/www/html/
COPY login.php /var/www/html/
COPY logout.php /var/www/html/
COPY mybest.php /var/www/html/
COPY assets /var/www/html/assets
COPY flag.txt /

WORKDIR /var/www/html/
CMD /usr/sbin/apache2ctl -D FOREGROUND
EXPOSE 80