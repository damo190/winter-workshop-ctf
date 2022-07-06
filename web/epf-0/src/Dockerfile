FROM tiangolo/uwsgi-nginx-flask:python3.9-2021-10-26
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
COPY ./epf.db /var/www/epf.db
COPY ./app/static/ /var/www/app/static
RUN pip install -r /var/www/requirements.txt
