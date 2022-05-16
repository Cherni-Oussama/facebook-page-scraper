FROM python:3.9.7


WORKDIR /facebook-page-scraper
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
