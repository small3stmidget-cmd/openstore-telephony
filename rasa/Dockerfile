FROM rasa/rasa:3.7.0

# Copy project files
COPY . /app
WORKDIR /app

# Install python dependencies for custom actions
RUN pip install --no-cache-dir rasa-sdk requests

CMD ["run", "--enable-api", "--cors", "*"]
