FROM python:3.8

LABEL maintener="oswahdez00"
LABEL version="1.0"
LABEL description="docker image for data science development"

# Mount volumes
VOLUME /home/notebooks /home/data

# Set working directory
WORKDIR /

# Expose container to host machine
EXPOSE 8888

RUN pip install jupyter

# Install dependencies
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
