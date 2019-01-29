FROM python
COPY . /server/
WORKDIR /server
RUN pip install flask
RUN pip install gunicorn
EXPOSE 9998
CMD gunicorn -b 0.0.0.0:9998 -w 4 server:app
