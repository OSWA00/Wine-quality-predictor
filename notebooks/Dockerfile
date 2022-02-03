FROM jupyter/minimal-notebook

# Install dependencies
COPY requirements.txt ./ 
RUN pip install -r requirements.txt

# Mount local volume & set work directory
VOLUME /notebooks
WORKDIR /notebooks

