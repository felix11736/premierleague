# base image
FROM python:3.9

# working directory 
WORKDIR /app

# copy semua file dan folder 
COPY app.python /app/

# menginstall dependencies
RUN pip install -r requirments.txt

#menjalankan aplikasi pythonnya 
CMD ["python", "app.python"]
