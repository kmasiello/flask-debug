from flask import Flask, render_template, request, redirect, url_for
#from werkzeug import secure_filename
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      files = request.files.getlist("file")
      for file in files:
          file.save(secure_filename(file.filename))
      
      #return 'file uploaded successfully'

      return redirect(url_for('upload_file'))

if __name__ == '__main__':
   app.run(debug = True)
