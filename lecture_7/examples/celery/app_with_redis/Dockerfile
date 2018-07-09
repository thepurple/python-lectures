FROM python:3
ADD . /code
WORKDIR /code

# add alias for ls -la
RUN echo "alias ll='ls -la --color=auto'" >> ~/.bashrc

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
