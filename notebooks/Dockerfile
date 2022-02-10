FROM jupyter/minimal-notebook

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
COPY requirements.txt ./ 
RUN pip install -r requirements.txt

# Mount local volume & set work directory
VOLUME /notebooks
WORKDIR /notebooks

