FROM python:3.7

# define workdir
WORKDIR /opt/toxic_comments

# install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy files
COPY files files/
COPY app app/

# local build
EXPOSE 8501


ENTRYPOINT ["streamlit", "run"]
CMD ["app/app.py"]