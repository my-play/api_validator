FROM python:3.8-slim

RUN mkdir -p /api-validator/report/

COPY . /api-validator

WORKDIR /api-validator

RUN pip3 install --no-cache-dir -r requirements.txt

RUN find /api-validator/ -type f -iname "*.sh" -exec  chmod +x {} \;

CMD ["/api-validator/start-test.sh"]
