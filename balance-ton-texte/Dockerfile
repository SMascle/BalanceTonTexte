FROM python:3.8

MAINTAINER SebastienMohamedNoemi

WORKDIR balance_ton_texte/
COPY . /balance_ton_texte/

ENV STATIC_PATH balance_ton_texte/static

RUN python -m pip install --upgrade pip
RUN pip install dist/balance_ton_texte-0.1.0-py3-none-any.whl

EXPOSE 8000

CMD [ "app" ]
