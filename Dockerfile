FROM python AS compile-image
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

FROM compile-image
WORKDIR /app
COPY . .
CMD ["sleep", "infinity"]